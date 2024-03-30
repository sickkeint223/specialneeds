import re
from telethon import TelegramClient, events

api_id = 27053740
api_hash = '4905e2c790084276f02734e4894ceff5'

client = TelegramClient('user', api_id, api_hash).start()

specific_responses = {
    "hello bot, i need assistance.": "We'll get back to you soon!",

    "80": "Out of stock, we have $115 and $200 available at the moment",

    "84.99": "Out of stock, we have $115 and $200 available at the moment",

    "85": "Out of stock, we have $115 and $200 available at the moment",

    "90": "Out of stock, we have $115 and $200 available at the moment",

    "100": "Sweet, what payment method",

    "110": "Sweet, what payment method",

    "114.99": "Sweet, what payment method",

    "115": "Sweet, what payment method?",

    "199.99": "Sweet, what payment method?",

    "200": "Sweet, what payment method?",

    "bank tranny": "I would usually accept bank transfers but right now I am having some issues receiving payments.\n"
                   " \n"
                   "Do you have 10 minutes for me to guide you through purchasing\n"
                   "crypto, Wont take long and is easy.\n"
                   " \n"
                   "If you would like to proceed say 'Yes'\n"
                   " \n"
                   "If you would not like to proceed say 'No'",

    "bank transfer": "I would usually accept bank transfers but right now I am having some issues receiving payments.\n"
                   " \n"
                   "Do you have 10 minutes for me to guide you through purchasing\n"
                   "crypto, Wont take long and is easy.\n"
                   " \n"
                   "If you would like to proceed say 'Yes'\n"
                   " \n"
                   "If you would not like to proceed say 'No'",

    "bank": "I would usually accept bank transfers but right now I am having some issues receiving payments.\n"
                   " \n"
                   "Do you have 10 minutes for me to guide you through purchasing\n"
                   "crypto, Wont take long and is easy.\n"
                   " \n"
                   "If you would like to proceed say 'Yes'\n"
                   " \n"
                   "If you would not like to proceed say 'No'",

    "transfer": "I would usually accept bank transfers but right now I am having some issues receiving payments.\n"
                   " \n"
                   "Do you have 10 minutes for me to guide you through purchasing\n"
                   "crypto, Wont take long and is easy.\n"
                   " \n"
                   "If you would like to proceed say 'Yes'\n"
                   " \n"
                   "If you would not like to proceed say 'No'",

    "asb": "I would usually accept bank transfers but right now I am having some issues receiving payments.\n"
                   " \n"
                   "Do you have 10 minutes for me to guide you through purchasing\n"
                   "crypto, Wont take long and is easy.\n"
                   " \n"
                   "If you would like to proceed say 'Yes'\n"
                   " \n"
                   "If you would not like to proceed say 'No'",

    "kiwibank": "I would usually accept bank transfers but right now I am having some issues receiving payments.\n"
                   " \n"
                   "Do you have 10 minutes for me to guide you through purchasing\n"
                   "crypto, Wont take long and is easy.\n"
                   " \n"
                   "If you would like to proceed say 'Yes'\n"
                   " \n"
                   "If you would not like to proceed say 'No'",

    "anz": "I would usually accept bank transfers but right now I am having some issues receiving payments.\n"
                   " \n"
                   "Do you have 10 minutes for me to guide you through purchasing\n"
                   "crypto, Wont take long and is easy.\n"
                   " \n"
                   "If you would like to proceed say 'Yes'\n"
                   " \n"
                   "If you would not like to proceed say 'No'",

    "bnz": "I would usually accept bank transfers but right now I am having some issues receiving payments.\n"
                   " \n"
                   "Do you have 10 minutes for me to guide you through purchasing\n"
                   "crypto, Wont take long and is easy.\n"
                   " \n"
                   "If you would like to proceed say 'Yes'\n"
                   " \n"
                   "If you would not like to proceed say 'No'",

    "btc": "This is my BTC address below send screenshot once done.\n"
           " \n"
           "bc1qjhjruq6lacsu52u68k3hdg2kdj537dgcdfnaws",

    "bitcoin": "This is my BTC address below send screenshot once done.\n"
               " \n"
               "bc1qjhjruq6lacsu52u68k3hdg2kdj537dgcdfnaws",

    "bit coin": "This is my BTC address below send screenshot once done.\n"
                " \n"
                "bc1qjhjruq6lacsu52u68k3hdg2kdj537dgcdfnaws",

    "ETH": "This is my ETH address below send screenshot once done.\n"
                " \n"
                "0xeF6D6E955e848568Ad73EAaC4218B9cae0821548",

    "Ethereum": "This is my ETH address below send screenshot once done.\n"
                " \n"
                "0xeF6D6E955e848568Ad73EAaC4218B9cae0821548",

    "Yes": "Download MetaMask from appstore and create a wallet,\n"
           " \n"
           "it has the fox as the logo. Say 'done' once done.",

    "Done": "Press the 'Buy ETH' button and buy $115/$200 worth of Eth depending on the PayPal you selected.\n"
             " \n"
             "Use debit or apple pay,\n"
             " \n"
             "Press get quotes and you will see some options use the\n"
            "'Ramp' option or 'Mercruryo' option\n"
            " \n"
             "Then proceed with payment.\n"
            " \n"
            "( Say 'finished' once finished )  ( If you have an issue say 'issue' ) ",

    "Finished": "It will take approximately 5 minutes to receive the the ETH into your wallet,\n"
                " \n"
                "(You will receive the ETH in USD so dont worry if the amount is lower then you purchased)\n"
                " \n"
                "Once you have received it say 'Received'",
    "Issue":  "Solutions to common issues -\n\n"
    "1. Amount showing less\n\n"
    "- EXAMPLE -\n\n"
    "$105 instead of $115 on the quote\n\n"
    "this is just because of fees.\n"
    "We are accounting for this, please just continue\n\n"
    "2. Ramp and Mercruryo Quotes not showing up\n\n"
    "Those are our preferred as they do not require ID\n"
    "but if not there continue with whatever quotes is available EG Moonpay ETC\n\n"
    "3. Funds coming up less than I purchased\n\n"
    "No need to worry it is just in USD, Say 'Finished'\n\n"
    "4. Payment not going through Ramp account locked / Transaction denied\n\n"
    "Your bank would have blocked the payment.\n\n"
    "The solution to this would be to call them and tell them to not block it\n\n"
    "but try other quotes first such as Transak.\n\n"
    "Any other issues we will come and help with.",
    "Received": "Press the bottom middle button and then the 'Send' button\n\n"
                "Then paste into the 'To' section the address im sending below",
    "No": " ",
}


async def handle_payment_response(sender, message_text):
    for word, response in specific_responses.items():
        if re.search(r'\b{}\b'.format(re.escape(word)), message_text, re.IGNORECASE):
            if word == "Received":
                # Send "dd" first
                await client.send_message(sender, response)
                # Then send the additional message
                await client.send_message(sender, "0xeF6D6E955e848568Ad73EAaC4218B9cae0821548")
                await client.send_message(sender, "After pasting the address above, Then press 'Next'.\n\n"
                                                  "If you have purchased $115 type 0.016 then next and then send.\n\n "
                                                  "If you have purchased $200 type 0.030 then next then send.\n\n"
                                                  "Once it has sent say 'Sent'")
            else:
                # Send the regular response
                await client.send_message(sender, response)
            return

    # If no match found, send a default response
    await client.send_message(sender, default_response())



@client.on(events.NewMessage)
async def handler(event):
    sender = await event.get_sender()
    message_text = event.raw_text.strip().lower()

    if "money ready" in message_text:
        await client.send_message(sender, "Which PayPal do you want to buy?")
    elif "payment method" in message_text:
        # Handle payment method response
        await handle_payment_response(sender, message_text)
    else:
        # Handle other user responses
        await handle_payment_response(sender, message_text)


def default_response():
    return ("This is what we have available, get back to me with which you would like to purchase.\n"
            "https://t.me/vexsenterprise/786")


client.run_until_disconnected()