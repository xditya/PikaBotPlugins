"""Songs Plugin for Pikabot
{i}song <song name>
"""
# Made By @ItzSjDude. All rights Reserved


import asyncio

@ItzSjDude(pattern="song (.*)")
async def _(event):
    chat='@songdl_Bot'
    input_str = str(event.text[6:])
    chut = await event.reply(f'**Searching for** `{input_str}`')
    async with event.client.conversation(chat) as bot_conv:
    	await event.client.send_message(chat, input_str)
    	await asyncio.sleep(10)
    	reply = await event.client.get_messages(chat)
    	if "Pick" in reply[0].message:
    		await reply[0].click(0)
    		await chut.edit('**Sending Your requested song...**')
    		await asyncio.sleep(3)
    		a = await event.client.get_messages(chat)
    		ac = a[0]
    		await event.client.send_file(event.chat_id, ac, caption=f'**{input_str}\nUploaded by [Pikabot](t.me/ItzSjDudeProjects)**')
    		await chut.delete()
    	else:
    		await chut.edit("**Failed to get your song...**")
    
    
