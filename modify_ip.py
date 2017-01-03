# -*- coding: cp936 -*-
import os

import time
import wmi

def config_ip(ip):
    wmiService = wmi.WMI()
    colNicConfigs = wmiService.Win32_NetworkAdapterConfiguration(IPEnabled = True)

    if len(colNicConfigs) < 1:
        print 'û���ҵ����õ�����������'
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
        #print '����IP�ɹ�'
        pass
    elif returnValue[0] == 1:
        #print '����IP�ɹ�'
        intReboot += 1
    else:
        print '�޸�IPʧ��: IP���÷�������'
        return 0

    if intReboot > 0:
        print '��Ҫ�������������'
    #print '�޸�IP����'
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

