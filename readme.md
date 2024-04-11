# Tech 258 - Understanding Python

![Python Logo](https://www.python.org/static/community_logos/python-logo-master-v3-TM-flattened.png)


## **What is Python where did it come from?**

Python is a computer programming language often used to build websites and software, automate tasks, and analyze data. A general-purpose language, used to create various programmes and isn’t specialised for any specific problems.
Thanks to its similarity with English syntax, Python is widely considered to be one of the easiest programming languages to write, read, and learn.<br>  professionals with little to no computer programming experience can pick up basic Python skills and scale them to more advanced coding techniques.
Python’s journey began in the late 1980s, where it was created by a dutch programer called Guido Van Rossum, who was trying to build a sucessor to the ABC programming language.

````python
print("Hello World")
````
## **Why is it so popular within DevOps?**

There are a number of reasons but the main ones are as follows : 
* *Versatility*: Python is a versatile language that supports multiple programming paradigms, including procedural, object-oriented, and functional programming.<br>
* *Community Support* : Python has a large and active community of developers who contribute to the language's development, maintain open-source projects, and provide support through forums, mailing lists, and online communities. <br>
* Integration Capabilities: Python's ability to easily integrate with other languages and tools makes it a valuable asset in the DevOps toolkit. It can interact with APIs, command-line tools, databases, and other systems, allowing DevOps engineers to automate tasks, orchestrate workflows, and build integrations between different tools and technologies.

![LinkedIn Article Cover](https://media.licdn.com/dms/image/C4E12AQFqu7-5lbuTeA/article-cover_image-shrink_720_1280/0/1615899327262?e=2147483647&v=beta&t=6oqgKfsK1OfmFzOMTydTZ7PY5dEL4ns_2a9k0dKate0)

## **What is a virtual environment?**
A virtual environment, often abbreviated as venv, is a self-contained directory that contains a specific version of Python interpreter along with a set of additional packages and dependencies. Virtual environments are used to isolate Python projects, ensuring that each project can have its own dependencies without affecting other projects or the system-wide Python installation.

By creating a virtual environment for each project, developers can manage dependencies more efficiently, avoid conflicts between different versions of packages, and ensure reproducibility of their projects across different environments.


## **What is a "PIP"?**

"Pip" is a package manager for Python, used to install and manage third-party packages and libraries that are not included in the Python standard library. It simplifies the process of installing, upgrading, and removing Python packages, making it easier for developers to manage dependencies for their projects.

With pip, developers can install packages from the Python Package Index (PyPI), a repository of software packages for Python. PyPI hosts thousands of open-source Python packages, covering a wide range of functionalities, including web development, data analysis, machine learning, automation, and more.

![Pip package manager in Python](https://ioflood.com/blog/wp-content/uploads/2023/09/Pip-package-manager-in-Python-command-line-interface-package-installation.jpg)

## **What is the difference between scripting and programming?**

Scripting and programming are often used interchangeably, but they have subtle differences. Scripting typically involves writing small programs or scripts to automate specific tasks or perform simple operations. These scripts are interpreted, executed line by line by an interpreter like Python, Perl, or Bash, without being compiled into machine code beforehand. Scripting languages are commonly used for system administration, web development, and automation. In contrast, programming encompasses a broader range of activities, including designing algorithms, organizing code into modules or classes, and optimizing performance.
## **Are there python libraries? What are some examples?**
Python comes with a comprehensive standard library that provides a wide range of modules and packages for various tasks. Some of the base/inbuilt Python libraries include:
* 'OS' <br> 
* 'SYS'<BR>
* 'math'
* 'random'


* TensorFlow'
* 'Django'
* 'Flask'

![Python Libraries for Machine Learning](https://analyticsdrift.com/wp-content/uploads/2022/10/python-libraries-for-ML.jpg)

## **Loops & Python...<br> What are the different types? <br>And what can we do with them?**


Loops are control structures in programming that allow you to execute 
a block of code repeatedly until a certain condition is met. 
There are mainly two types of loops: for loops and while loops.

*  A ```for``` loop is used when you know in advance how many times you want to execute a block of code. 
* It typically has a predefined iteration variable that changes each time through the loop.
```python
languages = ['JavaScript', 'Python', 'Ruby']

# Iterate over each element in the list
for language in languages:
    # Check if the letter 'p' exists in the string
    if 'p' in language.lower():
        print(language)

```

````python
# Should return
Python
````
* A ```while``` loop is used when you want to execute a block of code repeatedly as long as a condition is true. 
* It keeps looping as long as the condition remains true.
````python
number = 1

while number <= 3:
    print(number)
    number = number + 1
````
````
# Should return
1
2
3
````



Loops in Python are incredibly versatile and can be used for a variety of tasks. 
Here are some common use cases:

* Iterating over sequences: Loops can iterate over lists, tuples, strings, dictionaries, and other iterable objects.
* Repeating a block of code: Loops allow you to execute a block of code multiple times without duplicating it.
* Searching and filtering: Loops can be used to search for specific elements or filter out elements based on certain conditions.








