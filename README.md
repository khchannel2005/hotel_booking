# Hotel Booking Platform
Цей проект – REST API для бронювання готелів з такими можливостями:
- CRUD операції для готелів та кімнат
- Пагінація, фільтрація та сортування
- Валідація даних через Pydantic
- Зв'язок таблиць готелів та номерів
- Генерація документації через Swagger UI

## Встановлення
1. Клонуйте репозиторій:
git clone https://github.com/user/hotel_booking.git cd hotel_booking

markdown
Копіювати
Редагувати

2. Встановіть залежності:
pip install -r requirements.txt

markdown
Копіювати
Редагувати

3. Запустіть сервер:
uvicorn app.main:app --reload

markdown
Копіювати
Редагувати

4. Відкрийте Swagger-документацію за адресою:
http://127.0.0.1:8000/docs