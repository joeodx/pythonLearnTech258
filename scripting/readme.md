# What is scripting in Python? 

![Python Logo](https://i0.wp.com/build5nines.com/wp-content/uploads/2023/02/Get_Started_Python_Scripting_Featured_Image.jpg)


Scripting refers to the process of writing scripts, which are sequences of commands that are interpreted or executed by a computer program rather than compiled into a standalone executable. Scripting is commonly used for automating tasks, controlling applications, and manipulating data.

Scripts are typically written in scripting languages, which are designed to be easy to read and write,
and often prioritize rapid development and flexibility over performance.
Scripting languages include Python, JavaScript, Bash, PowerShell, and many others.

Scripting is widely used in various fields such as system administration, web development, data analysis, and automation. It allows users to automate repetitive tasks, customize software behavior, and glue together different software components to create integrated solutions.
<br>
## How is it it different to programing?

Scripting languages prioritize simplicity and ease of use,
making them well-suited for tasks like system administration,
automation, and web development. On the other hand, programming
encompasses a broader range of activities and involves writing
larger, more complex software applications. 
<br>
<br>
Programming languages
are often compiled into machine code before execution, offering better performance but requiring more time and effort for development.
Overall, scripting is focused on quick automation and task-specific solutions, 
while programming is more comprehensive and geared towards building sophisticated 
software systems.
<br>
<br>

![Scripting Language vs Programming Language](https://visionx.io/wp-content/uploads/2023/03/Scripting-Language-vs-Programming-Language-300x300.png)
<br>
## What are packages in the standard python library?
In Python, packages are a way of organizing related modules into a hierarchical directory structure. A package can contain multiple modules and sub-packages. Packages allow for better organization, maintainability, and scalability of Python code.

There are a number of packages in the standard python library, but here are a few : 

* *random*: Python's built-in module for generating random numbers and selecting random elements from lists or sequences.
````python
  print(random.random(1,11))
````
Should print random number between 1 and 10 to terminal : 
````python 
5
````

* *math*: Python's built-in module providing mathematical functions and constants for mathematical operations.
````python
  num_float = 23.66
  print(math.ceil(num_float)) # round to the closest number up
````
should print to the terminal : 
````python 
24
````

* *os*: Python's built-in module for interacting with the operating system, allowing tasks such as file and directory manipulation, environment variables, and process management.
````python
 working_dir = os.getcwd()
 print(f"current Working directory is: {working_dir}")
````
should print the directory you are on to the terminal : 
````python 
current Working directory is: C:\Users\Joe O'Donovan\Desktop\tech 258\SpartaGitHub\python_learning\scripting
````
There are plenty more of packages that you can us. <br>
Check out the following link https://docs.python.org/3/library/index.html
<br>

## A list of Python scripts a DevOps engineer may use or create


* **Automated** Deployment Script : A script to automate the deployment of applications or services to various environments, such as staging or production.
<br>
* **Configuration** Management Script :  Script to manage configuration files across multiple servers or environments, ensuring consistency and scalability.

* **Monitoring** and Alerting Script : Script to monitor system metrics, logs, and application performance, and send alerts based on predefined thresholds or conditions.

* **Backup and Restore**  Script : Script to automate the backup of critical data or configurations and restore them when needed, ensuring data integrity and disaster recovery.

* **Infrastructure Provisioning** Script :  Script to provision and configure infrastructure resources such as virtual machines, containers, or cloud services, using Infrastructure as Code (IaC) principles.

* **Log Analysis** Script : Script to parse and analyze log files from servers, applications, or services, identifying trends, anomalies, and potential issues.

* **Security Compliance** Script: Script to automate security checks and compliance audits on servers, networks, and applications, ensuring adherence to security policies and standards.

* **Continuous Integration/Continuous Deployment (CI/CD) Pipeline** Script: Script to automate the CI/CD pipeline, including building, testing, and deploying applications or services, integrating with version control systems and other tools.

* **Resource Optimization** Script: Script to optimize resource usage and cost, such as automatically scaling infrastructure based on demand or identifying underutilized resources for optimization.

* **Infrastructure Monitoring and Reporting** Script: Script to collect and aggregate metrics and logs from various sources, generate reports, and visualize data to gain insights into system performance and usage trends.