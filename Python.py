"""projekt_6.py: Šestý projekt do Engeto Online Tester s Pythonem

author: Vítězslav Dlábek
email: vitezslavdlabek@gmail.com
"""


import pytest_playwright
from playwright.sync_api import Page, expect

def test_pocitadlo_kosiku(page: Page): # Test ověřuje zda-li funguje počítadlo množství položek v košíku tím, že přejde na danou stranku, ověří jestli je aktualní stav košíku 0   
                                        #poté přejde  na produkt a přidá jej do košíku a opět zkontroluje jestli se stav změnil na 1.

    url = "https://www.luxor.cz"
    page.goto(url)

    pocitadlo_kosiku = page.locator(".header-item__count").first

    expect(pocitadlo_kosiku).to_have_text("0")

    vyhledavac = page.get_by_label("Vyhledávání").first
    vyhledavac.click()
    vyhledavac.fill("Temné břehy")
    page.keyboard.press("Enter")
  
    page.get_by_role("button", name= "DO KOŠÍKU").first.click()

    expect(pocitadlo_kosiku).to_have_text("1")


def test_animace_nacitani(page: Page): # Test ověřuje, jestli se při přechodu mezi dvěmi odkazy na strance spustí načítací animace stránky.
                          
    url = "https://www.luxor.cz"
    page.goto(url)
    
    nacitani = page.locator(".preloader.preloader--active")
    
    page.get_by_role("link", name="Prodejny").first.click()

    expect(nacitani).to_be_visible(timeout=2000)

    expect(nacitani).to_be_hidden(timeout=10000)




def test_tooltip(page: Page): # Test ověřuje, jestli se po najetí myší na ikonku "i" zobrazí tooltip s ukazatelem nejnižží ceny a po přesunu myši opět zmizí

    url = "https://www.luxor.cz"
    page.goto(url)

    tooltip = page.get_by_role("tooltip", name="Nejnižší cena za posledních 30 dní").first

    page.locator(".prices__tooltip").first.hover()   

    expect(tooltip).to_be_visible()

    page.get_by_role("heading", name="Novinky").first.hover()

    expect(tooltip).to_be_hidden

    

