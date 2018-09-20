#lists/dictionaries/tuples

#create a list and show how we can find certain items in list
#add item to list
dogList = ['golden retriever', 'cavalier king charles', 'chihuahua', 'golden doodle', 'cockapoo']
print("this is an example of a list:", dogList)

# tuples cannot be changed once created!
# helpful because sometimes you want to create
# something that you know will never change
fibs = (0,1,1,2,3)
print("this is an example of a tuble:", fibs)

#dictionaries aka dicts aka map
#key:value pairing

favoriteSports = {'Ralph Williams' : 'Football',
                    'Michael Tippitt' : 'Basketball',
                    'Edward Elgar' : 'Baseball',
                    'Rebecca Clark' : 'Netball',
                    'Ethyl Smith' : 'Badminton',
                    'Frank Bridge' : 'Rugby'}
print(favoriteSports['Rebecca Clark'])
del favoriteSports['Ethyl Smith']
print(favoriteSports)
