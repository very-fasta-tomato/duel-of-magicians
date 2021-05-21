import json
import os
import xml.etree.ElementTree as ET

def output(delta_enemy_hp, delta_enemy_mp, outputformat):
    if outputformat == "json":  # создание выходного файла на json
        data = {'delta_enemy_hp': delta_enemy_hp,
                'delta_enemy_mp': delta_enemy_mp}
        jsonoutput = json.dumps(data)
        return jsonoutput
    #if outputformat=="xml":