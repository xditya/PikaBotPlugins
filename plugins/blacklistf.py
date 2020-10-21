# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Filters
Available Commands:
{i}addblacklist <Blacklist Word>
{i}listblacklist |list all Blacklist words|
{i}rmblacklist <Removal word> """
import asyncio
import io
import re
import pikabot.sql_helper.blacklist_sql as sql
import pikabot.sql_helper.blacklistx_sql as sqlx
from telethon import events, utils
from telethon.tl import types, functions
from var import Var
from uniborg.util import admin_cmd
try:
  from pikabot import bot,bot2
except:
    pass
    
@borg.on(admin_cmd(incoming=True))
async def on_new_message(event):
    # TODO: exempt admins from locks
    if borg.me.id == event.from_id:
        return
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
        if re.search(pattern, name, flags=re.IGNORECASE):
            try:
                await event.delete()
            except Exception as e:
                await event.reply("I do not have DELETE permission in this chat")
                sql.rm_from_blacklist(event.chat_id, snip.lower())
            break


@ItzSjDude(pattern="blacklist ((.|\n)*)")
async def on_add_black_list(event):
    if event.from_id == bot.uid:
      text = event.pattern_match.group(1)
      to_blacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
      for trigger in to_blacklist:
          sql.add_to_blacklist(event.chat_id, trigger.lower())
      await event.edit("Added {} triggers to the blacklist in the current chat".format(len(to_blacklist)))
    elif event.from_id==bot2.uid:
      text = event.pattern_match.group(1)
      to_blacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
      for trigger in to_blacklist:
          sqlx.a_to_blx(event.chat_id, trigger.lower())
      await event.edit("Added {} triggers to the blacklist in the current chat".format(len(to_blacklist)))


@ItzSjDude(pattern="listblacklist", outgoing=True)
async def on_view_blacklist(event):
    if event.from_id==bot.uid:
      all_blacklisted = sql.get_chat_blacklist(event.chat_id)
      OUT_STR = "Blacklists in the Current Chat:\n"
      if len(all_blacklisted) > 0:
          for trigger in all_blacklisted:
              OUT_STR += f"👉 {trigger} \n"
      else:
          OUT_STR = "No BlackLists. Start Saving using `.addblacklist`"
      if len(OUT_STR) > Config.MAX_MESSAGE_SIZE_LIMIT:
          with io.BytesIO(str.encode(OUT_STR)) as out_file:
              out_file.name = "blacklist.text"
              await bot.send_file(
                  event.chat_id,
                  out_file,
                  force_document=True,
                  allow_cache=False,
                  caption="BlackLists in the Current Chat",
                  reply_to=event
              )
              await event.delete()
      else:
          await event.edit(OUT_STR)
    elif bot2 is not None and event.from_id==bot2.uid:
      all_blacklisted = sqlx.gc_blx(event.chat_id)
      OUT_STR = "Blacklists in the Current Chat:\n"
      if len(all_blacklisted) > 0:
          for trigger in all_blacklisted:
              OUT_STR += f"👉 {trigger} \n"
      else:
          OUT_STR = "No BlackLists. Start Saving using `.addblacklist`"
      if len(OUT_STR) > Config.MAX_MESSAGE_SIZE_LIMIT:
          with io.BytesIO(str.encode(OUT_STR)) as out_file:
              out_file.name = "blacklist.text"
              await bot2.send_file(
                  event.chat_id,
                  out_file,
                  force_document=True,
                  allow_cache=False,
                  caption="BlackLists in the Current Chat",
                  reply_to=event
              )
              await event.delete()
      else:
          await event.edit(OUT_STR)



@ItzSjDude(pattern="rmblacklist ((.|\n)*)")
async def on_delete_blacklist(event):
    if event.chat_id == bot.uid:
      text = event.pattern_match.group(1)
      to_unblacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
      successful = 0
      for trigger in to_unblacklist:
          if sql.rm_from_blacklist(event.chat_id, trigger.lower()):
              successful += 1
      await event.edit(f"Removed {successful} / {len(to_unblacklist)} from the blacklist")
    elif bot2 is not None and event.from_id==bot2.uid:
      text = event.pattern_match.group(1)
      to_unblacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
      successful = 0
      for trigger in to_unblacklist:
          if sqlx.rf_blx(event.chat_id, trigger.lower()):
              successful += 1
      await event.edit(f"Removed {successful} / {len(to_unblacklist)} from the blacklist")

if Var.STR2 is not None:
  @bot2.on(admin_cmd(incoming=True))
  async def on_new_message(event):
      # TODO: exempt admins from locks
      if bot2.me.id == event.from_id:
          return
      name = event.raw_text
      snips = sqlx.gc_blx(event.chat_id)
      for snip in snips:
          pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
          if re.search(pattern, name, flags=re.IGNORECASE):
              try:
                  await event.delete()
              except Exception as e:
                  await event.reply("I do not have DELETE permission in this chat")
                  sqlx.rf_blx(event.chat_id, snip.lower())
              break
