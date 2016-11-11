class mytime():
    month = {'01':31,'02':28,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
    l = ['01','02','03','04','05','06','07','08','09','10','11','12']

    #将2016-11-11转为20161111格式,返回int格式
    def get_time(self,st):
        nt = int(st.replace('-',''))
        return nt
    #将20161111转为2016-11-11格式
    def get_stime(self,nt):
        strt = str(nt)
        st = strt[0:4]+'-'+strt[4:6]+'-'+strt[6:]
        return st
    #获取每年每月对应的天数，返回字典格式
    def get_month(self,y1):
        if type(y1) == int:
            strt1 = str(y1)
        else:
            strt1 = y1
        month1 = self.month
        year1 = strt1[0:4]
        day1 = self.runnian(int(year1))
        if day1 == 366:
            month1['02'] = 29
        else:
            month1['02'] = 28
        return month1
    #将09格式转换为9
    def rezero(self,n):
        if n[0] == 0:
            n.replace('0','')
        return int(n)
    #判断是否是闰年，返回天数
    def runnian(self,year):
        y1 = year%4
        y2 = year%100
        y3 = year%400
        if y1 == 0 and y2>0:
            return 366
        elif y2 == 0 and y3 == 0:
            return 366
        else:
            return 365
    #获取两个时间相差的天数
    def get_days(self,t1,t2):
        year1 = str(t1)[0:4]
        year2 = str(t2)[0:4]
        mon1 = str(t1)[4:6]
        mon2 = str(t2)[4:6]
        day1 = str(t1)[6:8]
        day2 = str(t2)[6:8]
        m = self.rezero(mon1)-self.rezero(mon2)
        y = int(year1) - int(year2)
        v1 = [self.get_month(year1)[x] for x in self.l ]
        v2 = [self.get_month(year2)[x] for x in self.l]
        r1 = self.runnian(int(year1))
        r2 = self.runnian(int(year2))

        if y == 0:
            if m == 0:
                days = abs(self.rezero(day1)-self.rezero(day2))
            elif m == 1:
                days = self.rezero(day1)+self.month[mon2]-self.rezero(day2)
            elif m == -1:
                days = self.rezero(day2) + self.month[mon1] - self.rezero(day1)
            elif m>1:
                days = self.rezero(day1) +sum([v1[i] for i in range(self.rezero(mon2)-1,self.rezero(mon1)-1)])-self.rezero(day2)
            elif m<-1:
                days = self.rezero(day2) +sum([v1[i] for i in range(self.rezero(mon1)-1,self.rezero(mon2)-1)])-self.rezero(day1)
        #隔年天数计算
        elif y == 1:
            days = r2 - sum([v2[i] for i in range(0,self.rezero(mon2)-1)])-self.rezero(day2) + sum([v1[i] for i in range(0,self.rezero(mon1)-1)])+self.rezero(day1)
        elif y == -1:
            days = r1 - sum([v1[i] for i in range(0,self.rezero(mon1)-1)])-self.rezero(day1) + sum([v2[i] for i in range(0,self.rezero(mon2)-1)])+self.rezero(day2)
        #实现多年份天数计算
        elif y > 1:
            days = sum([self.runnian(x) for x in range(int(year2),int(year1))])- sum([v2[i] for i in range(0,self.rezero(mon2)-1)])-self.rezero(day2) + sum([v1[i] for i in range(0,self.rezero(mon1)-1)])+self.rezero(day1)
        elif y<-1:
            days = sum([self.runnian(x) for x in range(int(year1),int(year2))])- sum([v1[i] for i in range(0,self.rezero(mon1)-1)])-self.rezero(day1) + sum([v2[i] for i in range(0,self.rezero(mon2)-1)])+self.rezero(day2)
        return days
