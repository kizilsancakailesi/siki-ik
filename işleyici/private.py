from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        text=f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Jason](https://t.me/Wistkral).

Add me And @MusicPlugin to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [[
            InlineKeyboardButton("➕ Add To Your Group ➕", url="https://t.me/MissRoseMusic_Bot?startgroup=true")
            ],[
            InlineKeyboardButton("💬 Group", url="https://t.me/MissRoseSupportTr"),
            InlineKeyboardButton("Channel 📣", url="https://t.me/MarieNews")
            ],[
            InlineKeyboardButton("🎛 Commands", url="https://t.me/MissRoseSupportTr"),
            InlineKeyboardButton("About👨🏻‍🎓", url="https://t.me/MissRoseSupportTr")
            ],[
            InlineKeyboardButton("🌐 Website 🌐", url="https://t.ME/missRose_bot")
            ]]
        ),
        disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Rose Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("Group", url="https://t.me/MissRoseSupportTr"),
                    InlineKeyboardButton("Channel", url="https://t.me/MissRoseSupportTr")
                ]                
            ]
        )

@Client.on_message(filters.new_chat_members & filters.outgoing & filters.group)
async def new_chat(client, message)
    await client.reply_text(
         text=f"""**❤️ Thanks for adding me to the group!**

**Promote me as administrator of the group,** otherwise I will not be able to work properly.
            """,
            reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🎛Commands", url="https://t.me/MissRoseSupportTr"),
                    InlineKeyboardButton("Channel📣", url="https://t.me/MissRoseSupportTr")
                ]                
            ]
        )
