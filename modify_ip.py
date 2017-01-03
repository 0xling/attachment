# -*- coding: cp936 -*-
import os

import time
import wmi

def config_ip(ip):
    wmiService = wmi.WMI()
    colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)

    if len(colNicConfigs) < 1:
        print '没有找到可用的网络适配器'
        return 0
    objNicConfig = colNicConfigs[0]

    #print objNicConfig

    #for method_name in objNicConfig.methods:
    #    method = getattr(objNicConfig, method_name)
    #    print method
    arrIPAddresses = [ip]
    arrSubnetMasks = ['255.255.255.0']
    intReboot = 0
    returnValue = objNicConfig.EnableStatic(IPAddress = arrIPAddresses, SubnetMask = arrSubnetMasks)
    if returnValue[0] == 0:
        #print '设置IP成功'
        pass
    elif returnValue[0] == 1:
        #print '设置IP成功'
        intReboot += 1
    else:
        print '修改IP失败: IP设置发生错误'
        return 0

    if intReboot > 0:
        print '需要重新启动计算机'
    #print '修改IP结束'
    return 1

import urllib2

def check_connect():
    try:
        urllib2.urlopen('https://www.baidu.com/', timeout=10)
        return 1
    except:
        return 0

if __name__ == '__main__':
    while True:
        if check_connect():
            print 'network is ok'
            while True:
                time.sleep(60)
                if not check_connect():
                    break

        for i in range(2, 254):
            ip = '10.104.171.'+str(i)
            print 'try ip:' + ip
            if config_ip(ip):
                time.sleep(5)
                if not check_connect():
                    pass
                else:
                    print 'current ip is:' + ip
                    while True:
                        time.sleep(60)
                        if not check_connect():
                            break
            else:
                print 'config ip error'

#print check_connect()

