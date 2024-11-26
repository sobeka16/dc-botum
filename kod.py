import discord
from discord.ext import commands
import random

# Botu başlatma
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# cevapları
truths = [
    "Hangi ünlüyü gizli bir şekilde beğeniyorsun?",
    "En utandığın anını anlat.",
    "Hiç kimseye söylemediğin bir sırrını paylaş.",
    "Kendini en çok gururlandıran anını anlat.",
    "En korktuğun şey nedir?",
    "Bir arkadaşının önünde başına gelen en utanç verici şey ne?",
    "En son ne zaman yalan söyledin?",
    "En son ne zaman ağladın ve ne için?",
    "Annenin senin hakkında bilmediğine sevindiğin şey nedir?",
    "Hiç birini aldattın mı?",
    "Aşık olduğun kişiyi ilk kez ne zaman gördün?",
    "Hayatında en çok kimden etkilendin?"
]

dares = [
    "Bir şarkı söylemek.",
    "Kameranı aç ve 10 saniye boyunca dans et.",
    "Bir arkadaşına komik bir sesle mesaj at.",
    "En sevdiğin filmi anlat, ama hiç ses kullanma.",
    "İnstagram’da en son paylaştığın fotoğrafı 1 dakika boyunca açıklamak."
    "Etrafındaki bir nesneyi bir dakika boyunca öv.",
    "2 dakika boyunca tek ayak üstünde dur.",
    "En komik suratını yaparak bir selfie çek ve paylaş.",
    "Bir arkadaşını aniden arayıp ona aşkını ilan et.",
    "En sevdiğin şarkıyı mırıldanarak söyle.",
    "Başka bir oyuncunun seçtiği bir nesneyi taklit et.",
    "Bir masal anlatmaya çalış ama sürekli saçma şeyler ekle."
    "1 dakika boyunca ayna karşısında konuş.",
    
]


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yapıldı!')

# Doğruluk 
@bot.command(name="doğruluk")
async def truth(ctx):
    truth_response = random.choice(truths)
    await ctx.send(f"Doğruluğunuz: {truth_response}")

# Cesaret
@bot.command(name="cesaret")
async def dare(ctx):
    dare_response = random.choice(dares)
    await ctx.send(f"Cesaretiniz: {dare_response}")

#yardım 
@bot.command(name="yardım")
async def help(ctx):
    help_message = """
    !doğruluk : Doğruluk sorusu alırsınız.
    !cesaret : Cesaret görevi alırsınız.
    """
    await ctx.send(help_message)

# çalıştırma
bot.run("token") 
