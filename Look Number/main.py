import discord
from discord.ext import commands
import requests
import os


NUMVERIFY_API_KEY = "f0mD5adCFb1Y98yEo1T6w0Q21DSZAL9q"
IPINFO_API_KEY = "f0mD5adCFb1Y98yEo1T6w0Q21DSZAL9q"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')

@bot.command()
async def lookup(ctx, numero: str):
    """Recherche les informations d'un numéro de téléphone"""
    url = f'http://apilayer.net/api/validate?access_key={NUMVERIFY_API_KEY}&number={numero}'
    response = requests.get(url).json()
    
    if response.get("valid"):
        pays = response.get("country_name", "Inconnu")
        operateur = response.get("carrier", "Inconnu")
        localisation = response.get("location", "Inconnue")
        ligne_type = response.get("line_type", "Inconnu")
        
        ip_lookup_url = f'https://ipinfo.io/{response.get("country_code", "")}?token={IPINFO_API_KEY}'
        ip_response = requests.get(ip_lookup_url).json()
        ip = ip_response.get("ip", "Inconnue")
        coordonnees = ip_response.get("loc", "Inconnues")
        
        embed = discord.Embed(title="🔍 Informations du numéro", color=discord.Color.blue())
        embed.add_field(name="📍 Pays", value=pays, inline=True)
        embed.add_field(name="📡 Opérateur", value=operateur, inline=True)
        embed.add_field(name="📍 Localisation", value=localisation, inline=True)
        embed.add_field(name="📞 Type de ligne", value=ligne_type, inline=True)
        embed.add_field(name="🌍 IP Approx", value=ip, inline=True)
        embed.add_field(name="📌 Coordonnées", value=coordonnees, inline=True)
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("⚠️ Numéro invalide ou introuvable.")

bot.run("Your_bot_token")
