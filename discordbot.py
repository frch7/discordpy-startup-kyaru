# インストールした discord.py を読み込む
# Bot Commands Frameworkを使えるようにする
# OSに依存した機能を使えるようにする
# スタックトレース (エラー情報) を使えるようにする
import discord
from discord.ext import commands
import os
import traceback

# 接続に必要なオブジェクトを生成する
# Bot Commands Frameworkで頭文字「.」のコマンドを使えるようにする
# 自分のBotのアクセストークンを設定する
client = discord.Client()
bot = commands.Bot(command_prefix='.')
token = os.environ['DISCORD_BOT_TOKEN']


# エラー発生時に動作する処理 (頭文字「.」のコマンド)
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

# メッセージ受信時に動作する処理 (頭文字「.」のコマンド)
@bot.command()
async def ヤバい(ctx):
    await ctx.send('ヤバいわよ！')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')


# Botの起動とDiscordサーバーへの接続
bot.run(token)
