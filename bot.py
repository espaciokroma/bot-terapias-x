# bot.py
import tweepy
import random
import os

def leer_archivo(nombre):
    try:
        with open(nombre, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        return lines
    except FileNotFoundError:
        print(f"❌ Archivo no encontrado: {nombre}")
        return []

# Leer frases y enlaces
frases = leer_archivo("frases.txt")
enlaces = leer_archivo("enlaces.txt")

if not frases:
    print("⚠️ No hay frases. No se puede publicar.")
    exit()

# Decidir si publicar frase o enlace (10% de enlaces)
if enlaces and random.random() < 0.1:
    tweet = random.choice(enlaces)
else:
    tweet = random.choice(frases)

# Conectar con X
try:
    client = tweepy.Client(
        consumer_key=os.getenv("TWITTER_API_KEY"),
        consumer_secret=os.getenv("TWITTER_API_SECRET"),
        access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
        access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
    )
    client.create_tweet(text=tweet)
    print("✅ Tweet publicado:", tweet[:50] + "..." if len(tweet) > 50 else tweet)
except Exception as e:
    print("❌ Error al publicar:", str(e))
