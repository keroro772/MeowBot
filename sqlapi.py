#!/usr/bin/env python
import os
import sys
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_project.settings")
import django
django.setup()

from Catnip.models import Catnip


""" ---------------User Functions------------------- """
def create_user(name):
	user = Catnip(name=name, amount=0, currentAmount=0)
	user.save()
	
def Get_User_Amount(user):
	try:
		user_data = Catnip.objects.get(name=user)
		return user_data.amount
	except Catnip.DoesNotExist:
		return None

def deta_entry_add(Name, addCatnip):
	try:
		user = Catnip.objects.get(name=Name)
		newvalue = int(user.amount) + int(addCatnip)
		user.amount = newvalue
		user.save()
		newvalue = int(user.currentAmount) + int(addCatnip)
		user.currentAmount = newvalue
		user.save()
	except Catnip.DoesNotExist:
		create_user(Name)

def deta_entry_del(Name, delCatnip):
	try:
		user = Catnip.objects.get(name=Name)
		newvalue = int(user.currentAmount) - int(delCatnip)
		user.currentAmount = newvalue
		user.save()
	except Catnip.DoesNotExist:
		return

def gettotal():
	try:
		userlist = Catnip.objects.all().order_by('amount')
		allusers = []
		for x in userlist:
			allusers.append(x.name)
		return allusers
	except Exception as e:
		print(e)


    # c.execute('SELECT name FROM Catnip_catnip ORDER BY amount ASC')
    # data = c.fetchall()
    # data = list(data)
    # y = []
    # for x in data:
    #     y.append(x[0])
    # return y

""" -----------------Clip Functions----------------- """
# def get_all_clips():
# 	try:
# 		allclips = Clip.objects.all()
# 		return allclips
# 	except Clip.DoesNotExist:
# 		return None

# def get_clip_from_id(clipid):
# 	try:
# 		clip = Clip.objects.get(id=clipid)
# 		return clip.link
# 	except Clip.DoesNotExist:
# 		return None
