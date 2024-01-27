import time


LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket(browser):
    browser.get(LINK)
    time.sleep(30)
    try:
        btn = browser.find_element_by_css_selector("button.btn-add-to-basket")
    except:
        assert False, "Button add to basket is not found!"
