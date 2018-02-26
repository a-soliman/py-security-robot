known_users = ['Bob', 'Claire', 'Don', 'Harry']
print(len(known_users))

while True:
	print('Hi, My name is Travis!')
	name = input('What is your name? ').strip()

	if name in known_users:
		print('Hello {}!'.format(name))
		