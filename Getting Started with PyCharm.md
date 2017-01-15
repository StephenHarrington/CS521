### Getting Started in CS521


If you are new to Python, the CS521 facilitators recommend that you download [PyCharm](https://www.jetbrains.com/pycharm-edu/download) as your IDE (Integrated Development Environment), but you are welcome to use any other IDE that you are familiar with; for example [Anaconda](https://docs.continuum.io/anaconda/install#) is also a popular IDE.  We also support the IDLE interpreter that comes with the install from [python.org](https://www.python.org/downloads/).


This note explains how to set up Python and introduces you to pyCharm, the Python development environment we will be using throughout this course.  

#### DOWNLOAD THE PYTHON INSTALLER

Download the free [PyCharm Edu IDE](https://www.jetbrains.com/pycharm-edu/download).  The initial download is about 160M, depending on which operating system you use with Mac, Windows and Linux all supported.

![pyCharm Download](https://github.com/StephenHarrington/CS521/raw/master/images/pycharm1.JPG "pyCharm Splash Screen")


Alternatively, you can use either the IDLE interpreter from [python.org](https://www.python.org/downloads/) or [“Anaconda” Python distribution](https://www.continuum.io/downloads).  The Anaconda install may take some time since it contains the base Python 3.5 version as well as some packages you will find useful.   

*** Note.  CS521 uses Python 3.X (either 3.5 for pyCharm or 3.6 for IDLE), do not use Python 2.7 since all grading will assume Python 3.X ***

##### Operating Systems: 
Any of the popular IDEs (pyCharm, IDLE and Anaconda) will provide executable Windows installers.  Make sure to use the 32-bit **or** the 64-bit Windows versions, whichever is supported by your computer.  Microsoft provides instructions [here](https://support.microsoft.com/en-us/help/15056/windows-7-32-64-bit-faq) to determine whether you have a 32-bit or 64-bit setup. If you are running 32-bit Windows, be sure that you select the 32-bit version, and if you are running 64-bit Windows, you can download either version.    

*** Note. pyCharm and IDLE defaults to the 32-bit version when being installed on Windows. ***

The Macintosh Operating System (OS X) only provides 64-bit installers and that is the default for most python IDEs.

IDEs for Linux Operating Systems provides both 32-bit and 64-bit versions.


#### INSTALLING pyCharm

To install pyCharm after downloading the graphical installer, double click the .exe (Windows) or .pkg (Mac) file and follow the instructions on the screen.  

**Note. pyCharm's Python distribution may default to Python 2.7.  Make sure to select Python 3.5**


![pyCharm python version](https://github.com/StephenHarrington/CS521/raw/master/images/pycharm4.JPG "python 3.5")


When installing python, a pop-up menu may ask whether or not to “Add pyCharm to my PATH environment variable”, and “Register pyCharm as my default Python 3.5.” We suggest accepting both options for the purposes of this class.

The installation should take take about 15 minutes.


#### STARTING THE CODE EDITOR

When you download and install the pyCharm distribution of Python, you are getting several tools related to Python development. One of the tools is the JetBrains PyCharm Edu editor, an integrated development environment useful for writing, running, and debugging code. From the windows start menu click on PyCharm:

![windows start menu](https://github.com/StephenHarrington/CS521/raw/master/images/start%20menu%20showing%20pythons.JPG "python IDEs")



#### PyCharm APPLICATION OVERVIEW

Opening PyCharm should present you with the following window (screenshots are from a Windows machine, but a similar window should appear for MAC OS and Linux). This window contains two commonly used options, among others:

1. Create a New Project that lets you create and edit existing Python source files  
2. Introduction to Python, which guides you through a quick introduction to the Python programming language    


![PyCharm](https://github.com/StephenHarrington/CS521/raw/master/images/pycharm5.JPG "PyCharm")

  
    
      
      

A useful feature of PyCharm is the Introduction to Python.  Clicking on that option brings up the window shown below.  Note that there is a warning message telling you that an interpreter must be configured for the program to execute.  
  
    
    
![Intro](https://github.com/StephenHarrington/CS521/raw/master/images/pycharm6.JPG "Introduction to Python")
  
    
    

**Note. When you first start PyCharm, you must associate an interpreter (python version) with the code.**
  
    
    
Clicking on the link in the warning message brings up PyCharm's configuration settings.  On this machine, both Python 2.7 and Python 3.5 are available.  Make sure to configure using the Python 3.5 interpreter!  
  
    
    
![Interpreter](https://github.com/StephenHarrington/CS521/raw/master/images/pycharm7.JPG "Interpreter")

  
  
You may want to start PyCharm and make sure the Python 3.5 interpreter is associated with your code files.  


The Introduction to Python is a use tool to get familar with some of the basics of the python language as well as to familiarize yourself with the PyCharm IDE.  

Have fun!  

Stephen Harrington
January 15, 2017
 
