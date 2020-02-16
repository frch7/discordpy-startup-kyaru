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

# メッセージ受信時に動作する処理(頼んだわよ！)
@bot.command()
async def 頼んだ(ctx):
    await ctx.send('||http://bit.ly/2OYsFG5')

@bot.command()
async def たのんだ(ctx):
    await ctx.send('||http://bit.ly/2OYsFG5||')

@bot.command()
async def 頼む(ctx):
    await ctx.send('||http://bit.ly/2OYsFG5||')

@bot.command()
async def たのむ(ctx):
    await ctx.send('||https://stickershop.line-scdn.net/stickershop/v1/sticker/60968934/android/sticker.png;compress=true||')


# Botの起動とDiscordサーバーへの接続
bot.run(token)
