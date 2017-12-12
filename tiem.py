import  time
ticks=time.time()
print ("now the time is", ticks)
localtime=time.localtime(time.time())
print("本地时间为",localtime)
asctime=time.asctime(localtime)
print("利用规范化函数的本地规范化时间为",asctime)

time2=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print("自定义格式化时间1",time2)

time3=time.strftime("%A %B %d %H:%M:%S %Y",time.localtime())
print("自定义格式化时间2：",time3)

print("这一天是这一年中的第",time.strftime("%j",time.localtime()),"天")

import calendar
cal=calendar.month(2017,11)
print("2017年11月的日历\n",cal)
