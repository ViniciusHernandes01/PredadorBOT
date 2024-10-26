import discord
import asyncio
from datetime import datetime, timedelta
from discord.ext import tasks, commands
from config import TOKEN  # Importa o token do arquivo de configuração

bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

CHANNEL_ID = 1299844296542785636  # Verifique se o ID está correto

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")
    update_channel_name.start()  # Inicia a tarefa de atualização

@tasks.loop(minutes=1)
async def update_channel_name():
    print("Executando a função de atualização do nome do canal...")

    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        current_time_plus_3 = datetime.utcnow() + timedelta(hours=3)
        formatted_time = current_time_plus_3.strftime("%H:%M:%S")
        new_name = f"{formatted_time} UTC"

        try:
            await channel.edit(name=new_name)
            print(f"Canal atualizado para: {new_name}")
        except Exception as e:
            print(f"Erro ao tentar atualizar o nome do canal: {e}")
    else:
        print("Canal não encontrado. Verifique se o CHANNEL_ID está correto e o bot tem acesso ao canal.")

bot.run(TOKEN)  # Usa o token do arquivo de configuração
