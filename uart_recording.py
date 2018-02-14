# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 14:36:34 2018
@author: Administrator
"""

import _thread 
import com_function


def main():
    # 创建两个线程
    try: 
        
       _thread.start_new_thread( com_function.com1_fun,()) 
       _thread.start_new_thread( com_function.com9_fun,())

    except:
       print ("Error: unable to start thread")
     
    while 0:
       pass
    
    
    
if __name__ == '__main__':
  main()

