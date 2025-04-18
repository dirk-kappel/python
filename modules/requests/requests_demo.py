import requests

# Grab a web page

url = 'https://xkcd.com/353/'

r = requests.get(url)

print(r) # Will print out a 200 response
print(dir(r))   # Shows all the methods that can be used on r
# print(help(r))  # A more detailed explanation of everything on the object

# Print out the content of the source
print(r.text)

# To download the image
image_url = 'https://imgs.xkcd.com/comics/python.png'
r = requests.get(image_url)
# print(r.content)  # This will print out the bytes of the image

# To save to the machine
with open('comic.png', 'wb') as f:   # Use wb mode to write as bytes
    f.write(r.content)

# Check if we got a good response (status code)
print(r.status_code)  # 200
print(r.ok, end='\n\n')           # True for anything less than a 400 response

print(r.headers, end='\n\n')      # The headers returned with the response

# This is a testing website
payload = {
    'page': 2,
    'count': 25
}
url_test = 'https://httpbin.org/get'

# GET
r = requests.get(url_test, params=payload)  # Send the parameters (arguments) as dictionary defined above
print(r.text)
print(r.url)  # This will show what we requested. It is better than entering manually since that is prone to errors

# POST
payload = {
    'username': 'penny',
    'password': 'testing'
}
url_test = 'https://httpbin.org/post'
r = requests.post(url_test, data=payload)  # data is used by post to send data
print(r.text)
print(r.json(), end='\n\n') # This will return a python dictionary from the json response
# Capture in a python dictionary
r_dict = r.json()
print(r_dict['form'], end='\n\n') # Access a value from the dictionary

# Basic authorization

url_basic_auth = 'https://httpbin.org/basic-auth/penny/testing'
r = requests.get(url_basic_auth, auth=('penny', 'testing')) # The auth tuple is the username and password
print(r.text, end='\n\n')
# Wrong credentials
r = requests.get(url_basic_auth, auth=('penny', 'wrong_password')) 
print(r.text) # There will be no response text
print(r, end='\n\n')  # 401 response

# Set a timeout with a request
from requests.exceptions import ReadTimeout
url_basic_delay = 'https://httpbin.org/delay/5'
try:
    r = requests.get(url_basic_delay, timeout=3)  # Will result in a ReadTimeoutError exception
except ReadTimeout as e:
    print('Read Timeout:', e)