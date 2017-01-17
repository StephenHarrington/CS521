### Jupyter and iPython notebooks

Python has a neat feature called iPython notebooks that allow for interactive python sessions and supports markdown language for powerful descriptions of code segments.  [Jupyter](http://jupyter.org/) is an extension of iPython that expanded the kernels available beyond just python, first with Julia and the R programming language (the name Jupyter is a combination of **JU**lia + **PYT**hon + **R**).

PyCharm supports Jupyter notebooks, but the installation process is somewhat painful, so do not worry if you are unable to install Jupyter under the PyCharm IDE, it is not required for completing any assignments.  You can use the [browser based version](https://try.jupyter.org/) for any notebooks that we might supply.


![Jupyter](https://github.com/StephenHarrington/CS521/raw/master/images/jupyter tryit.JPG "Jupyter")


#### Installing Jupyter in PyCharm

PyCharm has an excellent tutorial for installing Jupyter, see [here](https://www.jetbrains.com/help/pycharm/2016.3/using-ipython-jupyter-notebook-with-pycharm.html) and mainly copied below.  There are only two *gotchas*.

1. PyCharm comes with pip 7.1 installed, you need to upgrade to 9.1
2. PyCharm installs iPython 5.1 by default, you need to select iPython 3.2.3

*** Note. Installing and using Jupyter is optional and none of the course material requires you to use it ***


To extend the basic python that comes with PyCharm, you need to understand how to manage, install and upgrade packages.  One of the strengths of python is the number and quality of packages, everything from scientific computing, data visualizations, machine learning, web development frameworks and natural language processing.

To install or upgrade a package, open up the project and virtual environment as described in the JetBrains tutorial above.  Click on the "+" symbol in the upper right corner and circled in red in the image below.  This will bring up a long list of available packages.  Search and select ***pip***.  The default PyCharm installation is ***pip 7.1***.  Select pip and in the bottom right, check the box for ***Select Version***.  Highlight pip 9.1 and click install.

  
    
![pip 9.1 install](https://github.com/StephenHarrington/CS521/raw/master/images/jupyter4.JPG "pip 9.1 install")

  
  
  
Once you have the correct pip version installed, time to install Jupyter.  From the same package install screen, type in ***jupyter***, select the package from the list and click install.  The jupyter package contains many dependencies which PyCharm automatically installs for you.  Once completed, your package list should look like this:

  
    
![PyCharm packages](https://github.com/StephenHarrington/CS521/raw/master/images/jupyter2.JPG "PyCharm packages")


  
  
PyCharm installs iPython 5.1 by default, however this will not work with Jupyter on PyCharm, so you have to degrade the installation to iPython 3.2.3.  The "Select Version" has a drop-down menu, scroll down and select the 3.2.3 version for iPython.  Click install.

![iPython 3.2.3 downgrade](https://github.com/StephenHarrington/CS521/raw/master/images/jupyter5.JPG "iPython 3.2.3 downgrade")


That is it!  Congratulations, you have learned to install packages and installed Jupyter, a very useful package.

*** Note. PyCharm's Jupyter implementation is not optimal.  To use the full features, you need to either install Anaconda or use the browser based version ***

  
    
![Jupyter notebook in PyCharm](https://github.com/StephenHarrington/CS521/raw/master/images/jupyter6.JPG "Jupyter notebook in PyCharm")
  
    


#### Using the IPython prompt:

The IPython prompt looks something like this: `In [1]:`, and can be used to run Python code. You can type Python code directly into this prompt, and pressing enter executes the code fragment. The result of the computation is preceded by the words `Out []`.  

Try typing the following after the prompt and pressing the enter key:  
  
```python
In [1]: 3*5
```  
  
You should see:  
  
```python
Out [1]: 15
```

