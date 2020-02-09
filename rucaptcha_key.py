import os

dirname = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(dirname, "resources/rucaptcha_key")

try:
    RUCAPTCHA_KEY = open(filepath).readline()
except FileNotFoundError:
    info_message = """You now have to provide a key to rucaptcha_key service to be able to pass your captcha to service for it to be solved manually.
To do so, one may add a file named 'rucaptcha_key' with a string containing his app's access token to resources folder of the project
How to obtain rucaptcha_key: https://rucaptcha.com/api-rucaptcha#solving_captchas
"""
    print(info_message)
    access_token = str(input("Insert your rucaptcha_key manually: "))
