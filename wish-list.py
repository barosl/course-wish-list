#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mechanize
import re

execfile('cfg.py')

br = mechanize.Browser()
br.open('http://ysweb.yonsei.ac.kr/new_sugang_win.jsp')
br.select_form(name='frmLogin')
br['id'] = username
br['pw'] = password
br.submit()
br.select_form(name='frm')
br.submit()
res = br.open('http://ysweb.yonsei.ac.kr/SG/new_sg13_wish_list.jsp')
data = res.read()

print '(남은 슬롯, 경쟁자, 학점)'
nums = [int(x) for x in re.findall('<td align="center" class="BoxText_1">([0-9]+)', data)]
for x in zip(*(iter(nums),)*3):
	print x
