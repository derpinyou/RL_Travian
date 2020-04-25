import numpy as np
import pandas as pd


granary_info = []
text_file = open("granary.txt", "r")
lines = text_file.readlines()
for line in lines:
    line = line[:-1]
    granary_info.append(line.split('\t'))


storage_info = []
text_file = open("storage.txt", "r")
lines = text_file.readlines()
for line in lines:
    line = line[:-1]
    storage_info.append(line.split('\t'))

main_building_info = []
text_file = open("main_building.txt", "r")
lines = text_file.readlines()
for line in lines:
    line = line[:-1]
    main_building_info.append(line.split('\t'))

farm_info = []
text_file = open("farm.txt", "r")
lines = text_file.readlines()
for line in lines:
    line = line[:-1]
    farm_info.append(line.split('\t'))

canyon_info = []
text_file = open("canyon.txt", "r")
lines = text_file.readlines()
for line in lines:
    line = line[:-1]
    canyon_info.append(line.split('\t'))

mine_info = []
text_file = open("mine.txt", "r")
lines = text_file.readlines()
for line in lines:
    line = line[:-1]
    mine_info.append(line.split('\t'))

lumber_info = []
text_file = open("lumber.txt", "r")
lines = text_file.readlines()
for line in lines:
    line = line[:-1]
    lumber_info.append(line.split('\t'))

print(granary_info)
print(farm_info)
print(main_building_info)
print(mine_info)
print(lumber_info)
print(canyon_info)
print(storage_info)
