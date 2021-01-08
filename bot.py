import random
import time
import discord
from discord.ext import commands
import os

prefix = "~"

client = commands.Bot(command_prefix = f"{prefix}")

@client.event
async def on_ready():

    print("Now, Lays Bot is successfully working")
    game = discord.Game("Mmm, Delicious Lays")
    await client.change_presence(status = discord.Status.online, activity = game)

@client.event
async def on_message(msg):
    if msg.channel.name == ":clipboard:명령어사용방:clipboard:" or msg.channel.name == "봇" or msg.channel.name == "📡ㅣ명령어방":
        if msg.content == "How Amazing" or msg.content == "으메이징" or msg.content == "음청나군":
            await msg.channel.send("맞아! 을마나 대다나니! (Lays)")
        if msg.content == "감자" or msg.content == "potato":
            await msg.channel.send("는 역시? Lays!")
        if msg.content == "알리올리오" or msg.content == "foilo":
            await msg.channel.send("스파게티 먹고싶다.")
        if msg.content == "와!" or msg.content == "Wa!":
            await msg.channel.send("샌주") 
        if msg.content == "표정" or msg.content == "emote":
            answer = [
                    ":clap:",
                    ":partying_face:",
                    ":potato:",
                    ":innocent:",
                    ":star_struck:",
                    ":blush:",
                    ":rage:",
                    ":worried:",
                    ":smirk:"
                    ]
            await msg.channel.send(random.choices(answer))
        if msg.content.startswith(str(prefix) + "Race") or msg.content.startswith(str(prefix) + "레이스"):
            string = msg.content[5:].split(" ")
            base = 20
            one = base
            two = base
            three = base
            four = base
            five = base
            six = base
            seven = base
            eight = base
            nine = base
            msgstring = ""

            winmsg = ""

            def Set(What, obj):
                nonlocal msgstring
                nonlocal winmsg
                rand = random.randrange(1, 4)
                Nahstring = ""
                for i in range(1, What - rand):
                    Nahstring = Nahstring + "-"
                msgstring = msgstring + Nahstring + string[obj - 1] + "\n"
                if obj == 1:
                    nonlocal one
                    one = What - rand
                elif obj == 2:
                    nonlocal two
                    two = What - rand
                elif obj == 3:
                    nonlocal three
                    three = What - rand
                elif obj == 4:
                    nonlocal four
                    four = What - rand
                elif obj == 5:
                    nonlocal five
                    five = What - rand
                elif obj == 6:
                    nonlocal six
                    six = What - rand
                elif obj == 7:
                    nonlocal seven
                    seven = What - rand
                elif obj == 8:
                    nonlocal eight
                    eight = What - rand
                elif obj == 9:
                    nonlocal nine
                    nine = What - rand
            for i in range(0, len(string)):
                msgstring = msgstring + "--------------------" + string[i] + "\n"
            mes = await msg.channel.send(msgstring)
            for w in range(1, base):
                msgstring = ""
                for i in range(0, len(string)):
                    if i == 0:
                        Set(one, 1)
                    elif i == 1:
                        Set(two, 2)
                    elif i == 2:
                        Set(three, 3)
                    elif i == 3:
                        Set(four, 4)
                    elif i == 4:
                        Set(five, 5)
                    elif i == 5:
                        Set(six, 6)
                    elif i == 6:
                        Set(seven, 7)
                    elif i == 7:
                        Set(eight, 8)
                    elif i == 8:
                        Set(nine, 9)
                time.sleep(0.5)
                await mes.edit(content = str(msgstring))
                if one <= 0 and winmsg.find(string[0]) == -1:
                    winmsg = winmsg + string[0] + " "
                if two <= 0 and winmsg.find(string[1]) == -1:
                    winmsg = winmsg + string[1] + " "
                if three <= 0 and winmsg.find(string[2]) == -1:
                    winmsg = winmsg + string[2] + " "
                if four <= 0 and winmsg.find(string[3]) == -1:
                    winmsg = winmsg + string[3] + " "
                if five <= 0 and winmsg.find(string[4]) == -1:
                    winmsg = winmsg + string[4] + " "
                if six <= 0 and winmsg.find(string[5]) == -1:
                    winmsg = winmsg + string[5] + " "
                if seven <= 0 and winmsg.find(string[6]) == -1:
                    winmsg = winmsg + string[6] + " "
                if eight <= 0 and winmsg.find(string[7]) == -1:
                    winmsg = winmsg + string[7] + " "
                if nine <= 0 and winmsg.find(string[8]) == -1:
                    winmsg = winmsg + string[8] + " "

                if len(string) == 1:
                    if one <= 0:
                        break
                elif len(string) == 2:
                    if one <= 0 and two <= 0:
                        break
                elif len(string) == 3:
                    if one <= 0 and two <= 0 and three <= 0:
                        break
                elif len(string) == 4:
                    if one <= 0 and two <= 0 and three <= 0 and four <= 0:
                        break
                elif len(string) == 5:
                    if one <= 0 and two <= 0 and three <= 0 and four <= 0 and five <= 0:
                        break
                elif len(string) == 6:
                    if one <= 0 and two <= 0 and three <= 0 and four <= 0 and five <= 0 and six <= 0:
                        break
                elif len(string) == 7:
                    if one <= 0 and two <= 0 and three <= 0 and four <= 0 and five <= 0 and six <= 0 and seven <= 0:
                        break
                elif len(string) == 8:
                    if one <= 0 and two <= 0 and three <= 0 and four <= 0 and five <= 0 and six <= 0 and seven <= 0 and eight <= 0:
                        break
                elif len(string) == 9:
                    if one <= 0 and two <= 0 and three <= 0 and four <= 0 and five <= 0 and six <= 0 and seven <= 0 and eight <= 0 and nine <= 0:
                        break
            Last = winmsg.split(" ")
            if len(Last)-1 == 1:
                await mes.edit(content = msgstring + "\n1위 " + str(Last[0]))
            elif len(Last)-1 == 2:
                await mes.edit(content = msgstring + "\n1위 " + str(Last[0]) + ", 2위 " + str(Last[1]))
            elif len(Last)-1 == 3:
                await mes.edit(content = msgstring + "\n1위 " + str(Last[0]) + ", 2위 " + str(Last[1]) + ", 3위 " + str(Last[2]))
            elif len(Last)-1 == 4:
                await mes.edit(content = msgstring + "\n1위 " + str(Last[0]) + ", 2위 " + str(Last[1]) + ", 3위 " + str(Last[2]) + ", 4위 " + str(Last[3]))
            elif len(Last)-1 == 5:
                await mes.edit(content = msgstring + "\n1위 " + str(Last[0]) + ", 2위 " + str(Last[1]) + ", 3위 " + str(Last[2]) + ", 4위 " + str(Last[3]) + ", 5위 " + str(Last[4]))
            elif len(Last)-1 == 6:
                await mes.edit(content = msgstring + "\n1위 " + str(Last[0]) + ", 2위 " + str(Last[1]) + ", 3위 " + str(Last[2]) + ", 4위 " + str(Last[3]) + ", 5위 " + str(Last[4]) + ", 6위 " + str(Last[5]))
            elif len(Last)-1 == 7:
                await mes.edit(content = msgstring + "\n1위 " + str(Last[0]) + ", 2위 " + str(Last[1]) + ", 3위 " + str(Last[2]) + ", 4위 " + str(Last[3]) + ", 5위 " + str(Last[4]) + ", 6위 " + str(Last[5]) + ", 7위 " + str(Last[6]))
            elif len(Last)-1 == 8:
                await mes.edit(content = msgstring + "\n1위 " + str(Last[0]) + ", 2위 " + str(Last[1]) + ", 3위 " + str(Last[2]) + ", 4위 " + str(Last[3]) + ", 5위 " + str(Last[4]) + ", 6위 " + str(Last[5]) + ", 7위 " + str(Last[6]) + ", 8위 " + str(Last[7]))
            elif len(Last)-1 == 9:
                await mes.edit(content = msgstring + "\n1위 " + str(Last[0]) + ", 2위 " + str(Last[1]) + ", 3위 " + str(Last[2]) + ", 4위 " + str(Last[3]) + ", 5위 " + str(Last[4]) + ", 6위 " + str(Last[5]) + ", 7위 " + str(Last[6]) + ", 8위 " + str(Last[7]) + ", 9위 " + str(Last[8]))
                        


        await client.process_commands(msg)
        
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
async def dicegame(ctx):
    await ctx.send(f"{random.randrange(1, 7)} 번의 주사위가 나왔습니다!")

@client.command(aliases = ["도움말"])
async def Help(ctx):
    embed=discord.Embed(title="도움말", description="도움말 입니다.", color=0x00aaaa)
    embed.set_author(name=ctx.author.name,icon_url=ctx.author.avatar_url)
    embed.add_field(name= f"{prefix}도움말", value=f"{prefix}도움말을 알려드립니다.", inline=False)
    embed.add_field(name=f"{prefix}에잇볼", value="질문에 대한 답을 해드립니다.", inline=False)
    embed.add_field(name=f"{prefix}지연시간", value="봇의 지연시간을 알려드립니다.", inline=False)
    embed.add_field(name=f"{prefix}청소", value="채팅방을 정한수만큼 청소해드립니다.", inline=False)
    embed.add_field(name=f"{prefix}주사위", value="1~6 사이의 숫자를 랜덤으로 줍니다.", inline=False)
    embed.add_field(name=f"{prefix}레이스", value=str(prefix) + "레이스 (이름) (이름) ... (이름) 으로 레이스를 할수 있습니다", inline=False)
    embed.set_footer(text="도움말이 끝났습니다.")
    await ctx.send(embed = embed)


client.run(os.environ["token"])