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
 Description: 取消关注(此操作请慎用)
 Copyright(©) 2017 by xiaomo.
"""
import logging.config

from tweepy import TweepError

from app_config import log_config_url, unfollow_url
from tweepy_api import get_api

logging.config.fileConfig(log_config_url)

# create logger
logger = logging.getLogger(__name__)


# 主函数
def main():
    api = get_api()
    me = api.me()
    uid_list = api.friends_ids(me.screen_name)
    for uid in uid_list:
        friendship = unfollow(api, uid)
        if friendship:
            logger.info("unfollow %s" % friendship.screen_name)
            bak_following(friendship)
        else:
            logger.warning('%s unfollow fail...' % friendship.screen_name)


# 取消关注的实际操作
def unfollow(api, uid):
    try:
        friend = api.get_user(uid)
        friendship = api.destroy_friendship(friend.screen_name)
        if friendship:
            logger.info("unfollow %s" % friendship.screen_name)
        return friendship
    except TweepError as e:
        logger.error("error: %s" % e)
    return None


# 备份被取消的关注者，可以使用批量关注再加回来
def bak_following(user):
    with open(unfollow_url, 'a+', encoding="utf-8") as f:
        f.write(user.screen_name)
        f.write("\n")


# 入口
if __name__ == '__main__':
    main()
