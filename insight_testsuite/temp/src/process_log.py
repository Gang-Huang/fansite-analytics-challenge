# program of fansite analytics
# !/usr/bin/env python

# importing the necessary module
import sys
import re
from collections import Counter
import operator
from datetime import datetime
import datetime as dt


#============================decoding the log.txt file==========================
host,timestamp,reply,request,byte,time_class,log,block=[],[],[],[],[],[],[],[]
req_bytes={}
def extract_data(filepath):
    f=open(filepath,'r',encoding="latin-1")
    for eachline in f:
        log.append(eachline)
        (tmp1,tmp2)=eachline.split(' - - ', 1)
        host.append(tmp1)
        timestamp.append(re.findall(r'\[([^]]*)\]', tmp2)[0])
        (tmp3, tmp4)=tmp2.split('" ', 1)
        (tmp5, tmp6)=tmp4.split(' ',1)
        reply.append(tmp5)
        if '-' in tmp6:
            tmp6='0'
        byte.append(tmp6)
        req=re.findall(r'\"\w*\s([^]]*)\"', tmp2)
        request.append(req[0] if req else [])
    f.close()
    return len(host)
#===============================================================================



#===================================TASK 1======================================
def task1(hosts):
    a=Counter(host).most_common(10)
    text_file = open(hosts, "w")
    for b in range(len(a)):
        text_file.write(a[b][0]+','+str(a[b][1])+'\n')
    text_file.close()
#===============================================================================



#===================================TASK 2======================================
def task2(resources):
    req_bytes={}
    for i in range(len(request)):
        if request[i]:
            if request[i] not in req_bytes:
                req_bytes.update({request[i]:int(byte[i])})
            else:
                req_bytes[request[i]]+=int(byte[i])  
    sorted_request=sorted(req_bytes.items(),key=operator.itemgetter(1),reverse=True)
    mixed_request=sorted_request[:10]
    text_file = open(resources, 'w')
    for j in mixed_request:
        text_file.write(j[0].replace(" HTTP/1.0","")+'\n')
    text_file.close()
#===============================================================================


#===================================TASK 3======================================
def task3(hours):
    for k in range(len(timestamp)):
        time_class.append(datetime.strptime(timestamp[k][:-6],'%d/%b/%Y:%H:%M:%S'))
       
    p1,p2=0,1
    busy_list=[]
    for i in range(10):
        busy_list.append([str(i),-1])

    length=len(time_class)      
    label=time_class[0]
    while label<=time_class[-1]:
        while time_class[p1]<label:
            if p1==length-1:
                break
            p1+=1
        while time_class[p2]<=label+dt.timedelta(0,3600):
            if p2==length-1:
                break
            p2+=1
        if p2<length-1:
            p2-=1
        nums=p2-p1+1
        if nums>busy_list[-1][1]:
            busy_list[-1]=(label,nums)
            busy_list=sorted(busy_list, key=lambda tup: tup[1],reverse=True)
        label+=dt.timedelta(0,1)

    text_file = open(hours, "w")
    for j in busy_list:
        if j[1]!=-1:
            text_file.write(j[0].strftime('%d/%b/%Y:%H:%M:%S -0400')+','+str(j[1])+'\n')
    text_file.close()
#===============================================================================


#-------------------------------------------------------------------------------
def printf(x):
    for k in range(x+1,len(host)):
        if (time_class[k]-time_class[x]).seconds/60<=5:
            if host[k]==host[x]:
                block.append(log[k])
        else:
            return
#-------------------------------------------------------------------------------


#===================================TASK 4======================================
def task4(blocked):
    dic={}
    report=[]
    rep={}
    past=datetime(1991, 3, 7, 0, 0, 0)
    for i in range(len(host)):
        if reply[i]=='401':
            if host[i] in dic:
                dic[host[i]]=[dic[host[i]][1],dic[host[i]][2],time_class[i]]
                if (time_class[i]-dic[host[i]][0])<=dt.timedelta(0,20):
                    report.append(i)
            else:
                dic.update({host[i]:[past,past,time_class[i]]})
        elif reply[i]=='200' and host[i] in dic:
            del dic[host[i]]



    for i in report:
        if host[i] not in rep:
            rep.update({host[i]:time_class[i]})
            printf(i)
        elif (time_class[i]-rep[host[i]]).seconds/60>=5:
            rep[host[i]]=time_class[i]
            printf(i)
              

    text_file = open(blocked, "w")
    for i in block:
        text_file.write(i)
    text_file.close()
#===============================================================================


def main(argv):
    filepath=argv[1]
    hosts=argv[2]
    resources=argv[4]
    hours=argv[3]
    blocked=argv[5]
    num=extract_data(filepath)
    task1(hosts)
    task2(resources)
    task3(hours)
    task4(blocked)
    

    
if __name__ == "__main__":
    main(sys.argv)
#==============================================================================
