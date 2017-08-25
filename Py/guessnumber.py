#used to random number to guess
import random
import sys
import time
import subprocess as sp

if sys.version_info[0] < 3:
    input = raw_input


def start_guess():
	tmp = sp.call('cls', shell=True)
	guessTaken = 0
	print 'Hello, what is your name ?'
	userName = input()
	# userName = 'Miqdad'

	randNumber = random.randint(1, 20)

	print '\nWell, ' + userName + ' let\'s play some game, try to guess what number am i thinking ? (1 - 20)'
	print 'Generating random number ...'
	time.sleep(1)
	print 'Done, now take a guess ...'

	while guessTaken < 6:
		try:
			if guessTaken == 0: answer = int(input("Your guess ? "))
			else :	answer = int(input("\nYour next guess ? "))
		except Exception as e:
			print 'Please only input number !'
			continue

		guessTaken = guessTaken + 1

		if answer == randNumber :
			print 'Well Done, you guess the number right !'
			break
		elif not 0 < answer < 20 :
			print 'only guess between 1 to 20 !'
		else :
			print 'Your guess is too {}'.format('high' if answer > randNumber else 'low')

	if guessTaken == 6 :
		print '\nToo bad, you can\'t guess the number. the number i was thinking of was ' + str(randNumber)

	retry_game()
	
def retry_game():
	tryAgain = input('Do you want to try again ? (Y/N)')
	if tryAgain.upper() == 'Y' :
		start_guess()
	else :
		print 'Well, good bye then ...'

if __name__ == '__main__':
	start_guess()