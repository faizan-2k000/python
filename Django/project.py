
# Are called query strings
# field1=value1&field2=value2&field3=value3...

# for example:
# https://www.google.com/search?q=harvard&sxsrf=AKL5yDj4-4t35eKCe0AdnR_KSK_78_gy-Q%3A1795501830306&atvm=2

# where an = separates the name of the parameter from its value, and the & symbol separates parameters from one another. 

# its the way form submits information to web server, by encoding the form data in the URL.

# q=Harvard
# q is the name, short for “query” and Harward is the value, pair of both are called GET Parameters
# It turns out that, while the other parameters provide useful data to Google, only the q parameter is required to perform a search. yourself by visiting https://www.google.com/search?q=Harvard, deleting all the other parameters. You should see the same Google results!

# **********************************************
# Introduction:
# for Dynamic web application, to dynemaically generate html and css

# HTTP (Client Server Request Process):
# we are going to create software that will run on web server. client can make request and server going to respond back using HTTP protocol, how messages are sent back and forth over the internet (client server request tranfer), 
# Server contain web application. Django will run on server and client are going to make request to that server, server will process the request and then return some sort of response.

# Request example (HTTP version 1):
#       GET / HTTP/1.1
#       Host: www.example.com 
#       ...
# GET is a example of request method, a way that you might try to get a page, like "I would like to get a particular page", in this case, slash "/" is the page I am trying to get
# 1.1 is the version of HTTP
# Host is the URL we are tying to access the web page for
#  Request will sent by browser. Any search on browser is the request server get, process and return/response
# Response example:
#       GET / HTTP/1.1 200 OK
#       Content-Type text/html
#       ...
# 200 OK is a response code, like the page was return succesfully
# Content-Type text/html is the fomat of the data that's coming back in this response which is html data

# Status code   |   Descripteion
    # 200       |   OK
    # 301       |   Moved Permenantly (you redirect from one site to another)
    # 403       |   Forbidden (You are trying to get access which is not allowed to you)
    # 404       |   Not Found
    # 500       |   Internal Server Error
         
# Django Framework make user free from the usual stuff so the developer can focus on the intersteing logic of building

# pip (python package manager)

# Install Django Framework
#     cmd: pip3 install Django
# pip3, as we are using python 3 

# To create Django Project:
#   cmd: django-admin startproject PROJECT_NAME 
#   it will create a stater files to be ready to process of building web application