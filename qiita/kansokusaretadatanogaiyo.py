from IPython.display import display
import pandas as pd

d = pd.read_csv("res/data.csv")
display(d.dtypes)
