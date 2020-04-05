# -*- coding: utf-8 -*-

# aikatsu : 話数からタイトルとあらすじを取ってくるやつ

import json
import codecs

JSON_PATH = "./json/aikatsu.json"

def display_aikatsu(episode_num):
    """
    話数からタイトルとあらすじを表示する

    Args:
        episode_num (str) : 
    return:
        dict :  
    """
    episode_num = episode_num - 1
    file_json = codecs.open(JSON_PATH, "r", "utf-8")
    aikatsu = json.load(file_json)
    str_dic = {"series": str(aikatsu[episode_num]["series"]), "title" : str(aikatsu[episode_num]["title"]), "story" : str(aikatsu[episode_num]["story"]) }
    return str_dic
