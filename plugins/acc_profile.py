"""Profile Related Commands
{i}autobio 
{i}autoname
{i}autopfp
{i}avengerspfp
{i}animepfp
{i}gamerpfp
{i}pbio <Bio>
{i}pname <Name>
{i}ppic <Reply to pic>
"""
import asyncio, urllib, os, time 
from telethon import events

import logging
from pikabot.utils import *
from pikabot.utils import ItzSjDude
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.tl import functions
from datetime import datetime
from pikabot.utils import ItzSjDude
from PIL import Image, ImageDraw, ImageFont
from time import sleep
from pikabot.main_plugs.pfpdata import *
from pikabot import ALIVE_NAME , AUTO_BIO
from telethon.errors import FloodWaitError
DEL_TIME_OUT = 60 ; 
DUSER = str(ALIVE_NAME) if ALIVE_NAME else "PikaBot"
DBIO = str(AUTO_BIO) if AUTO_BIO else "Pika is Love 🔥"


@ItzSjDude(outgoing=True, pattern="pbio (.*)")  
async def _(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await event.client(functions.account.UpdateProfileRequest(
            about=bio
        ))
        await event.edit("Succesfully changed my profile bio")
    except Exception as e: 
        await event.edit(str(e))

@ItzSjDude(outgoing=True, pattern="pname ((.|\n)*)")
async def _(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if  "\\n" in names:
        first_name, last_name = names.split("\\n", 1)
    try:
        await event.client(functions.account.UpdateProfileRequest(
            first_name=first_name,
            last_name=last_name
        ))
        await event.edit("My name was changed successfully")
    except Exception as e: 
        await event.edit(str(e))

@ItzSjDude(outgoing=True, pattern="ppic")  
async def _(event):
    if event.fwd_from:
        return
    reply_message = await event.get_reply_message()
    await event.edit("Downloading Profile Picture to my local ...")
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):  
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    photo = None
    try:
        photo = await event.client.download_media(
            reply_message,
            Config.TMP_DOWNLOAD_DIRECTORY
        )
    except Exception as e: 
        await event.edit(str(e))
    else:
        if photo:
            await event.edit("now, Uploading to @Telegram ...")
            file = await event.client.upload_file(photo)  
            try:
                await event.client(functions.photos.UploadProfilePhotoRequest(
                    file
                ))
            except Exception as e: 
                await event.edit(str(e))
            else:
                await event.edit("My profile picture was succesfully changed")
    try:
        os.remove(photo)
    except Exception as e:  
        logger.warn(str(e))

@ItzSjDude(outgoing=True, pattern="animepfp ?(.*)")
async def main(event):
    await event.edit(f"{r}")
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")  
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)

@ItzSjDude(outgoing=True, pattern="avengerspfp ?(.*)")
async def main(event):
    await event.edit(f"{s}")
    while True:
        await avengerspic()
        file = await event.client.upload_file("donottouch.jpg")  
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)

@ItzSjDude(outgoing=True, pattern="gamerpfp ?(.*)")
async def main(event):
    await event.edit(f"{t}")
    while True:
        await gamerpic()
        file = await event.client.upload_file("donottouch.jpg")  
        await event.client(functions.photos.UploadProfilePhotoRequest( file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)
        
@ItzSjDude(outgoing=True,pattern="autoname")
async def _(event):
    if event.fwd_from:
        return
    while True:
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"🕒{HM} ⚡{DUSER}⚡ 📅{DM}"
        logger.info(name)
        try:
            await event.client(functions.account.UpdateProfileRequest(
                first_name=name
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
    await event.edit(f"Auto Name has been started Master") 

@ItzSjDude(outgoing=True, pattern="autobio")
async def _(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | {DBIO} | ⌚️ {HM}"
        logger.info(bio)
        try:
            await event.client(functions.account.UpdateProfileRequest(
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)

logger = logging.getLogger(__name__)
if 1 == 1:
    name = "Profile Photos"
    @ItzSjDude(outgoing=True, pattern="poto(.*)")
    async def potocmd(event):
        id = "".join(event.raw_text.split(maxsplit=2)[1:])
        user = await event.get_reply_message()
        chat = event.input_chat
        if user:
            photos = await event.client.get_profile_photos(user.sender)
        else:
            photos = await event.client.get_profile_photos(chat)
        if id.strip() == "":
            try:
                await event.client.send_file(event.chat_id, photos)
            except a:
                photo = await event.client.download_profile_photo(chat)
                await event.client.send_file(event.chat_id, photo)
        else:
            try:
                id = int(id)
                if id <= 0:
                    await event.edit("`ID number you entered is invalid`")
                    return
            except:
                 await event.edit("`Are you Comedy Me ?`")
                 return
            if int(id) <= (len(photos)):
                send_photos = await event.client.download_media(photos[id - 1])
                await event.client.send_file(event.chat_id, send_photos)
            else:
                await event.edit("`No photo found of that Nigga , now u Die`")
                return
