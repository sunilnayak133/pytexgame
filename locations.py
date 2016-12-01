#to implement locations and movement between them

#first I define a class "location"
#Every location will be an object of this class.
class location:
	#define two variables for the class location
	#its name
	name = "placeaholdername"
	#and the text that's displayed the first time someone enters it
	firstTime = "placeholderFirstTime"
	visited = False

	#next, we need dlists (which is my way of naming lists which contain
	#all the possible locations reachable from a location by moving in any direction
	#eg. n, ne, s, se, e, nw, w, sw)

	#when initialized with just a name, the location gets a name and an empty dlist
	def __init__(self, name):
		self.name = name
		self.dlist = {}

	#there has to be a way to set a location object's dlist.
	def setdlist(self, dlist):
		self.dlist = dlist
	#and also a way to set its firstTime description
	def setfirst(self, first):
		self.firstTime = first

#now I define a player who has to have a current location (and maybe a previous location, a score, etc)
class player:
	#initialize a score variable to keep track of the score (if needed)
	score = 0
	#initialize a location variable to keep track of where the player is.
	location = None
	goal = None

	def __init__(self, start, goal):
		self.location = start
		self.goal = goal
		self.score = 0

	def checkgoal(self):
		if self.location == self.goal:
			print "You have reached the goal!"
			return True
		else:
			return False

	#when a player wants to change their location by moving in a direction, we call this method.
	def changeloc(self, dir):
		#change location only if that location is present in the current location's dlist
		if dir in self.location.dlist:
			self.location = self.location.dlist[dir]
		#else, print generic error message
		else:
			print "Nope, can't go there!"

#NOTE THAT THIS VERSION ASSUMES CORRECT MAPS ARE INPUT.
#IT IS YOUR RESPONSIBILITY TO ENTER CORRECT MAPS IN, ELSE THE GAME BREAKS.
#format for input file:
#start_location,goal_location
#other_location 1
#other_location 2
#. . .
#. . .
#$$$
#location_name
#location first time text (leave blank if nothing)
#dir:location_name,dir:location name, ...
#. . .
#. . .
#$$$
#note, each dir should occur only once.

f = open('locmap.txt','r')

start = f.readline()
start = start.split(',')
end = start[1][:-1]
start = start[0]
#print "Start: %s, End:%s" % (start, end)

stloc = location(start)
enloc = location(end)
locationlist = [stloc, enloc]
namelist = [start, end]

#input all location names
while(True):
	loc = f.readline()
	loc = loc[:-1]
	if('$' in loc):
		break
	L = location(loc)
	locationlist.append(L)
	namelist.append(loc)
	#print loc


#time to take map in, now. 
while(True):
	try:
		loc = f.readline()
		loc = loc[:-1]
		if('$' in loc):
			break
		li = namelist.index(loc)
		first = f.readline()
		dliststr = f.readline()[:-1].split(',')
		dlist = {}
		for i in dliststr:
			i=i.split(':')
			dlist[i[0]] = locationlist[namelist.index(i[1])]
		L = locationlist[li]
		L.setfirst(first)
		L.setdlist(dlist)
	except(EOFError):
		break

'''
#The old input method
start = raw_input()
print start
start = start.split(',')
end = start[1]
start = start[0]
#print "Start: %s, End:%s" % (start, end)

stloc = location(start)
enloc = location(end)
locationlist = [stloc, enloc]
namelist = [start, end]

#input all location names
while(True):
	loc = raw_input()
	if(loc == '$$$'):
		break
	L = location(loc)
	locationlist.append(L)
	namelist.append(loc)


#time to take map in, now. 
while(True):
	try:
		loc = raw_input()
		if(loc == '$$$'):
			break
		li = namelist.index(loc)
		first = raw_input()
		dliststr = raw_input().split(',')
		dlist = {}
		for i in dliststr:
			i=i.split(':')
			dlist[i[0]] = locationlist[namelist.index(i[1])]
		L = locationlist[li]
		L.setfirst(first)
		L.setdlist(dlist)
	except(EOFError):
		break
'''
#print locationlist
#print namelist
#print stloc, enloc

#eof = raw_input()
#declare player
plyr = player(stloc, enloc)
inp_list = ['n','s','e','w','ne','nw','se','sw']
#Now start taking player input:
print "Welcome. You are here: %s" % (stloc.name)
print stloc.firstTime
stloc.visited = True
while(True):
	print "Where do you wanna go next?"
	dir = raw_input('>')
	if dir not in inp_list:
		print "I'm not sure where that is"
	else:
		print "Going %s..." % (dir)
		plyr.changeloc(dir)
		if plyr.checkgoal() == False:
			print "You are now at %s" % plyr.location.name
			if plyr.location.visited == False:
				print plyr.location.firstTime
				plyr.location.visited = True
		else:
			#print "You have reached the goal!"
			break




