#!/usr/bin/env python

from time import gmtime, strftime
from grove_rgb_lcd import *
import json, requests
import time

while True:
	main_blocknumber = requests.get('https://api.infura.io/v1/jsonrpc/mainnet/eth_blockNumber?token=yrL0867Q4MwKTtVcVcSN',verify=False).json()
	intnum=int(main_blocknumber["result"],16)
        main_intnum=intnum
	lcdtxt="Mainnet: " + str(intnum)

	rinkeby_blocknumber = requests.get('https://api.infura.io/v1/jsonrpc/rinkeby/eth_blockNumber?token=yrL0867Q4MwKTtVcVcSN',verify=False).json()
	intnum=int(rinkeby_blocknumber["result"],16)
	rinkeby_intnum=intnum

	lcdtxt = lcdtxt + "\nRinkeby:" +str(intnum)

	setRGB(255,255,255)
	setText(lcdtxt)

	print strftime("%Y-%m-%d %H:%M:%S", gmtime()), main_intnum, rinkeby_intnum

	time.sleep(20)
done

