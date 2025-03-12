import discord

TOKEN = "MTM0ODc1NjQzODc4NDQwOTYyMA.GLIkCu.UCDSOBrpXLr8EaPvW-eeX0LWRIwdum9eS7uKxA"

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot is online! Logged in as {client.user}')

client.run(TOKEN)
