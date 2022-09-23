## 操作场景
在使用 Mongo Shell 连接数据库时，您可以启用 SSL（Secure Sockets Layer）加密功能提高数据链路的安全性。通过 SSL 加密功能可以在传输层对网络连接进行加密，在提升通信数据安全性的同时，保障数据的完整性。

## 前提条件
- 申请与云数据库 MongoDB 实例在同一地域同一个 VPC 内的 Linux [云服务器 CVM](https://cloud.tencent.com/document/product/213/2936)。
- 已在**数据库管理**页面的**账号管理**页签获取访问数据库实例用户名与密码信息。具体操作，请参见 [账号管理](https://cloud.tencent.com/document/product/240/32721)。
- 已在**实例列表**获取访问数据库实例的内网 IP 地址与端口。具体操作，请参见 [实例详情](https://cloud.tencent.com/document/product/240/64595)。
- 实例已开启 SSL 加密功能，详情请参见 [开启 SSL 认证](https://cloud.tencent.com/document/product/240/74729)。

## 操作步骤
本案例以 Linux 操作系统为例演示具体操作流程。

1. 下载 SSL CA 证书，具体操作，请参见  [开启 SSL 认证](https://cloud.tencent.com/document/product/240/74729)。
2. 将证书文件 **MongoDB-CA.crt** 上传至安装有 Mongo Shell 的 CVM 服务器上。
3. 在安装有 Mongo Shell 的 CVM 服务器，执行以下命令连接 MongoDB 数据库。
>? Mongo 4.2及之后的版本，使用 TLS（Transport Layer Security）进行数据认证。TLS 是传输层安全性协议，是 SSL 升级版。在不确定使用 SSL 认证还是 TLS 认证时，可执行 `./mongo_ssl -h` 确认认证方式。
>
 - **SSL 认证**
```
./bin/mongo -umongouser -plxh***** 172.xx.xx.xx:27017/admin --ssl --sslCAFile MongoDB-CA.crt --sslAllowInvalidHostnames
```
其中，如下参数，请根据实际情况进行替换。
    - -u ：指连接数据库的用户名。
    - -p ：指用户名的密码。
    - 172.xx.xx.xx和27017分别指定 MongoDB 实例的连接 IP 地址（含端口号）。如忘记用户名与密码，请参见 [账号管理](https://cloud.tencent.com/document/product/240/32721) 查看修改账号密码信息。
    - --sslCAFile：指 SSL 认证的证书文件路径。
 - **TLS 认证**：
```
./bin/mongo -umongouser -plxh***** 172.xx.xx.xx:27017/admin --tls --tlsCAFile /data/MongoDB-CA.crt --tlsAllowInvalidHostnames 
```
 --tlsCAFile：指 TLS 认证的证书文件路径。
4. 连接成功提示信息如下所示。
```
MongoDB shell version v4.2.16
connecting to: mongodb://172.x.x.X:27017/admin?compressors=disabled&gssapiServiceName=mongodb
Implicit session: session { "id" : UUID("aeb18f32-6413-49da-864a-5123b4d2****") }
MongoDB server version: 4.2.11
Welcome to the MongoDB shell.
```

## 更多参考
更多语言 SDK 连接方式，请参见 [使用多语言 SDK 通过 SSL 认证连接数据库](https://cloud.tencent.com/document/product/240/76361)。
