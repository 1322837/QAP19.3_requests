import requests
import json

base_url = 'https://petstore.swagger.io/v2/'

# Получаем список питомцев
res_get_all = requests.get(base_url + 'pet/findByStatus', params={'status': 'available'})

print("URL запроса: ", res_get_all.url)
print("Статус ответа: ", res_get_all.status_code)
print(res_get_all.json())

# Добавляем нового питомца
res_post = requests.post(base_url + 'pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                         data=json.dumps(
                             {
                                 "id": 0,
                                 "category": {
                                     "id": 322,
                                     "name": "CatEgoriya"
                                 },
                                 "name": "Egor",
                                 "photoUrls": [
                                     "cat.jpg"
                                 ],
                                 "tags": [
                                     {
                                         "id": 0,
                                         "name": "good"
                                     },
                                     {
                                         "id": 2,
                                         "name": "fun"
                                     }
                                 ],
                                 "status": "available"
                             }))

print("URL запроса: ", res_post.url)
print('Статус ответа: ', res_post.status_code)
print(res_post.json())
post_response_dict = res_post.json()

# Сохраняем ID только что добавленного питомца
petId = post_response_dict['id']

# Изменяем данные только-что добавленного питомца по ID
res_put = requests.put(base_url + f'pet', headers={'accept': 'application/json', 'Content-Type': 'application/json'},
                       data=json.dumps(
                           {
                               "id": petId,
                               "category": {
                                   "id": 223,
                                   "name": "Cat_Egor"
                               },
                               "name": "Egor",
                               "photoUrls": [
                                   "dog.jpg"
                               ],
                               "tags": [
                                   {
                                       "id": 3,
                                       "name": "good"
                                   },
                                   {
                                       "id": 5,
                                       "name": "fun"
                                   }
                               ],
                               "status": "sold"
                           }))

print("URL запроса: ", res_put.url)
print('Статус ответа: ', res_put.status_code)
print(res_put.json())

# Ищем нашего питомца по ID
res_get_ours = requests.get(base_url + f"pet/{petId}")

print("URL запроса: ", res_get_ours.url)
print("Статус ответа: ", res_get_ours.status_code)
print(res_get_ours.json())

# Удаляем добавленного питомца по его ID
res_del = requests.delete(base_url+f'pet/{petId}', headers={'accept': 'application/json'},)
print("URL запроса: ", res_del.url)
print('Статус ответа: ', res_del.status_code)
print(res_del.json())
