from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from core.risk_engine import calculate_risk
from core.actions import isolate_host

app = FastAPI()
templates = Jinja2Templates(directory="web/templates")

@app.get("/")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/api/hosts")
async def list_hosts():
    return {"hosts": ["192.168.1.1", "192.168.1.2"]}  # Заглушка

@app.post("/api/host/{ip}/isolate")
async def isolate(ip: str):
    isolate_host(ip)
    return {"status": "ok"}

app.mount("/static", StaticFiles(directory="web/static"), name="static")