# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.b (the "License");
# you may not use this file except in compliance with the License.
#
#

""" Userbot module for having some fun with people. """

import asyncio
import random
import re
import time

from collections import deque

import requests

from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName

from cowpy import cow

from pikabot import *
from pikabot.utils import register,admin_cmd




@register(outgoing=True, pattern=r"^.(\w+)say (.*)")
async def univsaye(cowmsg):
    """ For .cowsay module, userbot wrapper for cow which says things. """
    if not cowmsg.text[0].isalpha() and cowmsg.text[0] not in ("/", "#", "@", "!"):
        arg = cowmsg.pattern_match.group(1).lower()
        text = cowmsg.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await cowmsg.edit(f"`{cheese.milk(text).replace('`', '´')}`")


@register(outgoing=True, pattern="^.:/$")
async def kek(keks):
    if not keks.text[0].isalpha() and keks.text[0] not in ("/", "#", "@", "!"):
        """ Check yourself ;)"""
        uio = ["/", "\\"]
        for i in range(1, 15):
            time.sleep(0.3)
            await keks.edit(":" + uio[i % 2])


@register(pattern="^.slap(?: |$)(.*)", outgoing=True)
async def who(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        """ slaps a user, or get slapped if not a reply. """
        if event.fwd_from:
            return

        replied_user = await get_user(event)
        caption = await slap(replied_user, event)
        message_id_to_reply = event.message.reply_to_msg_id

        if not message_id_to_reply:
            message_id_to_reply = None

        try:
            await event.edit(caption)

        except:
            await event.edit("`Can't slap this person, need to fetch some sticks and stones !!`")

async def get_user(event):
    """ Get the user from argument or replied message. """
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        replied_user = await event.client(GetFullUserRequest(previous_message.from_id))
    else:
        user = event.pattern_match.group(1)

        if user.isnumeric():
            user = int(user)

        if not user:
            self_user = await event.client.get_me()
            user = self_user.id

        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                replied_user = await event.client(GetFullUserRequest(user_id))
                return replied_user
        try:
            user_object = await event.client.get_entity(user)
            replied_user = await event.client(GetFullUserRequest(user_object.id))

        except (TypeError, ValueError):
            await event.edit("`I don't slap aliens, they ugly AF !!`")
            return None

    return replied_user

async def slap(replied_user, event):
    """ Construct a funny slap sentence !! """
    user_id = replied_user.user.id
    first_name = replied_user.user.first_name
    username = replied_user.user.username

    if username:
        slapped = "@{}".format(username)
    else:
        slapped = f"[{first_name}](tg://user?id={user_id})"

    temp = random.choice(SLAP_TEMPLATES)
    item = random.choice(ITEMS)
    hit = random.choice(HIT)
    throw = random.choice(THROW)

    caption = "..." + temp.format(victim=slapped, item=item, hits=hit, throws=throw)

    return caption

@register(outgoing=True, pattern="^.-_-$")
async def lol(lel):
    if not lel.text[0].isalpha() and lel.text[0] not in ("/", "#", "@", "!"):
        """ Ok... """
        okay = "-_-"
        for _ in range(10):
            okay = okay[:-1] + "_-"
            await lel.edit(okay)

 
@register(outgoing=True, pattern="^.;_;$")
async def fun(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        t = ";__;"
        for j in range(10):
            t = t[:-1] + "_;"
            await e.edit(t)

@register(outgoing=True, pattern="^.cry$")
async def cry(e):
    """ y u du dis, i cry everytime !! """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(CRI))

@register(outgoing=True, pattern="^.insult$")
async def insult(e):
    """ I make you cry !! """
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit(random.choice(INSULT_STRINGS))

@register(outgoing=True, pattern="^.cp(?: |$)(.*)")
async def copypasta(cp_e):
    """ Copypasta the famous meme """
    if not cp_e.text[0].isalpha() and cp_e.text[0] not in ("/", "#", "@", "!"):
        textx = await cp_e.get_reply_message()
        message = cp_e.pattern_match.group(1)

        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await cp_e.edit("`😂🅱️IvE👐sOME👅text👅for✌️Me👌tO👐MAkE👀iT💞funNy!💦`")
            return

        reply_text = random.choice(EMOJIS)
        b_char = random.choice(
            message
        ).lower()  # choose a random character in the message to be substituted with 🅱️
        for owo in message:
            if owo == " ":
                reply_text += random.choice(EMOJIS)
            elif owo in EMOJIS:
                reply_text += owo
                reply_text += random.choice(EMOJIS)
            elif owo.lower() == b_char:
                reply_text += "🅱️"
            else:
                if bool(random.getrandbits(1)):
                    reply_text += owo.upper()
                else:
                    reply_text += owo.lower()
        reply_text += random.choice(EMOJIS)
        await cp_e.edit(reply_text)


@register(outgoing=True, pattern="^.vapor(?: |$)(.*)")
async def vapor(vpr):
    """ Vaporize everything! """
    if not vpr.text[0].isalpha() and vpr.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await vpr.get_reply_message()
        message = vpr.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await vpr.edit("`Ｇｉｖｅ ｓｏｍｅ ｔｅｘｔ ｆｏｒ ｖａｐｏｒ！`")
            return

        for charac in message:
            if 0x21 <= ord(charac) <= 0x7F:
                reply_text.append(chr(ord(charac) + 0xFEE0))
            elif ord(charac) == 0x20:
                reply_text.append(chr(0x3000))
            else:
                reply_text.append(charac)

        await vpr.edit("".join(reply_text))

			  
@register(outgoing=True, pattern="^.repo$")
async def source(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Click [Here](https://github.com/ItzSjDude/PikachuUserbot) to open this mdafuk'in cool userbot repo .")
			  
			  
@register(outgoing=True, pattern="^.str(?: |$)(.*)")
async def stretch(stret):
    """ Stretch it."""
    if not stret.text[0].isalpha() and stret.text[0] not in ("/", "#", "@", "!"):
        textx = await stret.get_reply_message()
        message = stret.text
        message = stret.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await stret.edit("`GiiiiiiiB sooooooomeeeeeee teeeeeeext!`")
            return

        count = random.randint(3, 10)
        reply_text = re.sub(
            r"([aeiouAEIOUａｅｉｏｕＡＥＩＯＵаеиоуюяыэё])",
            (r"\1"*count),
            message
        )
        await stret.edit(reply_text)


@register(outgoing=True, pattern="^.zal(?: |$)(.*)")
async def zal(zgfy):
    """ Invoke the feeling of chaos. """
    if not zgfy.text[0].isalpha() and zgfy.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await zgfy.get_reply_message()
        message = zgfy.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await zgfy.edit(
                "`gͫ ̆ i̛ ̺ v͇̆ ȅͅ   a̢ͦ   s̴̪ c̸̢ ä̸ rͩͣ y͖͞   t̨͚ é̠ x̢͖  t͔͛`"
            )
            return

        for charac in message:
            if not charac.isalpha():
                reply_text.append(charac)
                continue

            for _ in range(0, 3):
                randint = random.randint(0, 2)

                if randint == 0:
                    charac = charac.strip() + \
                        random.choice(ZALG_LIST[0]).strip()
                elif randint == 1:
                    charac = charac.strip() + \
                        random.choice(ZALG_LIST[1]).strip()
                else:
                    charac = charac.strip() + \
                        random.choice(ZALG_LIST[2]).strip()

            reply_text.append(charac)

        await zgfy.edit("".join(reply_text))
			  
@register(outgoing=True, pattern="^.pkill$")
async def killing (killed):
    """ Dont Kill Too much -_-"""
    if not killed.text[0].isalpha() and killed.text[0] not in ("/", "#", "@", "!"):
        if await killed.get_reply_message():
            await killed.edit(
                "`My Master killed targeted user by Headshot 😈......`\n"
		"#Sad_Reacts_Onli\n"
            )
			  
@register(outgoing=True, pattern="^.bt$")
async def bluetext(bte):
    """ Believe me, you will find this useful. """
    if not bte.text[0].isalpha() and bte.text[0] not in ("/", "#", "@", "!"):
        if await bte.get_reply_message():
            await bte.edit(
                "`BLUETEXT MUST CLICK.`\n"
                "`Are you a stupid animal which is attracted to colours?`"
            )
			  
@register(outgoing=True, pattern="^.rape$")
async def raping (raped):
    """ Dont Rape Too much -_-"""
    if not raped.text[0].isalpha() and raped.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(RAPE_STRINGS) - 1)
        reply_text = RAPE_STRINGS[index]
        await raped.edit(reply_text)
			  
@register(outgoing=True, pattern="^.pro$")
async def proo (pros):
    """ String for Pros only -_-"""
    if not pros.text[0].isalpha() and pros.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(PRO_STRINGS) - 1)
        reply_text = PRO_STRINGS[index]
        await pros.edit(reply_text)

@register(outgoing=True, pattern="^.fuk$")
async def chutiya (fuks):
    """ String for fhu only -_-"""
    if not fuks.text[0].isalpha() and fuks.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(FUK_STRINGS) - 1)
        reply_text = FUK_STRINGS[index]
        await fuks.edit(reply_text)

@register(outgoing=True, pattern="^.chu$")
async def chutiya (chus):
    """ String for Chu only -_-"""
    if not chus.text[0].isalpha() and chus.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(CHU_STRINGS) - 1)
        reply_text = CHU_STRINGS[index]
        await chus.edit(reply_text)
			  			  
@register(outgoing=True, pattern="^.thanos$")
async def thanos (thanos):
    """ String for thanos only -_-"""
    if not thanos.text[0].isalpha() and thanos.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(THANOS_STRINGS) - 1)
        reply_text = THANOS_STRINGS[index]
        await thanos.edit(reply_text)	
			  
@register(outgoing=True, pattern="^.hardabuse$")
async def fuckedd (abusehard):
    """ Dont Use this Too much bsdk -_-"""
    if not abusehard.text[0].isalpha() and abusehard.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(ABUSEHARD_STRING) - 1)
        reply_text = ABUSEHARD_STRING[index]
        await abusehard.edit(reply_text)
			  
			  
@register(outgoing=True, pattern="^.gey$")
async def geys (geyed):
    """ Use only for gey ppl -_-"""
    if not geyed.text[0].isalpha() and geyed.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(GEY_STRINGS) - 1)
        reply_text = GEY_STRINGS[index]
        await geyed.edit(reply_text)
			  
			  
@register(outgoing=True, pattern="^.abuse$")
async def abusing (abused):
    """ Dont Abuse Too much bsdk -_-"""
    if not abused.text[0].isalpha() and abused.text[0] not in ("/", "#", "@", "!"):
        index = random.randint(0, len(ABUSE_STRINGS) - 1)
        reply_text = ABUSE_STRINGS[index]
        await abused.edit(reply_text)


@register(outgoing=True, pattern="^.owo(?: |$)(.*)")
async def faces(owo):
    """ UwU """
    if not owo.text[0].isalpha() and owo.text[0] not in ("/", "#", "@", "!"):
        textx = await owo.get_reply_message()
        message = owo.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await owo.edit("` UwU no text given! `")
            return

        reply_text = re.sub(r"(r|l)", "w", message)
        reply_text = re.sub(r"(R|L)", "W", reply_text)
        reply_text = re.sub(r"n([aeiou])", r"ny\1", reply_text)
        reply_text = re.sub(r"N([aeiouAEIOU])", r"Ny\1", reply_text)
        reply_text = re.sub(r"\!+", " " + random.choice(UWUS), reply_text)
        reply_text = reply_text.replace("ove", "uv")
        reply_text += " " + random.choice(UWUS)
        await owo.edit(reply_text)


@register(outgoing=True, pattern="^.react$")
async def react_meme(react):
    """ Make your userbot react to everything. """
    if not react.text[0].isalpha() and react.text[0] not in ("/", "#", "@", "!"):
        await react.edit(random.choice(FACEREACTS))


@register(outgoing=True, pattern="^.shg$")
async def shrugger(shg):
    r""" ¯\_(ツ)_/¯ """
    if not shg.text[0].isalpha() and shg.text[0] not in ("/", "#", "@", "!"):
        await shg.edit(random.choice(SHGS))




@register(outgoing=True, pattern="^.noob$")
async def metoo(hahayes):
    """ Haha yes """
    if not hahayes.text[0].isalpha() and hahayes.text[0] not in ("/", "#", "@", "!"):
        await hahayes.edit(random.choice(NOOBSTR))
			  
@register(outgoing=True, pattern="^.rendi$")
async def metoo(hahayes):
    """ Haha yes """
    if not hahayes.text[0].isalpha() and hahayes.text[0] not in ("/", "#", "@", "!"):
        await hahayes.edit(random.choice(RENDISTR))
			 			  
@register(outgoing=True, pattern="^.oof$")
async def Oof(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        t = "Oof"
        for j in range(15):
            t = t[:-1] + "of"
            await e.edit(t)

@register(outgoing=True, pattern="^.10iq$")
async def iqless(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("♿")




@register(outgoing=True, pattern="^.mock(?: |$)(.*)")
async def spongemocktext(mock):
    """ Do it and find the real fun. """
    if not mock.text[0].isalpha() and mock.text[0] not in ("/", "#", "@", "!"):
        reply_text = list()
        textx = await mock.get_reply_message()
        message = mock.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await mock.edit("`gIvE sOMEtHInG tO MoCk!`")
            return

        for charac in message:
            if charac.isalpha() and random.randint(0, 1):
                to_app = charac.upper() if charac.islower() else charac.lower()
                reply_text.append(to_app)
            else:
                reply_text.append(charac)

        await mock.edit("".join(reply_text))


@register(outgoing=True, pattern="^.clap(?: |$)(.*)")
async def claptext(memereview):
    """ Praise people! """
    if not memereview.text[0].isalpha() and memereview.text[0] not in ("/", "#", "@", "!"):
        textx = await memereview.get_reply_message()
        message = memereview.pattern_match.group(1)
        if message:
            pass
        elif textx:
            message = textx.text
        else:
            await memereview.edit("`Hah, I don't clap pointlessly!`")
            return
        reply_text = "👏 "
        reply_text += message.replace(" ", " 👏 ")
        reply_text += " 👏"
        await memereview.edit(reply_text)




@register(outgoing=True, pattern="^.smk (.*)")
async def smrk(smk):
        if not smk.text[0].isalpha() and smk.text[0] not in ("/", "#", "@", "!"):
            textx = await smk.get_reply_message()
            message = smk.text
        if message[5:]:
            message = str(message[5:])
        elif textx:
            message = textx
            message = str(message.message)
        if message == 'dele':
            await smk.edit( message +'te the hell' + "ツ" )
            await smk.edit("ツ")
        else:
             smirk = " ツ"
             reply_text = message + smirk
             await smk.edit(reply_text)





@register(outgoing=True, pattern="^.lfy (.*)",)
async def let_me_google_that_for_you(lmgtfy_q):
    if not lmgtfy_q.text[0].isalpha() and lmgtfy_q.text[0] not in ("/", "#", "@", "!"):
        textx = await lmgtfy_q.get_reply_message()
        query = lmgtfy_q.text
        if query[5:]:
            query = str(query[5:])
        elif textx:
            query = textx
            query = query.message
        query_encoded = query.replace(" ", "+")
        lfy_url = f"http://lmgtfy.com/?s=g&iie=1&q={query_encoded}"
        payload = {'format': 'json', 'url': lfy_url}
        r = requests.get('http://is.gd/create.php', params=payload)
        await lmgtfy_q.edit(f"[{query}]({r.json()['shorturl']})")
        if BOTLOG:
            await bot.send_message(
                BOTLOG_CHATID,
                "LMGTFY query `" + query + "` was executed successfully",
            )			  

CMD_HELP.update({
    "memes": ".cowsay\
\nUsage: cow which says things.\
\n\n.milksay\
\nUsage: Weird Milk that can speak\
\n\n:/\
\nUsage: Check yourself ;)\
\n\n-_-\
\nUsage: Ok...\
\n\n;_;\
\nUsage: Like `-_-` but crying.\
\n\n.cp\
\nUsage: Copypasta the famous meme\
\n\n.vapor\
\nUsage: Vaporize everything!\
\n\n.str\
\nUsage: Stretch it.\
\n\n.10iq\
\nUsage: You retard !!\
\n\n.zal\
\nUsage: Invoke the feeling of chaos.\
\n\n.oof\
\nUsage: Ooooof\
\n\n.moon\
\nUsage: kensar moon animation.\
\n\n.clock\
\nUsage: kensar clock animation.\
\n\n.earth\
\nUsage: kensar earth animation.\
\n\n.hi\
\nUsage: Greet everyone!\
\n\n.coinflip <heads/tails>\
\nUsage: Flip a coin !!\
\n\n.owo\
\nUsage: UwU\
\n\n.react\
\nUsage: Make your userbot react to everything.\
\n\n.slap\
\nUsage: reply to slap them with random objects !!\
\n\n.cry\
\nUsage: y u du dis, i cri.\
\n\n.shg\
\nUsage: Shrug at it !!\
\n\n.runs\
\nUsage: Run, run, RUNNN! [`.disable runs`: disable | `.enable runs`: enable]\
\n\n.metoo\
\nUsage: Haha yes\
\n\n.mock\
\nUsage: Do it and find the real fun.\
\n\n.clap\
\nUsage: Praise people!\
\n\n.f <emoji/character>\
\nUsage: Pay Respects.\
\n\n.bt\
\nUsage: Believe me, you will find this useful.\
\n\n.smk <text/reply>\
\nUsage: A shit module for ツ , who cares.\
\n\n.type\
\nUsage: Just a small command to make your keyboard become a typewriter!\
\n\n.lfy <query>\
\nUsage: Let me Google that for you real quick !!\
\n\n.decide\
\nUsage: Make a quick decision.\
\n\n.abusehard\
\nUsage: You already got that! Ain't?.\
\n\n.chu\
\nUsage: Incase, the person infront of you is....\
\n\n.fuk\
\nUsage: The onlu word that can be used fucking everywhere.\
\n\n.thanos\
\nUsage: Try and then Snap.\
\n\n.noob\
\nUsage: Whadya want to know? Are you a NOOB?\
\n\n.pro\
\nUsage: If you think you're pro, try this.\
\n\n.abuse\
\nUsage: Protects you from unwanted peeps.\
\n\n\nThanks to 🅱️ottom🅱️ext🅱️ot (@NotAMemeBot) for some of these."
})
