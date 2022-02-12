#!/usr/bin/env python3

import json
import math
from itertools import islice

with open('AsteroidData.json', 'r') as f:
        data = f.read()

asteroid_data = json.loads(data)
#print(asteroid_data)

max_ores = {}

oke_pos = (11374785,-1984055,866615)

def get_dist(loc):
        dx = loc[0] - oke_pos[0]
        dy = loc[1] - oke_pos[1]
        dz = loc[2] - oke_pos[2]

        return math.sqrt(dx*dx + dy*dy + dz*dz)

test_loc = (11312505.699694332, -1983684.7709041561, 847236.6208426375)
print("TestDist: " + str(get_dist(test_loc)))


class AsteroidData(object):
        def __init__(self, ore_name, amount, loc):
                self.ore_name = ore_name
                self.amount = amount
                self.loc = loc

        #def get_gps(self, ore_name, ore_location):
        def __str__(self):
                return "GPS:" + self.ore_name + " [" + str(round(self.amount,1)) +"]:" + str(self.loc[0]) + ":" + str(self.loc[1]) + ":" + str(self.loc[2]) + ":#FFFF00:"

        def get_dist(self):
                dx = loc[0] - oke_pos[0]
                dy = loc[1] - oke_pos[1]
                dz = loc[2] - oke_pos[2]

                return math.sqrt(dx*dx + dy*dy + dz*dz)


        def __lt__(self, other):
                return self.amount < other.amount


for entity_id in asteroid_data:
        entity_data = asteroid_data[entity_id]
        #print(entity_data)
        ore_data = asteroid_data[entity_id]['OreData']
        loc_data = asteroid_data[entity_id]['Location']
        ore_loc = (loc_data['X'], loc_data['Y'], loc_data['Z'])
        distance = get_dist(ore_loc)
        #print(ore_data)
        for cur_ore in ore_data:
                print("Cur Ore: %s" % cur_ore)
                print("Amount: %s" % ore_data[cur_ore])
                print("Location: %s" % str(ore_loc))
                print("Dist From Okeanos: %s" % str(distance))
                if distance < 67000:
                        print("TOO CLOSE!")
                        continue
                if cur_ore not in max_ores:
                        print("Ore: %s no existing max, setting to %s" % (cur_ore, ore_data[cur_ore]))
                        max_ores[cur_ore] = []
                max_ores[cur_ore].append(AsteroidData(cur_ore, ore_data[cur_ore], ore_loc))
                #else:
        #               if  ore_data[cur_ore] > max_ores[cur_ore]['amount']:
        #                       max_ores[cur_ore] = {   'amount' : ore_data[cur_ore],
        #                                               'location' : get_gps(cur_ore, asteroid_data[entity_id]['Location'])
        #                                           }

#print(max_ores)
#print(json.dumps(max_ores, indent=4, sort_keys=True))
for cur_ore in max_ores:
        sorted_ore_list = sorted(max_ores[cur_ore])
        top_ten = list(islice(reversed(sorted_ore_list),0,5))
        top_ten.reverse()
        #print(len(top_ten))
        print("-------------------")
        for cur_ore_site in top_ten:
                print(cur_ore_site)
