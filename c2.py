import pandas as pd
import seaborn as sns

#loading the dataset
house_price = pd.read_csv('/home/nalin/Desktop/LABSML/ML_LAB1_Assignment/house_price_data.csv')

#displays the first few rows
house_price.head()

#analysing the data using pairplots : 

sns.stripplotplot(house_price[['property_id','neighborhood','distance_to_city_center','sale_price']], hue = "distance_to_city_center")


