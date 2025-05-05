# analytics/api/main.py
from fastapi import FastAPI
from .routes import fan, interacao, segmentar, kpi, notificacao


app = FastAPI(title="FURIA Fan Intelligence API")

app.include_router(fan.router,     prefix="/fans",          tags=["Fans"])
app.include_router(interacao.router,    prefix="/interacoes",    tags=["Interações"])
app.include_router(segmentar.router,    prefix="/segmentos",     tags=["Segmentos"])
app.include_router(kpi.router,          prefix="/kpis",          tags=["KPI Reports"])
app.include_router(notificacao.router,  prefix="/notificacoes",  tags=["Notificações"])

@app.get("/")
def health_check():
    return {"status": "ok"}
