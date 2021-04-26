**Preparations before running**:

Download and install redis-py at
https://github.com/andymccurdy/redis-py?spm=5176.730001.3.11.WvETSA

**Sample Codes**:

```
#!/usr/bin/env python 
#-*- coding: utf-8 -*- 
import redis 

#Replace with the host and port of the connected instance 
host = '192.168.0.195' 
port = 6379 

#Replace with instance ID and instance password 
user='username' 
pwd='password' 

#Specify AUTH information using parameter password upon connection. It is a combination of user and pwd joined by ":". 
r = redis.StrictRedis(host=host, port=port, password=user+':'+pwd) 

#Once the connection is established, you can perform database operations. For more information, please see https://github.com/andymccurdy/redis-py 
r.set('name', 'python_test'); 
print r.get('name')
```

**Execution results**:
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Pythpon-1.png)
