# encoder ring v? ... the first one

print("Welcome to encoder ring")

while True:
	print("Enter \"New\" to create a new file.")
	print("Enter \"Done\" to exit the program.")
	# top level user choice
	userInput = input("Please make a choice: ")
	userInput = userInput.lower()
	if userInput == "new":
		userFileName = input("Enter a filename: ")
		# creates a file in the same dir as the program
		newFile = open(userFileName + ".txt","w+")
		print("Enter \"End\" to save file and exit file definition.")
		for i in range(97, 123): # spans all lowercase letters of the eng alphabet
			print("Enter something you would like to assign to the character \"" + chr(i) + "\". ", end="") 
			userInputCh = input("")
			if userInputCh.lower() == "end":
				newFile.close()
				break
			else:
				newFile.write(str(i) + " = " + userInputCh + "\n")
			i += 1
	elif userInput == "done":
		break
print("Program terminated.")
quit()
