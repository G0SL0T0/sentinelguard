from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from core.risk_engine import calculate_risk
from core.actions import isolate_host

app = FastAPI()

@app.get("/api/host/{ip}/risk")
def get_risk(ip: str):
    return {"ip": ip, "risk": calculate_risk(ip)}

@app.post("/api/host/{ip}/isolate")
def api_isolate(ip: str):
    isolate_host(ip)
    return {"status": "ok"}

app.mount("/", StaticFiles(directory="web/static"), name="static")