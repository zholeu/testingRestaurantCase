**Тема:** "Разработка и автоматизация процессов тестирования REST API с применением Python и Pytest"

**Период:** весна 2025

# Структура проекта
```
.
├── tests/                      # Каталог с тестами
│   ├── test_delete_requests.py # DELETE-запросы
│   ├── test_get_endpoints.py   # GET-запросы
│   ├── test_post_endpoints.py  # POST-запросы
├── config/                
│   ├── payloads.py             # Все JSON тела запросов
│   └── config.py               # Конфигурации (BASE_URL, токен)       
├── fixtures/                   
│   └── common_fixtures.py      # Общие фикстуры
├── utils/                      # Утилиты и вспомогательные функции
│   └── auth.py                 # Класс BearerAuth для авторизации
├── requirements.txt            
└── README.md
```

 # Установка и запуск
 1. Клонирование и установка зависимостей 
 ```
git clone https://github.com/zholeu/testingRestaurantCase.git
pip install -r requirements.txt
```
2. Установить токен в файле config/config.py
3. Запуск
```
pytest -v
```




