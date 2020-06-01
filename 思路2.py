# 获取图片
#     def scr_img(self, axis=None):
#         if not axis:
#             lock.acquire() # 多线程时调会有BUG用使用锁
#             img = self.grab_t()
#             lock.release()
#         else:
#             img = array(ImageGrab.grab(axis))[..., ::-1] # axis 截图的坐标范围
#         return img


# class Block:
#     # 一个物品的信息类
#     def __init__(self, name, x, y, w, h):
#         self.name = name
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#
#     def __str__(self):
#         return "%s 坐标: %s ,宽高: %s" % (self.name, (self.x, self.y), (self.w, self.h))
#
#     # 获取信息
#     def block_find(self, *names, dict_name=None):
#         """色块识别 返回矩形信息
#         names:需要识别的物体名
#         """
#         if not names and dict_name is None:
#             raise Exception("请传入物体名")
#         goods = dict()
#         img = self.scr_img()
#         if names:
#             for name in names:
#                 if name == "ski":
#                     img = self.scr_img([533, 532, 710, 591])
#                 goods[name] = self.get_block(name, img)
#             return goods
#
#         if dict_name:
#             for name in dict_name:
#                 ret = self.get_block(name, img)
#                 if ret:
#                     return ret

# # 副本刷图
# def copy_swipe(self):
#     self.key_leonardo("y")  # 释放BUFF
#     while True:
#         if tool.EXIT:
#             tool.EXIT = False
#             exit()  # 退出程序
#         info_dict = self.block_find("hero", "spirit", "door")
#         if self.is_boos is not None:
#             # print("在BOOS房或附近")
#             boss_ret = self.boos_house()
#             if not boss_ret:
#                 return
#
#         if not info_dict["hero"]:
#             print("进图时无法获得人物坐标")
#             hero_ret = self.not_hero()
#             if not hero_ret:
#                 return
#             continue
#         self.hero = info_dict["hero"][0]
#
#         if info_dict["door"]:
#             # 判断是不是BOOS房附近
#             self.min_door = info_dict["door"]
#             spirit_ret = self.have_door_monster()
#             self.min_door = None
#             if not spirit_ret:
#                 return
#             continue
#
#         if not info_dict["spirit"]:
#             spirit_ret = self.have_door_monster()
#             if not spirit_ret:
#                 return
#             continue
#         self.spirit = info_dict["spirit"]
#         # 怪物，攻击
#         self.a_star_da()
#         # 控制循环速度
#         time.sleep(0.1)

#
# # 寻路攻击怪物
# def a_star_da(self, info):
#     # 人物坐标
#     hero = info["hero"][1], info["hero"][0]
#     # 怪物坐标，及怪物大小（w,h宽高）
#     x, y, w, h = info["spirit"]
#     s_x = x + w
#     s_y = y + h
#     if not self.zhiye == "鬼剑士":  # 远程职业和近程职业
#         off_x = 100
#     else:
#         off_x = 30
#
#     if info["hero"][0] >= s_x:
#         # 自动寻路到怪物坐标处(起点人物坐标，终点怪我坐标)
#         self.a_star(hero, (s_y, s_x))
#         # 控制释放技能方向
#         self.vk_key_run(VK_LEFT, 0.03)
#         # 放技能
#         self.put_skills()
#     else:
#         print("怪物左侧攻击")
#         if s_x - off_x > 0:
#             self.a_star(hero, (s_y, s_x - off_x))
#             self.vk_key_run(VK_RIGHT, 0.03)
#             self.put_skills()
#         else:
#             self.a_star(hero, (s_y, s_x))
#             self.put_skills()
#
#
# # # 智能获取可释放技能
# # def remove_ski(self, data):
# #     # data 技能框范围截图识别后的数据
# #     ski = deepcopy(self.ski)  # 复制配置中的技能（使用者设置这个职业哪些技能可用）
# #
# #     if not data["ski"]:
# #         # data不存在则配置中的所有技能均可释放
# #         return [k for k in self.ski]  # 返回所有可释放技能列表
# #
# #     for p in data["ski"]:  # 根据范围 删除冷却中的技能
# #         if 45 <= p.y <= 55:
# #             try:
# #                 if 1 < p.x < 25:
# #                     ski.pop("a")
# #                 elif 35 < p.x < 55:
# #                     ski.pop("s")
# #                 elif 65 < p.x < 85:
# #                     ski.pop("d")
# #                 elif 95 < p.x < 115:
# #                     ski.pop("f")
# #                 elif 125 < p.x < 145:
# #                     ski.pop("g")
# #                 elif 155 < p.x < 180:
# #                     ski.pop("h")
# #                 else:
# #                     print("超过范围1")
# #             except KeyError:
# #                 continue
# #         else:
# #             try:
# #                 if 1 < p.x < 25:
# #                     ski.pop("q")
# #                 elif 35 < p.x < 55:
# #                     ski.pop("w")
# #                 elif 65 < p.x < 85:
# #                     ski.pop("e")
# #                 elif 95 < p.x < 115:
# #                     ski.pop("r")
# #                 elif 125 < p.x < 145:
# #                     ski.pop("t")
# #                 elif 155 < p.x < 180:
# #                     ski.pop("y")
# #                 else:
# #                     print("超过范围2")
# #             except KeyError:
# #                 continue
# #     return [k for k in ski]  # 返回可释放技能列表
#     # 哪个门距离BOOS最近
#     def near_most(self, info_dict):
#
#         if (not info_dict["min_boos"]) or (not info_dict["min_me"]):
#             print("boos坐标或者自己坐标不存在")
#             return 7
#
#         if not info_dict["min_door"]:
#             # 没有小地图门未开启时，需要获得全局方向
#             return self.distance_boos(info_dict, v=True)
#
#         else:
#             # 都有坐标时先判断在不在boos房附近
#             addr = self.distance_boos(info_dict)
#             if addr != 2:
#                 return addr
#             me_x, me_y = info_dict["min_me"][0], info_dict["min_me"][1]
#
#             self.min_door.sort(key=lambda info: abs(self.min_boos.x - info.x) +
#                                                 abs(self.min_boos.y - info.y))
#
#             min_door = self.door[0]
#             if me_y - min_door[1] < -10:
#                 # 往下面走
#                 print("方向下")
#                 return VK_DOWN
#             if me_y - min_door[1] > 10:
#                 # 往上面走
#                 print("方向上")
#                 return VK_UP
#             if me_x - min_door[0] > 10:
#                 # 往左走
#                 print("方向左")
#                 return VK_LEFT
#             if me_x - min_door[0] < -10:
#                 # 往右走
#                 print("右方向")
#                 return VK_RIGHT
#
#             return 8
#
#     # 躲避障碍寻路
#     def a_star(self, start_axis, end_axis, func=None, direction=None, maps=None):
#         """ start_axis 起点 end_axis 终点 func 函数体 direction 方向  maps 地图 """
#
#         # "map_range": [0, 310, 800, 550]
#         def coordinate_axis(start, end, m_s):
#             if not (start or end):
#                 print("没有起点或终点坐标")
#                 self.error_num += 1
#                 self.is_block(self.error_num)
#                 return 8
#             s_x, s_y = ceil(start[0] / 10), ceil(start[1] / 10 - m_s[1] / 10)
#             e_x, e_y = ceil(end[0] / 10), ceil(end[1] / 10 - m_s[1] / 10)
#             e_x = e_x if e_x < int(m_s[2] / 10) else int(m_s[2] / 10 - 1)
#             e_y = e_y if e_y < int((m_s[3] - m_s[1]) / 10) else int((m_s[3] - m_s[1]) / 10 - 1)
#             # print("起点，终点",(s_y, s_x), (e_y, e_x))
#             return (s_y, s_x), (e_y, e_x)
#
#         if maps is None:
#             maps = th.threshold["map_range"]
#         else:
#             if end_axis[1] < 310:
#                 maps = [0, end_axis[1], 800, 550]
#                 print(329, maps)
#             else:
#                 maps = th.threshold["map_range"]
#
#         coord = coordinate_axis(start_axis, end_axis, maps)
#
#         a_star = xunlu.AStar(10, 10, maps, coord[0], coord[1])
#         # 获得没有障碍的移动路径
#         path_l = a_star.start()
#         if path_l is None:
#             self.error_num += 1
#             self.key_leonardo(VK_UP, s=0.5)
#             if self.error_num >= 3:
#                 self.is_block(self.error_num)
#                 return 9
#             elif self.error_num >= 15:
#                 raise Exception("超过15次没有获得寻路结果")
#             return 16
#
#         if func is None:
#             if direction == VK_DOWN:
#                 path_l.extend([direction for i in range(8)])
#
#         path_l.append(0)
#         key_num = 0
#         keys = len(path_l)
#         for k in range(keys):
#             key = k - 1
#             if path_l[k] != path_l[key] and k > 0:
#                 pad = k - key_num
#                 if path_l[key] == VK_UP or path_l[key] == VK_DOWN:
#                     ret = self.run_time(path_l[key], th.UP_DOWN_SPEED * pad, func, direction)
#                     if ret:
#                         return ret
#                 else:
#                     self.key_leonardo(path_l[key], s=0.03)
#                     ret = self.run_time(path_l[key], th.LEFT_RIGHT_SPEED * pad, func, direction)
#                     if ret:
#                         return ret
#                 key_num = k
#         if self.is_run:
#             self.is_run = False
# 	 def dnf_init(self):
# 	 	# 技能
#  		self.ski = th.KEY
#         # 全局方向
#         self.direction = None
#         # 技能释放控制
#         self.is_put = True
#         # 人物错误次数
#         self.hero_num = 0
#         # 没有发现BOSS次数
#         self.not_boos = 0
#         # 寻找怪物的次数
#         self.xunzhao = 0
#         self.door_x = None
#         # boss坐标是否获得
#         self.boos = None
#         # 人物坐标
#         self.hero = None
#         self.me = None
#         self.min_door_prev = None
#         # 怪物坐标
#         self.spirit = None
#         # 寻路起点
#         self.start_axis = None
#         # 正确的门坐标
#         self.door = None
#         # 上一次小地图自己坐标
#         self.prev_me = None
#         # 一个房间计时
#         self.time_room = 0
#         # 每一个房间的节点
#         self.point = Nonexx
# # 获取等级信息
#     def get_hero(self):
#         # 1.获得人物等级
#         lv = self.lv_get()
#         if not lv:
#             self.is_esc()
#             lv = self.lv_get()
#             if not lv:
#                 print("无法获得人物等级")
#                 return None
#         self.lv = lv
#         self.lv_info = self.hero_lv(self.lv)
#         print("人物等级: %s 级,任务地图位置:%s" % (self.lv, self.lv_info[2]))
#         return True
