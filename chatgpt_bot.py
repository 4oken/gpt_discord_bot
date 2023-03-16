import os
import openai
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

# OpenAI APIキーの設定
openai.api_key = os.getenv("OPENAI_API_KEY")

# Discord BOTトークンの設定
DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

# Intentsの設定
intents = discord.Intents.default()
intents.message_content = True

# BOTコマンドプレフィックスの設定
bot = commands.Bot(command_prefix="!", intents=intents)

# 起動時の処理
@bot.event
async def on_ready():
    print(f"{bot.user.name} がオンラインになりました。")


@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")

# ChatGPTと会話するコマンド
@bot.command(name="chat")
async def chat(ctx, *, prompt):
    print("chat command called")
    # GPT-4に問い合わせ
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    # 結果を取得して送信
    message = response.choices[0].text.strip()
    await ctx.send(message)

# BOTを起動
bot.run(DISCORD_BOT_TOKEN)
