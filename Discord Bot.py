import discord
import random
from discord.ext import commands

prefix = "~"

client = commands.Bot(command_prefix = f"{prefix}")

token = "Nzk1MjU1ODkyODczNDQ1Mzk2.X_GtxA.bujlChBJ8pC4tetFZpKKY_8lwEI"

@client.event
async def on_ready():

    print("Now, Lays Bot is successfully working")
    game = discord.Game("Mmm, Delicious Lays")
    await client.change_presence(status = discord.Status.online, activity = game)

@client.event
async def on_message(msg):
    if msg.content == "HowAmazing" or msg.content == "으메이징":
        await msg.channel.send("맞아! 을마나 대다나니! (Lays)")
    if msg.content == "감자" or msg.content == "potato":
        await msg.channel.send("는 역시? Lays!")
    if msg.content == "알리올리오" or msg.content == "foilo":
        await msg.channel.send("스파게티 먹고싶다.")
    if msg.content == "와!" or msg.content == "Wa!":
        await msg.channel.send("샌주") 
    if msg.content == "Fuck you" or msg.content == "퍽유":
        await msg.channel.send("**YOU SHUT UP**")
        
@client.command(aliases = ["지연시간", "레이턴시"])
async def latency(ctx):
    await ctx.send(f"봇의 지연시간 {round(client.latency *1000)}ms")

@client.command(aliases=["8ball", "에잇볼"])
async def eightball(ctx, *, question):
    response = [
                "아주 확실해.",
                "확실히 그래.",
                "의심할 여지 없이.",
                "그래 - 당연하지.",
                "믿어도 좋아.",
                "내가 볼땐 그런것같은데?.",
                "아마 그럴것같아.",
                "전망이 아주좋아.",
                "그래.",
                "질문이 이상해, 다시 말해봐.",
                "나중에 다시 물어봐.",
                "지금 말하지 않는것이 좋을것 같아.",
                "지금은 알수없어.",
                "집중하고, 다시 물어봐.",
                "그렇지 않을꺼야.",
                "내 대답은 아니.",
                "내 생각으론, 아니야.",
                "전망이 안좋아.",
                "매우 의심스러워.",
                "씨발"
                ]
    await ctx.send(f"질문: {question}\n대답: {random.choice(response)}")

@client.command(aliases = ["청소"])
async def clear(ctx, amount = 10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{ctx.author.name} 님의 요청으로 {amount} 개의 메세지를 청소했습니다.")

@client.command(aliases = ["주시위 게임", "주사위"])
async def dicegame(ctx, amount=1):
    await ctx.send(f"{random.randrange(1, amount)} 번의 주사위가 나왔습니다!")

@client.command(aliases = ["도움말"])
async def Help(ctx):
    embed=discord.Embed(title="도움말", description="도움말 입니다.", color=0x00aaaa)
    embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    embed.add_field(name= f"{prefix}도움말", value=f"{prefix}도움말을 알려드립니다.", inline=False)
    embed.add_field(name=f"{prefix}HowAmazing, {prefix}감자, {prefix}알리올리오", value="무언가로 대답합니다.", inline=False)
    embed.add_field(name=f"{prefix}에잇볼", value="질문에 대한 답을 해드립니다.", inline=False)
    embed.add_field(name=f"{prefix}지연시간", value="봇의 지연시간을 알려드립니다.", inline=False)
    embed.add_field(name=f"{prefix}청소", value="채팅방을 정한수만큼 청소해드립니다.", inline=False)
    embed.set_footer(text="도움말이 끝났습니다.")
    await ctx.send(embed = embed)

client.run(token)