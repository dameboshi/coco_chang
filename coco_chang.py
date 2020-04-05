# coding: utf-8
import configparser
import discord
import client as coco

config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

client = coco.MyClient()
client.run(config['DEFAULT']['coco_token'])
