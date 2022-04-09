#引用第三方库，用于绘制拟合曲线
import matplotlib.pyplot as plt
import numpy as np
#将拟合曲线设置为中文
from matplotlib.pylab import style
style.use('ggplot')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
#导入decimal模块中的Decimal函数实现保留小数时实现标准四舍六入五成双
from decimal import Decimal
#通用绘制拟合曲线函数
def nhqx(nh1,nh2,nh3,nh4,nh5,nh6,nhcs=10):
    fig = plt.figure(figsize=(7, 7))
    x = nh1                                                         #nh1应为数字列表
    y = np.array(nh2)                                               #nh2应为数字列表
    z1 = np.polyfit(x, y, nhcs)                                     #nhcs为正整数，建议8，10，12,默认10
    p1 = np.poly1d(z1)
    yvals = p1(x)
    plt.plot(x, y, '*', label='原始数据')
    plt.plot(x, yvals, 'r', label='拟合曲线')
    plt.xlabel(nh3)                                                 #nh3为字符串，函数横坐标物理量，注意加单位
    plt.ylabel(nh4)                                                 #nh4为字符串，函数纵坐标物理量，注意加单位
    plt.legend(loc=nh5)                                             #nh5为数字1,2,3,4之一，对应位置右上,左上,左下,右下
    plt.title(nh6)                                                  #nh6为字符串，图像标题
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
def shuchu(mz,mgls):                                             #通用输出内容函数，参数为输出项目，输出列表
    print(mz,end='：')
    for isc in mgls:
        print(isc,end='  ')
    print()
def konghang():                                                  #通用空行函数
    print()
    print()
    print()
def lsbsz(zfcls):                                                #返回字符串列表转换的数字列表
    linshils = []
    for izfc in zfcls:
        linshils.append(eval(izfc))
    return linshils
def lsbzfc(zfcls):                                               #返回数字列表转换的字符串列表
    linshils = []
    for isz in zfcls:
        linshils.append(str(isz))
    return linshils
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
    yjyz1 = ['0','0.5','0.8','1.0','1.2','1.3','1.4','1.5','1.6','1.7','2.0','3.0','4.0','5.0','6.0']
    yjyz2 = ['0','5','10','15','20','25','30','35','40','45','50','55','60','65','70','75','80','85']
    print('液晶光开关的电光特性：')
    yjsr1 = input('请输入15个透视率数据：')
    print('液晶光开关的视觉特性(水平方向)：')
    print('正角度：')
    yjsr2 = input('请输入18个Tmax数据：')
    yjsr3 = input('请输入18个Tmin数据：')
    print('负角度：')
    yjsr4 = input('请输入18个Tmax数据：')
    yjsr5 = input('请输入18个Tmin数据：')
    print('液晶光开关的视觉特性(垂直方向)：')
    print('正角度：')
    yjsr6 = input('请输入18个Tmax数据：')
    yjsr7 = input('请输入18个Tmin数据：')
    print('负角度：')
    yjsr8 = input('请输入18个Tmax数据：')
    yjsr9 = input('请输入18个Tmin数据：')
    yjsr1ls = yjsr1.split()
    yjsr2ls = yjsr2.split()
    yjsr3ls = yjsr3.split()
    yjsr4ls = yjsr4.split()
    yjsr5ls = yjsr5.split()
    yjsr6ls = yjsr6.split()
    yjsr7ls = yjsr7.split()
    yjsr8ls = yjsr8.split()
    yjsr9ls = yjsr9.split()
    tt1ls = []
    tt2ls = []
    tt3ls = []
    tt4ls = []
    for i1 in range(18):
        tt1 = yxchu(yjsr2ls[i1],yjsr3ls[i1])
        tt1ls.append(tt1)
    for i2 in range(18):
        tt2 = yxchu(yjsr4ls[i2],yjsr5ls[i2])
        tt2ls.append(tt2)
    for i3 in range(18):
        tt3 = yxchu(yjsr6ls[i3],yjsr7ls[i3])
        tt3ls.append(tt3)
    for i4 in range(18):
        tt4 = yxchu(yjsr8ls[i4],yjsr9ls[i4])
        tt4ls.append(tt4)
    #逆序输出图片
    yjyz1ht = lsbsz(yjyz1)
    yjsr1lsht = lsbsz(yjsr1ls)
    yjht1 = [-85,-80,-75,-70,-65,-60,-55,-50,-45,-40,-35,-30,-25,-20,-15,-10,-5,0,
               0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85]
    tt1lsht = lsbsz(tt1ls)
    tt2lsht = lsbsz(tt2ls)
    tt3lsht = lsbsz(tt3ls)
    tt4lsht = lsbsz(tt4ls)
    tt2lsht.reverse()
    yjht2 = tt2lsht + tt1lsht
    tt4lsht.reverse()
    yjht3 = tt4lsht + tt3lsht
    nhqx(yjht1, yjht2, u'角度(°)', u'对比度', 1, u'对比度-角度(垂直方向)')
    nhqx(yjht1, yjht3, u'角度(°)', u'对比度', 1, u'对比度-角度(水平方向)',nhcs=20)
    nhqx(yjyz1ht,yjsr1lsht,u'供电电压U(V)',u'透射率(%)',1,u'透射率-供电电压')
    plt.show()
    konghang()
    print('计算结果：')
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
        print('注意:输入多个数据时每个数据用一个或多个空格分隔,输入只能为纯数字')
        print('注意:输入格式错误或绘图横纵坐标数量不一致将导致程序运行不正常')
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