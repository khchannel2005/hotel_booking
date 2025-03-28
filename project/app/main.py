from fastapi import FastAPI
from fastapi_pagination import add_pagination
from app.api.endpoints import hotel

app = FastAPI(title="Hotel Booking API")

# Реєстрація маршрутів
app.include_router(hotel.router)

# Додавання пагінації
add_pagination(app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
