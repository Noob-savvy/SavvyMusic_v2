from config import LOG, LOG_GROUP_ID, MUSIC_BOT_NAME
from SavvyMusic.utils.database import is_on_off
from SavvyMusic import app


async def play_logs(message, streamtype):
    if await is_on_off(LOG):
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        logger_text = f"""
<b>{MUSIC_BOT_NAME} ᴘʟᴀʏ ʟᴏɢ</b>

<b>ᴄʜᴀᴛ ɪᴅ :</b> <code>{message.chat.id}</code>
<b>ᴄʜᴀᴛ ɴᴀᴍᴇ :</b> {message.chat.title}
<b>ᴄʜᴀᴛ ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.chat.username}

<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>
<b>ɴᴀᴍᴇ :</b> {message.from_user.mention}
<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}

<b>ǫᴜᴇʀʏ :</b> {message.text.split(None, 1)[1]}
<b>sᴛʀᴇᴀᴍᴛʏᴘᴇ :</b> {streamtype}"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    LOG_GROUP_ID,
                    f"{logger_text}",
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
