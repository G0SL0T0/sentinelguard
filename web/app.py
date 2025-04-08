from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from core.risk_engine import calculate_risk
from core.actions import isolate_host

app = FastAPI()
app.mount("/static", StaticFiles(directory="web/static"), name="static")
templates = Jinja2Templates(directory="web/templates")


@app.get("/api/hosts")  # API для фронта
async def get_hosts():
    
    return [ # Заглушка
        {"ip": "192.168.1.1", "risk": 65, "status": "active"},
        {"ip": "192.168.1.2", "risk": 90, "status": "blocked"}
    ]

@app.post("/api/host/{ip}/isolate")
async def isolate(ip: str):
    isolate_host(ip)
    return JSONResponse({"status": "ok"})


@app.get("/") # Рендер страниц
async def dashboard(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/host/{ip}")
async def host_details(request: Request, ip: str):
    return templates.TemplateResponse("host.html", {"request": request, "ip": ip})