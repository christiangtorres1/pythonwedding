#This will be a general data dump on varibles, funtcions, etc that will be used to build the wedding app

#Variables

weddingname = "Torres Wedding"
date = "11/3/2023"
venue = "Hayes Hollow at Hidden Falls"
venueaddress = "2222 Bridal Veil, Sping, Texas, 78070"
bride = "Megan F. Osborne"
groom = "Christian G. Torres"


#Sets

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
#simple print examples

print(f"The {weddingname} will take place on {date} with {bride} marrying {groom} we hope you can join us!")

# for loops examples

for names in groomsmen.values():
    print(names)

