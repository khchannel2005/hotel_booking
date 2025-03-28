# Hotel Booking Platform
Цей проект – REST API для бронювання готелів з такими можливостями:
- CRUD операції для готелів та кімнат
- Пагінація, фільтрація та сортування
- Валідація даних через Pydantic
- Зв'язок таблиць готелів та номерів
- Генерація документації через Swagger UI

## Встановлення
1. Клонуйте репозиторій:
git clone [[https://github.com/user/hotel_booking.git cd hotel_booking](https://github.com/khchannel2005/hotel_booking)](https://github.com/khchannel2005/hotel_booking)


2. Встановіть залежності:
pip install -r requirements.txt


3. Запустіть сервер:
uvicorn app.main:app --reload


4. Відкрийте Swagger-документацію за адресою:
http://127.0.0.1:8000/docs
