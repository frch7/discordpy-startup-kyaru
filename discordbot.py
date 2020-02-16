# インストールした discord.py を読み込む
# OSに依存した機能を使えるようにする
# スタックトレース(エラー情報)を使えるようにする
from discord.ext import commands
import os
import traceback

# Botが反応する頭文字を「.」に設定する
# 自分のBotのアクセストークンを設定する
bot = commands.Bot(command_prefix='.')
token = os.environ['DISCORD_BOT_TOKEN']

# エラー発生時に動作する処理
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

# メッセージ受信時に動作する処理
# （注）コメントアウトで使用できないように設定中
'''
@bot.command()
async def ping(ctx):
    await ctx.send('pongpong')
'''

# メッセージ受信時に動作する処理
@bot.command()
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「.neko」と発言したら「にゃーん」が返る処理
    if message.content == '.neko':
        await message.channel.send('にゃーん')

# Botの起動とDiscordサーバーへの接続
bot.run(token)
