#Two Hour Python Hacker

2 hours from now we hope to have a small application on the cloud!

There are a number of things we want to accomplish today. 

1. Install Python
2. use the REPL
3. Run our first program
4. Install a package - (Flask)
5. Uninstall a package
6. Install virtualenv
7. Install virtualenvwrapper or virtualenvwrapper-win
8. Create a virtual environment
9. Install flask and run our first app
10. Get access to an API
11. Create a webapp
12. Deploy

#Let's do this


## 1. Install Python

[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/)

[Mac](http://docs.python-guide.org/en/latest/starting/install/osx/)

## 2. use the REPL

The REPL stands for Read Evaluate Print Loop

Makes iterating and testing easy! 

python

'>>>'

try these commands:

x = 2 + 2

print x 

import this

[More Practice](http://timmyreilly.azurewebsites.net/python-introduction/)

## 3. Run our first program

Use your favorite text editor. I'm using [Visual Studio Code](https://code.visualstudio.com/)

beginnings.py

```python 
sentence = "Four score and seven years ago"
sentence_no_vowels = ""
for letter in sentence: 
    if letter not in "AEIOUaeiou":
        sentence_no_vowels = sentence_no_vowels + letter
         
print sentence_no_vowels
```

## 4. Install a package
	
Python Packages are installed with pip

We'll install [requests](http://docs.python-requests.org/en/latest/)

```
pip -v

pip install requests
```

## 5. Uninstall a package

```
pip uninstall requests

```

## 6. Install virtualenv

```
pip install virtualenv
```

## 7. Install virtualenvwrapper or virtualenvwrapper-win

virtualenv wrappers make it easy to manage multiple environments and can make iterating on project easy. 

[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/)

[Mac](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

## 8. Create a virtual environment

```
mkvirtualenv helloworld
```

cd into root of project

```
setprojectdir .

deactivate

workon helloworld
```


## 9. Install flask and run our first app

Now we need [flask](http://flask.pocoo.org/) for our first website!

```
pip install flask
```

Create our hello.py

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
```

SWEET!

```
python hello.py
 * Running on http://localhost:5000/
```

## 10. Get access to an API

[Bing Search](https://datamarket.azure.com/account)

[Project Oxford](https://www.projectoxford.ai/)

## 11. Create a webapp

We'll start from a project I've already built: 

[My Guide for Azure](http://timmyreilly.azurewebsites.net/starter-site-for-flask-on-azure-web-apps/)

## 12. Deploy

GIT deploy!
[Same Guide as above](http://timmyreilly.azurewebsites.net/starter-site-for-flask-on-azure-web-apps/)


## WEEEE!


Please contact me if you have any questions: 
[@timmyreilly](http://twitter.com/timmyreilly)