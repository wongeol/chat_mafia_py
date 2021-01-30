import tkinter as tk
import threading, socket

class client :

    client_socket = None
    label = None
    Msg = None
    root = None
    islogin = False
    radiobtn = [None, None, None, None, None]
    var_1 = None
    HOST = 'localhost'
    PORT = 5678

    def menu(self):
        print(self.HOST, self.PORT)
        self.client_socket.connect((self.HOST, self.PORT))

        while True :
            menu = int(input('1.로그인 2.회원가입'))
            if menu == 1 :
                self.login()
                # break
            elif menu == 2 :
                self.join()
                # break
            else :
                print('정확한 번호를 입력하세요')

    def login(self) :
        stat = 'login'
        id = input("id : ")
        pwd = input("pwd : ")

        self.client_socket.sendall(stat.encode())
        self.client_socket.sendall(id.encode())
        self.client_socket.sendall(pwd.encode())

        m = self.client_socket.recv(1024).decode()
        if m == 'True':
            self.islogin == True
            t2 = threading.Thread(target=self.th_read, args=())
            t2.start()

            # t1 = threading.Thread(target=self.sendmsg, args=())
            # t1.start()

            self.ui_init()
            root.mainloop()
        else :
            print("잘못된 계정정보 입니다. 계정을 확인하세요")

    def join(self):
        stat = 'join'
        id = input("계정을 입력하세요")
        pwd = input("비밀번호를 입력하세요")
        pwdcheck = input("비밀번호를 한번 더 입력하세요")
        if str(pwd) == str(pwdcheck) :
            self.client_socket.sendall(stat.encode())
            self.client_socket.sendall(id.encode())
            self.client_socket.sendall(pwd.encode())
        else :
            print("비밀 번호가 일치하지 않습니다.")

        m = self.client_socket.recv(1024).decode()
        if m == 'True':
            print("회원가입에 성공했습니다. 로그인하세요")
        else:
            print("이미 존재하는 계정입니다. 다른 계정을 사용하세요")



    def vote(self) :
        global client_socket

        choice = self.radiovalue.get()

        # print(choice)

        client_socket.sendall(choice)

        #버튼 클릭시 radio button 초기화 : 미구현
        # for i in range(0, len(self.radiobtn)) :
        #     # print(1)
        #     self.radiobtn[i].deselect()

        self.radiobtn1.deselect()
        self.radiobtn2.deselect()
        self.radiobtn3.deselect()
        self.radiobtn4.deselect()

    def send_name(self, name):
        # global client_socket

        msg = self.Msg.get()  # 입력박스에 입력한 텍스트 읽어옴
        client_socket.sendall(name.encode())

    def sendmsg(self, event):
        # global client_socket
        # global Msg

        msg = self.Msg.get()  # 입력박스에 입력한 텍스트 읽어옴
        print(msg)
        self.client_socket.sendall(msg.encode())
        self.Msg.delete(0, tk.END)


    def th_read(self):
        # global client_socket
        #global label

        while True:
            data = self.client_socket.recv(1024)
            msg = data.decode()
            # print(msg)
            # self.label.configure(text=self.label.cget('text') + '\n' + msg)
            # self.label.configure(text=msg)
            self.var_1.set(msg)
            # self.label["text"] = msg

            if msg == '/stop':
                break

        print('서버 메시지 출력 쓰레드 종료')

    def ui_init(self) :
        global root
        global radiovalue
        global Msg
        global var_1



        root = tk.Tk()
        root.geometry('400x500')
        self.frm = tk.Frame(root)
        self.var_1 = tk.StringVar()

        #레이블 생성
        self.label = tk.Label(root, text = '', relief = 'groove', borderwidth = 1, padx = 400, pady = 150,
                              textvariable = self.var_1)

        #입력박스 생성
        self.Msg = tk.Entry(root,width = 100)
        self.Msg.bind('<Return>', self.sendmsg)

        self.frm.pack()
        self.label.pack()
        self.Msg.pack()

        #투표 라디오박스
        self.radiovalue = tk.IntVar()
        list=[('1번 참가자', 1), ('2번 참가자', 2), ('3번 참가자', 3), ('4번 참가자', 4)]

        for txt, val in list:
            self.radiobtn[val] = tk.Radiobutton(root, text=txt, padx=20, variable=self.radiovalue, value=val,
                                                state='disable').pack(anchor='w')

        # self.radiobtn1 = tk.Radiobutton(root, text='1번참가자', padx=20, variable=self.radiovalue, value=1).pack(
        #     anchor='w')
        # self.radiobtn2 = tk.Radiobutton(root, text='2번참가자', padx=20, variable=self.radiovalue, value=2).pack(
        #     anchor='w')
        # self.radiobtn3 = tk.Radiobutton(root, text='3번참가자', padx=20, variable=self.radiovalue, value=3).pack(
        #     anchor='w')
        # self.radiobtn4 = tk.Radiobutton(root, text='4번참가자', padx=20, variable=self.radiovalue, value=4).pack(
        #     anchor='w')

        #투표 버튼
        btn = tk.Button(root, text="투표", command=self.vote, overrelief="solid", state='disable')
        btn.pack()

    def main(self) :
        global client_socket

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # client_socket.connect((HOST, PORT))

        self.menu()


        # if self.islogin == True :
        #     self.ui_init()
        #     root.mainloop()

client = client()
client.main()



