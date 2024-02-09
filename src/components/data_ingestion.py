import os
import sys
import pandas as pd
from dataclasses import dataclass
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split



class DataIngestionConfig():
    train_data_path=os.path.join("artifacts","train.csv")
    test_data_path=os.path.join("artifacts","test.csv")
    raw_data_path=os.path.join("artifacts","raw.csv")


class DataIngestion():
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()
    
    def initiate_data_ingestion(self):
        logging.info("Starting data ingestion")
        try:
            df=pd.read_csv("raw.csv")
            logging.info("raw data reading complete")
            
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            
            df.to_csv(self.ingestion_config.raw_data_path)
            
            
            train_set,test_set=train_test_split(df,test_size=0.25,random_state=42)
            logging.info("train and test split is done")
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            
            logging.info("data ingestion complete")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

   
        except Exception as ex:
            raise Exception
        
if __name__ == "__main__":
    data_ingestion=DataIngestion()
    data_ingestion.initiate_data_ingestion()