known_users = ['Bob', 'Claire', 'Don', 'Harry']
print(len(known_users))

while True:
	print('Hi, My name is Travis!')
	name = input('What is your name? ').strip()

	if name in known_users:
		print('Hello {}!'.format(name))
		remove = input('Would you like to be removed from the system (y/n)?: ').lower()

		if remove == 'y':
			print(known_users)
			known_users.remove(name)
			print(known_users)