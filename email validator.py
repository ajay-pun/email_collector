from playwright.sync_api import sync_playwright
from time import sleep
from bs4 import BeautifulSoup
from random import randint


def run(playwright):
    email="helloworld"
    browser =playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://accounts.google.com/signup/v2/webcreateaccount?biz=false&cc=IN&continue=https%3A%2F%2Fwww.google.com%2F&dsh=S1627445831%3A1674586118124237&flowEntry=SignUp&flowName=GlifWebSignIn&hl=en&ifkv=AWnogHeE6ezYEQseKsIsnL3Sij1w6QHgKm2F4llvOGbAMoPrX87M5Q8JfuyAdUGothHy14tW9ijl")
    page.keyboard.press("Tab")
    page.keyboard.press("Tab")
    email_list=['helloworld','jesonpun345678','wearehero8992713','wowe2323arth','lol123']
    
    for email in email_list:
        page.keyboard.type(email)
        page.keyboard.press("Shift+Tab")
        sleep(3)
        pagetxt=str(page.content())
        if 'That username is taken.' in pagetxt:
            print(email," is taken")
        else:
            print(email," is not taken")
            
        page.keyboard.press("Tab")
        page.keyboard.press("Control+A")
        page.keyboard.press("Control+X")
    
    

with sync_playwright() as playwright:
    run(playwright)
