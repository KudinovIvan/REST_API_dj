# REST_API

В данном проекте представлено небольшое REST API с использованием фреймворка DRF
____
## Тематика "Продажа машин автодилерами"
Используется два класса с отношением "один-ко-многим": Car и Dealer.
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
/api/cars/get
![Cars_get](https://avatars1.githubusercontent.com/u/5384215?v=3&s=460 "Орк")
/api/cars/post

/api/cars/put

/api/cars/delete

/api/dealers/get

/api/dealers/post

/api/dealers/put

/api/dealers/delete
