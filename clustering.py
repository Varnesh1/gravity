import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('stargravity.csv')

correct_distance = []

for planet_data in data:
  if planet_data[2] > 150 and planet_data[2] < 350:
    correct_distance.append(planet_data)

print(correct_distance)

 