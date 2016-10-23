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
You can download data with bash line commands. For example to download the data you can use the 
```
curl
```
or
```
wget
```
commands. You can run those from the python code as 
```
!curl -O http://some.url.here
```
or 
```
url = "http://some.url.here"
os.system("curl -O " + url)
```

In this case you MUST ALSO move the data to a directory pointed to by an environmental variable $PUIDATA. The directory MUST EXIST and BE A DIRECTORY before you move data to it with the command mv. Look at https://github.com/fedhere/PUI2016_fb55/blob/master/BashCommands.md if you have doubts about how to run these commands: cp and mv take 2 arguments, origin (the file you want to move) and destination (what you want to move it to). 

Notice how I used the "!curl" command when I hard-coded the url link in the command (spelled it directly in there), and I used "os.system" instead when the url was generated from a variable. If you know all the pieces of the command you can use "!", otherwise you can use "os.system" passing it as argument the string you want to be executed on the shell. e.g.:

```
os.system("mv data.csv " + os.getenv("PUIDATA"))
```
*If the destination is NOT an **existing** directory the file gets renamed to destination. *

Note also that since you **always** want to refer to the directory where the data is stored using the environmental variable PUIDATA, which is a variable, every time you want to use it you do not have all the pieces of the command: you need to create the command from the variable!

**Recommandations:** before running a command with os.system() print the string you want to pass it to verify you have created it properly! It is easy to miss spaces, or "/" in the construction of the strings! e.g.

```
cmdstr = "mv data.csv " + os.getenv("PUIDATA")
print (cmdstr)
```
then if you like what you see
```
os.system(cmdstr)
```

### 2. API data access

APIs allow us to access data interactively. The trick is to create the link that requires the sepcific data you want. 

Review HW2 where you used the API for MTA and the solution of HW5 
https://github.com/fedhere/PUI2016_fb55/blob/master/HW5_fb55/solutions/citibikes_goodness_of_fit_solution.ipynb
where I *use the google API to **reversegeocode** coordinates and get zip codes out of citibike data.*

Two things to be noticed: if you are asked to use an API you may need an API key. **Never hard-code your API key in the code**. Set an environmental variable (like I did in HW5, and like you did in your first homework) and use that to create the url. E.g.:
```
url = ("https://maps.googleapis.com/maps/api/geocode/json?latlng=" +
           "%f,%f&key=%s"%(
            latlon[0], latlon[1], os.getenv('GOOGLEAPI')))
```
look in detail at the link above: typical the link is static (the same for all requests) up to a "?" character. 
then begins the customization: here I want to get the reversegeocodes coordinates latitude and longitude (i.e. I know the coordinats and want a zipcode). URLs that start with "https://maps.googleapis.com/maps/api/geocode/json?latlng=" are designed for that, then the long and latitude values are the next piece of the url, for example: "https://maps.googleapis.com/maps/api/geocode/json?latlng=40.750020,-73.969053" .
Next (and last) the API wants the key. Variables passed to the API are generally separated by "&", followed by the name of the variable. In this case the name for the API key is "key" so the rest of the url goes: 
"https://maps.googleapis.com/maps/api/geocode/json?latlng=40.750020,-73.969053&key="
and then you pass it your key, which is a variable, so 
```
url = ("https://maps.googleapis.com/maps/api/geocode/json?latlng=" +
           "%f,%f&key=%s"%(
            latlon[0], latlon[1], os.getenv('GOOGLEAPI')))
```
returns 
```
https://maps.googleapis.com/maps/api/geocode/json?latlng=40.750020,-73.969053&key=XXXX-XXXX-XXXX
```
(where I replaced by key with XXXX-XXXX-XXXX because one should &**never share API keys** since if they are used illegally the owner of the key is legally responsible!)

**Important!: API usually limits the access to data to a certein number of requests per minute, or per hour, or per day.** Do not simply put API requests in a for look and just hammer away till you get it right! Do not submit the same request over and over again! If you get shut down for an hour you have lost 1/3 of the midterm time!! For example, in the EC in HW5 I am only asking the zipcode of each station once, by identifying the rides that originate from the same station ahead of time. This frops the number of requests from *hundreds of thousannds to ~100!*




