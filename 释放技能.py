# author=wrwillwin
list_to_time = [0,0,0,0,0,0,0,0,0,0,0]

list_skill =         ['q', 'e', 'r', 'i','t','y','j','k','f','g','h']
#技能按钮
list_skill_cooling = [  6.8, 9.6, 32,  9,   37, 103, 22,  0,  17.5,36, 120]
#技能冷却
skill_release_time = [  0.5, 0.5, 3,   0.5, 0.5, 7, 5,    0.3, 1,  1.5, 2]
#技能施法时间
list_key           = [0x10,0x12,0x11,0x20,0x14,0x15,0x1e,0x1f,0x21,0x22,0x23]
#按键码
def rel_skill(skill,ini_time):
    for i in list_skill:
        while(skill==i):
            list_to_time[list_skill.index(i)] = ini_time + list_skill_cooling[list_skill.index(i)] + skill_release_time[list_skill.index(i)]
            f = open('data.txt','w')
            for j in range(len(list_skill)):
                f.write(str(list_to_time[j])+'\n')
            f.close()
            key_press(list_key[list_skill.index(i)])
            time.sleep(skill_release_time[list_skill.index(i)]+0.8)
            break
    return
