#loadingdots = str
f = open("allgames.txt")
gametext = f.read()
print("⚾|MLB Baseball Database|⚾")
print("\nloading database...")
#print(gametext)
#allgames = list(games.split(","))
alllines = gametext.split('\n')
alllines.pop(0)
alllines.pop(-1) 
#print(alllines)


class Game:

    def __init__(self, date, homeTeam, awayTeam, homeScore, awayScore):
      self.homeTeam = homeTeam.strip()
      self.awayTeam = awayTeam.strip()
      self.homeScore = homeScore.strip()
      self.awayScore = awayScore.strip()
      month = date[4]+date[5]
      day = date[6]+date[7]
      year = date[0]+date[1]+date[2]+date[3]
      date = month + "." + day + "." + year
      self.date = date
      #print(self.homeTeam)
    
    def getKey(self):
      key = self.homeTeam + "," + self.awayTeam + "," + self.homeScore + "," + self.awayScore
      return key
    
    def printKey(self):
      organizedKey = self.homeTeam + ":" + self.homeScore + " - " + self.awayTeam + ":" + self.awayScore 
      return organizedKey

    def __str__(self):
      return "\n" + self.date + " -> " + self.printKey() + "\n"

    def __repr__(self):
      return self.__str__()

class HashTable:
    def __init__(self, size):
        self.size = size
        self.games = []
        for i in range(self.size):
            self.games.append([])

    def hf(self, key):
        #print(self.size)
        #print(hash(key))
        return abs(hash(key)) % self.size

    def insert(self, game):
        index = self.hf(game.getKey())
        #print(game.getKey(), index)
        self.games[index].append(game)
        pass

    def lookup(self, key):
        #print(key)
        index = self.hf(key)
        #print("index of", key, " is ", index)
        result = []
        none = "None Found"
        #print(self.games[index])
        for game in self.games[index]:
            #print(game.getKey())
            if key == game.getKey():
                result.append(game)
            else:
                result.append(none)
        print("\n" + "Games- ")
        for game in result:
          print(game)
#"\n" + "Games- ", 
length = len(alllines)
length = int(length)
#print(type(length))
#print(allgames)
#print(length)
#Units are mismatched, number of characters does not matter, number of lines is number of entries.
#Split the file by lines
i = 0
hashTable = HashTable(length)
for i in range(length):
    values = alllines[i].split(",")
    game = Game(values[0], values[1], values[2], values[3], values[4])
    #print(values)
    #print("%s -> %d" % (game.getKey(), hash(game.getKey())))
    hashTable.insert(game) 
while(True):
    userInput = input("\nWhat game would you like to find? \nRequest in format = Team 1, Team2, Score1, Score2:")
    #"PHI, TBA, 0, 5"
    providedKey = userInput.replace(" ", "")
    #print(hash(providedKey))
    #print(hash(providedKey))
    #print(hash(providedKey))
    #print(hash(providedKey))
    hashTable.lookup(providedKey)
    #print(providedKey)
    #print(hashTable.games)