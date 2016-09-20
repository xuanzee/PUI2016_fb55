# PUI2016 HW 3.

## ASSIGNED READING:

- [The Earth is Round (p<0.05)](http://ist-socrates.berkeley.edu/~maccoun/PP279_Cohen1.pdf) a critique of p-value based science


## ASSIGNMENTS:

### Assignment 1: Write an ipython notebook that demonstrates visually in a data-driven way the Central Limit Theorem. 
A skeleton notebook is [here](https://github.com/fedhere/PUI2016_fb55/blob/master/HW3_fb55/Assignment1.ipynb)

- ## GENERATE  100 samples of different sizes N (N>10 & N<2000) from each of 5 different distributions (500 samples in total), 
- ## _all with the same population mean_. Include a _Normal_, a _Poisson_, a _Binomial_, a _Chi-Squared_ distribution, and 1 more of your choice.                                       \n",
- ## For each sample plot the sample mean (dependent var.) against the sample size N (independent var.) (if you want you can do it with the sample standard deviation as well). 
- ## Describe the behavior you see in the plots in terms of the law of large numbers.
- ## PLOT the distributions of all sample means (together for all distributions). _Mandatory_: as a histogram. _Optional_: in any other way you think is convincing
## Extra Credit: FIT a gaussian to the distribution of means            

### Assignment 2: Set up the work for data-driven inference based on CitiBike data. You should, even more than usual, work in groups for this!

## Submission Info:
### You can work in groups, and you are encouraged to. Create a HW3\_\<netID> directory in your PUI2016\_\<netID> repository. Include a README.md that briefly summarizes the scope of the homework (so we know you understand what you did), and states with whome you worked and what you specifically contributed to.  Submit Assignment 1 and Assignment 2 by pushing the scripts into your PUI2016\_\<netID>/HW2\_\<netID>  repository. You can work on whatever computer you wish to develope these scripts. Work on Assignment 3 in the jupyter environment within CUSP (like you did for UCSL), so you have acces to the Data Facility. Keep in mind that we will look for possible cases of plagiarism, and if the code appears too similar to that of people that you did not work with to be original work (there are automated ways to look for plagiarism in code) *you will be penalized*. 
### I developed an example [here] (https://github.com/fedhere/PUI2016_fb55/blob/master/HW3_fb55/citibikes_gender.ipynb)

  
Work on [compute](https://github.com/fedhere/PUI2016_fb55/blob/master/computationalResources.md). 
Choose a citibikes [dataset within the CUSP data facility (DF)](https://datahub.cusp.nyu.edu/dataset).

1. Fire off a Jupyter notebook with Jupyter Hub --[here](https://datahub.cusp.nyu.edu/documents/guides/Jupyter_Notebook_from_your_browser_Mac.pdf) for Mac and Linux and [here](https://datahub.cusp.nyu.edu/documents/guides/Jupyter_Notebook_from_your_browser_Windows.pdf) for Windows--
and switch to the Kernel PUI2016_Python2 or PUI2016_Python3 from the Jupyter dropdown menu under Kernels -> Change Kernel.

   Write a Jupyter Notebook on compute. This will require you to use the JupyterHub ([instructions here](https://datahub.cusp.nyu.edu/documents/guides/Jupyter_Notebook_from_your_browser_Mac.pdf) ). Write a notebook that:

2. States the question you want to ask, and formulates the Null and Alternative hypothesis (remember the confidence level!)
3. Use pandas to read in the CitiBike files, either from the DF, or locally, but you must be able to download them on the spot (so the TA can reproduce your work). 
3. Display the top few rows of the DF in your notebook. This table __must be rendered__.
5. Display the reducted dataframe. This table __must be rendered__.
6. Plot your data distributions.

### GRADING: 

Your notebook must display
- the complete formulation of the hypothesis to be tested
- the data tables for the unreducted datasets (first few columns)
- the data tables for the reducted datasets (first few columns)
- the plots for each dataframe, with usual rules for plotting applying: visible and readable axes, title, legend, caption. 

Assignment 3: Finish z-test but lab and turn it in as a notebook.
