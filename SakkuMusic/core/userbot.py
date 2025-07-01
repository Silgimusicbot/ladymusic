from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []

class Userbot:
    def __init__(self):
        self.bots = []

        sessions = [
            ("SakkuAss1", config.STRING1),
            ("SakkuAss2", config.STRING2),
            ("SakkuAss3", config.STRING3),
            ("SakkuAss4", config.STRING4),
            ("SakkuAss5", config.STRING5),
        ]

        for name, string in sessions:
            if string:
                client = Client(
                    name=name,
                    api_id=config.API_ID,
                    api_hash=config.API_HASH,
                    session_string=str(string),
                    no_updates=True
                )
                self.bots.append(client)

    async def start(self):
        LOGGER(__name__).info("Assistants start edilir...")
        for index, bot in enumerate(self.bots, start=1):
            try:
                await bot.start()
                user = await bot.get_me()
                bot.id = user.id
                bot.name = user.mention
                bot.username = user.username
                assistants.append(index)
                assistantids.append(bot.id)

                try:
                    await bot.join_chat("rythmmusicchat")
                    
                except:
                    pass

                try:
                    await bot.send_message(config.LOGGER_ID, f"Assistant {index} Started")
                except:
                    LOGGER(__name__).error(f"Assistant {index} logger qrupuna daxil ola bilmədi. Admin etdiyinə əmin ol!")
                    continue

                LOGGER(__name__).info(f"Assistant {index} start edildi: {bot.name}")

            except Exception as e:
                LOGGER(__name__).error(f"Assistant {index} başlatma xətası: {e}")

    async def stop(self):
        LOGGER(__name__).info("Assistants dayandırılır...")
        for bot in self.bots:
            try:
                await bot.stop()
            except Exception:
                pass