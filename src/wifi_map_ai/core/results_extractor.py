import csv
import os.path
from pyaedt import Hfss

folder = r"D:\dev\wifi_planner"
project_name = "house_datalake.aedt"

project_name = os.path.join(folder, project_name)

datalake_dimension = 400

if os.path.exists(project_name + str(".auto")):
    os.remove(project_name + str(".auto"))

if os.path.exists(project_name + str(".lock")):
    os.remove(project_name + str(".lock"))

design_name = "EM_field_distribution"
hfss_design = Hfss(
    projectname=project_name, designname=design_name, specified_version="2023.2", non_graphical=True, close_on_exit=True
)
autosave = hfss_design.autosave_disable()

table_file = os.path.join(folder, "Datalake_Table.csv")

hfss_design.ooptimetrics.ExportParametricSetupTable("Datalake_Eval", table_file)


variations = []
with open(table_file, newline="") as csvfile:
    read_line = csv.reader(csvfile)
    next(read_line)  # Filter out header
    for raw in read_line:
        x_coord = raw[1]  # .replace('mm', '')  # at the moment we don't need units
        y_coord = raw[2]  # .replace('mm', '')
        variations.append((str(x_coord), str(y_coord)))

print(variations)

for var in variations:
    hfss_design.oreportsetup.CreateReport(
        "Table 1",
        "Near Fields",
        "Data Table",
        "Setup1 : Sweep",
        ["Context:=", "Rectangle1"],
        [
            "_u:=",
            ["All"],
            "_v:=",
            ["All"],
            "Freq:=",
            ["5GHz"],
            "paramX:=",
            ["Nominal"],
            "paramY:=",
            ["Nominal"],
            "x_coord:=",
            var[0],
            "y_coord:=",
            var[1],
        ],
        ["X Component:=", "_u", "Y Component:=", ["NearETotal/max(NearETotal)"]],
    )
    file_name = "NearE_" + str(var[0]) + "_" + str(var[1]) + ".csv"
    full_file_name = os.path.join(folder, file_name)
    hfss_design.oreportsetup.ExportToFile("Table 1", full_file_name, False)
    hfss_design.oreportsetup.DeleteReports(["Table 1"])
