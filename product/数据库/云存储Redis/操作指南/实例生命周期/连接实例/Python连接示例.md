**运行前必备**：
下载并安装 [redis-py](https://github.com/andymccurdy/redis-py?spm=5176.730001.3.11.WvETSA)。

**示例代码**：

```
#!/usr/bin/env python 
#-*- coding: utf-8 -*- 
import redis 

#这里替换为连接的实例 host 和 port 
host = '192.168.0.195' 
port = 6379 

#这里替换为实例 ID 和实例 password 
user='username' 
pwd='password' 

#连接时通过 password 参数指定 AUTH 信息，由 user,pwd 通过":"拼接而成 
r = redis.StrictRedis(host=host, port=port, password=user+':'+pwd) 

#连接建立后就可以进行数据库操作，请参见 https://github.com/andymccurdy/redis-py 
r.set('name', 'python_test'); 
print r.get('name')
```

**运行结果**：
![](//qzonestyle.gtimg.cn/qzone/vas/opensns/res/img/Pythpon-1.png)
