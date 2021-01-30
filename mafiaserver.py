import threading, socket, pymysql, time
import mafia.mafiavo as vo
import mafia.mafiadao as dao
import mafia.mafiaservice as serv
import operator
import mafia.player as player

class server :

    def __init__(self):
        self.serv = serv.service()
        self.player_list = []
        self.index=0


    soc_list = []  # 채팅방. 연결된 클라이언트 소켓

    def playgame(self) :
        print('5명이 모였습니다')


    def client(self, soc, addr):

        self.soc_list.append(soc)  # 방금 접속한 클라이언트 소켓을 리스트에 담음
        jobsetlist = {}
        wait = True


        stat = str(soc.recv(1024).decode())
        id = str(soc.recv(1024).decode())
        pwd = str(soc.recv(1024).decode())

        print(stat, id, pwd)

        #로그인
        if operator.eq(stat, 'login'):

            m = self.serv.login(id, pwd)
            if m == True :
                soc.sendall("True".encode())

                #로그인 성공 시 해당 계정 정보로 객체를 생성하여 리스트에 추가
                print(self.index)
                joblist = self.serv.setJob()

                gplayer = player.player(soc, id, joblist[self.index])
                self.player_list.append(gplayer)

                print(gplayer.getId())
                print(gplayer.getJob())

                #클라이언트 리스트가 추가될때 마다 직업 리스트의 인덱스를 1씩 증가하여 할당하기 위한 code
                if self.index<5 :
                    self.index = self.index + 1
            else :
                soc.sendall("False".encode())

        if operator.eq(stat, 'join'):
            m = self.serv.join(id, pwd)
            if m == True :
                soc.sendall("True".encode())

            else :
                soc.sendall("False".encode())



        if len(self.soc_list) == 2 and len(self.player_list) == 2:
            time.sleep(2)
            print("참가자가 모두 입장하였습니다.")
            for s in self.soc_list :
                s.sendall("5명이 모두 입장하였습니다. 역할을 지정합니다.".encode())

            #    **퇴장했을 경우 소켓 리스트에서 삭제하는 거 구현 필요**

            while True:
                data = soc.recv(1024)
                msg = data.decode()
                if msg == '/stop':
                    soc.sendall(data)  # 본인한테 /stop 전송
                    self.soc_list.remove(soc)
                    msg = str(addr) + ' 님이 퇴장하셨습니다.'
                    for s in self.soc_list:
                        s.sendall(msg.encode())
                    break
                else:
                    print('Received from', addr, msg)
                    msg = str(addr) + ' : ' + msg
                    for s in self.soc_list:
                        s.sendall(msg.encode())
            soc.close()
            print(addr, '퇴장')

    def main(self) :
        HOST = 'localhost'
        PORT = 5678

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 포트 여러번 바인드하면 발생하는 에러 방지
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 바인드:오픈한 소켓에 IP와 PORT 할당
        server_socket.bind((HOST, PORT))

        # 이제 accept할 수 있음을 알림
        server_socket.listen()

        print('server start')

        while True:
            client_socket, addr = server_socket.accept()
            print('Connected by', addr)
            t = threading.Thread(target=self.client, args=(client_socket, addr))
            t.start()

        # self.soc_list.append(client_socket)  # 방금 접속한 클라이언트 소켓을 리스트에 담음

        server_socket.close()

server = server()
server.main()
