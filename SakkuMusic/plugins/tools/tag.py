import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus

from SakkuMusic import app

tagging_active = {}

def is_admin(status):
    return status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]

@app.on_message(filters.command("tag", prefixes=["/"]) & filters.group)
async def tag_all(client: Client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not is_admin(user.status):
        return await message.reply("❌ Bu komutu sadece yöneticiler kullanabilir.")

    custom_text = " ".join(message.command[1:])
    sent = await message.reply("👥 Etiketleme başlatılıyor...")

    tagging_active[message.chat.id] = True
    count = 0
    tagged = 0
    text = ""

    async for member in client.get_chat_members(message.chat.id):
        if not tagging_active.get(message.chat.id):
            return await sent.edit(f"⛔ Etiketleme durduruldu. Toplam: {tagged} kişi etiketlendi.")

        if member.user.is_bot:
            continue

        text += f"[{member.user.first_name}](tg://user?id={member.user.id}) "
        count += 1
        tagged += 1

        if count % 5 == 0:
            await message.reply(f"{custom_text}\n\n{text}" if custom_text else text)
            await asyncio.sleep(2)
            text = ""

    if text:
        await message.reply(f"{custom_text}\n\n{text}" if custom_text else text)

    tagging_active[message.chat.id] = False
    await sent.edit(f"✅ Etiketleme tamamlandı. Toplam: {tagged} kişi etiketlendi.")



@app.on_message(filters.command("admintag", prefixes=["/"]) & filters.group)
async def tag_admins(client: Client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not is_admin(user.status):
        return await message.reply("❌ Bu komutu sadece yöneticiler kullanabilir.")

    custom_text = " ".join(message.command[1:])
    sent = await message.reply("👥 Yönetici etiketleme başlatılıyor...")

    text = ""
    count = 0
    tagged = 0

    async for member in client.get_chat_members(message.chat.id):
        if member.user.is_bot:
            continue
        try:
            m_status = (await client.get_chat_member(message.chat.id, member.user.id)).status
            if is_admin(m_status):
                text += f"[{member.user.first_name}](tg://user?id={member.user.id}) "
                count += 1
                tagged += 1
        except:
            continue

        if count % 5 == 0 and text:
            await message.reply(f"{custom_text}\n\n{text}" if custom_text else text)
            await asyncio.sleep(2)
            text = ""

    if text:
        await message.reply(f"{custom_text}\n\n{text}" if custom_text else text)

    await sent.edit(f"✅ Yönetici etiketleme tamamlandı. Toplam: {tagged} yönetici etiketlendi.")


@app.on_message(filters.command("tektag", prefixes=["/"]) & filters.group)
async def tag_individual(client: Client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not is_admin(user.status):
        return await message.reply("❌ Bu komutu sadece yöneticiler kullanabilir.")

    custom_text = " ".join(message.command[1:])
    sent = await message.reply("👤 Tek tek etiketleme başlatılıyor...")

    tagging_active[message.chat.id] = True
    tagged = 0

    async for member in client.get_chat_members(message.chat.id):
        if not tagging_active.get(message.chat.id):
            return await sent.edit(f"⛔ Etiketleme durduruldu. Toplam: {tagged} kişi etiketlendi.")
        if member.user.is_bot:
            continue

        try:
            text = f"{custom_text}\n[{member.user.first_name}](tg://user?id={member.user.id})" if custom_text else f"[{member.user.first_name}](tg://user?id={member.user.id})"
            await message.reply(text)
            await asyncio.sleep(1.5)
            tagged += 1
        except Exception as e:
            print(f"Hata: {e}")

    tagging_active[message.chat.id] = False
    await sent.edit(f"✅ Tek tek etiketleme tamamlandı. Toplam: {tagged} kişi etiketlendi.")

@app.on_message(filters.command("stoptag", prefixes=["/"]) & filters.group)
async def stop_tag(client: Client, message: Message):
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if not is_admin(user.status):
        return await message.reply("❌ Bu komutu sadece yöneticiler kullanabilir.")

    tagging_active[message.chat.id] = False
    await message.reply("🛑 Etiketleme işlemi durduruldu.")