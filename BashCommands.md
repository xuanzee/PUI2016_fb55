**Common and useful BASH comands**

_pwd: present working directory_
    tells you what the directory you are working in is. Many people (like me) set up their prompt to indicate the path to the present working directory. 
    Note the ~ symbol in my prompt. That is the symbol indicateing your home directory.
    
_cd: lets you move to a directory_ 
    - cd without argument takes you to the home directory
    - cd - (minus sign) takes you to the directory where you were working before
    - cd <path> takes you to <path> where <path> is the full or relative path to a directory (relative means everything after the directory you are already in. absolute means starging with the original directory in the file system. in this case "/home". so i went to "/home/fbianco/..." which is equivalent to "~/..."
    
_ls: lists the content a directory_ 
    - ls without argument lists the content of the present working directory 
    - ls with an argument lists the content of the directory given as argument (if it exists). It also  lists a file if a file is given as argument (Untitled.ipynb for example). The usefulness of that resides in the ability to use it with "wildcards": caracter that can mean multiple things. For example '*' means basically anything. So ls Screen* will list all files in the pwd starting with "Screen"
    - ls -l will list information about the files it lists, including permissions, ownership, size, and last modification time stamp
    
_mkdir: creates a directory_ 
    It requires the name of the directory as argument.

_touch: creates a file_ 
    It requires the name of the file as argument. 
    The file created is empty. 
    It also changes the timestamp of a file, without changing the file. 
    
cp: copies a file
    -the first argument is the file to be copied
    - if the second argument is not an existing directory it is interpreted as the destination name, and the file is copied to a file by that name
    - if the second argument is the path to an existing directory a copy of the file is deposited in that directory. (note that I used ../ to indicate a directory before the pwd)
    
mv: moves a file
    Same behavior as cp, but removes the original file
    
rm: removes a file
    - the argument(s) is(are) the file(s) to be removed. THIS CANNOT BE UNDONE
    - if the argument is a directory you must add "-r" to demove the content of the directory "recursively"
    
echo: prints to standard output (i.e. to the terminal)
    - the argument is what gets printed
    - >> means "redirect" and if used with for example echo the command will then print to wherever you are redirecting the content. You need a file name after >> (exisiting or not)
    
less: opens the file for vieweing in a buffer
    - requires the file name as argument
    (you exit the less buffer by typing 'q')
    
    (less is fine if the file is small. but for large files it may need a lot of memory)
    
head: shows the top of a file (10 lines by default)
    - argument: file name
    - adding "-N" will change the behavior to show N lines
    
tail: same as head but shows the bottom of the file

grep: shows all files in the pwd (or a given path) containing a given string
    - arguments: the string to look for
    - the files where to look. e.g. "*" means everywhere in the pwd
    - it prints to standard output the file name, ":", the entire line where the content is found.
    
**Lets move to commands that run things, instead of commands that deal with files. **


top: shows the current running processes (dynamically updated)
    - no arguments: shows all processes
    - arguments are allowd. for example -U fbianco shows all processes owned by user fbianco
    - shows CPU, Memory, time running, state....
    
ps: shows all running processes ID and name only (static)

bg: puts a process in the background
    (that way you can use the same shell that started the process) first you must put the process to sleep with Control+z. If you just type Control+Z the process becoms inactive: bg makes the process run in the background. )

fg: puts a sleeping process or a background process back in the foreground

**Connecting to other machines and moving files.**

You can work remotely on a machine connected to the internet.

_ssh: secure shell_ connects your terminal to another terminal
    - the full address of the remote machine. 
    **at CUSP to connect to a CUSP machine you have first to connect to gw (gateway) like I just did, then you can connect to another CUSP machine, for example compute. 
    **gw.cusp.nyu.edu is NOT A MACHINE EHRE YOU CAN WORK. it is only used as a "gateway" to the rest of the CUSP machines.
    (Control-d closes the connection)
    
to connect to compute and enable the use of windows (text editors for example) you need to use a few keyword when you connect. I saved the full command to connect to compute.cusp.nyu.edu in an "alias" called "computeme". The full command is 
ssh -X -A -t gw.cusp.nyu.edu ssh -A -X compute
(this version assumes that the user name on your machine and on compute are the same. otherwise you need to specify it: 
ssh -X -A -t fbianco@gw.cusp.nyu.edu ssh -A -X compute
)










    