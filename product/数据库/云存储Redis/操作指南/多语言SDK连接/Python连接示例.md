
本文列举客户端 Python 代码示例，辅助您通过 SSL 加密或不加密方式访问数据库。

## 准备工作
- 在 [Redis 控制台](https://console.cloud.tencent.com/redis) 的**实例详情**页面的**网络信息**区域，获取连接数据库的**内网IPv4地址**及端口。具体信息，请参见 [查看实例详情](https://cloud.tencent.com/document/product/239/75437)。
- 已获取访问数据库的账号与密码。具体操作，请参见 [管理账号](https://cloud.tencent.com/document/product/239/36710)。
- 下载并安装 [redis-py](https://github.com/andymccurdy/redis-py?spm=5176.730001.3.11.WvETSA)，推荐使用最新版本。
- 如果使用 SSL 加密方式连接数据库，请 [开通 SSL 加密](https://cloud.tencent.com/document/product/239/75865)，获取 SSL 认证证书文件。

## 未开通 SSL 加密方式连接示例
您需要根据注释修改参数：连接数据库的 IP、端口及账号密码信息。
```
#!/usr/bin/env python3
#-*- coding: utf-8 -*- 
import redis 

#这里替换为连接的实例 host 和 port 
host = '192.xx.xx.195' 
port = 6379 

#这里替换为实例 ID 和实例 password 
user='username' 
pwd='password' 

#连接时通过 password 参数指定 AUTH 信息，如果通过默认帐号连接，password 为 pwd， 如果自定义帐号连接，需将 user, pwd 通过@拼接
r = redis.StrictRedis(host=host, port=port, password=user+'@'+pwd) 

#连接建立后就可以进行数据库操作，请参见 https://github.com/andymccurdy/redis-py 
r.set('name', 'python_test'); 
print r.get('name')
```

 **运行结果**：
![img](https://main.qcloudimg.com/raw/b819ac84617439c8dcb107b0d7f4c641.png) 

## 通过 SSL 加密方式连接示例
您需要根据注释修改参数：SSL 证书文件、连接数据库的 IP、端口及账号密码信息。
```
import redis3 as redis3

if __name__ == "__main__":
# vip 为连接数据库的内网 IPv4 地址，6379为默认的端口号，pwd 为默认账号的密码，ca.pem 为获取的 SSL 证书文件，您需根据实际情况替换。
    client = redis3.Redis(host="vip", port=6379, password="pwd", ssl=True, ssl_cert_reqs="required",
                          ssl_ca_certs="ca.pem")
    print(client.ping())
```

