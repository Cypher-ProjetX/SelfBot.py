import discord, asyncio
from os import system
import shutil
import subprocess
import socket, sys, discord, base64, mysql.connector, threading, requests
from tpblite import TPB
from sys import argv
import psutil
import logging
from requests import get
from time import sleep
from discord.ext import commands
from colorama import init, Fore
from bs4 import BeautifulSoup
from os import system
#import ctypes ctypes.windll.kernel32.SetConsoleTitleA("M")

init()
system("@echo off")
system("cls")
system("mode con: cols=105 lines=30")
system('title ' + ' Get good SelfBot')

def logo():
    try:
        print(Fore.LIGHTGREEN_EX)
        msg = f"""
  ____                _                 
 / ___| _   _  _ __  | |__    ___  _ __ 
| |    | | | || '_ \ | '_ \  / _ \| '__|
| |___ | |_| || |_) || | | ||  __/| |   
 \____| \__, || .__/ |_| |_| \___||_|   
        |___/ |_|                    \n
        """
        for l in msg:
            print(l, end="")

    except KeyboardInterrupt:
        sys.exit()

logo()

print(Fore.RESET)
print('  ')
print('{}╔═════ Commands ════════════════════════════════╗{}'.format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
print('{}║{}'.format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
print('{}║ [1] Clear :{} (CLEAR MESSAGES)'.format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
print('{}║ [3] Cstream :{} (Arrive...'.format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
print('{}║ [5] ClearGroupe66 :{} (leaves all the groups ur in))'.format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
print('{}║{}'.format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
print('{}╚══════════════════════════════════════════════╝{}'.format(Fore.LIGHTGREEN_EX, Fore.LIGHTWHITE_EX))
print('  ')

client = discord.Client()

token = "Token"

def murder(cmd):
    subprocess.call(cmd, shell=True)

@client.event
async def on_ready():

    width = shutil.get_terminal_size().columns

    def ui():
        print()
        print("SelfBot".center(width))
        print()
        print("[-] CypherBOT [-]".center(width))
        print()
    ui()
 
 
@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        if commands[0] == 'Clear':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass


        if commands[0] == 'Cstream':
                        msg = message.content.split("zzz", 1)
                        args = msg[1].split(" http", 1)
                        name = args[0]
                        url = "http"+args[1]
                        await message.delete()
                        await client.change_presence(status=discord.Status.dnd, activity=discord.Streaming(name=name, url=url))
                        container = discord.Embed(title="terror", color=0xFF3633)
                        container.add_field(name="status:", value="**"+name+"**")
                        container.set_footer(text="//")
                        await channel.send(embed=container)

        if commands[0] == "ClearGroupe66":
                await message.delete()
                count = 0
                for channel in client.private_channels:
                        if isinstance(channel, discord.GroupChannel):
                                if channel.id != message.channel.id:
                                        count = count + 1
                                        await channel.leave()

client.run(token, bot=False)


#	 Dev @W3bCypher