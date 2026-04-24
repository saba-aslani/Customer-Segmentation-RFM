import pandas as pd

def extract(path):
  # Load dataset
  df = pd.read_csv(path, encoding='ISO-8859-1')
  return df
