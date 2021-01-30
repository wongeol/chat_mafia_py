class player :

    def __init__(self, sock, id, job):
        self.sock = sock
        self.id = id
        self.job = job

    def getSock(self):
        return self.sock

    def setSock(self, sock):
        self.sock = sock

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def getJob(self):
        return self.job

    def setJob(self, job):
        self.job = job
