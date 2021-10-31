from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_localization_site(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    messages = ["Ajouter au panier", "Añadir al carrito", 'Добавить в корзину', 'Add to basket']
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assertion_text = button.text
    assert assertion_text in messages
