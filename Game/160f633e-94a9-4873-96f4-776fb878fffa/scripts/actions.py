Scarlett = ("Scarlett", "62a2ba76-9872-481b-b8fc-ec35447ca640")
Mickey = ("Mickey", "38d55f36-04d7-4cf9-a496-06cb84de567d")
Tony = ("Tony", "e9a419ff-5154-41cf-b84f-95149cc19a2a")
Jack = ("Jack", "f24eb0c4-8405-4599-ba80-95bc009ae9fb")
Marcel = ("Marcel", "53f20b83-6292-4017-abd0-511efdaf710d")
Stitches = ("Stitches", "6987d1a6-55ab-4ced-bbec-4e5b3490a40e")


def sitstand(group, x = 0, y = 0):
    isstanding = me.getGlobalVariable("standing")
    if isstanding == "1":
        notify("{} is now sitting.".format(me))
        me.setGlobalVariable("standing","0")
    else:
        notify("{} is now standing.".format(me))
        me.setGlobalVariable("standing","1")

def ssstatus(group, x = 0, y = 0):
    notify("Getting sit stand")
    for p in players:
        gv = p.getGlobalVariable("standing")
        if gv == "1":
            notify("{} is standing.".format(p))
        else:
            notify("{} is sitting.".format(p))

def becomedealer(group,x=0,y=0):
    notify("{} is now dealer.".format(me))
    setGlobalVariable("dealer",me._id)

def whosdealer(group,x=0,y=0):
    ret = getGlobalVariable("dealer")
    notify("{} dealer num".format(ret))
    ret = int(ret)
    notify("{} dealer num".format(ret))
    for p in players:
        if p._id == ret:
            notify("{} is dealer.".format(p))
            break

def rolldice(group, x = 0, y = 0):
    mute()
    n = rnd(1, 6)
    notify("{} rolls {} on a 6-sided die.".format(me, n))

def flipcoin(group, x = 0, y = 0):
    mute()
    n = rnd(1, 2)
    if n == 1:
      notify("{} flips heads.".format(me))
    else:
      notify("{} flips tails.".format(me))
	  
def listplayers(group, x = 0, y = 0):
    notify("{}".format(players))

def interrupt(group, x = 0, y = 0):
    notify('{} interrupts the game.'.format(me))

def passturn(group, x = 0, y = 0):
    notify('{} passes.'.format(me))

def tap(card, x = 0, y = 0):
  mute()
  card.orientation ^= Rot90
  if card.orientation & Rot90 == Rot90:
    notify('{} turns {} sideways'.format(me, card))
  else:
    notify('{} turns {} upright'.format(me, card))

def flip(card, x = 0, y = 0):
    mute()
    if card.isFaceUp == True:
      notify("{} flips {} face down.".format(me, card))
      card.isFaceUp = False
    else:
      card.isFaceUp = True
      notify("{} flips {} face up.".format(me, card))

def discard(card, x = 0, y = 0):
  mute()
  src = card.group
  fromText = " from the table" if src == table else " from their " + src.name
  card.moveTo(shared.Discard)
  notify("{} discards {}{}.".format(me, card, fromText))

def highlightcard(card, x = 0, y = 0):
  mute()
  if card.highlight == "#ff0000":
    card.highlight = None
    notify('{} removes highlight from {}'.format(me, card))
  else:
    card.highlight = "#ff0000"
    notify('{} highlights {}'.format(me, card))

def draw(group, x = 0, y = 0):
    if len(shared.goons) == 0: return
    mute()
    shared.goons[0].moveTo(me.hand)
    notify("{} draws a card.".format(me))

def drawMany(group, count = None):
    if len(shared.goons) == 0: return
    mute()
    if count == None: count = askInteger("Draw how many cards?", 7)
    for c in shared.goons.top(count): c.moveTo(me.hand)
    notify("{} draws {} cards.".format(me, count))

def dealMany(group, count=None):
    dealerid = int(getGlobalVariable("dealer"))
    if me._id != dealerid:
        whisper("You are not the dealer player.")
        return
    if len(shared.goons) == 0: return
    mute()
    if count == None: count = askInteger("Deal how many cards?", 5)
    for num in range(count):
        for p in players:
            standing = int(p.getGlobalVariable("standing"))
            if standing == 0:
                notify("Dealing {} a card.".format(p))
                for c in shared.goons.top(1): c.moveTo(p.hand)

def dealManyToTable(group, x = 0, y = 0, count=None):
    dealerid = int(getGlobalVariable("dealer"))
    if me._id != dealerid:
        whisper("You are not the dealer player.")
        return
    if len(shared.goons) == 0: return
    mute()
    if count == None: count = askInteger("Deal how many cards to table?", 5)
    for c in shared.goons.top(count): 
        c.moveTo(table)
    notify("Dealing {} cards to table.".format(count))

def dealManyToTableDown(group,x = 0, y = 0, count=None):
    dealerid = int(getGlobalVariable("dealer"))
    if me._id != dealerid:
        whisper("You are not the dealer player.")
        return
    if len(shared.goons) == 0: return
    mute()
    if count == None: count = askInteger("Deal how many cards to table face down?", 5)
    for c in shared.goons.top(count): 
        c.moveTo(table)
        c.isFaceUp = False
    notify("Dealing {} cards to table face down.".format(count))

def drawManyDown(group, count = None):
    if len(shared.goons) == 0: return
    mute()
    if count == None: count = askInteger("Draw how many cards?", 7)
    for c in shared.goons.top(count):
        c.moveTo(me.hand)
        c.isFaceUp = False
    notify("{} draws {} cards face down.".format(me, count))

def mill(group, count = None):
    if len(shared.goons) == 0: return
    mute()
    if count == None: count = askInteger("Mill how many cards?", 1)
    for c in shared.goons.top(count): c.moveTo(shared.Discard)
    notify("{} mills the top {} cards from the Deck.".format(me, count))

def shuffle(group, x = 0, y = 0):
   mute()
   shared.goons.shuffle()
	 
def shufflegang(group, x = 0, y = 0):
   mute()
   shared.gang.shuffle()  
   
def Setup(group,x=0,y=0):
	mute()
	shared.Goons.shuffle()
	shared.Gang.shuffle()   
	 
def shuffleIntoDeck(group, x = 0, y = 0):
    mute()
    for c in group: c.moveTo(shared.goons)
    shared.goons.shuffle()
    notify("{} shuffled the discard pile into the deck.".format(me))

StandardMarker = ("Marker", "40bba10f-82e5-4f7e-986b-e9c850524f88")

def addanymarker(cards, x = 0, y = 0):
    mute()
    marker, quantity = askMarker()
    if quantity == 0: return
    for card in cards:
      card.markers[marker] += quantity
      notify("{} adds {} {} counters to {}.".format(me, quantity, marker[0], card))

def addmarker(card, x = 0, y = 0):
    mute()
    card.markers[StandardMarker] += 1
    notify("{} adds a marker to {}.".format(me, card))

def removemarker(card, x = 0, y = 0):
    mute()
    card.markers[StandardMarker] -= 1
    notify("{} removes a marker from {}.".format(me, card))
	
def addScarlett(card, x = 1, y = 1):
    addToken(card, Scarlett)
    
def addMickey(card, x = 0, y = 0):
    addToken(card, Mickey)
    
def addTony(card, x = 0, y = 0):
    addToken(card, Tony)  

def addJack(card, x = 0, y = 0):
    addToken(card, Jack)  

def addMarcel(card, x = 0, y = 0):
    addToken(card, Marcel)  

def addStitches(card, x = 0, y = 0):
    addToken(card, Stitches)  

def addTurn(card, x=0, y=0):
	if isFirstPlayerToken([card]):
		shared.counters['Round'].value += 1

def addToken(card, tokenType):
	mute()
	card.markers[tokenType] += 1
	notify("{} adds a {} to '{}'".format(me, tokenType[0], card))
	
def subScarlett(card, x = 0, y = 0):
    subToken(card, Scarlett)

def subMickey(card, x = 0, y = 0):
    subToken(card, Mickey)

def subTony(card, x = 0, y = 0):
    subToken(card, Tony)
	
def subJack(card, x = 0, y = 0):
    subToken(card, Jack)  

def subMarcel(card, x = 0, y = 0):
    subToken(card, Marcel)  

def subStitches(card, x = 0, y = 0):
    subToken(card, Stitches)  

def subTurn(card, x=0, y=0):
	if isFirstPlayerToken([card]) and shared.counters['Round'].value > 0:
		shared.counters['Round'].value -= 1

def subToken(card, tokenType):
    mute()
    card.markers[tokenType] -= 1
    notify("{} removes a {} from '{}'".format(me, tokenType[0], card))
	
def PlayCardFaceDown(card, x = 0, y = 0):
    mute()
    card.isFaceUp = False
    card.moveToTable(0, 0, True)
    card.peek()