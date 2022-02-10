try:
    print('1 霍尔效应')
    print('2 介质介电常数的测量')
    print('3 液晶的光电效应')
    print('4 惠斯登电桥测电阻')
    print('5 光电效应测定普朗克常数')
    print('6 音叉的受迫振动与共振')
    print('7 太阳能电池基本特性测定')
    print('8 迈克尔逊干涉仪的调节和使用')
    print()
    print()
    sym=eval(input('请输入实验编号(每次输入完成回车结束):'))
#a
    if sym==1 :
        print('目前仅支持实验6 8')
#b
    elif sym==2 :
        print('目前仅支持实验6 8')
#c
    elif sym==3 :
        print('目前仅支持实验6 8')
#d
    elif sym==4 :
        print('目前仅支持实验6 8')
#e
    elif sym==5 :
        print('目前仅支持实验6 8')
#f
    elif sym==6 :
        '''print()
        print()
        print('注意:输入多个数据时每个数据用一个或多个空格分隔')
        print('注意:输入格式错误将导致程序运行不正常')
        fsr1=input('请输入数据:')
        fsr1ls=fsr1.split()
        fsr2=input('请输入数据:')
        fsr2ls=fsr2.split()
        fsr3=input('请输入数据:')
        fsr3ls=fsr3.split()
        fsr4=input('请输入数据:')
        fsr4ls=fsr4.split()
        fsr5=input('请输入数据:')
        fsr5ls=fsr5.split()
        fls1=[]
        fls2=[]
        fls3=[]
        fls4=[]
        fls5=[]
        for fi1 in range(6):
        for fi2 in range(6):
        for fi3 in range(6):





        print()
        print()
        print()
        print('实验报告答案：')
        print('T²×105分别为')
        for fi in range(4):
            print()
        print()'''
#g
    elif sym==7 :
        print('目前仅支持实验6 8')
#h
    elif sym==8 :
        print()
        print()
        print('注意:输入多个数据时每个数据用一个或多个空格分隔')
        print('注意:输入格式错误将导致程序运行不正常')
        hsr1=input('请输入6个M1镜位置d1数据:')
        hsr1ls=hsr1.split()
        hsr2=input('请输入6个M1镜位置d2数据:')
        hsr2ls=hsr2.split()
        hls1=[]
        hls2=[]
        hls3=[]
        h1=0
        h2=0
        for hi1 in range(6):
            hls1.append(eval(hsr1ls[hi1]))
            hls2.append(eval(hsr2ls[hi1]))
        for hi4 in range(6):
            hts=abs(hls1[hi4]-hls2[hi4])
            hts=hts*20000
            hts=hts/3
            hts=round(hts,3)
            hls3.append(hts)
        for hi2 in range(6):
            h1 += hls3[hi2]
        h1=h1/6
        for hi3 in range(6):
            h2 += (hls3[hi3]-h1)**2
        h2=h2/5
        h2=h2**0.5
        h2=h2*1.05
        h3=1.5*h1*0.01
        h4=h2**2+h3**2
        h4=h4**0.5
        h5=h1
        h6=h4
        print()
        print()
        print()
        print('实验报告答案：')
        print('Δd分别为：')
        for hi5 in range(6):
            ts3=abs(hls1[hi5]-hls2[hi5])
            ts3=round(ts3,5)
            print(ts3,end=' , ')
        print()
        print('λi分别为：')
        for hi6 in range(6):
            print(hls3[hi6],end=' , ')
        print()
        print('波长平均值为：{:.3f}'.format(h1))
        print('A类不确定度：{:.3f}'.format(h2))
        print('B类不确定度：{:.3f}'.format(h3))
        print('总不确定度：{:.3f}'.format(h4))
        print('表达式空1：{:.3f}'.format(h5))
        print('表达式空2：{:.3f}'.format(h6))
    else:
        print('输入编号错误，请重启程序')
    input('输入任意内容退出程序')
except:
    input('运行错误，请输入任意内容退出程序后重启程序')

