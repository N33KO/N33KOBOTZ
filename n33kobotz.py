import discord
import os  # ✅ Import os to get environment variables

# ✅ Fetch the token securely from Railway
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is online! Logged in as {client.user}')

client.run(TOKEN)
