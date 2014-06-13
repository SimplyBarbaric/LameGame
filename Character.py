class Character(object):
    #defaults for all character statistics
    name = str()
    health = 100
    fullHealth = 100
    attackPower = 30
    fullAttackPower = 30
    magicPower = 30
    fullMagicPower =30
    defense = 30
    fullDefense = 30
    attackList={"attack1":  "attack1","attack2":  "attack2","attack3":  "attack3","attack4":  "attack4"}

    def __init__(self, name, engine, level):
        self.engine = engine
        self.name = name
        self.level = level
        self.setDefaults()
        self.resetToDefaults()

    def resetToDefaults(self):
        self.health = self.fullHealth
        self.magicPower = self.fullMagicPower
        self.attackPower = self.fullAttackPower
        self.defense = self.fullDefense

    #override this in subclasses
    def setDefaults(self):
        #do nothing
        pass

    #override this in subclasses
    def attack1(self, opponent):
        #do nothing
        pass

    #override this in subclasses
    def attack2(self, opponent):
        #do nothing
        pass

    #override this in subclasses
    def attack3(self, opponent):
        #do nothing
        pass

    #override this in subclasses
    def attack4(self, opponent):
        #do nothing
        pass

    #override this in subclasses
    def secretAttack(self, opponent):
        #do nothing
        pass

     #override this in subclasses
    def sayIntroQuote(self):
        #do nothing
        pass

    #override this in subclasses
    def sayQuote(self):
        #do nothing
        pass

     #override this in subclasses
    def sayVictoryQuote(self):
        #do nothing
        pass

     #override this in subclasses
    def sayDefeatQuote(self):
        #do nothing
        pass

    def damageHealth(self, amount):
        damage = amount - (1/2) * self.defense
        if(damage < 0):
            damage = 0
        self.health -= damage
        if self.health <= 0:
            self.health = 0
        return damage

    def reduceDefense(self, amount):
        self.defense -= amount
        if self.defense <= 0:
            self.defense = 0
        return self.defense

    def reduceAttack(self, amount):
        self.attackPower -= amount
        if self.attackPower <= 0:
            self.attackPower = 0
        return self.attackPower

    def reduceMagic(self, amount):
        self.magicPower -= amount
        if self.magicPower<= 0:
            self.magicPower = 0
        return self.magicPower

    def heal(self, amount):
        self.health += amount
        if(self.health > self.fullHealth):
            self.health = self.fullHealth


    def status(self):
        print(""+str(self.name)+" status\nLevel "+str(self.level)+"\nHealth "+str(self.health)+"/"+str(self.fullHealth)+"\nAttack " + str(
              self.attackPower)+"/"+str(self.fullAttackPower)+"\nMagic "+str(self.magicPower)+"/"+str(self.fullMagicPower)+"\nDefense " + str(
              self.defense)+"/"+str(self.fullDefense)+"\n")

    def play(self, command, opponent):
        return self.engine.play(command, self,  opponent)

    def levelUp(self):
        self.level +=1
        self.setDefaults()
        self.resetToDefaults()

