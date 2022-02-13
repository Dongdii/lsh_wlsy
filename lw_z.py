#引用第三方库，用于绘制拟合曲线
import matplotlib.pyplot as plt
import numpy as np
#导入decimal模块中的Decimal函数实现保留小数时四舍六入五成双
from decimal import Decimal
#绘制拟合曲线函数
def nhqx(nh1,nh2,nh3,nh4,nh5,nh6,nhcs=10):
    x = nh1                                                         #nh1应为数字列表
    y = np.array(nh2)                                               #nh2应为数字列表
    z1 = np.polyfit(x, y, nhcs)                                     #nhcs为正整数，建议8，10，12,默认10
    p1 = np.poly1d(z1)
    print(p1)
    yvals = p1(x)
    plt.plot(x, y, '*', label='original values')
    plt.plot(x, yvals, 'r', label='polyfit values')
    plt.xlabel(nh3)                                                 #nh3为字符串，函数横坐标物理量，注意加单位
    plt.ylabel(nh4)                                                 #nh4为字符串，函数纵坐标物理量，注意加单位
    plt.legend(loc=nh5)                                             #nh5为数字1,2,3,4之一，对应位置右上,左上,左下,右下
    plt.title(nh6)                                                  #nh6为字符串，图像标题
    plt.show()
#保留正确的有效数字的函数，四舍六入五成双的规则，+-*/，输入为字符串
#quantize加入参数rounding = "ROUND_HALF_UP"改为四舍五入规则
def zss(zs):                                                        #输入字符串，计算整数位数
    try:
        zsls=zs.split('.')
        zslen=len(zsls[0])
        return zslen                                                #返回均为数字
    except:
        zslen = len(zs)
        return  zslen
def xss(xs):                                                        #计算小数位数
    try:
        xsls=xs.split('.')
        xslen=len(xsls[1])
        return xslen
    except:
        return 0
def yxsz(sz):                                                       #有效数字位数
    yxlen=zss(sz)+xss(sz)
    return yxlen
#有效数字保留函数
def sslrwsc(jg1,jg2,jg3):                                           #运算数1，运算数2，原始结果
    if yxsz(jg1)>yxsz(jg2):                                         #第二个数有效位数少
        yxws = yxsz(jg2)
    else:                                                           #第一个数有效位数少
        yxws = yxsz(jg1)
    if yxws > zss(jg3):                                             #最终结果有小数
        xsws = yxws-zss(jg3)
        jg=Decimal(jg3).quantize(Decimal('{}'.format(1/10**xsws)))
    else:                                                           #最终结果无小数
        jg = str(eval(jg3)/(10**(zss(jg3)-yxws)))
        xsws = yxws-zss(jg)
        if xsws ==0:                                                #保留整数时要用1而不能用1.0
            xsws = 1
        else:
            xsws = 1 / 10 ** xsws
        jg = Decimal(jg).quantize(Decimal('{}'.format(xsws)))
        jg = int(jg*(10**(zss(jg3)-yxws)))
    return str(jg)             #输出字符串
def yxjia(yx1,yx2):
    he = str(eval(yx1)+eval(yx2))
    yxhe = sslrwsc(yx1,yx2,he)
    return yxhe
def yxjian(yx1,yx2):
    cha = str(eval(yx1)+eval(yx2))
    yxcha = sslrwsc(yx1,yx2,cha)
    return yxcha
def yxcheng(yx1,yx2):
    ji = str(eval(yx1)*eval(yx2))
    yxji = sslrwsc(yx1,yx2,ji)
    return yxji
def yxchu(yx1,yx2):
    shang = str(eval(yx1)/eval(yx2))
    yxshang = sslrwsc(yx1,yx2,shang)
    return yxshang
#以函数形式编写实验运算
def shuchu(mz,mgls):                                             #标准输出内容函数，参数为输出项目，输出列表
    print(mz,end='：')
    for isc in mgls:
        print(isc,end='  ')
    print()
def konghang():                                                  #输出答案空行函数
    print()
    print()
    print()
#惠斯登电桥测电阻
def hsddq():
    print('原始数据输入：')
    hsdsr0 = input('请输入电桥的准确度等级(回车跳过，默认0.1)：')
    if hsdsr0 == '':
        hsdsr0 = '0.1'
    hsdsr1 = input('请输入所有比率臂K数据：')
    hsdsr2 = input('请输入所有比较臂R0数据：')
    hsdsr3 = input('请输入所有n数据：')
    hsdsr4 = input('请输入所有ΔR0数据：')
    hsdsr1ls = hsdsr1.split()
    hsdsr2ls = hsdsr2.split()
    hsdsr3ls = hsdsr3.split()
    hsdsr4ls = hsdsr4.split()
    hsd_sls=[]                                                   #s数据列表
    hsd_rxls=[]                                                  #rx数据列表
    hsd_urxls=[]                                                 #urx数据列表
    for i1 in range(len(hsdsr3ls)):                                #计算s
        hsd_s = yxchu(hsdsr3ls[i1],hsdsr4ls[i1])
        hsd_sls.append(hsd_s)
    for i2 in range(len(hsdsr1ls)):                                #计算Rx
        hsd_rx = round(eval(hsdsr1ls[i2])*eval(hsdsr2ls[i2]),8)
        if hsd_rx==int(hsd_rx):
            hsd_rx = int(hsd_rx)
        hsd_rx = str(hsd_rx)
        hsd_rxls.append(hsd_rx)
    for i3 in range(len(hsd_rxls)):                                #计算urx
        hsd_urx = round(eval(hsd_rxls[i3])*eval(hsdsr0)*0.01,8)
        if hsd_urx==int(hsd_urx):
            hsd_urx = int(hsd_urx)
        hsd_urx = str(hsd_urx)
        hsd_urxls.append(hsd_urx)
    konghang()
    print('计算结果：')
    print('表格：')
    shuchu('比率臂K',hsdsr1ls)
    shuchu('比较臂R0',hsdsr2ls)
    shuchu('Rx',hsd_rxls)
    shuchu('n',hsdsr3ls)
    shuchu('ΔR0',hsdsr4ls)
    shuchu('S',hsd_sls)
    shuchu('Urx',hsd_urxls)
    print('等式：')
    for i4 in range(len(hsd_rxls)):
        print(hsd_rxls[i4],'±',hsd_urxls[i4],'Ω')
#液晶的电光效应
def yjdgxy():
    print('hello')
#太阳能电池基本特性测定
def tyndc():
    print('python')
#备用实验函数
def by1():
    print('备用实验选项，暂未添加内容')
#备用实验函数
def by2():
    print('备用实验选项，暂未添加内容')
#用户界面引导和提示，引用实验计算和绘图函数，程序主体
def main():                                                         #主函数
    print('1 惠斯登电桥测电阻')
    print('2 液晶的电光效应')
    print('3 太阳能电池基本特性测定')
    print('4 备用')
    print('5 备用')
    xzsy=input('请输入实验编号(每次输入完成回车结束):')
    konghang()
    if eval(xzsy) in [1,2,3]:                                       #若为已知实验输出。规范格式，提示防止误输入。
        print('注意:输入多个数据时每个数据用一个或多个空格分隔')
        print('注意:输入格式错误将导致程序运行不正常')
        print('原始数据输入完成后将在此对话框显示计算结果')
        print('需要绘图时会弹出图像，有多个图像时关闭第一个图像后显示后序图像')
        print('数据计算保留一位可疑数字，图像为拟合曲线，请用ctrl+c或+v复制或粘贴')
    if xzsy=='1':
        hsddq()
    elif xzsy=='2':
        yjdgxy()
    elif xzsy=='3':
        tyndc()
    elif xzsy=='4':
        by1()
    elif xzsy=='5':
        by2()
    else:
        print('输入内容有误，请重新启动程序')
    konghang()
    input('程序运行结束，请输入任意内容退出程序')
try:                                                                 #总异常处理
    main()
except:                                                              #总异常处理
    konghang()
    input('输入内容有误，请输入任意内容退出程序后重启程序')
