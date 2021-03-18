import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = 'Hello, {}'.format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Tim'))

r = requests.get("http://coreyms.com")
print(r.status_code)


name = input("your name? ")
print("Hello,", name)
