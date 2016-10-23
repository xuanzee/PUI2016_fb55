# PreMidterm review Friday 10/21

## These are topics we reviewed o Friday in sight of the midterm.


## - Data access

You may be required to access data in any of the way we have accessed data in the class: 
1. By direct url access.
2. Through an API.
3. From the DataFacility. 

You will not be required to access data from databases, of course, since we have not covered that yet in PUI.

### 1. Direct URL access: if you are given the link to a dataset, or directed to find such a link,
may be able to access the data directly :
```
import pandas as pd
c = pd.read_csv("https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv")
print(c)
```
or you may need to download the date (e.g. if it is a zipped csv, like the citibike data).




