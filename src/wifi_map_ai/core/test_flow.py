from wifi_map_ai.core.core_functions import *

# On UI open
model_file = main_path / "Data" / "Trained_Model" / 'model.dill'
test_installation_point = [1230, 750]

model = load_models(model_file)

# for prediction
pred = make_prediction(model, test_installation_point)

png_file = main_path / "Data" / "prediction_images" / 'test_prediction.png'
result = generate_plot(pred, png_file)

pass