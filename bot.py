# bot.py
import tweepy
import random
import os

# === LEE LOS ARCHIVOS ===
def leer_archivo(nombre):
    with open(nombre, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

# === ELEGIR MENSAJE ===
frases = leer_archivo("frases.txt")
enlaces = leer_archivo("enlaces.txt")

# 10% de probabilidad de publicar enlace
if random.random() < 0.1 and enlaces:
    tweet = random.choice(enlaces)
else:
    tweet = random.choice(frases)

# === PUBLICAR EN X ===
client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
)

try:
    client.create_tweet(text=tweet)
    print("✅ Tweet publicado:", tweet)
except Exception as e:
    print("❌ Error:", e)