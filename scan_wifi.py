import network,os,socket,sys,time,json,gc
import logging

logging.basicConfig(format="%(asctime)s,%(levelname)-7s,[%(name)s]: %(message)s")
logger = logging.getLogger("boot.py")

logger.info("Initializing WiFi")

wlan_config_file=open("wlan.json", 'r')
wlan_config = json.load(wlan_config_file)

wlan = network.WLAN(network.WLAN.IF_STA)
wlan_ap=network.WLAN(network.WLAN.IF_AP)

wlan.active(True)

aps=wlan.scan()
ap_names=[]
for ap in aps:
    ap_names.append(ap[0].decode('ascii'))
logger.info('Available APs include: '+str(ap_names))

for c in wlan_config:
    if c['ssid'] in ap_names:
        logger.info('Founded AP: '+c['ssid'])
        logger.info('connecting to: '+c['ssid'])
        wlan.config(hostname='supermini')
        wlan.connect(c['ssid'], c['password'])
        while not wlan.isconnected():
            passimport network,os,socket,sys,time,json,gc
import logging

logging.basicConfig(format="%(asctime)s,%(levelname)-7s,[%(name)s]: %(message)s")
logger = logging.getLogger("boot.py")

logger.info("Initializing WiFi")

wlan_config_file=open("wlan.json", 'r')
wlan_config = json.load(wlan_config_file)

wlan = network.WLAN(network.WLAN.IF_STA)
wlan_ap=network.WLAN(network.WLAN.IF_AP)

wlan.active(True)

aps=wlan.scan()
ap_names=[]
for ap in aps:
    ap_names.append(ap[0].decode('ascii'))
logger.info('Available APs include: '+str(ap_names))

for c in wlan_config:
    if c['ssid'] in ap_names:
        logger.info('Founded AP: '+c['ssid'])
        logger.info('connecting to: '+c['ssid'])
        wlan.config(hostname='supermini')
        wlan.connect(c['ssid'], c['password'])
        while not wlan.isconnected():
            pass

        ip=wlan.ifconfig()[0]
        ip_mark=wlan.ifconfig()[1]
        ip_dns1=wlan.ifconfig()[2]
        ip_dns2=wlan.ifconfig()[3]
        logger.info('WiFi is OK. Network config:')
        logger.info('  IP:'+ip)
        logger.info('  Mark:'+ip_mark)
        logger.info('  DNS1:'+ip_dns1)
        logger.info('  DNS2:'+ip_dns2)


        ip=wlan.ifconfig()[0]
        ip_mark=wlan.ifconfig()[1]
        ip_dns1=wlan.ifconfig()[2]
        ip_dns2=wlan.ifconfig()[3]
        logger.info('WiFi is OK. Network config:')
        logger.info('  IP:'+ip)
        logger.info('  Mark:'+ip_mark)
        logger.info('  DNS1:'+ip_dns1)
        logger.info('  DNS2:'+ip_dns2)
