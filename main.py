from telethon import TelegramClient, events

api_id = 29200882
api_hash = '14b9bfd2dfe047c0b99839519cd81481'

client = TelegramClient('session', api_id, api_hash)

@client.on(events.NewMessage(outgoing= True, pattern=".hello"))
async def greeting(event):
  chat = await event.get_chat()
 # await client.send_message(chat, "Hello! How are you?")
 # await client.edit_message(event.message, "Hello! How are you?")
  await client.reply("Hello! How are you?")






client.start()
print("Userbot runned!!!")
client.run_until_disconnected()

