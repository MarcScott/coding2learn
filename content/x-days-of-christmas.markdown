Title: X Days of Christmas
date: 2013-12-13 08:39
slug: x-days-of-christmas

Just a quick one from me today.

I woke up this morning with a lesson idea in my head, that was also a Python script.

I've a few teacher followers, so I thought I'd shove it up here for others to use if they want. You'll have to forgive my poor coding and poorer use of the English language.

The challenge for the students is to create a program that will produce the lyrics for 'The X Days of Christmas'.

You can find my solution at the bottom of the post, and here's a few files - [xdays.py]({filename}/docs/XDays/xdays.py), [nouns.txt]({filename}/docs/XDays/nouns.txt), [verbs.txt]({filename}/docs/XDays/verbs.txt)

The results can be quite amusing - my particular favorites have been "20 kittens a bleeding", "99 rats a computing" and "11 creators a mating"

I've even had ones that make sense, like "8 pies a baking".

Here's an example final verse that I quite enjoyed.

>On the 12th day of Christmas my true love sent to me:  
>12 roads a developing  
>11 faucets a mating  
>10 planes a combing  
>9 worms a solving  
>8 tents a liing  
>7 kittens a slaying  
>6 tubs a handing  
>5 passengers a scattering  
>4 bats a utilizing  
>3 mornings a promoting  
>2 pollutions a foreseing  
>and a partridge in a pear tree  



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
