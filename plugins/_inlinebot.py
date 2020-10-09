'''©ItzSjDude Officially made for PikachuUserbot'''

from math import ceil
import asyncio
import json
import random
import re
from telethon import events, errors, custom
from var import Var
import io
from pikabot import CMD_LIST
try:
   from pikabot import bot2, bot3, bot4
except:
    pass

b1=bot.me
if bot2:
    b2 = bot2.me
else: 
    b2=b1
if bot3:
    b3 = bot3.me
else: 
    b3=b1
if bot3:
    b4 = bot4.me
else: 
    b4=b1   

if Var.TG_BOT_USER_NAME_BF_HER is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)  # pylint:disable=E0602
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        if event.query.user_id == b1.id or event.query.user_id == b2.id or event.query.user_id == b3.id or event.query.user_id == b4.id and query.startswith("Pïkå¢hµ"):
            rev_text = query[::-1]
            buttons = paginate_help(0, CMD_LIST, "helpme")
            result = builder.article(
                "©Pikachu Userbot Help",
                text="{}\nCurrently Loaded Plugins: {}".format(
                    query, len(CMD_LIST)),
                buttons=buttons,
                link_preview=False
            )
        await event.answer([result] if result else None)
        
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_next\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == b1.id or event.query.user_id == b2.id or event.query.user_id == b3.id or event.query.user_id == b4.id and query.startswith("Pïkå¢hµ"):
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number + 1, CMD_LIST, "helpme")
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
        
        else:
            reply_pop_up_alert = "Please get your own PikaBot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)


    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"helpme_prev\((.+?)\)")
    ))
    async def on_plug_in_callback_query_handler(event):
        if event.query.user_id == b1.id or event.query.user_id == b2.id or event.query.user_id == b3.id or event.query.user_id == b4.id and query.startswith("Pïkå¢hµ"):
            current_page_number = int(
                event.data_match.group(1).decode("UTF-8"))
            buttons = paginate_help(
                current_page_number - 1,
                CMD_LIST,  # pylint:disable=E0602
                "helpme"
            )
            # https://t.me/TelethonChat/115200
            await event.edit(buttons=buttons)
 
        else:
            reply_pop_up_alert = "Please get your own PikaBot, and don't use mine!"
            await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            
    @tgbot.on(events.callbackquery.CallbackQuery(  # pylint:disable=E0602
        data=re.compile(b"us_plugin_(.*)")
    ))
    async def on_plug_in_callback_query_handler(event):
        usr= event.query
        if usr.user_id == b1.id or usr.user_id == b2.id or usr.user_id == b3.id or usr.user_id == b4.id and query.startswith("Pïkå¢hµ"):
             plugin_name = event.data_match.group(1).decode("UTF-8")
             help_string = CMD_LIST[plugin_name].__doc__.format(i=rx) 
                 
             reply_pop_up_alert = help_string if help_string is not None else \
             "No DOCSTRING has been setup for {} plugin".format(plugin_name)
             reply_pop_up_alert += "\n\n Use .unload {} to remove this plugin\n\
               ©PikaBot".format(plugin_name)
             if len(help_string) > 200:
               try:
                 pop_up = "Command list too long check Saved Messages"
                 await event.answer(pop_up, cache_time=0, alert=True)
                 if bot is not None and event.query.user_id==bot.uid:
                    await bot.send_message('me', help_string) 
                 if bot2 is not None and event.query.user_id==bot2.uid:
                    await bot2.send_message('me', help_string)
                 if bot3 is not None and event.query.user_id==bot3.uid:
                    await bot3.send_message('me', help_string) 
                 if bot4 is not None and event.query.user_id==bot4.uid:
                    await bot4.send_message('me', help_string)
               except:
                   pass
             else:
               await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
                 
             

        else:
             z=await bot.get_entity(await bot.get_input_entity(usr.user_id))
             reply_pop_up_alert = "Hi {},\n       Why r u clicking this this.Please get your own PikaBot, and don't use mine!".format(z.first_name)
             await event.answer(reply_pop_up_alert, cache_time=0, alert=True)
            
def paginate_help(page_number, loaded_plugins, prefix):
    number_of_rows = 5
    number_of_cols = 2
    helpable_plugins = []
    for p in loaded_plugins:
        if not p.startswith("_"):
            helpable_plugins.append(p)
    helpable_plugins = sorted(helpable_plugins)
    modules = [custom.Button.inline(
        "{} {} {}".format("🚀",x, "🛸"),
        data="us_plugin_{}".format(x))
        for x in helpable_plugins]
    pairs = list(zip(modules[::number_of_cols], modules[1::number_of_cols]))
    if len(modules) % number_of_cols == 1:
        pairs.append((modules[-1],))
    max_num_pages = ceil(len(pairs) / number_of_rows)
    modulo_page = page_number % max_num_pages
    if len(pairs) > number_of_rows:
        pairs = pairs[modulo_page * number_of_rows:number_of_rows * (modulo_page + 1)] + \
            [
            (custom.Button.inline("Previous", data="{}_prev({})".format(prefix, modulo_page)),
             custom.Button.inline("Next", data="{}_next({})".format(prefix, modulo_page)))
        ]
    return pairs
