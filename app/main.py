from fastapi import FastAPI, Request
from app.whatsapp import verify_webhook, handle_message

app = FastAPI()

@app.get("/webhook")
async def verify(request: Request):
    return verify_webhook(request)

@app.post("/webhook")
async def receive_message(request: Request):
    return await handle_message(request)
