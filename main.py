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
 Date: 2018/1/27 10:25 
 Description: 
 Copyright(©) 2017 by xiaomo.
"""
import json
import logging.config

import tweepy
from tweepy import TweepError

logging.config.fileConfig('logging_config.ini')

# create logger
logger = logging.getLogger(__name__)


# 获取tweepy的api实例
def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


# 读取文件中需要follow的名字列表
def get_name_list():
    name_list = dict()
    with open('follow.txt', 'r', encoding='utf-8') as f:
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
    with open('cfg.json') as f:
        setting = json.load(f)
        return setting


# 主函数
def main():
    cfg = get_config()
    api = get_api(cfg)
    name_list = get_name_list()
    for (key, value) in name_list.items():
        try:
            friendship = api.create_friendship(value)
            if friendship:
                logger.info("following %s" % friendship.screen_name)
            else:
                logger.warning('%s :%s is not found' % (key, value))
        except TweepError as e:
            logger.error("%s ,error: %s" % (value.replace("\n", ""), e))


# 入口
if __name__ == '__main__':
    main()
