class Enemy:
    def __init__(self, name="Enemy"):
        self.name = name
        self.stamina = 30
        self.hp = 20
        self.uron=10
class Wither(Enemy):
    def __init__(self, name="wither"):
        self.name = name
        self.manna =200

class RedWither(Wither) :
    def __init__(self, name=" RedWithe"):
        self.name = name
        self.redmanna = 10

class tigr(Enemy):
    def __init__(self, name=" tigr"):

        self.name = name
    self.ostrotakoghte=3

class magicktigr(tigr):

    def __init__(self, name=" magicktigr"):
        self.name = name
        self.mannaorange = 333333
