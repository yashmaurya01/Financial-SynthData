import pandas as pd

splits = {'train': 'data/train-00000-of-00001.parquet', 'test': 'data/test-00000-of-00001.parquet'}
df = pd.read_parquet("hf://datasets/gretelai/gretel-financial-risk-analysis-v1/" + splits["train"])

#save data set
df.to_csv("gretel-financial-risk-analysis-v1.csv", index=False)