## 应用场景

数据安全审计 SaaS 型自6.0.2版本起，已支持自建 MySQL、MariaDB 的 SSL 加密审计。本文档对该功能的限制、配置、常见问题做必要说明。



## 功能限制

本功能限制如下：
- 仅支持自建的 MySQL、MariaDB，不支持云数据库，也不支持其他类型的数据库。
- 支持的协议版本及加密算法如下，其他协议及加密算法暂不支持。下方提供对应检测方式。
  - 支持的通信协议版本：TLS 1.2。
  - 支持的加密算法：TLS_RSA_WITH_AES_128_CBC_SHA 、TLS_RSA_WITH_AES_256_CBC_SHA 、TLS_RSA_WITH_AES_128_CBC_SHA256、 TLS_RSA_WITH_AES_256_CBC_SHA256。

## 检测方式[](id:JCFS)
### 步骤1：检测是否开启加密
1. 在数据库中，输入如下命令，确认是否开启了 SSL 加密。
```
show global variables like '%ssl%';
```
2. 若 have_ssl 的值为 YES，则表明已经开启了 SSL，需要关闭 SSL 后才能审计到。
```
dba:(none)> show global variables like '%ssl%';
+---------------+-----------------+
| Variable_name | Value           |
+---------------+-----------------+
| have_openssl  | YES             |
| have_ssl      | YES             |    #已经开启了SSL
| ssl_ca        | ca.pem          |
| ssl_capath    |                 |
| ssl_cert      | server-cert.pem |
| ssl_cipher    |                 |
| ssl_crl       |                 |
| ssl_crlpath   |                 |
| ssl_key       | server-key.pem  |
+---------------+-----------------+
```

### 步骤2：检测通信协议版本
1. 在数据库中，输入如下命令，检测通信协议版本。
```
show variables like "tls_version";
```
2. 若 tls_version 的值为 TLSv1.2，则表示是支持的，若包含其他值，如下所示则表示不支持，需要进行修改。
```
dba:(none)> show global variables like 'tls_version';
+---------------+----------------------+
| Variable_name | Value                |
+---------------+----------------------+
| tls_version   | TLSv1,TLSv1.1,TLSv1.2|    #不只包含TLSv1.2，是不支持的
+---------------+----------------------+
```

### 步骤3：检测加密算法
1. 在数据库中，输入如下命令，检测加密算法。
```
show global variables like 'ssl_cipher';
```
2. 若 ssl_cipher 的值中只包含 AES128-SHA、AES256-SHA、AES128-SHA256、AES256-SHA256四个中的一个或多个，则表示是支持的，否则表示不支持，需要进行修改。
```
dba:(none)> show global variables like 'ssl_cipher';
+---------------+-----------------+
| Variable_name | Value           |
+---------------+-----------------+
| ssl_cipher    |                 |     #此处为空，需要修改
+---------------+-----------------+
```

## 修改方式
通过修改数据库的相关配置，使数据安全审计可以审计到数据库语句。可根据实际情况，任意选择如下一种修改方式。

### 关闭 SSL 加密
MySQL 的 SSL 虽然提高了安全性，但也特性了部分性能。如果用户单位是否没有必须开启 SSL 加密的相同规定，可以考虑直接关闭 SSL 加密，一劳永逸。
>!该方法需要重启数据库。

1. 修改配置文件 my.cnf，在[mysqld]下增加如下内容：
```
# disable_ssl
skip_ssl
```
2. 输入如下指令，重启 MySQL。
```
service mysqld restart
```
3. 使用上述 [检测方式](#JCFS)，验证是否修改成功。
```
dba:(none)> show global variables like '%ssl%';
+---------------+-----------------+
| Variable_name | Value           |
+---------------+-----------------+
| have_openssl  | DISABLED        |
| have_ssl      | DISABLED        |    #已经关闭了SSL
| ssl_ca        | ca.pem          |
| ssl_capath    |                 |
| ssl_cert      | server-cert.pem |
| ssl_cipher    |                 |
| ssl_crl       |                 |
| ssl_crlpath   |                 |
| ssl_key       | server-key.pem  |
+---------------+-----------------+
```

### 设置通信协议和加密算法
在配置文件中，设置通信协议和加密算法，该方法可以对数据库的所有连接生效。
>!该方法需要重启数据库。

1. 修改配置文件my.cnf，在[mysqld]下增加如下内容：
```
# 设置通信协议
tls_version=TLSv1.2
# 设置加密算法
ssl_cipher="AES128-SHA:AES256-SHA:AES128-SHA256:AES256-SHA256"
```
2. 输入如下指令，重启 MySQL。
```
service mysqld restart
```
3. 使用上述 [检测方式](#JCFS)，验证是否修改成功。
```
dba:(none)> show global variables like 'tls_version';
+---------------+----------------------+
| Variable_name | Value                |
+---------------+----------------------+
| tls_version   | TLSv1.2|    #只包含TLSv1.2
+---------------+----------------------+
```
```
dba:(none)> show global variables like 'ssl_cipher';
+---------------+--------------------------------------------------+
| Variable_name | Value                                            |
+---------------+--------------------------------------------------+
| ssl_cipher    | AES128-SHA:AES256-SHA:AES128-SHA256:AES256-SHA256|     
+---------------+--------------------------------------------------+
```


### 在客户端连接时指定参数
若不想修改数据库配置，可以在客户端建立连接时，指定参数，如：
```
mysql -u root  -pxxxx -h10.3.1.17 --ssl-cipher=AES128-SHA --tls-version=TLSv1.2
```
>?该方法只针对本连接，不会影响其他连接。


