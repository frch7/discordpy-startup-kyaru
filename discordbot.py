# Bot Commands Frameworkを使えるようにする
# OSに依存した機能を使えるようにする
# スタックトレース (エラー情報) を使えるようにする
from discord.ext import commands
import os
import traceback

# Bot Commands Frameworkで頭文字「.」のコマンドを使えるようにする
# 自分のBotのアクセストークンを設定する
bot = commands.Bot(command_prefix='.')
token = os.environ['DISCORD_BOT_TOKEN']

# エラー発生時に動作する処理
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

# メッセージ受信時に動作する処理(やばいですね☆)
@bot.command()
async def yabai(ctx):
    await ctx.send('http://bit.ly/2vTUUz8')

@bot.command()
async def やばい(ctx):
    await ctx.send('http://bit.ly/2vTUUz8')


# メッセージ受信時に動作する処理(オイッス～！)
@bot.command()
async def oisu(ctx):
    await ctx.send('http://bit.ly/38SinPJ')

@bot.command()
async def おいっすー(ctx):
    await ctx.send('http://bit.ly/38SinPJ')


# メッセージ受信時に動作する処理(しょんぼり...)
@bot.command()
async def syonbori(ctx):
    await ctx.send('http://bit.ly/2PjrpgR')

@bot.command()
async def しょんぼり(ctx):
    await ctx.send('http://bit.ly/2PjrpgR')


# メッセージ受信時に動作する処理(ありがとうございます)
@bot.command()
async def arigatou(ctx):
    await ctx.send('http://bit.ly/2vcmEyT')

@bot.command()
async def ありがとう(ctx):
    await ctx.send('http://bit.ly/2vcmEyT')


# メッセージ受信時に動作する処理(さすがです、主さま)
@bot.command()
async def sasuga(ctx):
    await ctx.send('http://bit.ly/2w0E1CY')

@bot.command()
async def さすが(ctx):
    await ctx.send('http://bit.ly/2w0E1CY')


# メッセージ受信時に動作する処理(おやすみなさいませ)
@bot.command()
async def oyasumi(ctx):
    await ctx.send('http://bit.ly/32h9dd6')

@bot.command()
async def おやすみ(ctx):
    await ctx.send('http://bit.ly/32h9dd6')


# メッセージ受信時に動作する処理(畏まりました)
@bot.command()
async def kasiko(ctx):
    await ctx.send('http://bit.ly/37UpK7Q')

@bot.command()
async def かしこ(ctx):
    await ctx.send('http://bit.ly/37UpK7Q')


# メッセージ受信時に動作する処理(頼んだわよ！)
@bot.command()
async def tanomu(ctx):
    await ctx.send('http://bit.ly/2OYsFG5')

@bot.command()
async def たのむ(ctx):
    await ctx.send('http://bit.ly/2OYsFG5')


# メッセージ受信時に動作する処理(嫌いじゃないかも)
@bot.command()
async def suki(ctx):
    await ctx.send('http://bit.ly/2uXk67L')

@bot.command()
async def すき(ctx):
    await ctx.send('http://bit.ly/2uXk67L')


# メッセージ受信時に動作する処理(いい感じじゃない！)
@bot.command()
async def iikanji(ctx):
    await ctx.send('http://bit.ly/2TaKl2i')

@bot.command()
async def iikanzi(ctx):
    await ctx.send('http://bit.ly/2TaKl2i')

@bot.command()
async def いいかんじ(ctx):
    await ctx.send('http://bit.ly/2TaKl2i')


# メッセージ受信時に動作する処理(バカじゃないの？)
@bot.command()
async def baka(ctx):
    await ctx.send('http://bit.ly/2T8WTre')

@bot.command()
async def ばか(ctx):
    await ctx.send('http://bit.ly/2T8WTre')


# メッセージ受信時に動作する処理(ばいばーい)
@bot.command()
async def baibai(ctx):
    await ctx.send('http://bit.ly/2HTAvN3')

@bot.command()
async def bye(ctx):
    await ctx.send('http://bit.ly/2HTAvN3')

@bot.command()
async def ばいばい(ctx):
    await ctx.send('http://bit.ly/2HTAvN3')


# メッセージ受信時に動作する処理(あたし、やればできる子なのよ)
@bot.command()
async def dekiruko(ctx):
    await ctx.send('http://bit.ly/37OLimw')

@bot.command()
async def できるこ(ctx):
    await ctx.send('http://bit.ly/37OLimw')


# Botの起動とDiscordサーバーへの接続
bot.run(token)
