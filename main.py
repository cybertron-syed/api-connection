# from fastapi import FastAPI
# import httpx

# app = FastAPI()

# @app.get('/send message')
# def message(): 
#     return {'message': 'sent'}

# TOKEN = "6690667187:AAFrZGj94Cxot2beC6b-BkRM_lR8nyzG6L8"
# CHAT_ID = '1392527389'


# async def sendTgMessage(message:str):
#     """
#     Sends the Message to telegram with the Telegram BOT API
#     """
#     tg_msg = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
#     API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
#     async with httpx.AsyncClient() as client:
#         await client.post(API_URL, json=tg_msg)


import httpx
from fastapi import FastAPI, Request


TOKEN = "6690667187:AAFrZGj94Cxot2beC6b-BkRM_lR8nyzG6L8"
BASE_URL = f"https://api.telegram.org/bot{TOKEN}"

client = httpx.AsyncClient()

app = FastAPI()


@app.post("/")
async def send_message(req: Request):
    data = await req.json()
    name = data['name']
    message = data['message']

    await client.get(f"{BASE_URL}/sendMessage?name={name}&message={message}")

    return data


# chat_id = data['name']['email']['mobile']