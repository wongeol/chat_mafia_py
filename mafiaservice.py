import mafia.mafiadao as dao
import mafia.mafiavo as vo
import random

class service :

    def __init__(self):
        self.dao = dao.mafiaDao()

    def join(self, id, pwd):
        m = self.dao.select(id)

        print(id, pwd)

        if m != None :
            print('이미 존재하는 계정입니다.')
            return False
        else :
            self.dao.insert(vo.mafiavo(id, pwd, 0, 0))
            return True

    def login(self, id, pwd):
        m = self.dao.select(id)

        if m == None :
            print('없는 계정입니다. 회원 가입을 해세요')
        else :
            if pwd == m.pwd :
                print("로그인 성공")
                return True
            else :
                print('비밀 번호가 틀렸습니다.')
                return False

    def setJob(self):
        job = ['mafia', 'citizen', 'citizen', 'citizen', 'police']
        random.shuffle(job)
        return job

    def exsetJob(self):
        job = ['mafia', 'citizen']
        mixjob = random.shuffle(job)
        return job
