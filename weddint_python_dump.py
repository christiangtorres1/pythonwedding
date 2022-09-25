#This will be a general data dump on varibles, funtcions, etc that will be used to build the wedding app

#Variables

weddingname = "Torres Wedding"
date = "November 3 2023"
venue = "Hayes Hollow at Hidden Falls"
venueaddress = "2222 Bridal Veil, Sping, Texas, 78070"
bride = "Megan F. Osborne"
groom = "Christian G. Torres"
groomfirst = groom.split()[0]
bridefirst = bride.split()[0]


#Dictionaries

groomsmen = {
    "bestman": "Amador Yeverino",
    "groomsman1": "Robert Villareal",
    "groomsman2": "Adan Torres",
    "groomsman3": "Jon Davidson",
    "groomsman4": "DJ Valenzuela"
}

bridesmaids =  {
    "maidofhonor": "Ashley Newheart",
    "bridesmaid1": "Lori Osborne"
}

#simple print example

print(f"The {weddingname} will take place on {date} with {bride} marrying {groom} we hope you can join us!")

# for loops examples

print(f"{groom}'s groomsmen will be:")
for names in groomsmen.values():
    print(names)

print(f"{groomfirst}'s best man is {groomsmen.get('bestman')}")

print(f"{bride}'s bridesmaids will be:")
for names in bridesmaids.values():
    print(names)

print(f"{bridefirst}'s Maid of Honor is {bridesmaids.get('maidofhonor')}")