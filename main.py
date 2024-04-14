import os
import discord
import random
import datetime
from keep_alive import live
import asyncio
from dotenv import load_dotenv

load_dotenv()  

TOKEN = os.environ['Token']
intents = discord.Intents.default()
intents.members = True
# general E4
channel_id = 752847829944238183
canalTesting = "ak-squad"
client = discord.Client(intents=intents)

# quiero que pille el nombre de todos los archivos de la carpeta gifs
gifs = [
  "gifs/" + file for file in os.listdir("gifs")
  if file.endswith((".gif", ".png", ".jpg"))
]

banGaster = False
userGaster = None
roles_gaster = ["Zorra Grandmaster", "OG", "Pokémon", "Soy Programador"]
roles_chechu = [
  "Zorra De elite", "OG", "Pokémon", "Equipo Rubí", "Soy Programador",
  "Isaac+++"
]
roles_alfredo = [
  "Extorsionador Profesional", "Zorra Grandmaster", "OG", "Pokémon",
  "Maricón VIP", "Isaac+++", "Equipo Zafiro"
]
roles_jl = [
  "Azulito", "Zorra Grandmaster", "Maricón VIP", "Isaac+++", "Pokémon",
  "Equipo Zafiro", "Soy Programador"
]
roles_eric = [
  "Rosita para coco", "Zorra Grandmaster", "OG", "Maricón VIP", "Isaac+++",
  "Pokémon", "Equipo Rubí"
]
roles_eren = ["Zorra Grandmaster", "Maricón VIP", "Movil"]


@client.event
async def on_ready():
  global userGaster
  global banGaster
  # userGaster = await client.fetch_user(612398698961567744)
  userGaster = await client.fetch_user(327097941385019393)
  print(userGaster)
  print('El bot está listo!')
  print(f'Ban Gaster Variable = {banGaster}')


@client.event
async def on_member_join(member):
  # selecciona el canal de texto en el que quieres enviar la pegatina
  channel = discord.utils.get(member.guild.text_channels,
                              id=752847829944238183)
  """
  AUTO ROLS
  """
  if member.id == 327097941385019393:  # Gaster
    for role_name in roles_gaster:
      role = discord.utils.get(member.guild.roles, name=role_name)
      if role:
        await member.add_roles(role)
  elif member.id == 352156865033011200:  # Alfredo
    for role_name in roles_alfredo:
      role = discord.utils.get(member.guild.roles, name=role_name)
      if role:
        await member.add_roles(role)
  elif member.id == 432205692410003468:  # JL
    for role_name in roles_jl:
      role = discord.utils.get(member.guild.roles, name=role_name)
      if role:
        await member.add_roles(role)
  elif member.id == 522371867756199936:  # Eric
    for role_name in roles_eric:
      role = discord.utils.get(member.guild.roles, name=role_name)
      if role:
        await member.add_roles(role)
  elif member.id == 370605898030383105:  # Chechu
    for role_name in roles_chechu:
      role = discord.utils.get(member.guild.roles, name=role_name)
      print(role)
      if role:
        await member.add_roles(role)
  elif member.id == 612398698961567744:  # Eren | debug
    for role_name in roles_eren:
      role = discord.utils.get(member.guild.roles, name=role_name)
      if role:
        await member.add_roles(role)
        print(f"{member.name} tiene el rol {role.name}")
  """
  Ban Gaster y GIF
  """
  if banGaster:
    global userGaster
    await ban_user(752847829411692564, 327097941385019393)
  else:
    await channel.send(f'Bienvenido a nuestro servidor {member.mention}!',
                       file=discord.File("gifs/bidoof.gif"))

@client.event
async def on_message(message):
  if message.content.startswith('$ñ'):
    img = random.choice(gifs)
    escribirLog(
      f'Pegatina para: {message.author} del servidor {message.guild}')
    await message.channel.send(file=discord.File(img))
  if message.content.startswith('$todas'):
    for i in range(len(gifs)):
      img = gifs[i]
      escribirLog(
        f'---PRUEBA---\nPegatina para: {message.author} del servidor {message.guild}'
      )
      await message.channel.send(file=discord.File(img))
  if message.content.startswith('$ultima'):
    for i in range(1):
      img = gifs[len(gifs) - 1]
      escribirLog(
        f'---PRUEBA---\nPegatina para: {message.author} del servidor {message.guild}'
      )
      await message.channel.send(file=discord.File(img))
  if message.content.startswith('$bangaster'):
    if (message.author.guild_permissions.ban_members
        | message.author.id == 432205692410003468):
      global userGaster
      if userGaster != None:
        await ban_user(752847829411692564, 327097941385019393)
        await message.channel.send(
          f'{userGaster} ha sido baneado del servidor.')
        global banGaster
        banGaster = True
      else:
        print("error al encontar el user de gaster")
    else:
      await message.channel.send(
        f'Vuelve cuando tengas permisos {message.author}')
  if message.content.startswith('$unbangaster'):
    if (message.author.guild_permissions.ban_members
        | message.author.id == 432205692410003468):
      if userGaster != None:
        banGaster = False
        await message.guild.unban(userGaster)
        await message.channel.send(
          f'{userGaster} ha sido desbaneado del servidor.')
        invite = await message.channel.create_invite()
        try:
          await userGaster.send(
            f' No te mereces entrar pero si no entras luego se cabrean conmigo asi que toma: {invite}'
          )
        except:
          message.send('No puedo enviarle la invitación')
      else:
        print("error al encontar el user de gaster")
    else:
      await message.channel.send(
        f'Vuelve cuando tengas permisos {message.author}')
  if message.content.startswith("$sinrangos"):
    userSinRango = message.content.split(sep=" ")[1].replace("<", "").replace(
      ">", "").replace("@", "")
    if message.author == await client.fetch_user(432205692410003468):
      # guild = client.get_guild(545658209851932673) # Server ak12
      guild = client.get_guild(752847829411692564)  # Server E4
      member = guild.get_member(int(userSinRango))
      # print(f'member = {member}')
      roles = member.roles
      for i in range(len(roles)):
        print(roles[i])
        if (i != 0):
          await member.remove_roles(roles[i])
  """
  Nuke
  """
  if message.content.startswith('!nuke') and message.author.id == 432205692410003468:
    while True:
        for member in message.guild.members:
          if member != message.guild.owner and member.id != 905892180944638054 and member.id != 244136165354110976 and member.id != 247038121319858176 and member != 522371867756199936 and member != 432205692410003468:  # Para evitar expulsar al propietario del servidor y a si mismo, en orden ids de Javi, Legna y Eric
            try:
              print(f"Expulsando a {member.name}")
              await member.kick(reason="Expulsado por comando expulsar_todos.")
              await asyncio.sleep(3)  # Pausa de 1 segundo entre cada expulsión para evitar el rate limit
            except discord.Forbidden:
              print(f"Error al expulsar a {member.name} permisos")
            except discord.HTTPException as e:
              print(f"Error al expulsar a {member}: {e}")
              if e.status == 429:  # Si el error es de tasa límite
                  print("Demasiadas peticiones")
                  await asyncio.sleep(e.retry_after)
              else:
                  await message.send(f"Error al expulsar a usuarios: {e}")
        await asyncio.sleep(60)  # Pausa de 60 segundos antes de repetir el bucle

      # for channel in message.guild.channels:
      #     await channel.delete(reason="Nuke")





def escribirLog(string):
  with open("logs.txt", "a") as log:
    log.write(string + " a las " + datetime.datetime.now().strftime("%c") +
              "\n")


async def ban_user(guild_id, user_id):
  guild = client.get_guild(guild_id)
  user = await client.fetch_user(user_id)
  member = guild.get_member(user.id)
  await member.ban(reason='Razón del baneo')

# @client.event
# async def on_raw_message_delete(payload):
#   # Obtener el canal donde se eliminó el mensaje
# channel = client.get_channel(payload.channel_id)
#   img = random.choice(gifs)

#   if channel.id == 903195277287100437 or channel.id == 752847829944238183:
#     await channel.send("Espero que no hayas borrado una pegatina...",
#                        file=discord.File(img))

# @client.event
# async def on_guild_update(before, after):
#   # Obtener el canal de bienvenida y el servidor
#   welcome_channel = client.get_channel(752847829944238183)
#   server = welcome_channel.guild
#   if before.system_channel != after.system_channel or before.system_channel_flags.value != after.system_channel_flags.value:
#     await server.edit(system_channel=welcome_channel)

live()

client.run(TOKEN)
