import re

print("Bitte geben Sie die gefragten Angaben ein")

print("Marke eingeben, bitte erster Buchstabe klein und ohne Bindestriche:")

x1 = input()

print("Kilometerstand eingeben, bitte nur ganze Zahlen eingeben:")

x2 = int(input())

print("PS eingeben, bitte nur Zahlenverwenden:")


x3 = int(input())

print("Leergewicht eingeben, bitte nur ganze Zahlen eingeben:")

x4 = int(input())

print("Getriebsart eingeben, Auswahl = Schaltgetriebe, Automat oder Automat Sequentiell, - :")

x5 = input()

print("Hubraum eingeben, bitte nur Zahlen verwenden:")

x6 = int(input())

print("Antribesart eingeben, Auswahl = Allrad, Vorderradantireb, Hinterradantrieb, - ")

x7 = input()

print("Anzahl Türen:")

x8 = int(input())

print("Anzahl Sitze:")

x9 = int(input())

print("Treibstoffart eingeben, Auswahl = Benzin Bleifrei, Benzin verbleit,Diesel,Elektrisch,Hybrid :")

x10 = input()

print("Verbrauch pro 100km eingeben, bitte nur Zahlen verwenden:")

x11 = int(input())


numberdic = {"aixam" : "1",
"alfa romeo " : "2",
"aston martin" : "3",
'aston martin ' : "3",
"audi" : "4",
"bentley" : "5",
"bmw" : "6",
"bmw-alpina" : "7",
"buick" : "8",
"cadillac" : "9",
"chevrolet" : "10",
"chrysler" : "11",
"citroen" : "12",
'citroën' : "12",
"dacia" : "13",
"daewoo" : "14", 
"daihatsu" : "15", 
"daimler" : "16",
"de tomaso " : "17",
"dodge" : "18", 
"ferrari" : "20",
"fiat" : "21",
"ford" : "22",
"honda" : "23",
"hs" : "24",
"hummer" : "25",
"hyundai" : "26",
"innocenti" : "27",
"isuzu" : "28",
"jaguar" : "29",
"jeep" : "30",
"kia" : "31",
"lamborghini" : "32",
"lancia" : "33",
"land rover " : "34",
'land rover' : "34",
"lexus" : "35",
"lotus" : "36",
"maserati" : "37",
"mazda" : "38",
"mercedes-benz" : "39",
"mg" : "40",
"mini" : "41",
"mitsubishi" : "42",
"nissan" : "43",
"oldsmobile" : "44",
"opel" : "45",
"peugeot" : "46",
"pontiac" : "47",
"porsche" : "48",
"renault" : "49",
"rolls-royce" : "50",
"rover" : "51",
"saab" : "52",
"seat" : "53",
"skoda" : "54",
"smart" : "55",
"ssang yong " : "56",
'ssangyong' : "56",
"subaru" : "57",
"suzuki" : "58",
"toyota" : "59",
"tvr" : "60",
"volvo" : "61",
"vw" : "62",
"wiesmann" : "63",
"datsun" : "64",
"gmc" : "65",
"infiniti" : "66",
"plymouth" : "67",
"piaggio" : "68",
"ac" : "69",
"autobianchi" : "70",
"mercury" : "71",
"dkw" : "72",
'dkw de ' : "73",
"mercury" : "73",
"pgo" : "74",
"studebaker" : "75",
"triumph" : "76",
"tesla" : "77",
"mclaren" : "78",
"ds automobiles " : "79", 
"american motors amc " : "80",
"austin" : "81",
"caterham" : "82",
'lada' : "83",
'morgan' : "84",
'puch' : "85",
'talbot' : "86",
'tata' : "87",
'iveco' : "88",
'lincoln' : "89",
'maybach' : "90",
'morris' : "91",
'simca' : "92",
'trabant' : "93",
'amc' : "80",
'delorean de ' : "94",
'fisker' : "95",
"-" : "0", 
"Vorderradantrieb" : "1",
"Hinterradantrieb" : "2",
"Allrad" : "3",


'-' : "0",
"Andere" : "1",
"Benzin Bleifrei" : "2",
"Benzin verbleit" : "3",
"Diesel" : "4", 
"Elektrisch" : "5",
"Elektrisch (Plug-in) / Benzin" : "8",
'Elektrisch (Plug-in) / Diesel' : "9",
"Erdgas (CNG)" : "6",
'Erdgas (CNG) / Benzin' : "6",
"Ethanol E85 / Benzin" : "7",
"Hybrid" : "8",


"-" : "0",
"0 l/100km (kombiniert)" : "0",
"0.6 l/100km (kombiniert)" : "0.6",
"1 l/100km (kombiniert)" : "1",
"1.2 l/100km (kombiniert)" : "1.2",
"1.3 l/100km (kombiniert)" : "1.3",
"1.4 l/100km (kombiniert)" : "1.4",
"1.5 l/100km (kombiniert)" : "1.5",
"1.6 l/100km (kombiniert)" : "1.6",
"1.7 l/100km (kombiniert)" : "1.7",
"1.8 l/100km (kombiniert)" : "1.8",
"1.9 l/100km (kombiniert)" : "1.9",
"10 l/100km (kombiniert)" : "10",
"10.1 l/100km (kombiniert)" : "10.1",
"10.2 l/100km (kombiniert)" : "10.2",
"10.3 l/100km (kombiniert)" : "10.3",
"10.4 l/100km (kombiniert)" : "10.4",
"10.5 l/100km (kombiniert)" : "10.5",
"10.6 l/100km (kombiniert)" : "10.6",
"10.7 l/100km (kombiniert)" : "10.7",
"10.8 l/100km (kombiniert)" : "10.8",
"10.9 l/100km (kombiniert)" : "10.9",
"11 l/100km (kombiniert)" : "11",
"11.1 l/100km (kombiniert)" : "11.1",
"11.2 l/100km (kombiniert)" : "11.2",
"11.3 l/100km (kombiniert)" : "11.3",
"11.4 l/100km (kombiniert)" : "11.4",
"11.5 l/100km (kombiniert)" : "11.5",
"11.6 l/100km (kombiniert)" : "11.6",
"11.7 l/100km (kombiniert)" : "11.7",
"11.8 l/100km (kombiniert)" : "11.8",
"11.9 l/100km (kombiniert)" : "11.9",
"12 l/100km (kombiniert)" : "12",
"12.1 l/100km (kombiniert)" : "12.1",
"12.2 l/100km (kombiniert)" : "12.2",
"12.3 l/100km (kombiniert)" : "12.3",
"12.4 l/100km (kombiniert)" : "12.4",
"12.5 l/100km (kombiniert)" : "12.5",
"12.6 l/100km (kombiniert)" : "12.6",
"12.7 l/100km (kombiniert)" : "12.7",
"12.8 l/100km (kombiniert)" : "12.8",
"12.9 l/100km (kombiniert)" : "12.9",
"13 l/100km (kombiniert)" : "13",
"13.1 l/100km (kombiniert)" : "13.1",
"13.2 l/100km (kombiniert)" : "13.2",
"13.3 l/100km (kombiniert)" : "13.3",
"13.4 l/100km (kombiniert)" : "13.4",
"13.5 l/100km (kombiniert)" : "13.5",
"13.6 l/100km (kombiniert)" : "13.6",
"13.7 l/100km (kombiniert)" : "13.7",
"13.8 l/100km (kombiniert)" : "13.8",
"13.9 l/100km (kombiniert)" : "13.9",
"14 l/100km (kombiniert)" : "14",
"14.1 l/100km (kombiniert)" : "14.1",
"14.2 l/100km (kombiniert)" : "14.2",
"14.3 l/100km (kombiniert)" : "14.3",
"14.4 l/100km (kombiniert)" : "14.4",
"14.5 l/100km (kombiniert)" : "14.5",
"14.6 l/100km (kombiniert)" : "14.6",
"14.7 l/100km (kombiniert)" : "14.7",
"14.8 l/100km (kombiniert)" : "14.8",
"14.9 l/100km (kombiniert)" : "14.9",
"15 l/100km (kombiniert)" : "15",
"15.1 l/100km (kombiniert)" : "15.1",
"15.2 l/100km (kombiniert)" : "15.2",
"15.3 l/100km (kombiniert)" : "15.3",
"15.4 l/100km (kombiniert)" : "15.4",
"15.5 l/100km (kombiniert)" : "15.5",
"15.6 l/100km (kombiniert)" : "15.6",
"15.7 l/100km (kombiniert)" : "15.7",
"15.8 l/100km (kombiniert)" : "15.8",
"15.9 l/100km (kombiniert)" : "15.9",
"16 l/100km (kombiniert)" : "16",
"16.1 l/100km (kombiniert)" : "16.1",
"16.2 l/100km (kombiniert)" : "16.2",
"16.3 l/100km (kombiniert)" : "16.3",
"16.4 l/100km (kombiniert)" : "16.4",
"16.5 l/100km (kombiniert)" : "16.5",
"16.6 l/100km (kombiniert)" : "16.6",
"16.7 l/100km (kombiniert)" : "16.7",
"16.9 l/100km (kombiniert)" : "16.9",
"17 l/100km (kombiniert)" : "17",
"17.2 l/100km (kombiniert)" : "17.2",
"17.4 l/100km (kombiniert)" : "17.4",
"17.5 l/100km (kombiniert)" : "17.5",
"17.7 l/100km (kombiniert)" : "17.7",
"17.8 l/100km (kombiniert)" : "17.8",
"18 l/100km (kombiniert)" : "18",
"18.1 l/100km (kombiniert)" : "18.1",
"18.3 l/100km (kombiniert)" : "18.3",
"19 l/100km (kombiniert)" : "19",
"19.1 l/100km (kombiniert)" : "19.1",
"19.2 l/100km (kombiniert)" : "19.2",
"19.3 l/100km (kombiniert)" : "19.3",
"19.5 l/100km (kombiniert)" : "19.5",
"2 l/100km (kombiniert)" : "2",
"2.1 l/100km (kombiniert)" : "2.1",
"2.4 l/100km (kombiniert)" : "2.4",
"2.5 l/100km (kombiniert)" : "2.5",
"20 l/100km (kombiniert)" : "20",
"20.8 l/100km (kombiniert)" : "20.8",
"21 l/100km (kombiniert)" : "21",
'21.1 l/100km (kombiniert)' : "21.2",
"21.3 l/100km (kombiniert)" : "21.3",
"21.5 l/100km (kombiniert)" : "21.5",
"21.8 l/100km (kombiniert)" : "21.8",
"22 l/100km (kombiniert)" : "22",
"23 l/100km (kombiniert)" : "23",
"24.9 l/100km (kombiniert)" : "24.9",
"25 l/100km (kombiniert)" : "25",
"25.1 l/100km (kombiniert)" : "25.1",
'42 l/100km (kombiniert)' : "42",
'43 l/100km (kombiniert)' : "43",
'47 l/100km (kombiniert)' : "47",
'48 l/100km (kombiniert)' : "48",
'50 l/100km (kombiniert)' : "50",
'51 l/100km (kombiniert)' : "51",
'67 l/100km (kombiniert)' : "67",
"3 l/100km (kombiniert)" : "3",
"3.2 l/100km (kombiniert)" : "3.2",
"3.3 l/100km (kombiniert)" : "3.3",
"3.4 l/100km (kombiniert)" : "3.4",
"3.5 l/100km (kombiniert)" : "3.5",
"3.6 l/100km (kombiniert)" : "3.6",
"3.7 l/100km (kombiniert)" : "3.7",
"3.8 l/100km (kombiniert)" : "3.8",
"3.9 l/100km (kombiniert)" : "3.9",
"35 l/100km (kombiniert)" : "35",
"36 l/100km (kombiniert)" : "36",
"38 l/100km (kombiniert)" : "38",
"39 l/100km (kombiniert)" : "39",
"4 l/100km (kombiniert)" : "4",
"4.1 l/100km (kombiniert)" : "4.1",
"4.2 l/100km (kombiniert)" : "4.2",
"4.3 l/100km (kombiniert)" : "4.3",
"4.4 l/100km (kombiniert)" : "4.4",
"4.5 l/100km (kombiniert)" : "4.5",
"4.6 l/100km (kombiniert)" : "4.6",
"4.7 l/100km (kombiniert)" : "4.7",
"4.8 l/100km (kombiniert)" : "4.8",
"4.9 l/100km (kombiniert)" : "4.9",
"5 l/100km (kombiniert)" : "4",
"5.1 l/100km (kombiniert)" : "5.1",
"5.2 l/100km (kombiniert)" : "5.2",
"5.3 l/100km (kombiniert)" : "5.3",
"5.4 l/100km (kombiniert)" : "5.4",
"5.5 l/100km (kombiniert)" : "5.5",
"5.6 l/100km (kombiniert)" : "5.6",
"5.7 l/100km (kombiniert)" : "5.7",
"5.8 l/100km (kombiniert)" : "5.8",
"5.9 l/100km (kombiniert)" : "5.9",
"6 l/100km (kombiniert)" : "6",
"6.1 l/100km (kombiniert)" : "6.1",
"6.2 l/100km (kombiniert)" : "6.2",
"6.3 l/100km (kombiniert)" : "6.3",
"6.4 l/100km (kombiniert)" : "6.4",
"6.5 l/100km (kombiniert)" : "6.5",
"6.6 l/100km (kombiniert)" : "6.6",
"6.7 l/100km (kombiniert)" : "6.7",
"6.8 l/100km (kombiniert)" : "6.8",
"6.9 l/100km (kombiniert)" : "6.9",
"7 l/100km (kombiniert)" : "7",
"7.1 l/100km (kombiniert)" : "7.1",
"7.2 l/100km (kombiniert)" : "7.2",
"7.3 l/100km (kombiniert)" : "7.3",
"7.4 l/100km (kombiniert)" : "7.4",
"7.5 l/100km (kombiniert)" : "7.5",
"7.6 l/100km (kombiniert)" : "7.6",
"7.7 l/100km (kombiniert)" : "7.7",
"7.8 l/100km (kombiniert)" : "7.8",
"7.9 l/100km (kombiniert)" : "7.9",
"8 l/100km (kombiniert)" : "8",
"8.1 l/100km (kombiniert)" : "8.1",
"8.2 l/100km (kombiniert)" : "8.2",
"8.3 l/100km (kombiniert)" : "8.3",
"8.4 l/100km (kombiniert)" : "8.4",
"8.5 l/100km (kombiniert)" : "8.5",
"8.6 l/100km (kombiniert)" : "8.6",
"8.7 l/100km (kombiniert)" : "8.7",
"8.8 l/100km (kombiniert)" : "8.8",
"8.9 l/100km (kombiniert)" : "8.9",
"9 l/100km (kombiniert)" : "9",
"9.1 l/100km (kombiniert)" : "9.1",
"9.2 l/100km (kombiniert)" : "9.2",
"9.3 l/100km (kombiniert)" : "9.3",
"9.4 l/100km (kombiniert)" : "9.4",
"9.5 l/100km (kombiniert)" : "9.5",
"9.6 l/100km (kombiniert)" : "9.6",
"9.7 l/100km (kombiniert)" : "9.7",
"9.8 l/100km (kombiniert)" : "9.8",
"9.9 l/100km (kombiniert)" : "9.9",


"-" : "0",
"Automat" : "1",
"Schaltgetriebe" : "2",
"Automat Sequentiell" : "3",
'Sonstiges' : "4"
}




pattern = re.compile(r'\b(' + '|'.join(numberdic.keys()) + r')\b')
newx1 = pattern.sub(lambda x: numberdic[x.group()], x1)
newx5 = pattern.sub(lambda x: numberdic[x.group()], x5)
newx7 = pattern.sub(lambda x: numberdic[x.group()], x7)
newx10 = pattern.sub(lambda x: numberdic[x.group()], x10)

newx1 =int(newx1)
newx5 =int(newx5)
newx7 = int(newx7)
newx10 = int(newx10)


t1 = 0
t2 = 0.60728501
t3 = -0.04215118
t4 = -0.08041125
t5 = 0.04965925
t6 = -0.01676428
t7 = -0.00089649
t8 = 0.05744553
t9 = -0.06702858
t10 = 0.03630458
t11 = -0.00667139

y = newx1*t1 + x2*t2 + x3*t3 + x4*t4 + newx5*t5 + x6*t6 + newx7*t7 + x8*t8 + x9*t9 + newx10*t10 + x11*t11

print("Ihr Auto hat den Wert von " + str(y) + " CHF")
