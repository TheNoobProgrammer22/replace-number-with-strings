import pandas as pd
file_handler = open("car.csv", "r")
data = pd.read_csv(file_handler, sep=",")
file_handler.close()
data.buying[ data.buying == 'low'] = 1
data.buying[ data.buying == 'med'] = 2
data.buying[ data.buying == 'high'] = 3
data.buying[ data.buying == 'vhigh'] = 4
data.to_csv("car_example.csv")