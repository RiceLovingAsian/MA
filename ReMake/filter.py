brands = ["lamborghini","peugeot","volvo"]

name ="volvo xc60 allrad blabliblö"

nameS = name.split(' ')
print( list(filter(lambda x: x in brands, nameS)))
