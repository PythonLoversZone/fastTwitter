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
 Date: 2018/1/27 14:19 
 Description: 
 Copyright(©) 2017 by xiaomo.
"""

# !/usr/local/bin/python
# -*- coding: utf-8 -*-

# !/usr/local/bin/python
# -*- coding: utf-8 -*-
import logging.config

logging.config.fileConfig('logging_config.ini')

# create logger
logger = logging.getLogger('root')

# 'application' code
logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
