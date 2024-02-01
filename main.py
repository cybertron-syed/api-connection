from fastapi import FastAPI, request
import httpx

app = FastAPI()

@app.get('/')
def message(): 
    return {'data': 'ey'}


















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