from fastapi.responses import PlainTextResponse
from app.config import VERIFY_TOKEN
import json

def verify_webhook(request):
    params = request.query_params
    if (
        params.get("hub.mode") == "subscribe"
        and params.get("hub.verify_token") == VERIFY_TOKEN
    ):
        return PlainTextResponse(params.get("hub.challenge"))
    return PlainTextResponse("Verification failed", status_code=403)

async def handle_message(request):
    body = await request.json()
    print(json.dumps(body, indent=2))
    return {"status": "received"}
