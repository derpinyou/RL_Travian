import numpy as np

import gym
from gym import spaces
from gym.utils import seeding

village_n = int(input())  # сколько деревнь?
village_info_list = []
for j in range(village_n):
    village_info_list.append([int(x) for x in input().split(' ')]) ### ффффффккккллллрррргсазгджн + время
keys = ['village' + str(j+1) for j in range(village_n)]
village_info_dict_of_lists = {}
for j in range(len(keys)):
    village_info_dict_of_lists[keys[j]] = village_info_list[j]



buildings_info = []



class TravianEnv(gym.Env):

    def __init__(self, X, buildings_info):
        self.VillageDict = X
        self.village_n = ...
        self.action_space = spaces.Discrete(21*self.village_n + 2*self.village_n + self.village_n**self.village_n)
        self.buildings_info = buildings_info
        self.n = 0
        self.gold = ...
        self.current_time = ...
        self.corn_capacity = ...
        self.others_capacity = ...

    def count_action_price(self, action):
        """
        Для каждого текущего доступного action считаем его ресурсную стоимость
        :param action:
        :return:
        """
        return price
    
    def isavailable(self, action):
        """
        проверяем, не строится ли что-то ещё и есть ли ресурсы
        :param action:
        :return:
        """
        if ...:
            available = 1
        else:
            available = 0
        return available == 1

    def is_corn_ok(self): # чекаем, не кушаем ли мы больше положенного


    def count_time_pace(self, ): #будем настраивать, сколько времени "ждёт" агент, если выбирает действие ждать
        return time_pace

    def reset(self):
        return

    def step(self, action):
        if isavailable(action) == False:
            pass
        else:
            #если действие того требует, пересчитываем ресурсы с учётом count_time_pace


        return obs, reward, done, {}


