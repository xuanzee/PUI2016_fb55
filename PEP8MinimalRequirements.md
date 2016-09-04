## Minimal PEP8 requitements:
The full list of PEP8 style guidelines is far longer https://www.python.org/dev/peps/pep-0008/ but here are the main tules that we will be strict about starting with the midterm.

- Maximum line length: 79 characters. you will not be failed if your lines get to 85 or anything like that, but dont get crazy with the line length

- import packages one at a time:
  ```
  import os
  import sys
  ```
  instead of:

  ```
  import os,sys
  ```
- use descriptive name variables:
  ```
  ridesByZip = ...
  ```
	instead of:
  ```
  rzp = ...
  ```
	or even worse:
	```
	a = ...
	```
	that way we can read your code if needed and understand what you did. That may save 
  you if your code does not run for silly reasons: if we can fix it we may award partial 
  points (if the reason is silly enough)

- use spaces between operators:   
	```
  	a + b
	```
  instead of:
	```
	a+b
  	```
  	
- if you use the try/except syntx name your allowed exceptions:

  	```
  	try: 
  		do_blah()
  	except ValueError, IndexError:        <or wwhatever exceptions you want to allow>
		pass <or whatever you need to do>
   	```
  instead of: 
  	```
   	try: 
    		do_blah()
  	except:
		pass
  	```
- indent by 4 spaces, not by tabs
