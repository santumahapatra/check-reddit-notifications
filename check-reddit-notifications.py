import praw

r = praw.Reddit(user_agent='example')

def user_details(): 

	print("Please enter username: ")
	username = raw_input()

	print("Please enter password: ")
	password = raw_input()

	try:
		r.login(username, password)
		return True
	except Exception :
		user_details()

user_details()

count = 0

for msg in r.get_unread(limit=None):
	count += 1

print("You have " + str(count) + " unread messages.")