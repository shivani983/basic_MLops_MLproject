import os

os.system("python src/data_ingestion.py")
print("data ingestion done")
os.system("python src/data_preprocessing.py")
print("data preprocessing done")


os.system("python src/feature_engineering.py")
print("feature engineering done")

os.system("python src/model_building.py")
print("model building done")

os.system("python src/model_evaluation.py")
print("model evaluation done")