#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from csvUtil import CsvUtil
lucy=CsvUtil()
lucy.open('2017年电影实时评论数据.csv')
lucy.read()
# print(lucy.row_generator().__next__())
# print(lucy.row_generator().__next__())
# # lucy.readAll()
# # lucy.write(['17590427', '249894', '206189876', '嘿嘿个', '期待雷神，没有道理！', '5', '5', '0', '2015-06-09 21:14:25'])
# lucy.read()
# lucy.writeAll(['17590427', '249894', '206189876', '嘿嘿个', '期待雷神，没有道理！', '5', '5', '0', '2015-06-09 21:14:25'],['17590427', '249894', '206189876', '嘿嘿个', '期待雷神，没有道理！', '5', '5', '0', '2015-06-09 21:14:25'])