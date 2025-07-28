import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from wifi_map_ai.core import main_path
import dill

import time

# Loading files

X = np.load(main_path / "Data" / "Clean" / "X.npy")
Y = np.load(main_path / "Data" / "Clean" / "Y.npy")


# Shape check

print(f"The shape of the input date is: {X.shape}")  # this should (400, 2)
print(f"The shape of the input date is: {Y.shape}")  # this should be (400, 10201)
assert X.shape == (400, 2)
assert Y.shape == (400, 10201)

# Create the data set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

params = {"n_estimators": 196, "min_samples_split": 2, "max_features":1.0, "max_samples":0.5273 }

# Train the model
rf = RandomForestRegressor(random_state=3, n_jobs=12, **params)
t0 = time.time()
rf.fit(X_train, Y_train)  # fit() with instantiated object
print(f"Default RandomForestRegressor elapsed time: {time.time()-t0} s")
score = rf.score(X_test, Y_test)
print(f"The score for Default RandomForestRegressor is: {score}")

# Save the model
model_file = main_path / "Data" / "Trained_Model" / "model.dill"
dill.dump(rf, open(model_file, 'wb'))
