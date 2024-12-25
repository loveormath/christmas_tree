import random
import time
from colorama import Fore, Back, Style, init
 

init(autoreset=True)
treehigh = 20  # 圣诞树高度 
do_sonw = True  # 是否打印雪花效果
def print_christmas_tree(height):

    for i in range(1, height + 1):
        stars = ''
        for j in range(2 * i - 1):
            if random.random() < 0.45:  # 概率放彩灯
                stars += random.choice([Fore.RED + 'o', Fore.YELLOW + '+', Fore.GREEN + '*'])  #给树上色
            else:
                stars += Fore.GREEN + '*'   
        spaces = ' ' * (height - i)  
        print(spaces + stars)
 
    trunk_width = treehigh // 5
    trunk_height = treehigh // 5
    trunk_spaces = ' ' * (height - trunk_width // 2 - 1)
    for _ in range(trunk_height):
        print(trunk_spaces + Fore.YELLOW + '*' * trunk_width)
 
    # 可选：添加简单的雪花效果
    if do_sonw:
        for _ in range(3):  # 打印三行雪花
            snow = ''.join(random.choice([' ', Fore.WHITE + '.', Fore.WHITE + '*', Fore.WHITE + 'o']) for _ in range(2 * height - 1))
            print(snow)
            time.sleep(0.5)  # 稍微延迟，使效果更有节奏感
 
print_christmas_tree(treehigh)