import pandas as pd
import numpy as np


sonar_data = pd.read_csv("Copy of sonar data.csv")

print(sonar_data.iloc[:,60])