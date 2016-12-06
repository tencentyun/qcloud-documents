#coding:utf-8
try:
    import rmarshal as marshal
except:
    import marshal
"""
r=open('vstation_vsScheduler_3_20161202.log')
f=r.read().splitlines()
a=0  #耗时大于0.4s SQL所用时间之和
b=0  #小于0.4s SQL 所用时间只和
u=0
uc=0
for i,t in enumerate(f):
    if 'hooked_query' in t and 'None' not in t and 'HOOK' not in t and 'cost' not in t:
           try:
              n=float(t.split(" ")[1])
           except:
              continue
           if  n>0.4:
               a+=n 
               if 'update t_host_resource set' in f[i-2]: # 输出耗时大于0.4秒的SQL
                  u+=n
                  uc+=1        
           else:
               b+=n
"""


class a():
    b=None
    c="ccc"
    pass

def entry_point(argv):

    v=[]
    for i in range(10000):
        v.append(a())
    v[1].b=v[2]
    v[2].b=v[1]
    print v[1].b.b.b.b.b.b.b.b.b.b.b.b.b.c 
    print marshal.dumps("{'a':3}")
    return 0

# _____ Define and setup target ___

def target(*args):
    return entry_point, None

if __name__ == '__main__':
      import sys
      entry_point(sys.argv)
#print a
#print b
#print u 
#print uc
