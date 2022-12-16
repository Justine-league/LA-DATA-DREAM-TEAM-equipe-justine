import matplotlib.pyplot as plt
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import explained_variance_score, mean_absolute_error
from time import time
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import ExtraTreesRegressor, RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor

data_base = pd.read_csv("ressources/data_without_zero.csv")
# Perform Scaling
from sklearn.preprocessing import StandardScaler


class Model_predict_price:
    trained_models = {
        # "KNeighborsRegressor": [],
        # "GradientBoostingRegressor": [],
        # "ExtraTreesRegressor": [],
        "RandomForestRegressor": [],
        # "DecisionTreeRegressor": [],
        # "LinearRegression": [],
        # "Lasso": [],
        # "ElasticNet": [],
        # "Ridge": [],
    }
    index_models = [
        # "KNeighborsRegressor",
        # "GradientBoostingRegressor",
        # "ExtraTreesRegressor",
        "RandomForestRegressor",
        # "DecisionTreeRegressor",
        # "LinearRegression",
        # "Lasso",
        # "ElasticNet",
        # "Ridge"
    ]
    data = data_base[["product_price", "weight", "lenght", "height", "width", "distance", "prix_de_livraison"]]
    data = data.dropna()
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]

    sc = StandardScaler()
    X_sc = sc.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X_sc, y, test_size=0.4)

    regressors = [
        # KNeighborsRegressor(),
        # GradientBoostingRegressor(),
        # ExtraTreesRegressor(),
        RandomForestRegressor(),
        # DecisionTreeRegressor(),
        # LinearRegression(),
        # Lasso(),
        # ElasticNet(),
        # Ridge()
    ]

    head = 10
    for model in regressors[:head]:
        start = time()
        print(regressors[:head].index(model))
        trained_models[index_models[regressors[:head].index(model)]].append(model.fit(X_train, y_train))
        train_time = time() - start
        start = time()
        y_pred = model.predict(X_test)
        predict_time = time() - start
        print(model)
        print("\tTraining time: %0.3fs" % train_time)
        print("\tPrediction time: %0.3fs" % predict_time)
        print("\tExplained variance:", explained_variance_score(y_test, y_pred))
        print("\tMean absolute error:", mean_absolute_error(y_test, y_pred))
        print("\tR2 score:", r2_score(y_test, y_pred))

    def predict_ExtraTreesRegressor(self, to_train):
        res = self.trained_models['ExtraTreesRegressor'][0].predict(to_train)
        print(res)
        return res
    def predict_RandomForestRegressor(self, to_train):
        res = self.trained_models['RandomForestRegressor'][0].predict(to_train)
        print(res)
        return res


