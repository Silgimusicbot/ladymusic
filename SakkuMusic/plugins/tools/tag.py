import asyncio
import re
from pyrogram.enums import ChatMemberStatus, ParseMode
from pyrogram.types import Message
from pyrogram import filters
from SakkuMusic import app  


tag_durdur = {}

def escape_markdown(text: str) -> str:
    return re.sub(r"([\[\]()_~`>#+\-=|{}.!])", r"\\\1", text)

@app.on_message(filters.command("stoptag") & filters.group)
async def stop_tag(_, message: Message):
    chat_id = message.chat.id
    tag_durdur[chat_id] = True
    await message.reply("⛔ Etiketleme işlemi durduruldu.")

@app.on_message(filters.command("tag") & filters.group)
async def tag_command(client, message: Message):
    await tag_users(client, message, only_admins=False, tektek=False)

@app.on_message(filters.command("tektag") & filters.group)
async def tektag_command(client, message: Message):
    await tag_users(client, message, only_admins=False, tektek=True)

@app.on_message(filters.command("admintag") & filters.group)
async def admintag_command(client, message: Message):
    await tag_users(client, message, only_admins=True, tektek=True)

async def tag_users(client, message: Message, only_admins=False, tektek=False):
    chat_id = message.chat.id
    custom_text = message.text.split(None, 1)[1] if len(message.text.split()) > 1 else "Buraya bax 🫵"

    if only_admins:
        members = [member async for member in app.get_chat_members(chat_id) if member.status in (ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER)]
    else:
        members = [member async for member in app.get_chat_members(chat_id)]

    tag_durdur[chat_id] = False
    count = 0
    temp_tags = []

    for member in members:
        if tag_durdur.get(chat_id):
            break
        if not member.user or member.user.is_bot:
            continue

        name = escape_markdown(member.user.first_name)
        mention = f"[{name}](tg://user?id={member.user.id})"

        if tektek:
            text = f"{mention} {custom_text}"
            await message.reply(text, parse_mode=ParseMode.MARKDOWN)
            await asyncio.sleep(1.5)
        else:
            temp_tags.append(mention)
            if len(temp_tags) == 5:
                text = " ".join(temp_tags) + f" {custom_text}"
                await message.reply(text, parse_mode=ParseMode.MARKDOWN)
                temp_tags.clear()
                await asyncio.sleep(2)

        count += 1

    if not tag_durdur.get(chat_id):
        await message.reply(f"✅ Toplam {count} kişi etiketlendi.")

    tag_durdur[chat_id] = False