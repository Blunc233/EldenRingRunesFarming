import win32con
import win32api
import time
import win32gui
print('请进入游戏后（推荐无边框窗口化运行）打开地图传送至王朝断崖赐福点，启动脚本前切勿走动，切换到此程序\n')
if input('按下Enter以继续'):
    pass
print('ok')
maxnum = int(input('请输入重复刷取次数（整数）: '))
key_map = {
    'CTRL': 17,
    '0': 49,
    '1': 50,
    '2': 51,
    '3': 52,
    '4': 53,
    '5': 54,
    '6': 55,
    '7': 56,
    '8': 57,
    '9': 58,
    'A': 65,
    'B': 66,
    'C': 67,
    'D': 68,
    'E': 69,
    'F': 70,
    'G': 71,
    'H': 72,
    'I': 73,
    'J': 74,
    'K': 75,
    'L': 76,
    'M': 77,
    'N': 78,
    'O': 79,
    'P': 80,
    'Q': 81,
    'R': 82,
    'S': 83,
    'T': 84,
    'U': 85,
    'V': 86,
    'W': 87,
    'X': 88,
    'Y': 89,
    'Z': 90 }

def key_down(key):
    '''
    函数功能：按下按键
    参    数：key:按键值
    '''
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), 0, 0)


def key_up(key):
    '''
    函数功能：抬起按键
    参    数：key:按键值
    '''
    key = key.upper()
    vk_code = key_map[key]
    win32api.keybd_event(vk_code, win32api.MapVirtualKey(vk_code, 0), win32con.KEYEVENTF_KEYUP, 0)


def key_press(key):
    '''
    函数功能：点击按键（按下并抬起）
    参    数：key:按键值
    '''
    key_down(key)
    time.sleep(0.05)
    key_up(key)


def move(x, y):
    '''
    函数功能：移动鼠标到指定位置
    参  数：x:x坐标
         y:y坐标
    '''
    win32api.SetCursorPos((x, y))


def get_cur_pos():
    '''
    函数功能：获取当前鼠标坐标
    '''
    p = {
        'x': 0,
        'y': 0 }
    pos = win32gui.GetCursorPos()
    p['x'] = pos[0]
    p['y'] = pos[1]
    return p


def left_click():
    '''
    函数功能：鼠标左键点击
    '''
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def right_click():
    '''
    函数功能：鼠标右键点击
    '''
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN | win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def left_down():
    '''
    函数功能：鼠标左键按下
    '''
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)


def left_up():
    '''
    函数功能：鼠标左键抬起
    '''
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


def right_down():
    '''
    函数功能：鼠标右键按下
    '''
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)


def right_up():
    '''
    函数功能：鼠标右键抬起
    '''
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)


def go_first_target():
    key_down('W')
    time.sleep(3.7)
    key_up('W')
    time.sleep(0.5)
    key_down('A')
    time.sleep(0.75)
    key_up('A')
    time.sleep(0.5)
    key_down('W')
    time.sleep(1.75)
    key_up('W')
    time.sleep(0.5)


def teleport():
    key_press('G')
    time.sleep(0.5)
    # adjust_map()
    time.sleep(0.5)
    key_press('F')
    time.sleep(0.4)
    key_press('E')
    time.sleep(0.3)
    key_press('E')
    time.sleep(0.1)


def use_skill():
    key_press('CTRL')
    time.sleep(7)


def main_event():
    time.sleep(6)
    go_first_target()
    use_skill()
    teleport()


def start_auto_Runes(maxnum):
    i = 0
    time.sleep(3)
    while i < maxnum:
        main_event()
        print('目前第',i+1,'次运行')
        i += 1
        time.sleep(1)

start_auto_Runes(maxnum)
print('Success')