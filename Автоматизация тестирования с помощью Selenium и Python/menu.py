import time
import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()

# Ссылка на которую нам нужно перейти
link = "Тут должна быть ссылка на наш сайт"
driver.get(link)

# get(url) - загрузить страницу по указанному URL.
# find_element(by, value) - найти элемент на странице по заданным критериям by и value.
# find_elements(by, value) - найти все элементы на странице по заданным критериям by и value.
# send_keys(*keys) - отправить последовательность клавиш в текущий элемент.
# click() - кликнуть на текущий элемент.
# clear() - очистить текущий элемент.
# get_attribute(name) - получить значение атрибута элемента по его имени.
# text - получить текст текущего элемента.
# submit() - отправить форму на сервер.
# back() - перейти на предыдущую страницу в истории браузера.
# forward() - перейти на следующую страницу в истории браузера.
# refresh() - обновить текущую страницу.


        #SELECT____SELECT____SELECT____SELECT____SELECT____SELECT____SELECT

# # находим select элемент на странице
# select_element = driver.find_element_by_id("select-element-id")
# # создаем объект класса Select
# select = Select(select_element)
#
# После создания объекта Select можно выбрать значение из списка по индексу, тексту или значению:
#
# # выбираем элемент по индексу
# select.select_by_index(1)
#
#  выбираем элемент по тексту
# select.select_by_visible_text("Текст элемента")
#
#  выбираем элемент по значению
# select.select_by_value("значение элемента")
# Также можно получить список всех вариантов в select элементе и выбрать их по индексу, тексту или значению:
#
#  получаем список всех элементов в select элементе
# options = select.options
#
#  выбираем элемент по индексу
# select.select_by_index(1)
#
#  выбираем элемент по тексту
# select.select_by_visible_text("Текст элемента")
#
#  выбираем элемент по значению
# select.select_by_value("значение элемента")

# Если select элемент позволяет выбрать несколько вариантов, можно выбирать несколько элементов с помощью методов select_by_index(), select_by_visible_text() и select_by_value():
#
#  выбираем несколько элементов по индексу
# select.select_by_index(1)
# select.select_by_index(3)
#
#  выбираем несколько элементов по тексту
# select.select_by_visible_text("Текст элемента 1")
# select.select_by_visible_text("Текст элемента 3")
#
#  выбираем несколько элементов по значению
# select.select_by_value("значение элемента 1")
# select.select_by_value("значение элемента 3")

# Если нужно отменить выбор элемента, можно использовать метод deselect_all() или deselect_by_index(), deselect_by_visible_text() и deselect_by_value():
#
#  отменяем выбор всех элементов
# select.deselect_all()
#
#  отменяем выбор элемента по индексу
# select.deselect_by_index(1)
#
#  отменяем выбор элемента по тексту
# select.deselect_by_visible_text("Текст элемента")
#
#  отменяем выбор элемента по значению
# select.deselect_by_value("значение элемента")

    # ALERT  ALERT  ALERT  ALERT  ALERT  ALERT  ALERT  ALERT  ALERT  ALERT  ALERT
#ALERT = Вслывающие модальное окно
alert = browser.switch_to.alert     #   Переключаемся на окно alert
alert.accept()                      #   Принимаем его

alert_text = alert.text             #   Находим текст
#   confirm - модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него
confirm = browser.switch_to.alert   #   Переключаемся на окно confirm
confirm.accept()                    #   Согласие
confirm.dismiss()                   #   Отказ
#   prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():
prompt = browser.switch_to.alert    #   Переключаемся на окно prompt
prompt.send_keys("My answer")       #   Ввод текста
prompt.accept()                     #   Отправка


    #   Переход на новую вкладку браузера
    #   Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
    #   Это делается с помощью команды switch_to.window:
# browser.switch_to.window(window_name)
    #   Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок.
    #   Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
# new_window = browser.window_handles[1]
    #   Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
# first_window = browser.window_handles[0]


    #   ВЫКЛЮЧЕНИЕ
try:
    print("Скрипт прошел")
finally:
    print("Даже если он упал,я буду жить")

#browser.close() - закрыть вкладку
#browser.quit() - закрыть браузер