import discord
import json
import requests
import os



intents = discord.Intents.default()
intents.message_content = True

def get_weather(city):
    ans = city
    url = ("http://api.weatherapi.com/v1/forecast.json?key=aec09acaba4544b4a5413116220911&q="+ans+"&days=1&aqi=yes&alerts=no")
    response = requests.get(url)
    data = response.json()
    return data
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$weather'):
        city = message.content.split('$weather ', 1)[1]
        weather_data = get_weather(city)
        em = discord.Embed(title=city, description=weather_data['current']['condition']['text'], color=0x00ff00)
        em.add_field(name='Temperature', value=str(weather_data['current']['temp_c']) + '°C')
        em.add_field(name= 'Wind Speed', value=str(weather_data['current']['wind_kph']) + 'kph')
        em.set_thumbnail(url="https:" +weather_data['current']['condition']['icon'])
        await message.channel.send(embed=em)

client.run('MTAzOTQxNjAzNzg5NDAwODg4Mw.GHCQyH.G1GdjQ94RHZ5M81p-Io-LhtjHQx8pglx5RCkYo')

