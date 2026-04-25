import pandas as pd

def extract(path):
  # Load dataset
  df = pd.read_csv(path, encoding='utf-8-sig')
  return df
