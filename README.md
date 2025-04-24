# Проекты лабораторных работ

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
 ```
git clone https://github.com/zholeu/testingRestaurantCase.git
pip install -r requirements.txt
```




