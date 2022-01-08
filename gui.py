from tkinter import*
import pymysql
import paramiko

#변수
serverip='192.168.68.118'
serverport=3306
id='webmaster'
webpassword='jiho0304'
database='db'

#main title 
root = Tk()
root.title("시험관리프로그램")
root.geometry("540x380")


#student list title
def studentlist():
    print("great")
    stulist = Tk()
    stulist.title("학생목록")
    stulist.geometry("540x380")

    studentlistframe = Frame(stulist)
    studentlistframe.pack()

    studentlistboxscrollbar = Scrollbar(studentlistframe)
    studentlistboxscrollbar.pack(side="right",fill="y")

    studentlistbox = Listbox(studentlistframe, selectmode="extended", height=10,yscrollcommand=studentlistboxscrollbar.set)
    for i in range(1,32):
        studentlistbox.insert(END, str(i) + "day")
    studentlistbox.pack()
    studentlistboxscrollbar.config(command=studentlistbox.yview) 

    stulist.mainloop()
#student list title end



#menu
menu = Menu(root)
menu_manage = Menu(menu, tearoff=0)
menu_manage.add_command(label="학생리스트",command=studentlist)
menu.add_cascade(label="관리", menu=menu_manage)
root.config(menu=menu)

#menu end





#register
ent = Entry(root, width=30)
ent.pack()
ent.insert(0,"학생이름을 넣어주고 등록해주세요")


def btncmd():
    print(ent.get())
    conn = pymysql.connect(host=serverip, port=serverport, user=id, password=webpassword, db=database, charset='utf8')
    cursor = conn.cursor() 
    studentname = ent.get()

    sql = "INSERT INTO student (id) VALUES ('"+ studentname +"')" 

    cursor.execute(sql) 


    conn.commit() 

    conn.close()
    
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(serverip,username="namakblocktechs",password=webpassword)
        print('ssh connected.')
        stdin,stdout,stderr=ssh.exec_command("cd ../../var/www/html/englishtest/testpaper")
        stdin,stdout,stderr=ssh.exec_command("mkdir '"+studentname+"' ")

    
        ssh.close()
    except Exception as err:
        print(err)


btn = Button(root, text="학생등록", command=btncmd)
btn.pack()
#register end


root.mainloop()