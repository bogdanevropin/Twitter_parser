import tweepy


def parse_ids(link_account):
	#
	#
	# auth = tweepy.OAuthHandler(..., ...)
	# auth.set_access_token(..., ...)
	#
	# api = tweepy.API(auth)
	#
	# ids = []
	# for page in tweepy.Cursor(api.followers_ids, screen_name="Meowlinch🔞").pages():
	# 	ids.extend(page)
	# 	time.sleep(60)
	# client_name = link_account
	
	# followers = tweepy.Client.get_list_followers(
	# 	link_account, expansions=None, max_results=15000, pagination_token=None, tweet_fields=None, user_fields=None, user_auth=False)
	# # sub = tweepy.API.get_list_subscribers()
	# print(followers)
	
	import time
	import tweepy
	
	auth = tweepy.OAuthHandler(..., ...)
	auth.set_access_token(..., ...)
	
	api = tweepy.API(auth)
	
	ids = []
	for page in tweepy.Cursor(api.followers_ids, screen_name=link_account).pages():
		ids.extend(page)
		time.sleep(60)
	
	len(ids)

if __name__ == "__name__":
	parse_ids("@nyalinch")
	