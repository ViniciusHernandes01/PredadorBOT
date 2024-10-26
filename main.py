import discord
from datetime import datetime, timedelta
from discord.ext import tasks, commands

# Configurações do bot
bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())
CHANNEL_ID = 1299614585573212180  # ID do canal desejado

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

# Inicia o bot
bot.run("MTI5OTgzNzQ4OTI3NTYwMDk1NQ.G_ZUf5.q1q1NDudjTm0bO9o5_l_J03en5kAbKy-AmCuCc")  # Substitua pelo token do seu bot
