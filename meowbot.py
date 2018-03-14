#!/user/bin/env python
import asyncio
import datetime
import json
import os
import pickle
import random
import re
import socket
import sys
import threading
import time
import traceback
from statistics import mode
from urllib.request import urlopen

import asynctwitch
import requests

import sqlapi
from modules import *
from settings import *

# --------------------------------------------- Start Settings ----------------------------------------------------
CHAN = os.environ['CHANNEL']
PASS = str(os.environ['MEOWBOT_PASS'])
ClientID = str(os.environ['CLIENT_ID'])
meowkey = str(os.environ['MEOW_AUTH'])
meowID = str(os.environ['MEOW_ID'])

bot = asynctwitch.Bot(
    user = "MrBotChow",
    oauth = os.environ['MEOWBOT_PASS'],
    channel = os.environ['CHANNEL'],
#	client_id = os.environ['CLIENT_ID'],
	prefix = "!",
)

# --------------------------------------------- End Settings -------------------------------------------------------
#---------------------------------------------- Load extras---------------------------------------------------------
cot = False
viewers = []

# --------------------------------------------- Start Command Functions --------------------------------------------

def parse_online():
	headers = {'client-id': ClientID}
	j = requests.get(f'https://api.twitch.tv/kraken/streams/{CHAN}', headers=headers)
	j_obj = json.loads(j.text)
	return j_obj

def testThread(x):
	global cot
	while True:
		try:
			status = parse_online()
		except Exception as e:
			pass
		if str(status["stream"]) == "None":
			if cot == True:
				cot = False
				print("Stream offline")
		else:
			if cot == False:
				cot = True
				print("Stream online")
		if cot == True:
			try:
				for x in viewers:
					sqlapi.deta_entry_add(x, 1)
				increasecount()
				print("catnip given")
			except Exception as x:
				print(x)
		if increasecount(ret=True) == 5:
			pass
			# bot.stop(exit=True)
		time.sleep(60)

t4 = threading.Thread(target = testThread, args=(bot,)).start()

catnipgivencount = 0
def increasecount(ret=False):
	global catnipgivencount
	if ret == True:
		return catnipgivencount
	else:
		catnipgivencount += 1

async def command_addtrusted(msg, name:str):
	if msg.author.name == "mrmeowchow":
		trusted.append(name.lower())
		await bot.say(msg.channel, name + ' is now added to the trusted list and can use the !gc commands and the betting commands in senpai\'s leave.')


async def command_removetrusted(msg, name:str):
	if sender == "mrmeowchow":
		trusted.remove(name)
		await bot.say(msg.channel, name +  ' has now been removed by senpai.')


async def removeme(msg):
	if msg.author.name in playerqueue:
		playerqueue.remove(msg.author.name)
		await bot.say(msg.channel, 'Ok ' + msg.author.name + ' you have been removed from the queue')
	else:
		await bot.say(msg.channel, msg.author.name + ' you aren\'t in the queue.')
	file = "queue.txt"
	Writetofile.writefile(file, playerqueue)


async def joinqueue(msg):
	if msg.author.name in playerqueue:
		await bot.say(msg.channel, msg.author.name +' Already in queue')
	else:
		playerqueue.append(msg.author.name.lower())
		await bot.say(msg.channel, msg.author.name + ' Added to the queue. New queue length is: ' + str(len(playerqueue)))
		file = "queue.txt"
		Writetofile.writefile(file, playerqueue)


async def nextup(msg):
	if msg.author.name in trusted:
		if len(playerqueue) > 0:
			await bot.say(msg.channel, playerqueue[0] + ' Is up next! New queue length is: ' + str(len(playerqueue)-1))
			playerqueue.remove(playerqueue[0])
			file = "queue.txt"
			Writetofile.writefile(file, playerqueue)
		else:
			await bot.say(msg.channel, 'The queue is currently empty people can use !join to join if you have the game being played.')


async def qlength(msg):
	await bot.say(msg.channel, 'Current queue length is: ' + str(len(playerqueue)))


async def qinfo(msg):
	await bot.say(msg.channel, 'So the channel has a queue system when playing games with cap, to enter the queue use the command !join, be sure to keep an eye on chat to see when your name is called.')


async def myplace(msg):
	if sender in playerqueue:
		senderplace = playerqueue.index(msg.author.name.lower())
		remainder = len(playerqueue) - senderplace
		await bot.say(msg.channel, 'Your place in the queue ' + msg.author.name + ' is: ' + str(senderplace + 1) +  ' there are ' + str(remainder - 1) + ' in the queue after you.')
	else:
		await bot.say(msg.channel, 'You are not in the queue ' + msg.author.name)


async def myrank(msg):
	total = sqlapi.gettotal()
	try:
		percentrank = cookieranks.getrankpercent(total, msg.author.name)
		await bot.say(msg.channel, msg.author.name + percentrank)
	except ValueError:
		await bot.say(msg.channel, 'You dont have any catnip try again in 10 mins')


async def userrank(msg, name:str):
	total  = sqlapi.gettotal()
	if msg.author.name in trusted:
		try:
			percentrank = cookieranks.getrankpercent(total, name)
			await bot.say(msg.channel, name + percentrank)
		except Exception as x:
			print(x)


async def watchtime(msg):
	watchtime = watchtimecalc(msg.author.name.lower())
	await bot.say(msg.channel, watchtime)

def watchtimecalc(name):
	try:
		catnipcount = int(sqlapi.Get_User_Amount(name))
	except:
		pass
	numinhours = catnipcount / 60
	numindays = numinhours / 24
	
	if catnipcount >= 1:
		if numindays >= 1:
			message = '{} has watched for {} days'.format(name, str(round(numindays, 2)))
			return message
		else:
			message = '{} has watched for {} hours'.format(name, str(round(numinhours, 2)))
			return message
	else:
		message = '{} has watched for less than 1 min :('.format(name)
		return message

async def catnip(msg):
	catnipcount = sqlapi.Get_User_Amount(msg.author.name)
	if catnipcount > 0:
		await bot.say(msg.channel, '{} you have, {} catnip'.format(msg.author.name, str(int(catnipcount))))
	else:
		await bot.say(msg.channel, '{} senpai has not given you catnip yet :('.format(msg.author.name))

async def test(msg):
	print(bot.viewers)

# def command_clip():
# 	try:
# 		id = line[4]
# 		clip = sqlinteraction.get_clip_from_id(str(line[4]))
# 		name = sqlinteraction.get_name_from_id(id)
# 		send_message(CHAN, 'Clip: {} - {}: {}'.format(line[4], str(name[0]).strip('(),'), clip))
# 	except IndexError:
# 		rand_clip = random.choice(sqlinteraction.get_all_clips())
# 		rand_id = sqlinteraction.get_id_from_clip(rand_clip[0])
# 		rand_name = sqlinteraction.get_name_from_id(rand_id[0][0])
# 		send_message(CHAN, "Clip: {} - {}: {}".format(str(rand_id[0][0]), str(rand_name[0]).strip('(),'), rand_clip[0]))

# def command_clipCount():
# 	clipcount = len(sqlinteraction.get_all_clips())
# 	send_message(CHAN, 'The number of clips saved is: {}'.format(clipcount))

# --------------------------------------------- End Command Functions ----------------------------------------------
# ----------------------------------------------- override Functions -----------------------------------------------

async def parse_message(msg,passto):
	if len(msg.content) >= 1:
		msg = msg.content.split(' ')
		options = {
					'!join' : joinqueue,
					'!qlength' : qlength,
					'!nextup': nextup,
					'!queueinfo' : qinfo,
					'!myplace' : myplace,
					'!leaveq' : removeme,
					'!catnip' : catnip,
					'!addtrusted' : command_addtrusted,
					'!rmtrusted' : command_removetrusted,
					'!myrank' : myrank,
					'!watchtime' : watchtime,
					'!userrank' : userrank,
					'!test' : test,
					# '!clip' : command_clip,
					# '!clipcount' : command_clipCount,
					}
		if msg[0] in options:
				await options[msg[0]](passto)

@bot.override
async def event_message(msg):
	print(f"{msg.author.name} | {msg}")
	global catnipgivencount
	catnipgivencount = 0
	await parse_message(msg,msg)

@bot.override
async def event_user_join(user):
	print(f'{user.name} has joined the channel')
	try:
		viewers.append(user.name)
	except Exception as x:
		print(x)
		pass

@bot.override
async def event_user_leave(user):
	print(f'{user.name} has left the channel')
	try:
		viewers.remove(user.name)
	except Exception as x:
		print(f"failed to remove {user.name} not in list")
		pass

@bot.override
async def event_subscribe(message, tags):
	print(tags)
	if message.author.name.lower() == "twitch":
		await bot.say(message.channel, f'Thank you for the donation to the stream and charity!!!')
	elif tags['msg-id'] == 'raid':
		numberofraiders = tags['msg-param-viewerCount']
		await bot.say(message.channel, f'Thank you {message.author.name} for the raid of {numberofraiders}')
		pass
	elif int(tags['msg-param-months']) > 1:
		numberofmonths = tags['msg-param-months']
		await bot.say(message.channel, f'Thank you {message.author.name} for the resubscribe of {numberofmonths} months!!!')
		pass
	else:
		await bot.say(message.channel, f'Thank you {message.author.name} for the subscribe!!!')

# @bot.override
# async def raw_event(data):
# 	print(data)

# bot.debug()
bot.start(tasked=True)
