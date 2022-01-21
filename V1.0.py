import tkinter as tk  # 使用Tkinter前需要先导入
import logging
from   tkinter.constants import ALL, TRUE
import serial
from serial.serialutil import PortNotOpenError
import serial.tools.list_ports
import time
import threading

# Configure file
logging.basicConfig(filename='比赛记录日志.log', filemode='a',
                    format='%(levelname)s -> %(asctime)s: %(message)s', level=logging.DEBUG)
 
# logging.warning("Warning log.")
# logging.info("Info log.")
# logging.debug("Debug log.")


ser1 = serial.Serial() # 串口对象
ser_state = False # 用于指示串口是否打开
truevalue = 0
str1 = "fuck"
str2 = "fuck"

window = tk.Tk()
window.title('RoboMaster校内赛裁判系统V1.0')
window.geometry('1024x768')  # 这里的乘是小x
window.configure(bg='Gray')

# windowlog = tk.Tk()
# windowlog.title('比赛实时记录')
# window.geometry('640x480')
# windowlog.configure(bg='Black')
# l = tk.Label(window, text='你好！this is Tkinter', bg='green', font=('Arial', 12), width=30, height=2)
# l.pack()    # Label内容content区域放置位置，自动调节尺寸

counter = 0
def change_bps_115200():
    global counter
    counter = 115200
    l.config(text=str(counter))
    logging.info("串口波特率被设置为115200.")
    print("串口波特率被设置为115200.")
def change_bps_38400():
    global counter
    counter = 38400
    l.config(text=str(counter))
    logging.info("串口波特率被设置为38400.")
def change_bps_19200():
    global counter
    counter = 19200
    l.config(text=str(counter))
    logging.info("串口波特率被设置为19200.")
def change_bps_9600():
    global counter
    counter = 9600
    l.config(text=str(counter))
    logging.info("串口波特率被设置为9600.")
def change_bps_4800():
    global counter
    counter = 4800
    l.config(text=str(counter))
    logging.info("串口波特率被设置为4800.")
def None_Move():
    logging.info("空操作")
def Start_Game():
    global RHP
    global BHP
    RHP = 8
    RED_HP_1.set('RED_HP = '+str(RHP))
    BHP = 8
    BLUE_HP_1.set('BLUE_HP = '+str(BHP))
    GAME_NOW.set('比赛开始')
    logging.info("-------------------------------比赛开始-----------------------------------")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-------------------------------比赛开始-----------------------------------")
    ser1.write('1'.encode())


def Finish_Game():
    GAME_NOW.set('比赛结束')
    logging.info("-------------------------------比赛手动结束-----------------------------------")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-------------------------------比赛手动结束-----------------------------------")
    ser1.write('4'.encode())

def ChangeColor():
    l.configure(bg='green')

def reset_hp_R():
    global RHP
    RHP = 8
    RED_HP_1.set('RED_HP = '+str(RHP))
    logging.info("-------------------------------红方发生裁判血量重置-----------------------------------")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-------------------------------红方发生裁判血量重置-----------------------------------")
    ser1.write('3'.encode())

def reset_hp_B():
    global BHP
    BHP = 8
    BLUE_HP_1.set('BLUE_HP = '+str(BHP))
    logging.info("-------------------------------蓝方发生裁判血量重置-----------------------------------")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-------------------------------蓝方发生裁判血量重置-----------------------------------")
    ser1.write('4'.encode())


RED_HP_1  = tk.StringVar()
BLUE_HP_1 = tk.StringVar()
def decrease_hp_R():
    global RHP
    RHP = RHP - 1
    if RHP <= 0:
        RHP = 0
    RED_HP_1.set('RED_HP = '+str(RHP))
    logging.info("-------------------------------红方发生裁判扣血-----------------------------------"+"当前血量 = "+str(RHP))
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-------------------------------红方发生裁判扣血-----------------------------------"+"当前血量 = "+str(RHP))
    ser1.write('9'.encode())



def decrease_hp_B():
    global BHP
    BHP = BHP - 1
    if BHP <= 0:
        BHP = 0
    BLUE_HP_1.set('BLUE_HP = '+str(BHP))
    logging.info("-------------------------------蓝方发生裁判扣血-----------------------------------"+"当前血量 = "+str(BHP))
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-------------------------------蓝方发生裁判扣血-----------------------------------"+"当前血量 = "+str(BHP))
    ser1.write('8'.encode())


GAME_NOW= tk.StringVar()    

TIME= tk.StringVar()    

# def GAME_STATE_START():
#     GAME_NOW.set('比赛暂停')
def RESET_ALL():
    global RHP
    global BHP
    RHP = 8
    RED_HP_1.set('RED_HP = '+str(RHP))
    BHP = 8
    BLUE_HP_1.set('BLUE_HP = '+str(BHP))
    logging.info("-------------------------------比赛重置-----------------------------------")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-------------------------------比赛重置-----------------------------------")
    ser1.write('5'.encode())

def Blue_lose():
    GAME_NOW.set('比赛结束')
    logging.info("-------------------------------比赛手动结束-----------------------------------")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-------------------------------比赛手动结束-----------------------------------")
    ser1.write('6'.encode())

def Red_lose():
    GAME_NOW.set('比赛结束')
    logging.info("-------------------------------比赛手动结束-----------------------------------")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-------------------------------比赛手动结束-----------------------------------")
    ser1.write('7'.encode())

def Red_build_poweroff():
    logging.info("红方工程断电")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-红方工程断电-")
    ser1.write('A'.encode())
def Red_build_poweron():
    logging.info("红方工程上电")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-红方工程上电-")
    ser1.write('E'.encode())

def Red_stantard_poweroff():
    logging.info("红方步兵断电")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-红方步兵断电-")
    ser1.write('B'.encode())
def Red_stantard_poweron():
    logging.info("红方步兵上电")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-红方步兵上电-")
    ser1.write('F'.encode())

def Blue_build_poweroff():
    logging.info("蓝方工程断电")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-蓝方工程断电-")
    ser1.write('C'.encode())
def Blue_build_poweron():
    logging.info("蓝方工程上电")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-蓝方工程上电-")
    ser1.write('G'.encode())

def Blue_stantard_poweroff():
    logging.info("蓝方步兵断电")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-蓝方步兵断电-")
    ser1.write('D'.encode())
def Blue_stantard_poweron():
    logging.info("蓝方步兵上电")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-蓝方步兵上电-")
    ser1.write('H'.encode())

def Blue_energy_off():
    logging.info("蓝方能量机关关")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-蓝方能量机关关-")
    ser1.write('Q'.encode())
def Blue_energy_on():
    logging.info("蓝方能量机关开")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-蓝方能量机关开-")
    ser1.write('R'.encode())

def Red_energy_off():
    #TIME.set('str(str2)')
    logging.info("红方能量机关关")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-红方能量机关关-")
    ser1.write('M'.encode())
def Red_energy_on():
    logging.info("红方能量机关开")
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"-红方能量机关开-")
    ser1.write('N'.encode())

def recv(serial):
    while True:
        data = serial.read_all()
        if data == '':
            continue
        else:
            break
        sleep(0.02)
    return data

      

RHP = 8
BHP = 8
l = tk.Label(window, text='----------------------------------RoboMaster校内赛裁判系统V1.0----------------------------------', bg='Silver')
l.pack()
RED_HP = tk.Label(window, width=25 , font=('Arial', 14),fg = 'white', height=1, textvariable = RED_HP_1,bg='red').place(x=1024, y=30,anchor='ne')
BLUE_HP = tk.Label(window, width=25, height=1, font=('Arial', 14),fg = 'white',textvariable = BLUE_HP_1,   bg='blue').place(x=0, y=30,anchor='nw')

Start_Game
# a.place(x=0, y=0,anchor='center')
# a.pack(side = 'right')
reset_hp_B = tk.Button(window, text='RESET HP', font=('Arial', 12), width=15, height=1,bg = 'white', command = reset_hp_B).place(x = 0 ,y = 60,anchor='nw')
reset_hp_R = tk.Button(window, text='RESET HP', font=('Arial', 12), width=15, height=1,bg = 'white', command = reset_hp_R).place(x = 1024 ,y = 60,anchor='ne')

decrease_hp_B = tk.Button(window, text='蓝方基地扣血', font=('Arial', 12), width=12, height=1,bg = 'white', command = decrease_hp_B).place(x = 150 ,y = 60,anchor='nw')
decrease_hp_R = tk.Button(window, text='红方基地扣血', font=('Arial', 12), width=12, height=1,bg = 'white', command = decrease_hp_R).place(x = 874 ,y = 60,anchor='ne')

Blue_lose = tk.Button(window, text='蓝方判负', font=('Arial', 12), width=15, height=1,bg = 'white', command = Blue_lose).place(x = 140 ,y = 100,anchor='ne')
Red_lose  = tk.Button(window, text='红方判负', font=('Arial', 12), width=15, height=1,bg = 'white', command = Red_lose).place(x = 1024 ,y = 100,anchor='ne')

Blue_engineer_POWEROFF = tk.Button(window, text='蓝方工程断电', font=('Arial', 12), width=15, height=1,bg = 'white', command = Blue_build_poweroff).place(x = 140 ,y = 140,anchor='ne')
Blue_engineer_POWERON = tk.Button(window, text='蓝方工程上电', font=('Arial', 12), width=15, height=1,bg = 'white', command = Blue_build_poweron).place(x = 300 ,y = 140,anchor='ne')

Blue_stan_POWEROFF = tk.Button(window, text='蓝方步兵断电', font=('Arial', 12), width=15, height=1,bg = 'white', command = Blue_stantard_poweroff).place(x = 140 ,y = 180,anchor='ne')
Blue_stan_POWERON = tk.Button(window, text='蓝方步兵上电', font=('Arial', 12), width=15, height=1,bg = 'white', command = Blue_stantard_poweron).place(x = 300 ,y = 180,anchor='ne')

Red_engineer_POWEROFF = tk.Button(window, text='红方工程断电', font=('Arial', 12), width=15, height=1,bg = 'white', command = Red_build_poweroff).place(x = 864 ,y = 140,anchor='ne')
Red_engineer_POWERON = tk.Button(window, text='红方工程上电', font=('Arial', 12), width=15, height=1,bg = 'white', command = Red_build_poweron).place(x = 1024 ,y = 140,anchor='ne')

Red_stan_POWEROFF = tk.Button(window, text='红方步兵断电', font=('Arial', 12), width=15, height=1,bg = 'white', command = Red_stantard_poweroff).place(x = 864 ,y = 180,anchor='ne')
Red_stan_POWERON = tk.Button(window, text='红方步兵上电', font=('Arial', 12), width=15, height=1,bg = 'white', command = Red_stantard_poweron).place(x = 1024 ,y = 180,anchor='ne')

Red_Energy_On = tk.Button(window, text='蓝方能量机关激活', font=('Arial', 12), width=15, height=1,bg = 'white', command = Blue_energy_on).place(x = 140 ,y = 220,anchor='ne')
Red_Energy_Off = tk.Button(window, text='蓝方能量机关关闭', font=('Arial', 12), width=15, height=1,bg = 'white', command = Blue_energy_off).place(x = 300 ,y = 220,anchor='ne')

Blue_Energy_On = tk.Button(window, text='红方能量机关激活', font=('Arial', 12), width=15, height=1,bg = 'white', command = Red_energy_on).place(x = 864 ,y = 220,anchor='ne')
Blue_Energy_Off = tk.Button(window, text='红方能量机关关闭', font=('Arial', 12), width=15, height=1,bg = 'white', command = Red_energy_off).place(x = 1024 ,y = 220,anchor='ne')

# Red_lose  = tk.Button(window, text='红方判负', font=('Arial', 12), width=15, height=1,bg = 'white', command = Red_lose).place(x = 1024 ,y = 100,anchor='ne')


GAME_STATE_1 = tk.Label(window, width=25, height=1, font=('Arial', 14),fg = 'black',textvariable = GAME_NOW,   bg='Gold').pack(side = 'top')

TIME = tk.Label(window, width=25, height=1, font=('Arial', 14),fg = 'black',textvariable = TIME,   bg='White').pack(side = 'bottom')

x = tk.Button(window, text='START', font=('Arial', 13), width=10, height=1,bg = 'green', command = Start_Game)
# b.place(x=256, y=192, anchor='nw')
x.pack(side='top')
c = tk.Button(window, text='RESET', font=('Arial', 13), width=10, height=1, command = RESET_ALL)
# b.place(x=256, y=192, anchor='nw')
c.pack(side='top')
d = tk.Button(window, text='STOP', font=('Arial', 13), width=10, height=1, bg = 'red',command = Finish_Game)
# b.place(x=256, y=192, anchor='nw')
d.pack(side='top')


def Open_Port(num):
    global ser1
    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"准备打开串口"+str(num))
    ser1 = serial.Serial(str(num),9600)
    ser1.open
    ser1.write('COM DETECTED!\n'.encode())



#choice = 'case1'                         # 获取选择
#switch.get(choice, default)()            # 执行对应的函数，如果没有就执行默认的函数

Port_list = list(serial.tools.list_ports.comports())
# 获得所有可用的串口号
def GetComPortList():
    # filemenu2.delete(5)
    # filemenu2.delete(4)
    # filemenu2.delete(3)
    # filemenu2.delete(2)
    # filemenu2.delete(1)
    # filemenu2.delete(0)

    print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"搜索串口")

    port_list = list(serial.tools.list_ports.comports())
    Port_list = port_list
    if len(port_list) == 0:
       filemenu2.add_command(label='None', command=None_Move)
       logging.info("未搜索到串口")
       print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"未搜索到串口")

       #port_list[0] = '找不到串口'
    else:
        for i in range(0,len(port_list)):
            if i == 0 :
                filemenu2.add_command(label=str(port_list[i][0]),command=lambda: Open_Port(port_list[0][0]))
            if i == 1 :
                filemenu2.add_command(label=str(port_list[i][0]),command=lambda: Open_Port(port_list[1][0]))
            if i == 2 :
                filemenu2.add_command(label=str(port_list[i][0]),command=lambda: Open_Port(port_list[2][0]))
            if i == 3 :
                filemenu2.add_command(label=str(port_list[i][0]),command=lambda: Open_Port(port_list[3][0]))
            if i == 4 :
                filemenu2.add_command(label=str(port_list[i][0]),command=lambda: Open_Port(port_list[4][0]))
            if i == 5 :
                filemenu2.add_command(label=str(port_list[i][0]),command=lambda: Open_Port(port_list[5][0]))
        

 #          filemenu2.config(label=str(port_list[i][0]),command = Open_Port )
           # SWITCH_COM(str(port_list[i][0]))
            print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+"-->"+"串口号与名称为："+str(port_list[i]))
        
        
            # print(port_list[i])
            pass
    return port_list


menubar = tk.Menu(window)
# 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
filemenu = tk.Menu(menubar, tearoff=0)
filemenu2 = tk.Menu(menubar, tearoff=0)
filemenu3 = tk.Menu(menubar, tearoff=0)

menubar.add_cascade(label='串口选择', menu=filemenu2)
menubar.add_cascade(label='波特率设置', menu=filemenu)
menubar.add_cascade(label='串口操作', menu=filemenu3)

# 创建第二级菜单，即菜单项里面的菜单
#创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
filemenu.add_command(label='115200', command=change_bps_115200)
filemenu.add_command(label='38400', command=change_bps_38400) 
filemenu.add_command(label='19200', command=change_bps_19200)
filemenu.add_command(label='9600', command=change_bps_9600) 
filemenu.add_command(label='4800', command=change_bps_4800) 
#创建一个Edit菜单项（默认不下拉，下拉内容包括Cut，Copy，Paste功能项）
#创建第三级菜单命令，即菜单项里面的菜单项里面的菜单命令（有点拗口，笑~~~）
# selectmenu.add_command(label='COM', command=change_bps_115200)
filemenu3.add_command(label='搜索串口', command=GetComPortList) 
# def ReadUART():#接收串口数据
#          while(TRUE):
#             try:
#                 str2 = ser1.readline()  # 串口读取数据
#                 print(str2)  
#             except:  #串口有异常退出
#                 str1 = "shit"

# ReadUARTThread = threading.Thread(target=ReadUART)#多线程
# ReadUARTThread.start()

window.config(menu=menubar)
window.mainloop()