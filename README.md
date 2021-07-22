# REST_API

В данном проекте представлено небольшое REST API с использованием фреймворка DRF
____
## Тематика "Продажа машин автодилерами"
Используется два класса с отношением "один-ко-многим": Dealer и Car.
Класс Car представляет собой класс машины на продажу с полями: name (название), mark (марка), dealer (дилер). Поле dealer является внешним ключом и 
ссылается на соответствующий класс. Класс Dealer имеет поле name (название)
## JSON Schemas
Car
```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "mark": {
      "type": "string"
    },
    "dealer": {
      "type": "integer"
    }
  },
  "required": [
    "id",
    "name",
    "mark",
    "dealer"
  ]
}
```
Dealer
```json
{
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name"
  ]
}
```
## Endpoints
API поддерживает все операции CRUD приложения (Запись, чтение, изменение и удаление данных)
## /api/cars/get/
![Cars_get](https://github.com/KudinovIvan/REST_API_dj/blob/master/assets/cars_get.png)
## /api/cars/post/
![Cars_post](https://github.com/KudinovIvan/REST_API_dj/blob/master/assets/cars_post.png)
## /api/cars/put/\<int:pk>/
![Cars_put](https://github.com/KudinovIvan/REST_API_dj/blob/master/assets/cars_put.png)
## /api/cars/delete/\<int:pk>/
![Cars_delete](https://github.com/KudinovIvan/REST_API_dj/blob/master/assets/cars_delete.png)
## /api/dealers/get/
![Dealers_get](https://github.com/KudinovIvan/REST_API_dj/blob/master/assets/dealers_get.png)
## /api/dealers/post/
![Dealers_post](https://github.com/KudinovIvan/REST_API_dj/blob/master/assets/dealers_post.png)
## /api/dealers/put/\<int:pk>/
![Dealers_put](https://github.com/KudinovIvan/REST_API_dj/blob/master/assets/dealers_put.png)
## /api/dealers/delete/\<int:pk>/
![Dealers_delete](https://github.com/KudinovIvan/REST_API_dj/blob/master/assets/dealers_delete.png)
