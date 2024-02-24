import sys 
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer  # ColumnTransformer is basically used for pipeline
from sklearn.impute import SimpleImputer # this is used for handling missing values
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os 

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self): 
        # this funtion is basically used for data tranformation
        try:
            numerical_columns = ["writting_score", "reading_score"]
            categorical_columns= ["gender", "race_ethnicity", "parental_leval_of_education", "lunch", "test_preparation_course"]

            num_pipeline= Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler())
                ]
            )

            cat_pipeline= Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder())
                    ("scaler", StandardScaler())

                ]
            )
            logging.info("Numerical columns standard scaling completed")

            logging.info("Categorical columns encoding completed")

            preprocessor=ColumnTransformer(
                [
                    ("num-pipeline", num_pipeline, numerical_columns),
                    ("cat-pipeline", cat_pipeline, categorical_columns)
                ]
            )

            return preprocessor
        

        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_transformation(self, train_path, test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read Train and test data completed")
            logging.info("Obtaining preprocessing object")
        except:
            pass