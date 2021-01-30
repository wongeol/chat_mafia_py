class mafiavo :
    def __init__(self, id, pwd, win, lose):
        self.id = id
        self.pwd = pwd
        self.win = win
        self.lose = lose

    def getId(self):
        return self.id

    def setIp(self, id):
        self.id = id

    def getPwd(self):
        return self.pwd

    def setPwd(self, pwd):
        self.pwd = pwd

    def getWin(self):
        return self.win

    def setWin(self, win):
        self.win =win

    def getLose(self):
        return self._lose

    def setLose(self, lose):
        self._lose = lose



