from pyrogram import Client, filters
from utils import check_user, multi_rec, getChannels

app = Client(
    "Myone123nbot",
    bot_token = "1799299844:AAGFgfIc9SmEWalsvc7nwCw4mqiPopYqhgs",
    api_id = 2929027,
    api_hash = "2beecc3ee357e6e3f2b2e783d4159f9f"
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
        message.reply_text("<b>A Mega Recording Telegram bot by Team Disney Cartoons</b>\n\n<b>Made with Love by @kids_movies_and_Episodes_founder</b>")
        return
    # Don't remove Conan76 from here, Resepct the Developer...
    
app.run()
