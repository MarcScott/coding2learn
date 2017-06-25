from random import randrange
nouns=[]
verbs=[]
parings=[]

days = int(input('How many days of Christmas are there?'))+1

with open('nouns.txt','r') as file1:
	for line in file1:
		noun = line.rstrip()
		if noun[-1] == 's':
			nouns.append(noun)
		elif noun[-1] == 'y':
			if noun[-2] == 'e':
				noun=noun[0:-2]+'ies'
			else:
				noun=noun[0:-1]+'ies'
		else:
			noun=noun+'s'
		nouns.append(noun)

with open('verbs.txt','r') as file2:
	for line in file2:
		verb = line.rstrip()
		if verb[-1]=='e':
			verb = verb[0:-1]+'ing'
		else:
			verb = verb+'ing'
		verbs.append(verb)

for i in range(days):
	paring = nouns.pop(randrange(len(nouns)))+' a '+verbs.pop(randrange(len(verbs)))
	parings.append(paring)


for day in range(1,days):
	if str(day)[-1] == 1 or day ==1:
		ending = 'st'
	elif str(day)[-1] == 2 or day ==2:
		ending = 'nd'
	elif str(day)[-1] == 3 or day ==3:
		ending = 'rd'
	else:
		ending = 'th' 
	print('On the',str(day)+ending,'day of Christmas my true love sent to me:')
	for count in range(day,1,-1):
		print(count,parings[count])
	if day == 1:
		print('a partridge in a pear tree')
	else:
		print('and a partridge in a pear tree', )
	print('')