from .pages.product_page import BookPage
import time



def test_guest_can_add_book_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BookPage(browser, link)
    page.open()
    page.add_book_to_basket()
    page.solve_quiz_and_get_code()
    # time.sleep(150)
    time.sleep(5)
    page.should_be_right_book_and_price()
    # time.sleep(10)
    

