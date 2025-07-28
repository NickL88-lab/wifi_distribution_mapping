import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from bayes_opt import BayesianOptimization
from bayes_opt.util import UtilityFunction

from pathlib import Path
import time


def rmse(y_test, y_pred):
    return np.sqrt(np.average((y_test - y_pred) ** 2, axis=0))


# Loading files

main_path = Path().absolute()

X = np.load(main_path / "Data" / "Clean" / "X.npy")
Y = np.load(main_path / "Data" / "Clean" / "Y.npy")

# X = X[:100, :]
# Y = Y[:100, :]

# Shape check

print(f"The shape of the input date is: {X.shape}")  # this should (400, 2)
print(f"The shape of the input date is: {Y.shape}")  # this should be (400, 10201)
assert X.shape == (400, 2)
assert Y.shape == (400, 10201)

# Create the data set
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

params = {}

# Train the model
rf_def = RandomForestRegressor(random_state=3, n_jobs=12, **params)
t0 = time.time()
rf_def.fit(X_train, Y_train)  # fit() with instantiated object
# Y_predicted = rf_def.predict(X_test)  # Make predictions and save it in dict under key: name
print(f"Default RandomForestRegressor elapsed time: {time.time()-t0} s")
print(f"The score for Default RandomForestRegressor is: {rf_def.score(X_test, Y_test)}")

# def stratified_kfold_score(clf, x, y, n_fold):
#     x, y = x.values, y.values
#     strat_kfold = StratifiedKFold(n_splits=n_fold, shuffle=True, random_state=1)
#     accuracy_list = []
#
#     for train_index, test_index in strat_kfold.split(x, y):
#         x_train_fold, x_test_fold = x[train_index], x[test_index]
#         y_train_fold, y_test_fold = y[train_index], y[test_index]
#         clf.fit(x_train_fold, y_train_fold)
#         accuracy_test = clf.score(x_test_fold, y_test_fold)
#         accuracy_list.append(accuracy_test)
#
#     return np.array(accuracy_list).mean()


def bo_params_rf(n_estimators, min_samples_split, max_features, max_samples):
    clf = RandomForestRegressor(
        n_estimators=int(n_estimators),
        min_samples_split=int(min_samples_split),
        max_features=max_features,
        max_samples=max_samples,
        random_state=3,
        n_jobs=12,
    )
    # score = stratified_kfold_score(clf, X_train, Y_train, 5)
    clf.fit(X_train, Y_train)  # fit() with instantiated object
    score = clf.score(X_test, Y_test)
    return score


# define the param for the optimization
bounds = {
    "n_estimators": (100, 300),
    "min_samples_split": (2, 5),
    "max_features": (0.5, 1),
    "max_samples": (0.2, 1),
}

all_params = {}
for uf in ["ucb", "ei", "poi"]:
    print(f"Utility Function: {uf}")

    rf_optim = BayesianOptimization(bo_params_rf, bounds)
    # Run the param optimization
    t0 = time.time()
    results = rf_optim.maximize(n_iter=1000, init_points=50, acquisition_function=UtilityFunction(kind=uf))
    print(f"Optimization parameters elapsed time: {time.time()-t0} s")

    # Get the optimum parameter set
    params = rf_optim.max["params"]
    params["n_estimators"] = int(params["n_estimators"])
    params["min_samples_split"] = int(params["min_samples_split"])
    print(params)
    all_params[uf] = params


# Run the Random Forest with optimum parameters

print(f"\nSummary")

for uf in ["ucb", "ei", "poi"]:
    params = all_params[uf]
    print(f"\n({uf}): {params}")

    t0 = time.time()
    rf = RandomForestRegressor(
        n_estimators=params["n_estimators"],
        min_samples_split=params["min_samples_split"],
        max_features=params["max_features"],
        max_samples=params["max_samples"],
        random_state=3,
        n_jobs=12,
    )
    rf.fit(X_train, Y_train)  # fit() with instantiated object
    # Y_predicted = rf.predict(X_test)  # Make predictions and save it in dict under key: name
    print(f"Optimized ({uf}) RandomForestRegressor elapsed time: {time.time()-t0} s")
    print(f"The score for Optimized ({uf}) RandomForestRegressor is: {rf.score(X_test, Y_test)}")
