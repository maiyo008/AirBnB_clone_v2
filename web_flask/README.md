# 0x04. AirBnB clone - Web framework

## Resources
**Read or watch:**

* [What is a Web Framework?](https://intelegain-technologies.medium.com/what-are-web-frameworks-and-why-you-need-them-c4e8806bd0fb)
* [A Minimal Application](https://flask.palletsprojects.com/en/1.0.x/quickstart/#a-minimal-application)
* [Jinja](https://jinja.palletsprojects.com/en/2.9.x/templates/)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

**General**
* What is a Web Framework
* How to build a web framework with Flask
* How to define routes in Flask
* What is a route
* How to handle variables in a route
* What is a template
* How to create a HTML response in Flask by using a template
* How to create a dynamic template (loops, conditions…)
* How to display in HTML data from a MySQL database

## More Info

Install Flask
```
$ pip3 install Flask
```
![Web framework](https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step3.png)


## Tasks

### Task 0. Hello Flask!
<Details>
Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
    * /: display “Hello HBNB!”
* You must use the option strict_slashes=False in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 
```
</Details>

### Task 1. HBNB
<Details>
Write a script that starts a Flask web application:

* Your web application must be listening on 0.0.0.0, port 5000
* Routes:
    * `/`: display “Hello HBNB!”
    * `/hbnb`: display “HBNB”
* You must use the option strict_slashes=False in your route definition
```
guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
```
In another tab:
```
guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ * 
```
</Details>