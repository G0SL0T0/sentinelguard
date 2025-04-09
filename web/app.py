from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime
import random

app = FastAPI()
app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")

# Тестовые данные
def generate_logs():
    threats = ["SQLi", "XSS", "Brute Force", "Port Scan"]
    return [
        {
            "id": i,
            "ip": f"192.168.1.{random.randint(1, 50)}",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "threat": random.choice(threats),
            "risk": random.randint(10, 100)
        } for i in range(1, 100)
    ]

@app.get("/api/logs") # API для фронта
async def get_logs():
    return generate_logs()

@app.get("/api/actions")
async def get_actions():
    actions = ["Isolate Host", "Limit Speed", "Scan Host"]
    return [
        {
            "id": i,
            "ip": f"10.0.0.{random.randint(1, 20)}",
            "action": random.choice(actions),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        } for i in range(1, 30)
    ]

# Рендер страниц
@app.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/logs")
async def logs(request: Request):
    return templates.TemplateResponse("logs.html", {"request": request})

@app.get("/actions")
async def actions(request: Request):
    return templates.TemplateResponse("actions.html", {"request": request})