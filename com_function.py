# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 14:38:50 2018

@author: Administrator
"""
import serial
import time
import codecs

counter_max = 10000

def Short2Dec(value):
    rawBin='{0:b}'.format(value)
    rawBin=rawBin.zfill(16)
    iniValue=int(rawBin,2)
    MaxValue=2**16     
    if rawBin[0]=='1':
        return(str(iniValue-MaxValue))
    else:
        return(str(iniValue))


def com1_fun():   
    #ser=serial.Serial("com1",9600,timeout=0.5)#winsows系统使用com1口连接串行口
    ser = serial.Serial()
    ser.baudrate = 115200  
    ser.port = "com1"  
    ser.bytesize = 7
    ser.stopbits = 1
    ser.parity = 'E'
    ser.timeout = 0.1  
    #字符串转Bytes
    #cmd = "R01\r"
    #cmd = bytes([0x52,0x30,0x31,0x0D])
    #for i in cmd:
    #  print('%#x'%ord(i))
            
    cmd = bytes([0x52,0x30,0x31,0x0D])
    counter = 0
    
#    print (cmd)
    
    str_file_name = 'data\encode_data_%s.txt'%((time.time()))
    
    if ser.isOpen() : 
        ser.close() 
    else :
        ser.open()
        
    if ser.isOpen() :  
        print('open com1 succeed!\n')
        fo = codecs.open(str_file_name,'w+')
        #ser.write("R01\r".encode());
        while True:
            counter = counter+1
            if counter > counter_max:
                break
            time.sleep(0.05)
            ser.write(cmd)
            data = ser.read(11)
        #    print (data)
        #    print(type(data))
        #    print('%#x'%data[0])
            if data[0] == 0x02:
                num = (data[5]-0x30)*10000+(data[6]-0x30)*1000+(data[7]-0x30)*100+(data[8]-0x30)*10+(data[9]-0x30)
                print (num,counter)
                fo.write('%d,%d'%(num,counter))
                fo.write('\n')
        #        buffer_data.append(num)
        #       print(type(num))  
    ser.close()
    print('close com1 succeed!\n')
    fo.close()


# 为线程定义一个函数
def com9_fun():
    #ser=serial.Serial("com1",9600,timeout=0.5)#winsows系统使用com1口连接串行口
    ser = serial.Serial()
    ser.baudrate = 115200  
    ser.port = "com9"  
    ser.bytesize = 8
    ser.stopbits = 1
    #ser9.parity = 'N'
    ser.timeout = 0.1
    cmd = bytes([0x55,0x30,0x31,0x0D,0x0A])
    data = bytes([])
    counter = 0
#   counter_max = 100
#    print (cmd)
    
    str_file_name = 'data\imu_data_%s.txt'%((time.time()))

    if ser.isOpen() : 
        ser.close() 
    else :
        ser.open()
        
    if ser.isOpen() :  
        print('open com9 succeed!\n')
        fo = codecs.open(str_file_name,'w+')
        while True:
            counter = counter+1
            if counter > counter_max:
                break
            time.sleep(0.05)
            ser.write(cmd)
            data = ser.read(32)
        
            ax = ((data[3]<<8)|(data[4]))
            ay = (data[5]<<8)|(data[6])
            az = (data[7]<<8)|(data[8])
            
            wx = ((data[9]<<8) |data[10])
            wy = ((data[11]<<8)|data[12])
            wz = ((data[13]<<8)|data[14])
            
            hx = (data[15]<<8)|(data[16])
            hy = (data[17]<<8)|(data[18])
            hz = (data[19]<<8)|(data[20])
            
            roll = (data[21]<<8)|(data[22])
            pitch = (data[23]<<8)|(data[24])
            yaw = (data[25]<<8)|(data[26])
            
            
            str_ax = Short2Dec(ax)
            str_ay = Short2Dec(ay)
            str_az = Short2Dec(az)
            
            str_wx = Short2Dec(wx)
            str_wy = Short2Dec(wy)
            str_wz = Short2Dec(wz)
            
            str_hx = Short2Dec(hx)
            str_hy = Short2Dec(hy)
            str_hz = Short2Dec(hz)
            
            str_roll = Short2Dec(roll)
            str_pitch = Short2Dec(pitch)
            str_yaw = Short2Dec(yaw)
                       
            if data[0] == 0x88:
                print('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d'%(str_ax,str_ay,str_az,str_wx,str_wy,str_wz,str_roll,str_pitch,str_yaw,str_hx,str_hy,str_hz,counter),end='\n')
                fo.write('%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%d'%(str_ax,str_ay,str_az,str_wx,str_wy,str_wz,str_roll,str_pitch,str_yaw,str_hx,str_hy,str_hz,counter))
                fo.write('\n')
    ser.close()
    print('close com9 succeed!\n')
    fo.close()
