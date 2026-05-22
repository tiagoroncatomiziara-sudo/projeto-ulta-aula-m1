import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def separacao_lixo(ctx):
    await ctx.send("""Separação de lixo  Papel e papelão vão no lixo azul.
Plásticos vão no lixo vermelho.
Vidros vão no lixo verde.
Metais vão no lixo amarelo.
Restos de comida vão no lixo marrom orgânico.
""")

@bot.command()
async def economizar_agua(ctx):
    await ctx.send(""" Economizar água  Tome banhos mais curtos — 5 minutos já é suficiente!
Feche a torneira enquanto escova os dentes.
Lave a louça com a torneira fechada.
Regue plantas de manhã cedo ou à noite.
Aproveite água da chuva para regar plantas.""")
    
@bot.command()
async def alternativas_sustentaveis(ctx):
    await ctx.send("""Alternativas sustentáveis  Troque sacolinhas plásticas por sacolas reutilizáveis.
Use garrafinha reutilizável em vez de garrafa pet.
Prefira produtos com menos embalagem.
Compre em feiras locais para reduzir embalagens.
Use esponja de luffa no lugar de esponjas sintéticas.""")


bot.run("")
