#!/user/bin/env python
import asynctwitch

# --------------------------------------------- Start Settings ----------------------------------------------------


bot = asynctwitch.CommandBot(
    user = "MrBotChow",
    oauth = "oauth:95vzjsunmnmeewgg6liiwx0a4a8mp4",
    channel = "mrmeowchow",
    prefix = "!",
)

# --------------------------------------------- End Settings -------------------------------------------------------
#---------------------------------------------- Load extras---------------------------------------------------------
cot = False
viewers = []

# --------------------------------------------- Start Command Functions --------------------------------------------

# --------------------------------------------- End Command Functions ----------------------------------------------
# ----------------------------------------------- override Functions -----------------------------------------------

@bot.override
async def event_user_join(user):
	print(f'{user.name} has joined the channel')
	# viewers.append(user.name)

@bot.override
async def event_user_leave(user):
	print(f'{user.name} has left the channel')
	# viewers.remove(user.name)

@bot.override
async def event_subscribe(message, tags):
	print(message.author.name)
	#sub = tags.keys['user']
	#await bot.say(message.channel, f'Thank you {sub} for the (re)subscribe!!!')

bot.start()