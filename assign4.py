#Exercise 3-1: Names
names = ["briya","faiza","fizza","kiran","mehreen"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print(names[4])
#Exercise 3-2: Greetings
print(f'{names[0]} is enjoying her work')
print(f'{names[1]} is enjoying her work')
print(f'{names[2]} is enjoying her work')
print(f'{names[3]} is enjoying her work')
print(f'{names[4]} is enjoying her work')
#alternative method
print("...Alternative method...")
for name in names:
    print(f'{name} is enjoying her work')
#Exercise 3-3: Your Own List
transportations = ["Honda motorcycle", "Tesla Model S", "Yamaha R1", "BMW X5"]
for transportation in transportations:
    print(f'I would like to own a {transportation}')
#Exercise 3-4: Guest List
guests = ["Obama","Donald Trump","Steve Jobs","Markus Brownie"]
for guest in guests:
    print(f'Dear {guest}, you are cordially invited for an annual dinner at my place')
#Exercise 3-5: Changing Guest List
print(f"Unfortunately, {guests[0]} can't make it to the dinner")
guests[0] = "Mark Zukerburg"
for guest in guests:
    print(f"Dear {guest}, you are cordially invited for an annual dinner at my place")
#Exercise 3-6: More Guests
print("Great News! we have found a bigger table")
guests.insert(0,"Issac Newton")
guests.insert(3, "Leonardo De Capri")
guests.append("Brad Pitt")
for guest in guests:
    print(f"Dear {guest}, You are cordially invited for an annual dinner at my place")
#Exercise 3-7: Shrinking Guest List
print("Sorry, I can invite only two people to dinner")
while len(guests) > 2:
    removed_guests = guests.pop()
    print(f"sorry i can't invite you Mr. {removed_guests} to your dinner")

for guest in guests:
    print(f"Dear {guest}, you are cordially invited for an annual dinner at my place")

del guests[0]
del guests[0]

print(guests)
#Exercise 3-8: Seeing the World
places = ["London","Paris","Italy","Maldives","Turkey"]
print("original order",places)
print("Alphabetical order",sorted(places))
print("original order",places)
print("reverse alphabetical order",sorted(places,reverse=True))
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)
#Exercise 3-9: Every Function
Fav_things = ["Nanga Parbat","Rakaposhi","Mount Everest","Lhotsu","Makalu","Cho Oyu"]
print(sorted(Fav_things))
print(sorted(Fav_things,reverse=True))
Fav_things.append("Manaslu")
Fav_things.sort()
Fav_things.reverse()
Fav_things.extend(["K2","Kangchenjunga"])
Fav_things.insert(0,"Dhaulagiri")
Fav_things.remove("K2")
print("after all functions",Fav_things)
#Exercise 3-10: Intentional Error
languages = ["python","PhP","C++"]
#print(languages[4])
print(languages[2])