import network,os,socket,struct,sys,time,json
from machine import SPI,I2C,Pin,RTC,SoftI2C
import logging
from ntp import Ntp

tag='[boot]'

logging.basicConfig(format="%(asctime)s,%(levelname)-7s,[%(name)s]: %(message)s")
logger = logging.getLogger("boot.py")

logger.info("Run in MicroPython")

logger.info("Initializing WiFi")

wlan_config_file=open("wlan.json", 'r')
wlan_config = json.load(wlan_config_file)
#print(wlan_config[0]['ssid'])

if 'wlan' not in locals():
    wlan = network.WLAN(network.WLAN.IF_STA)
else:
    wlan=locals()['wlan']
    
    

if not wlan.active() or not wlan.isconnected():
    wlan.active(True)
    aps=wlan.scan()
    ap_names=[]
    for ap in aps:
        ap_names.append(ap[0].decode('ascii'))
    for c in wlan_config:
        if c['ssid'] in ap_names:
            logger.info('Founded AP: '+c['ssid'])
            logger.info('connecting to: '+c['ssid'])
            wlan.config(hostname='uclock')
            wlan.connect(c['ssid'], c['password'])
            while not wlan.isconnected():
                pass

ip=wlan.ifconfig()[0]
ip_mark=wlan.ifconfig()[1]
ip_dns1=wlan.ifconfig()[2]
ip_dns2=wlan.ifconfig()[3]
logger.info('WiFI is OK. Network config:')
logger.info('  IP:'+ip)
logger.info('  Mark:'+ip_mark)
logger.info('  DNS1:'+ip_dns1)
logger.info('  DNS2:'+ip_dns2)

logger.info("Initializing NTP client and sync rtc time")
_rtc = RTC()
Ntp.set_datetime_callback(_rtc.datetime)
Ntp.set_hosts(('time.windows.com',))
Ntp.set_ntp_timeout(1)
Ntp.set_timezone(8, 0)
Ntp.set_epoch(Ntp.EPOCH_2000)
Ntp.rtc_sync()

