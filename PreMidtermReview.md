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
curl
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
If the destination is NOT a directory the file gets renamed to destination. 

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



