#!/bin/python3

class Stock():
    def __init__(self):
	name = ''
	code = ''
	tags = []
	trade = true # 交易状态(true: 正常交易, false: 停牌） 
	isST = false
