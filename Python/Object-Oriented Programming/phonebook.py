class Phonebook:

	def __init__(self, surname, familyname, number):
		self.surname = surname
		self.familyname = familyname
		self.number = number
	
		x = int(self.number)
		if x <= 759999999 or x >= 800000000:   #telnr varieren von 760000000 - 799999999
			print("That's not a real number") 



	def show(self):
		print("Surname = {0}, Familyname = {1}, Number = {2}.".format(self.surname ,self.familyname, self.number))
		



a = Phonebook("Danus", "Mohan", 787127888 )
a.show()

b = Phonebook("Max", "Mustermann", 784361245)
b.show()


