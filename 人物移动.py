# author=wrwillwin
def moveTo(monsters_x, monsters_y, person_x, person_y, flag=0):
    ''' flag = 1 时，为 人物 向 门口 移动
        flag = 0 时，为 人物 向 怪物 移动 ， 距离怪物 80 个像素时 ， 释放技能
    '''

    if (flag == 0):
        # 释放技能的位置，在怪物前方60像素
        skill_pos = 60
    else:
        skill_pos = 0
    # 1 怪物 在 人物 的 右上
    if ((person_x - monsters_x) < 0 and (person_y - monsters_y) > 0):
        if (monsters_x - person_x < skill_pos):
            print('距离右边怪物挺近,直接往上移动')
            key_press(0x34)
            key_press(0x25, abs(person_y - monsters_y) / y_speed)
        else:
            move_time = abs(monsters_x - person_x - skill_pos) / x_speed - abs(person_y - monsters_y) / y_speed
            if (move_time > 0):
                print('跑啊跑，往右上移动')
                key_press(0x34)
                key_down(0x34)
                time.sleep(0.1)
                key_press(0x25, abs(person_y - monsters_y) / y_speed)
                time.sleep(move_time)
                key_up(0xb4)
            else:
                print('不值得跑，先往右，后往上')
                key_press(0x34)
                key_press(0x34, abs(monsters_x - skill_pos - person_x) / x_speed)
                key_press(0x25, abs(person_y - monsters_y) / y_speed)
