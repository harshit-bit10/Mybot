from pyrogram import Client, filters
from utils import check_user, multi_rec, getChannels

app = Client(
    "SharkRipsbot",
    bot_token = "7254163662:AAGt5w43odIV5YjjzHXqv3L9ZVG1UxDItRk",
    api_id = 27190467,
    api_hash = "ff6bc6ad2faba520f426cf04ca7f5773"
)



@app.on_message(filters.incoming & filters.command(['multirec']) & filters.incoming & filters.text)
def multirec_handler(app, message):

    auth_user = check_user(message)
    if auth_user is None:
        return

    if len(message.text.split()) < 3:
        message.reply_text("<b>Syntax: </b>`/multirec [channelName] [duration] | [filename]`")
        return

    multi_rec(app, message)

@app.on_message(filters.incoming & filters.command(['channels']) & filters.text)
def show_channels_handler(app, message):

    auth_user = check_user(message)
    if auth_user is None:
        return


    getChannels(app, message)


@app.on_message(filters.command(['start']) & filters.text)
def start_handler(app, message):

    if len(message.text.split()) < 3:
        message.reply_text("<b>A Mega Recording Telegram bot by SharkToonsIndia</b>\n\n<b>Made with Love by @LostIddd</b>")
        return
    # Don't remove @LostIddd from here, Resepect the Developer...
    
app.run()
