import time
import os
from dotenv import load_dotenv

from login import System
from utils.selenium import init_driver

def main():
    load_dotenv()
    user = os.getenv("SYSTEM_USER")
    password = os.getenv("SYSTEM_PASSWORD")

    url = input("Digite a URL do sistema: ")

    driver = init_driver()
    system = System(driver)

    try:
        driver.get(url)
        system.login(user, password)

    except Exception as e:
        print(f"Ocorreu um erro {e}")

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()
