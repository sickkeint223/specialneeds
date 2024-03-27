from telethon import TelegramClient, events

# api_id and api_hash from https://my.telegram.org/apps
api_id = 27053740
api_hash = '4905e2c790084276f02734e4894ceff5'

client = TelegramClient('user', api_id, api_hash).start()

# The default message is what is sent when none of the specific_responses are sent
default_message = "Hello! Thank you for contacting me 👍\nI'll be back soon and reply to your message."

# Dictionary
specific_responses = {

    "Hello bot, I need assistance.": "We'll get back to you soon!",
    "80": "We only have 110s.",
    "90": "We only have 190s",

    # Add more specific messages and their responses here
    # : is the seperator, left is the specified word, right is the response if the specified word is in the user reply
}


@client.on(events.NewMessage())
async def handler(event):
    sender = await event.get_input_sender()
    msg_text = event.message.text.lower() if event.message.text else None
    response = specific_responses.get(msg_text, default_message)
    await client.send_message(sender, response)


client.run_until_disconnected()