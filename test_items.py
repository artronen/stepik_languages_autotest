from selenium import webdriver
from selenium.webdriver.common.by import By

def test_localization_site(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    message_fr = "Ajouter au panier"
    browser.get(link)
    button = browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
    assertion_text = button.text
    assert message_fr == assertion_text