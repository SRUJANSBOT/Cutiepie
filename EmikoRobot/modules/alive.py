import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from EmikoRobot.events import register
from EmikoRobot import telethn as tbot


@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ʜɪɪ [{event.sender.first_name}](tg://user?id={event.sender.id}), ɪ'ᴍ ᴛᴇᴅᴅy ʀᴏʙᴏᴛ.** \n"
  TEXT += "⚪ **ɪ'ᴍ ᴡᴏʀᴋɪɴɢ ᴩʀᴏᴩᴇʀʟy** \n"
  TEXT += f"⚪ **ᴍy ᴍᴀꜱᴛᴇʀ : [ꜱᴜʀᴜ](https://t.me/smokerr_xd)** \n"
  TEXT += f"⚪ **ʟɪʙʀᴀʀy ᴠᴇʀꜱɪᴏɴ :** `{telever}` \n"
  TEXT += f"⚪ **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{tlhver}` \n"
  TEXT += f"⚪ **ᴩyʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{pyrover}` \n"
  TEXT += "**ᴛʜᴀɴᴋꜱ ꜰᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ, ᴅᴀʀʟɪɴɢ❤️**"
  BUTTON = [[Button.url("♡ ʜᴇʟᴩ ♡", "https://t.me/Teddyrobot_bot?start=help"), Button.url("♡ ꜱᴜᴩᴩᴏʀᴛ ♡", "https://t.me/Teddysupport")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
