import requests
import json


# Метод POST
# Адрес
url = "https://restful-booker.herokuapp.com/booking/"
# Тело
body = {
    "firstname" : "Test",
    "lastname" :"Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
                     }}
# Заголовок
json_headers = {
    "Content-type": "application/json"}
# Запрос
r = requests.post(url, headers=json_headers, json=body)
# Проверка статуса ответа
if r.status_code == 200:
    print("POST Статус: 200")
else:
    print("POST Ошибка: Статус:", r.status_code)
# Получаем id из ответа
r_dict = r.json()
id = r_dict["bookingid"]
print("Id:",id)
# Записываем данные в файл
f = open("C://Users//Виталий//Desktop//Autotest//api.txt", "w")
f.write('Метод POST: url:' + url + "\n")
f.write('Статус: '+ str(r.status_code) + "\n")
f.write("\n")

# Метод GET
# Запрос
r2 = requests.get(url+str(id))
# Проверка статуса ответа
if r2.status_code == 200:
    print("GET Статус: 200")
else:
    print("GET Ошибка: Статус:", r2.status_code)
print(r2.text)
# Записываем данные в файл
f.write('Метод GET: url:' + url+str(id) + "\n")
f.write('Статус: ' +str(r2.status_code) + "\n")
f.write('Тело: ' + r2.text + "\n")
f.write("\n")

# Метод PUT
# Тело
body3 = {
    "firstname" : "James",
    "lastname" : "test",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"}
# Заголовок
json_headers3 = {
    "Content-type": "application/json"}
# Запрос
r3 = requests.put(url+str(id), headers=json_headers3, json=body3,auth=('admin', 'password123'))
# Проверка статуса ответа
if r3.status_code == 200:
    print("PUT Статус: 200")
else:
    print("PUT Ошибка: Статус:", r3.status_code)
print(r3.text)
# Записываем данные в файл
f.write('Метод PUT: url:' + url+str(id) + "\n")
f.write('Статус: ' +str(r3.status_code) + "\n")
f.write('Тело: ' + r3.text + "\n")
f.write("\n")

# Метод GET 2
# Запрос
r4 = requests.get(url+str(id))
# Проверка статуса ответа
if r4.status_code == 200:
    print("GET 2 Статус: 200")
else:
    print("GET 2 Ошибка: Статус:", r4.status_code)
print(r4.text)
# Записываем данные в файл
f.write('Метод GET 2: url:' + url+str(id) + "\n")
f.write('Статус: ' +str(r4.status_code) + "\n")
f.write('Тело: ' + r4.text + "\n")
f.write("\n")

# Метод DELETE
# Запрос
r5 = requests.delete(url+str(id),auth=('admin', 'password123'))
# Проверка статуса ответа
if r5.status_code == 201:
    print("DELETE Статус: 201")
else:
    print("DELETE Ошибка: Статус:", r5.status_code)
print(r5.text)
# Записываем данные в файл
f.write('Метод DELETE: url:' + url+str(id) + "\n")
f.write('Статус: ' +str(r5.status_code) + "\n")
f.write('Тело: ' + r5.text + "\n")
f.write("\n")

# Метод GET 3
# Запрос
r6 = requests.get(url+str(id))
# Проверка статуса ответа
if r6.status_code == 404:
    print("GET 2 Статус: 404")
else:
    print("GET 2 Ошибка: Статус:", r6.status_code)
print(r6.text)
# Записываем данные в файл
f.write('Метод GET 3: url:' + url+str(id) + "\n")
f.write('Статус: ' +str(r6.status_code) + "\n")
f.write('Тело: ' + r6.text + "\n")
f.write("\n")
# Закрываем файл
f.close()