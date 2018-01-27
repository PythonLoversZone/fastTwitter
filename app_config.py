#! /usr/bin/python3

"""
 把今天最好的表现当作明天最新的起点．．～
 いま 最高の表現 として 明日最新の始発．．～
 Today the best performance  as tomorrow newest starter!
 Created by IntelliJ IDEA.
 author: xiaomo
 github: https://github.com/syoubaku
 email: xiaomo@xiamoo.info
 QQ_NO: 83387856
 Date: 2018/1/27 16:27 
 Description: 
 Copyright(©) 2017 by xiaomo.
"""
import json

base = 'config/'
follower_url = base + 'follow.txt'
log_config_url = base + 'logging_config.ini'
api_config = base + 'cfg.json'
unfollow_url = base + 'unfollow.txt'


# 读取文件中需要follow的名字列表
def get_name_list():
    name_list = dict()
    with open(follower_url, 'r', encoding='utf-8') as f:
        for line in f:
            names = line.split(" ")
            if len(names) < 2:
                continue
            first = names[0]
            second = names[1]
            name_list.setdefault(first, second)
        return name_list


# 读取配置文件
def get_config():
    with open(api_config) as f:
        setting = json.load(f)
        return setting
