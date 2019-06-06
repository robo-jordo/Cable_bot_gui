#!/usr/bin/env python
import serialCom_v2 as sc
import time

starttime = time.time()
set_packet = [
		'0 m 10000 1;',
		'1 m 0 0;',
		'2 m 0 0;',
		'3 m 0 0;',
		'4 e 0 0;']

stop_packet = [
		'0 m 0 0;',
		'1 m 0 0;',
		'2 m 0 0;',
		'3 m 0 0;',
		'4 e 0 1;']

test = sc.SerialCOm("/dev/ttyUSB0")
for i in range(2):
	test.writeDataPack(set_packet)

test.writeDataPack(stop_packet)

print(time.time()-starttime)