import requests
import sys
import json
import allure
from configuration import *


@allure.story('Method Post')
def test_post():
    """
    Этот тест проверяет создание нового объекта (Post)
    """
    global id_response
    body = body_post
    with allure.step("Отправка запроса"):
        r = requests.post(SERVICE_URL, json=body)
        response = Response(r)
    with allure.step("Валидация ответа"):
        response.assert_len(2).assert_status_code(200)
    with allure.step("Сохранение id"):
        id_response = response.response_json["bookingid"]

@allure.story('Method Get')
def test_get():
    """
    Этот тест проверяет  созданный объект (Get)
    """
    with allure.step("Отправка запроса"):
        r = requests.get(SERVICE_URL + str(id_response))
        response = Response(r)
    with allure.step("Валидация ответа"):
        response.assert_len(5).assert_status_code(200)

@allure.story('Method Put')
def test_put():
    """
    Этот тест проверяет изменения параметра объекта (Put)
    """
    with allure.step("Отправка запроса"):
        body = body_put
        r = requests.put(SERVICE_URL + str(id_response), json=body, auth=(login, password))
        response = Response(r)
    with allure.step("Валидация ответа"):
        response.assert_len(6).assert_status_code(200)

@allure.story('Method Get_2')
def test_get_2():
    """
    Этот тест проверяет  измененный объект (Get)
    """
    with allure.step("Отправка запроса"):
        r = requests.get(SERVICE_URL + str(id_response))
        response = Response(r)
    with allure.step("Валидация ответа"):
        response.assert_len(6).assert_status_code(200)

@allure.story('Method Delete')
def test_delete():
    """
    Этот тест проверяет  удаление объекта (Delete)
    """
    with allure.step("Отправка запроса"):
        r = requests.delete(SERVICE_URL + str(id_response), auth=(login, password))
        response = Response(r)
    with allure.step("Валидация ответа"):
        response.assert_status_code(201)

@allure.story('Method Get_3')
def test_get_3():
    """
    Этот тест проверяет, что объект удален (Get)
    """
    with allure.step("Отправка запроса"):
        r = requests.get(SERVICE_URL + str(id_response))
        response = Response(r)
    with allure.step("Валидация ответа"):
        response.assert_status_code(404)

