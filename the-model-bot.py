import tweepy as tp
import time
import os
import random

# credentials to login to twitter api
consumer_key = '263kVylFtvonNaSY1aFGRfJ6v'
consumer_secret = 'NIx42btxoEXJtgI9m3hTStMPLI5VUbhIKUsWlq0Bs9bC2VhPwn'
access_token = '719004797047857153-9D0eXKQrmhRJSmAz4VJsAB9OEEG6tGE'
access_secret = 'cyCj6Rl9qYXQlW7V0wRtG3l8njbGVuAV2dhw2umKCLsz1'

# login to twitter account api
auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

lista =[]
fol = api.followers_ids(915385670532763648)
nums_to_select = 3
list_of_random_fol = random.sample(fol, nums_to_select)
for f in list_of_random_fol:
    user = api.get_user(f)
    lista.append(user.screen_name)


follower1 = api.followers_ids(2945669283)
nums_to_select = 3
list_of_random_follower1 = random.sample(follower1, nums_to_select)
for f in list_of_random_follower1:
    user = api.get_user(f)
    lista.append(user.screen_name)

follower2 = api.followers_ids(192220607)
nums_to_select = 4
list_of_random_follower2 = random.sample(follower2, nums_to_select)
for f in list_of_random_follower2:
    user = api.get_user(f)
    lista.append(user.screen_name) 

f1 = lista[0]
f2 = lista[1]
f3 = lista[2]
f4 = lista[3]
f5 = lista[4]
f6 = lista[5]
f7 = lista[6]
f8 = lista[7]
f9 = lista[8]
f9 = lista[9]


os.chdir('models')
# iterates over pictures in models folder
for model_image in os.listdir('.'):
    api.update_with_media(model_image,status='.'f'@{f1}' ' ' f'@{f2}' ' ' f'@{f3}' ' ' f'@{f4}' ' ' f'@{f5}' ' ' f'@{f6}' ' ' f'@{f7}' ' ' f'@{f8}' ' ' f'@{f9}')
    time.sleep(43200)

