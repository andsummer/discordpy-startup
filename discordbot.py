from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def プリコネの年末年始は(ctx):
    await ctx.send('ヤバイわよ！')

@bot.command()
async def ヤバいわ代(ctx):
    await ctx.send('
                   ヤバイわ代
                   作詞:キャル 作曲:Cygames
                   ヤバイわ代は パチンコ代に家賃代に
                   シンフォギアでデュランダル折り 北斗無双で金保留外れ貧困層となりて
                   天龍で捲ろうと残資金をつぎ込みやけくそになって餃子の王将で散財するまで
                   ')
    
bot.run(token)
