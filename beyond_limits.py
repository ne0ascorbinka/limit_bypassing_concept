# beside imports
import logging
import sys
import os
import json
import asyncio

# pyrogram imports
from pyrogram import Client, filters
from pyrogram.types import Message

with open("config.json") as file:
    data = json.load(file)

chat_ids_path = data["chat_ids_path"]
chat_ids = set()

BOT_NAME = data["bot_name"]

def get_client():
        api_id = data["api_id"]
        api_hash = data["api_hash"]
        return Client("my_account",
                api_id=api_id,
                api_hash=api_hash)

app = get_client()

@app.on_message(filters.text & filters.private)
async def message_handler(client: Client, message: Message ):
    await message.reply_text("Sending video...")
    print("sending video...")
    await message.reply_video("video.mp4")

def main():
    app.run()

if __name__ == "__main__":
    main()