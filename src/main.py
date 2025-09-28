import pandas as pd
import time
import os
from dotenv import load_dotenv

from login import System
from main_menu import MainMenu
from neighborhood_page import NeighborhoodPage
from utils.path import resource_path
from utils.selenium import init_driver

def main():
    df = pd.read_csv("bairros.csv")

    dotenv_path = resource_path('.env')
    load_dotenv(dotenv_path=dotenv_path)

    user = os.getenv("SYSTEM_USER")
    password = os.getenv("SYSTEM_PASSWORD")

    if not user or not password:
        input("ERRO CRÍTICO: Não foi possível ler as credenciais. Pressione Enter para sair.")
        return

    url = input("Digite a URL do sistema do cliente: ")

    driver = init_driver()
    system = System(driver)
    main_menu = MainMenu(driver)
    neighborhood_page = NeighborhoodPage(driver)

    try:
        driver.get(url)
        system.login(user, password)

        main_menu.go_to_neighborhood_page()

        for row in df.itertuples():
            neighborhood_page.add_new_neighborhood(
                neighborhood=row.descricao,
                price=row.valor_motoboy,
                city=row.cidade
            )

    except Exception as e:
        print(f"Ocorreu um erro {e}")

    finally:
        print("Automação finalizada.")
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    main()
