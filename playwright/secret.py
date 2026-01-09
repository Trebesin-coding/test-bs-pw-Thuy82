from playwright.sync_api import sync_playwright #synchroni kód=> znamená řádek po řádku postupně
from dotenv import load_dotenv
from os import getenv

load_dotenv()

login = getenv("LOGIN")
password = getenv("PASSWORD")
number = getenv("NUMBER") # proč je tu number?

# proč používáte .env? kde je soubor s .env?

def main():
    
    with sync_playwright() as p: 
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://souhrada.github.io/playwright-exam/")

        page.fill('input#login', login )

        page.fill('input#pass', password)

        page.click('.login-btn')#prihlasi se to

        message = page.locator('p.super-secret-text').text_content()

        print(message)




        
       




        input("zmáčni jakoukoli klávesu pro zavření prohlížeče")

        browser.close()#uzavře prohlížeč


if __name__== "__main__":
    main()