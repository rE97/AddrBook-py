import os
import sys
import subprocess as sp
import time

if sys.version_info[0] < 3:
	input = raw_input

check = 0
fullPath = ''

def main():
	global fullPath
	tmp = sp.call('cls', shell=True)
	userName = input("Username : ")

	# Check if file with username as filename is exists or not
	fullPath = 'D:\\Exercise\\Py\\AddrBook\\'+userName+'.txt'
	try:
		f = open(fullPath, 'r')
		f.close()
		chooseAction()
	except :
		pass

	if check == 0:
		pass
		print 'Address Book for ' + userName + ' is not found.'
		createBook = raw_input('\nDo you want to create new address book ? (Y/N) ')
		if createBook.upper() == 'Y' :
			# Create File
			f = open(fullPath, 'w+')
			f.close()
			print 'File succesfully created.'
			time.sleep(2)
			chooseAction()
		else :
			reset = raw_input('\nDo you want to try with another username ? (Y/N) ')
			if reset.upper() == 'Y' :
				main()
			else :
				print '\nEnd of Program'

def chooseAction():
	global check
	check = 1

	tmp = sp.call('cls', shell=True)
	print '\n============================================='
	print '               CHOOSE ACTION'
	print '=============================================\n'

	print '1. Show all entry'
	print '2. Add new entry'
	print '3. Search specific entry'
	print '4. Edit entry'
	print '5. Delete this book'

	action = raw_input('\nChoose Action : ')
	if action == '1':
		show_entry()
	elif action == '2':
		new_entry()
	elif action == '3':
		search_entry()
	elif action == '4':
		edit_entry()
	elif action == '5':
		del_book()
	elif action == 'exit':
		sys.exit()
	else:
		print 'Please Choose the right number.'
		time.sleep(1)
		chooseAction()

def show_entry():
	global fullPath
	tmp = sp.call('cls',shell=True)

	print '\n============================================='
	print '               SHOW ALL ENTRY'
	print '=============================================\n'

	fr = open(fullPath, 'r')
	fl = fr.readlines()
	
	if not fl:
		fr.close
		new_input = raw_input("No entry yet, do you want to add new entry ? (Y/N) ")
		if new_input.upper() == 'Y':
			new_entry()
		else:
			chooseAction()

	else:
		for x in fl:
			a, b, c, d = x.split("|")
			splited = x.split("|")
			print 'Name : ' + a
			print 'Phone : ' + b
			print 'Email : ' + c
			print 'Address : ' + d

		fr.close()

		back = raw_input("Back to main menu ? (Y/N) ")
		if back.upper() == 'Y':
			chooseAction()
		else:
			print '\nClosing current session.'
			sys.exit()

def new_entry():
	tmp = sp.call('cls',shell=True)

	print '\n============================================='
	print '               ADD NEW ENTRY'
	print '=============================================\n'
	entry_name = raw_input('What is the person name : ')
	# check apakah nama udh ada ato belum
	entry_phone = raw_input('What is ' + entry_name + ' phone number : ')
	entry_email = raw_input('What is ' + entry_name + ' email : ')
	entry_address = raw_input('What is ' + entry_name + ' address : ')

	entry_info = entry_name + "|" + entry_phone + "|" + entry_email + "|" + entry_address
	insert_to_file (entry_info)

def search_entry():
	pass

def edit_entry():
	pass

def del_book():
	global fullPath
	os.remove(fullPath)
	print 'Current Address Book is deleted'
	time.sleep(1)
	print 'closing current session.'
	sys.exit()

def insert_to_file (entry_info):
	global fullPath
	try:
		appendFile = open(fullPath, 'a+')
		appendFile.write(entry_info)
		appendFile.write('\n')
		appendFile.close

		print 'New record added to address book'
		time.sleep(2)
		chooseAction()

	except Exception as e:
		print e

if __name__ == '__main__':
	main()