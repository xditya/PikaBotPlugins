from pikabot.sql_helper.mute_sql import *
from pikabot.utils import admin_cmd
import asyncio

@bot.on(admin_cmd(pattern=r"mute ?(\d+)?"))
async def startmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.reply("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/mute", "!mute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.reply("Please reply to a user or add their userid into the command to mute them.")
        chat_id = event.chat_id
        chat = await event.get_chat()
        if "admin_rights" in vars(chat) and vars(chat)["admin_rights"] is not None: 
            if chat.admin_rights.delete_messages is True:
                pass
            else:
                return await event.reply("`You can't mute a person if you dont have delete messages permission. ಥ﹏ಥ`")
        elif "creator" in vars(chat):
            pass
        elif private == True:
            pass
        else:
            return await event.reply("`You can't mute a person without admin rights niqq.` ಥ﹏ಥ  ")
        if is_muted(userid, chat_id):
            return await event.reply("This user is already muted in this chat ~~lmfao sed rip~~")
        try:
            mute(userid, chat_id)
        except Exception as e:
            await event.reply("Error occured!\nError is " + str(e))
        else:
            await event.reply("Successfully muted that person.\n**｀-´)⊃━☆ﾟ.*･｡ﾟ **")

@bot.on(admin_cmd(pattern=r"unmute ?(\d+)?"))
async def endmute(event):
    private = False
    if event.fwd_from:
        return
    elif event.is_private:
        await event.reply("Unexpected issues or ugly errors may occur!")
        await asyncio.sleep(3)
        private = True
    if any([x in event.raw_text for x in ("/unmute", "!unmute")]):
        await asyncio.sleep(0.5)
    else:
        reply = await event.get_reply_message()
        if event.pattern_match.group(1) is not None:
            userid = event.pattern_match.group(1)
        elif reply is not None:
            userid = reply.sender_id
        elif private is True:
            userid = event.chat_id
        else:
            return await event.reply("Please reply to a user or add their userid into the command to unmute them.")
        chat_id = event.chat_id
        if not is_muted(userid, chat_id):
            return await event.reply("__This user is not muted in this chat__\n（ ^_^）o自自o（^_^ ）")
        try:
            unmute(userid, chat_id)
        except Exception as e:
            await event.reply("Error occured!\nError is " + str(e))
        else:
            await event.reply("Successfully unmuted that person\n乁( ◔ ౪◔)「    ┑(￣Д ￣)┍")
            


@bot.on(admin_cmd(incoming=True))
async def watcher(event):
    if is_muted(event.sender_id, event.chat_id):
        await event.delete()

