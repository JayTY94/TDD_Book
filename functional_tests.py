from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.binary_location = r"C:\Program Files\Mozilla Firefox\Firefox.exe"

# Edith has heard about a cool new online to-do app. She goes
# to check its home page
browser = webdriver.Firefox(options=options)
browser.get('http://localhost:8000')

# She notices the page title and header mention to-do lists
assert 'To-Do' in browser.title