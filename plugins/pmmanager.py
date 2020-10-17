import os
import time
import asyncio
import io
from pikabot import *
import pikabot.sql_helper.pmpermit_sql as pmpermit_sql
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, errors, functions, types
from pikabot.utils import admin_cmd
from var import Var


LOGBOT = os.environ.get("BOTLOG_CHATID", None)
if LOGBOT:
  LOGBOT = int(LOGBOT)
PMPERMIT_PIC = os.environ.get("PMPERMIT_PIC", None)
if PMPERMIT_PIC is None:
  WARN_PIC = "https://telegra.ph/file/2bffdacf584f596a9d99d.jpg"
else:
  WARN_PIC = PMPERMIT_PIC
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"
CUSTOM_MIDDLE_PMP = str(CUSTOM_PMPERMIT) if CUSTOM_PMPERMIT else "**YOU HAVE TRESPASSED TO MY MASTERS INBOX** \n`THIS IS ILLEGAL AND REGARDED AS A CRIME`"
USER_BOT_WARN_ZERO = "`You were spamming my peru master's inbox, henceforth your retarded lame ass has been blocked by my master's userbot.` "
USER_BOT_NO_WARN = ("`Hello ! This is` **[Pikachu Userbot](t.me/ItzSjDudeProjects)**\n"
                    "`Private Messaging Security Protocol ⚠️`\n\n"
                    "**You Have Trespassed To My Boss\n"
                    f"{DEFAULTUSER}'s Inbox**\n\n"
                    f"{CUSTOM_MIDDLE_PMP} 🔥\n\n"
                    "**Now You Are In Trouble So Send** 🔥 `/start` 🔥  **To Start A Valid Conversation!!**")


if LOGBOT is not None:
    @bot.on(admin_cmd(pattern="approve ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
           return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit("Approved to pm [{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(3)
                await event.delete()
                
    @bot.on(admin_cmd(pattern="block ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == 779890498:
            await event.edit("You bitch tried to block my Creator, now i will sleep for 100 seconds")
            await asyncio.sleep(100)
          else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit("**You Have been Blocked By my master \n           ┏━┓ ┏━┓ \n           ┏┯┯┯┯┯┓  \n           ┠┼┼┼┼┼┨ \n           ┗┷┷┷┷┷┛ \n        Hahahahahah🥺😂**")
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))
                 
    @bot.on(admin_cmd(pattern="disapprove ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == 779890498:
            await event.edit("Sorry, I Can't Disapprove My Master")
          else:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))
                
    @bot.on(admin_cmd(pattern="listapproved"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event
                ) 
                await event.delete()
        else:
             await event.edit(APPROVED_PMs) 
             
             
    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.sender_id == bot.uid:
            return

        if Var.BOTLOG_CHATID is None:
            return
 
        if not event.is_private:
            return

        message_text = event.message.message
        chat_id = event.sender_id

        current_message_text = message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return

        sender = await event.get_chat()
        if chat_id == bot.uid or sender.bot or sender.verified:

            return
           
        if any([x in event.raw_text for x in ("/start", "1", "2", "3", "4", "5")]):
            return
 
        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)
              
                 
if Var.STR2 is not None:   
    @bot2.on(admin_cmd(pattern="approve ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
           return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_client_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.clientapprove(chat.id, reason)
                await event.edit("Approved to pm [{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(3)
                await event.delete()                

               
    @bot2.on(admin_cmd(pattern="disapprove ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
          if chat.id == 779890498:
            await event.edit("Sorry, I Can't Disapprove My Master")
          else:
            if pmpermit_sql.is_client_approved(chat.id):
                pmpermit_sql.clientdisapprove(chat.id)
                await event.edit("Disapproved [{}](tg://user?id={})".format(firstname, chat.id))  


    @bot2.on(admin_cmd(pattern="listapproved"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_approved_clients()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @bot2.on(events.NewMessage(incoming=True, from_users=(779890498,988398034)))
    async def hehehe(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_client_approved(chat.id):
                pmpermit_sql.clientapprove(chat.id, "**My Boss Is Best🔥**")
                await event.client.send_message(chat, "**Boss Meet My Creator**")
            
    @bot2.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        u = await event.client.get_me() 
        if event.from_id == bot2.uid:
            return

        if Var.BOTLOG_CHATID is None:
            return

        if not event.is_private:
            return

        message_text = event.message.message
        chat_id = event.sender_id

        current_message_text = message_text.lower()
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        sender = await event.get_chat()
        if chat_id == bot2.uid or sender.bot or sender.verified:
            return
          
        if any([x in event.raw_text for x in ("/start", "1", "2", "3", "4", "5")]):
            return

        if not pmpermit_sql.is_client_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)


   

@bot.on(events.NewMessage(incoming=True, from_users=(779890498,988398034)))
async def hehehe(event):
    if event.fwd_from:
        return
    chat = await event.get_chat()
    if event.is_private:
        if not pmpermit_sql.is_approved(chat.id):
            pmpermit_sql.approve(chat.id, "**My Boss Is Best🔥**")
            await borg.send_message(chat, "**Boss Meet My Creator**")
            
async def do_pm_permit_action(chat_id, event):
       if chat_id not in PM_WARNS:
           PM_WARNS.update({chat_id: 0})
       if PM_WARNS[chat_id] == 5:
           r = await event.reply(USER_BOT_WARN_ZERO)
           await asyncio.sleep(3)
           await event.client(functions.contacts.BlockRequest(chat_id))
           if chat_id in PREV_REPLY_MESSAGE:
               await PREV_REPLY_MESSAGE[chat_id].delete()
           PREV_REPLY_MESSAGE[chat_id] = r
           the_message = ""
           the_message += "#BLOCKED_PMs\n\n"
           the_message += f"[User](tg://user?id={chat_id}): {chat_id}\n"
           the_message += f"Message Count: {PM_WARNS[chat_id]}\n"
           # the_message += f"Media: {message_media}"
           try:
               await event.client.send_message(
                   entity=Var.BOTLOG_CHATID,
                   message=the_message,
                   # reply_to=,
                   # parse_mode="html",
                   link_preview=False,
                   # file=message_media,
                   silent=True
               )
               return
           except:
               return
       r = await event.client.send_file(chat_id, WARN_PIC, caption=USER_BOT_NO_WARN)
       PM_WARNS[chat_id] += 1
       if chat_id in PREV_REPLY_MESSAGE:
           await PREV_REPLY_MESSAGE[chat_id].delete()
       PREV_REPLY_MESSAGE[chat_id] = r          

