from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from category_encoders import LeaveOneOutEncoder
from sklearn.compose import ColumnTransformer

class Modeltrainer:

    def __init__(self):
        self.regressor = KNeighborsRegressor(n_neighbors = 30, p = 1, weights = 'uniform')
        self.standardizer = MinMaxScaler()

    def preprocessor(self):
        columns_trans = ColumnTransformer(
            transformers=[
                ('leaveoneout', LeaveOneOutEncoder(), ["Country", "DevType"]),
                ('onehot', OneHotEncoder(handle_unknown='ignore'), ["EdLevel"])
            ], 
            remainder='passthrough'
        )

        preprocessor = make_pipeline(
            columns_trans,
            self.standardizer,
            self.regressor
        )

        return preprocessor
