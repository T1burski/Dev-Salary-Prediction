import pandas as pd
from preprocessing import Preprocess
from model import Modeltrainer
import pickle
import warnings

warnings.filterwarnings('ignore')

df = pd.read_csv("data/dataset.csv")
df_ingestion = Preprocess(data=df).total_preprocess()

preprocessed_regressor = Modeltrainer().preprocessor()

X = df_ingestion.drop(columns=["Salary"])
y = df_ingestion["Salary"]

preprocessed_regressor.fit(X, y.values.ravel())

with open('artifacts\model_regressor.pkl', 'wb') as model_file:
    pickle.dump(preprocessed_regressor, model_file)