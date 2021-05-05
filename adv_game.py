from adventurelib import *
import adventurelib
import time

ghost_hp = 10
player_attack = 2

def playerAttack(ghost):
	global player_attack
	global alive
	global ghost_hp
	ghost_hp = ghost_hp - player_attack
	print("The ghost has ",ghost_hp, " HP left.")
	if ghost_hp == 0:
		say("You have defeated the ghost!")
		alive = False
		return alive
	else:
		alive = True
		return alive

# Make sure to widen your command prompt window for better formatting of text!!

# INTRODUCTION
say("JANUARY 22, 1894")
time.sleep(1.5)
say("It is a cold and rainy night when you stumble upon an old mansion, hidden in the woods.")
time.sleep(4)
say("You are relieved to find shelter for the night after walking all day, trying to find your way back home.")
time.sleep(4)
say("The mansion looks eerie, dark...")
time.sleep(2.5)
say("You decide to go in anyway.")
print("")
time.sleep(2)
say("------------------------------- GAME RULES --------------------------------------")
time.sleep(0.25)
say("• move through rooms by typing '[north, south, east, west]'")
say("• take items by typing 'take [item name]'")
say("• give items to another character by typing 'give [item name] to [recipient name]'")
say("• look around by typing 'look'")
say("• attack the ghost by typing 'hit [target name] with [weapon name]'")
say("• get list of commands available by typing 'help'")
say("---------------------------------------------------------------------------------")
time.sleep(1)
say("")
say("You are standing in the Entrance of the mansion when you walk in.")
say("Find and defeat the ghost using items you find!")

# DECLARE ROOMS AND DESCRIPTIONS
entrance = Room("""
	You are standing in the Entrance of the mansion.
	""")

kitchen = Room("""
	You are in the grandest Kitchen you've ever seen in your life.
	""")

living = Room("""
	You are in the Living Room, full of expensive paintings and furniture.
	""")

dining = Room("""
	You are in the Dining Room. You get hungry just thinking about the food that was eaten here.
	""")

bathroom = Room("""
	You are in the Bathroom. The mirror is making you feel uneasy...
	""")

library = Room("""
	You are in the Library. The bookshelves line every wall to the ceiling.
	""")

office = Room("""
	You are in the Office. This is where the home owner must have spent most of their time.
	""")

master_bed = Room("""
	You are in the Master Bedroom. Chills run down your spine the second you enter.
	""")

guest_bed = Room("""
	You are in the Guest Bedroom. It is smaller than the master bedroom, but bigger than your house.
	""")

basement = Room("""
	You are in the Basement. You know nothing good ever happens in basements.
	""")

# ROOM CONNECTIONS
entrance.north = living
entrance.east = dining
entrance.west = library
kitchen.north = guest_bed
kitchen.west = dining
living.west = bathroom
living.south = entrance
living.east = basement
dining.west = entrance
dining.east = kitchen
dining.north = basement
bathroom.west = master_bed
bathroom.east = bathroom
bathroom.south = office
library.east = entrance
library.north = bathroom
library.west = office
office.north = master_bed
office.east = library
master_bed.south = office
master_bed.east = bathroom
guest_bed.south = kitchen
guest_bed.west = basement
basement.west = living
basement.east = guest_bed
basement.south = dining

# ITEM MODIFICATIONS
Item.desc = ""

# ITEM DEFINITIONS
apple = Item('apple', 'apples', 'the apple')
apple.def_name = "apple"
apple.desc = "The apple looks very tasty. Your stomach rumbles."

knife = Item('knife', 'the knife', 'a knife')
knife.def_name = "knife"
knife.desc = "This might come in handy. This place seems dangerous."

bread = Item('bread', 'the bread')
bread.def_name = 'bread'
bread.desc = "It's so fluffy and warm... as if someone just baked it."

candlestick = Item('candlestick', 'the candlestick', 'candle')
candlestick.def_name = "candlestick"
candlestick.desc = "You could use this to look around."

shoe = Item('shoe', 'the shoe')
shoe.def_name = "shoe"
shoe.desc = "The shoe looks fairly worn out and dusty. This could be used as a weapon, if need be."

book = Item('book', 'the book')
book.def_name = "book"
book.desc = "The book is very thick, could do some damage if thrown hard enough."

sandwich = Item('sandwich', 'the sandwich')
sandwich.def_name = "sandwich"
sandwich.desc = "This sandwich doesn't look moldy...might still be good to eat."

pencil = Item('pencil', 'the pencil')
pencil.def_name = "pencil"
pencil.desc = "There is an engravement on the pencil. It is mostly faded now."

journal = Item('journal', 'the journal')
journal.def_name = "journal"
journal.desc = "The journal says, 'Something weird is going on in my house...but I am not sure what is giving me this feeling."

sheets = Item('sheets', 'sheet', 'the sheets', 'the sheet')
sheets.def_name = "sheets"
sheets.desc = "This can be used to keep warm at night."

banana = Item('banana', 'the banana')
banana.def_name = "banana"
banana.desc = "The banana is just ripe enough to eat."

medicine = Item('medicine', 'the medicine')
medicine.def_name = "medicine"
medicine.desc = "Medicine can be taken for healing."

painting = Item('painting', 'the painting')
painting.def_name = "painting"
painting.desc = "This painting must be worth a fortune. No one would miss it..."

sword = Item('sword', 'the sword')
sword.def_name = "sword"
sword.desc = "This sword is meant for decoration, but also makes for a great weapon."

broom = Item('broom', 'the broom')
broom.def_name = "broom"
broom.desc = "The broom looks almost broken. It doesn't look very useful."

medicine2 = Item('medicine', 'the medicine')
medicine2.def_name = "medicine"
medicine2.desc = "Medicine can be taken for healing."

wallet = Item('wallet', 'the wallet')
wallet.def_name = "wallet"
wallet.desc = "The wallet has money in it. No one needs it."

red_ghost = Item('red ghost', 'the red ghost')
red_ghost.def_name = "red ghost"
red_ghost.desc = "You encounter a red ghost! It looks angry..."

# BAG CONSTRUCTORS
entrance.items = Bag([shoe])
kitchen.items = Bag([apple, knife, bread])
dining.items = Bag([candlestick])
library.items = Bag([book, sandwich])
office.items = Bag([pencil, journal])
master_bed.items = Bag([sheets, banana])
bathroom.items = Bag([medicine])
living.items = Bag([painting, sword])
basement.items = Bag([broom, medicine2, red_ghost])
guest_bed.items = Bag([wallet])
inventory = Bag()

# BINDS
@when('look around')
@when('look')
def look():
	global current_room
	print(current_room)
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)

@when('inventory')
def show_inventory():
	say("You have: ")
	if not inventory:
		say("Nothing")
		return
	for item in inventory:
		say(f"• {item}")

@when('look at mirror')
def look_mirror():
	if current_room == bathroom:
		say("You look at the mirror.")
		time.sleep(1)
		say("An ugly, raggedy ghost looks back at you with vicious eyes.")
	else:
		say("There is no mirror here.")
	

@when('north', dir = 'north')
@when('south', dir = 'south')
@when('east', dir = 'east')
@when('west', dir = 'west')
def go(dir):
	global current_room
	room = current_room.exit(dir)
	if room:
		current_room = room
		say(f"You go {dir}.")
		look()
	else:
		say("There is no exit this way.")


@when('get ITEM')
@when('take ITEM')
def get(item):
	
	if item in current_room.items:
		item = current_room.items.take(item)
		inventory.add(item)
		say("You take the {}.".format(item))
		say(item.desc)
	else:
		say("You don't see a(n) {}.".format(item))
		
@when('give ITEM to RECIPIENT')
def give(item, recipient):
	if item in inventory:
		inventory.take(item)
		print(f"You give the {item} to the {recipient}.")
	
@when('hit TARGET with WEAPON')
def hit(target, weapon):
	if weapon in inventory:
		if target in current_room.items:
			say(f"You attacked the {target} with your {weapon}!")
			alive = playerAttack(target)
			if alive == False:
				current_room.items.take(target)
		else:
			say("There is nothing to hit in this room.")
	else:
		say("You do not have this item in your inventory.")

# JUST BEFORE GAME
current_room = entrance
start()