import random
import cv2
import os.path
import math
import numpy as np
from Rectangle_Detection import detect_domain, is_green, are_nearby, get_black_pixels
from pyaedt import Hfss

project_name = 'Hackathon3_AEDT_File\house.aedt'

datalake_dimension = 800

if os.path.exists(project_name + str(".auto")):
    os.remove(project_name + str(".auto"))

if os.path.exists(project_name + str(".lock")):
    os.remove(project_name + str(".lock"))

design_name = "EM_field_distribution"
hfss_design = Hfss(projectname=project_name, designname=design_name, specified_version="2023.2", non_graphical=False, close_on_exit=True)
autosave = hfss_design.autosave_disable()
print(autosave)
primitives = hfss_design.modeler

try:
    obj_id = hfss_design.oeditor.GetObjectIDByName("Domain")
    obj_id = primitives.objects[obj_id]
    obj_id.transparency = 0

except:
    print("Domain is not defined")

hfss_design.post.export_model_picture(full_name="Hackathon3_images\house.png", show_axis=False, show_grid=False, show_ruler=False, orientation="top", width=1920, height=1080)

primitives.model_units = 'mm'
primitives.create_air_region(z_pos=10, z_neg=10)
calibration_id = hfss_design.oeditor.GetObjectIDByName('Region')
obj_id = primitives.objects[calibration_id]
obj_id.transparency = 0
obj_id.display_wireframe = False
hfss_design.post.export_model_picture(full_name="Hackathon3_images\environment.png", show_axis=False, show_grid=False, show_ruler=False, orientation="top", width=1920, height=1080)

vertex_id = primitives.get_object_vertices(calibration_id)
calibration_vertex_list = []
pos_x = []
pos_y = []

for id in vertex_id:
    pos = primitives.get_vertex_position(id)
    calibration_vertex_list.append(pos)
    pos_x.append(pos[0])
    pos_y.append(pos[1])

length_x = abs(max(pos_x)-min(pos_x))
length_y = abs(max(pos_y)-min(pos_y))

cs_coords = []
cs_coords.append(min(pos_x))
cs_coords.append(min(pos_y))
cs_coords.append(1000)

print("Coordinates new CS[mm]: ", cs_coords)
print("Length along X[mm]: ", length_x)
print("Length along Y[mm]: ", length_y)

primitives.create_coordinate_system(origin=cs_coords, name="top_left_corner")

wifi_cs_coords = []
hfss_design.variable_manager.set_variable(variable_name="x_coord", expression="1000mm")
wifi_cs_coords.append("x_coord")
hfss_design.variable_manager.set_variable(variable_name="y_coord", expression="1000mm")
wifi_cs_coords.append("y_coord")
wifi_cs_coords.append(0)
primitives.create_coordinate_system(origin=wifi_cs_coords, name="wifi_antenna", reference_cs="top_left_corner")

obj_id = hfss_design.oeditor.GetObjectIDByName("Region")
obj_id = primitives.objects[obj_id]
obj_id.delete()

hfss_design.create_sbr_antenna(antenna_type=hfss_design.SbrAntennas.WireDipole, target_cs="wifi_antenna", antenna_name="WiFi_Tx_Antenna")

img_house = cv2.imread("Hackathon3_images\house.png")
img_env = cv2.imread("Hackathon3_images\environment.png")

# Domain detection
coordinates, lengths, LPRs = detect_domain(img_env, length_x, length_y)

print("Coordinates: ", coordinates)
print("Lengths: ", lengths)
print("LPRs Computation: ", LPRs)
x = coordinates[0]
y = coordinates[1]

lx = lengths[0]
ly = lengths[1]

LPR_x = LPRs[0]
LPR_y = LPRs[1]

# Cut of the original picture
img_house_map = img_house[y:y+ly, x:x+lx]
cv2.imwrite("Hackathon3_images\house_installation_cut.png", img_house_map)

wifi_pos_x = []
wifi_pos_y = []
pixel_pos = []
black_pixels = get_black_pixels(img_house_map)

for _ in range(datalake_dimension):
    flag = True

    while flag:
        pixel_coord_x = random.randint(0,lx-1)
        pixel_coord_y = random.randint(0, ly-1)

        if is_green(img_house_map[pixel_coord_y, pixel_coord_x]) and not are_nearby((pixel_coord_x, pixel_coord_y), pixel_pos, max_distance=8) and not are_nearby((pixel_coord_x, pixel_coord_y), black_pixels, max_distance=25):
            cv2.circle(img_house_map, (pixel_coord_x, pixel_coord_y), 2, (255, 0, 0), 2)
            pixel_pos.append((pixel_coord_x,pixel_coord_y))
            x = LPR_x * pixel_coord_x
            y = LPR_y * pixel_coord_y
            wifi_pos_x.append(int(x))
            wifi_pos_y.append(int(y))
            flag = False

        else:
            flag = True


parametric_setup = hfss_design.parametrics.add("x_coord", start_point = str(wifi_pos_x[0])+"mm", variation_type="SingleValue",parametricname="Datalake_Eval")
parametric_setup.add_variation("y_coord", start_point = str(wifi_pos_y[0])+"mm", variation_type="SingleValue")
parametric_setup.sync_variables(["x_coord", "y_coord"], sync_n=1)

for i in range(1,datalake_dimension):
    parametric_setup.add_variation("x_coord", start_point=str(wifi_pos_x[i]) + "mm", variation_type="SingleValue")
    parametric_setup.add_variation("y_coord", start_point=str(wifi_pos_y[i]) + "mm", variation_type="SingleValue")
    parametric_setup.sync_variables(["x_coord", "y_coord"], sync_n=1)

parametric_setup.sync_variables(["x_coord", "y_coord"], sync_n=1)

cv2.imshow("WiFi Installation Points", img_house_map)
cv2.imwrite("Hackathon3_images\house_installation_points.png", img_house_map)
cv2.waitKey(0)
cv2.destroyAllWindows()
