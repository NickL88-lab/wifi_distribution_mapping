# Functions to load the trained model and to run prediction and to plot
from wifi_map_ai.core import main_path
import numpy as np
import dill
import pandas as pd
import matplotlib.pyplot as plt
import os.path


model_file = main_path / "Data" / "Trained_Model" / 'model.dill'

test_installation_point = np.array([[1230, 750]])


def load_models(model_path):
    print(f"Loading model")
    with open(model_path, 'rb') as f:
        model = dill.load(f)
    return model


def make_prediction(model, installation_point):
    # Make a test prediction
    installation_point_reshape = np.array([installation_point])
    prediction = model.predict(installation_point_reshape)
    return prediction


def generate_plot(prediction, filename):

    # get the image pixels coordinates
    file_path = main_path / "Data" / "Clean" / "u_v_coordinates.csv"
    if not file_path.is_file():
        raise FileNotFoundError(f"File {file_path} does not exist!")
    df = pd.read_csv(file_path)
    x_y_coords = df[["_v", "_u"]].to_numpy()

    # values of the image
    values = prediction

    # Plot the image
    plt.figure(figsize=(8, 6))
    plt.scatter(x_y_coords[:, 0], x_y_coords[:, 1], c=values[0, :], cmap='rainbow')
    plt.colorbar(label='Image values')
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title('Original Image Plot')
    # Save the plot as a PNG file
    if os.path.splitext(filename)[1] != ".png":
        filename = filename + ".png"
    plt.savefig(filename)
    # plt.show()
    return str(filename)


