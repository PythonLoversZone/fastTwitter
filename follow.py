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
 Description:关注
 Copyright(©) 2017 by xiaomo.
"""
import logging.config

from tweepy import TweepError

from app_config import get_name_list, log_config_url
from tweepy_api import get_api

logging.config.fileConfig(log_config_url)

# create logger
logger = logging.getLogger(__name__)


# 主函数
def main():
    api = get_api()
    name_list = get_name_list()
    for (key, value) in name_list.items():
        try:
            # 实际只用到了value
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
