import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt

trends = TrendReq()

trends.build_payload(kw_list=['Machine Learning'])

data = trends.interest_by_region()
date = data.sort_values(by="Machine Learning")

data = data.head(10)

print(data)