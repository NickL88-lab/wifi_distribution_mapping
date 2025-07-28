from pathlib import Path
import numpy as np
import pandas as pd

main_path = Path().absolute()
data_path = main_path / "Data" / "Raw"

num_samples = 400

X = np.zeros([num_samples, 2])
Y = np.zeros([num_samples, 10201])

# for i in range(0, num_samples):
#    df = pd.read_csv(data_path / f"Near E Table {i+1}.csv")
#    X[i,0], X[i,1] = df["paramX []"].iloc[0], df["paramY []"].iloc[0]
#    Y[i,:] = df["NearETotal/max(NearETotal) []"]

num = 0
for file_path in data_path.glob("*"):
    if file_path.is_file():
        df = pd.read_csv(file_path)
        X[num, 0], X[num, 1] = df["x_coord [mm]"].iloc[0] / 1000, df["y_coord [mm]"].iloc[0] / 1000
        Y[num, :] = df["NearETotal/max(NearETotal) []"]
        num += 1
    print(f"Finished processing {num} files")


export_path = main_path / "Data" / "Clean"
np.save(export_path / "X.npy", X)
np.save(export_path / "Y.npy", Y)
