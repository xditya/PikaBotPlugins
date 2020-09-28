import asyncio, subprocess
import time, re, io
from userbot import bot, BOTLOG, BOTLOG_CHATID, CMD_HELP
from telethon import events, functions, types
from telethon.events import StopPropagation
from telethon.tl.functions.messages import ExportChatInviteRequest
from telethon.tl.functions.contacts import BlockRequest
from telethon.tl.functions.channels import LeaveChannelRequest, CreateChannelRequest, DeleteMessagesRequest
from collections import deque
from telethon.tl.functions.users import GetFullUserRequest
from userbot.events import register
from userbot.utils import ItzSjDude
from SysRuntime import *

@ItzSjDude(outgoing=True, pattern="leave$")
async def leave(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("`I iz Leaving dis Lol Group kek!`")
        time.sleep(3)
        if '-' in str(e.chat_id):
            await bot(LeaveChannelRequest(e.chat_id))
        else:
            await e.edit('`But Boss! This is Not A Chat`')

@ItzSjDude(outgoing=True, pattern=";_;$")
async def fun(e):
    t = ";__;"
    for j in range(10):
        t = t[:-1] + "_;"
        await e.edit(t)

@ItzSjDude(outgoing=True, pattern="yo$")
async def Ooo(e):
    t = "yo"
    for j in range(15):
        t = t[:-1] + "oo"
        await e.edit(t)

@ItzSjDude(outgoing=True, pattern="Oof$")
async def Oof(e):
    t = "Oof"
    for j in range(15):
        t = t[:-1] + "of"
        await e.edit(t)

@ItzSjDude(outgoing=True, pattern="ccry$")
async def cry(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("(;´༎ຶД༎ຶ)")

@ItzSjDude(outgoing=True, pattern="fp$")
async def facepalm(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("🤦‍♂")

@ItzSjDude(outgoing=True, pattern="moon$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🌗🌘🌑🌒🌓🌔🌕🌖"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
		
@ItzSjDude(outgoing=True, pattern="source$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(f"{sys4}")

@ItzSjDude(outgoing=True, pattern="readme$")
async def reedme(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(f"{sys4}/blob/master/README.md")



@ItzSjDude(outgoing=True, pattern="heart$")	
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("❤️🧡💛💚💙💜🖤"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@ItzSjDude(outgoing=True, pattern="fap$")
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🍆✊🏻💦"))
	for _ in range(32):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)



CMD_HELP.update({
    "leave": "Leave a Chat"
})
CMD_HELP.update({
    ";__;": "You try it!"
})
CMD_HELP.update({
    "cry": "Cry"
})
CMD_HELP.update({
    "fp": "Send face palm emoji."
})
CMD_HELP.update({
    "moon": "Bot will send a cool moon animation."
})
CMD_HELP.update({
    "clock": "Bot will send a cool clock animation."
})
CMD_HELP.update({
    "readme": "Reedme."
})
CMD_HELP.update({
    "source": "Gives the source of your userbot"
})
CMD_HELP.update({
    "myusernames": "List of Usernames owned by you."
})
CMD_HELP.update({
    "oof": "Same as ;__; but ooof"
})
CMD_HELP.update({
    "earth": "Sends Kensar Earth animation"
})
CMD_HELP.update({
    "heart": "Try and you'll get your emotions back"
})
CMD_HELP.update({
    "fap": "Faking orgasm"
})
