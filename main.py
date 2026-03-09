# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ZAS-TRAC Test API")

# Разрешаем запросы с любого источника для теста (упростит проверку с GitHub Pages, телефона и т.д.)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Для теста ок. В проде сузим.
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "ZAS-TRAC Test API is alive"}
