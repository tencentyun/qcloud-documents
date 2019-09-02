
在腾讯云云服务器（CVM）中可用 MongoDB 提供的 shell 客户端 （[查看安装文档](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-linux/)）连接腾讯云 MongoDB 服务进行数据管理，请注意使用最新版本的 MongoDB 客户端套件。

### 快速开始
典型的连接命令如下：
```
mongo 10.66.187.127:27017/admin -u mongouser -p thepasswordA1
```
如图：
![典型的连接命令截图示例](https://mc.qcloudimg.com/static/img/ce6b26f8cd6b1cc2981bc0cd44f9d09d/shell_default.png)

### 多种认证方式的连接说明
在 [连接示例](https://cloud.tencent.com/doc/product/240/3563) 文档中有说明，腾讯云 MongoDB 默认提供了 “rwuser” 和 “mongouser” 两个用户名分别支持 “MONGODB-CR” 和 “SCRAM-SHA-1” 两种认证方式。
对于这两种认证方式，shell 令的参数是不一样的，具体请看下文。

### SCRAM-SHA-1 认证（mongouser）
**默认用户 “mongouser” 以及在控制台创建的所有新用户都使用 SCRAM-SHA-1 认证**，其 shell 连接参数与 [快速开始](#.E5.BF.AB.E9.80.9F.E5.BC.80.E5.A7.8B) 章节完全一样，无需添加额外参数，示例如下：
```
mongo 10.66.187.127:27017/admin -u mongouser -p thepasswordA1
```
特殊的，如果您希望连接 MongoDB 服务后直接进入到某一个 db，例如 “singer”，请按示例操作：
```
mongo 10.66.187.127:27017/singer -u mongouser -p thepasswordA1 --authenticationDatabase admin
```
如图：
![直入某个db的连接命令截图示例](https://mc.qcloudimg.com/static/img/c30cc3e6e2db6c8bd3cce2e327ce63db/sha1_sonedb.png)

### MONGODB-CR 认证（rwuser）
**请注意，只有默认用户 “rwuser” 使用 MONGODB-CR 认证**，其 shell 连接参数需要指明认证方式为 MONGODB-CR，请看示例：
```
mongo 10.66.187.127:27017/admin -u rwuser -p thepasswordA1 --authenticationMechanism=MONGODB-CR
```
如图：
![MONGODB-CR认证截图示例](https://mc.qcloudimg.com/static/img/ff200b49c3fa5c70812027dd89e3ebc3/cr_default.png)
特殊的，如果您希望连接 MongoDB 服务后直接进入到某一个 db，例如 “singer”，请按示例操作：
```
mongo 10.66.187.127:27017/singer -u rwuser -p thepasswordA1 --authenticationMechanism=MONGODB-CR --authenticationDatabase admin
```
如图：
![直入某个db的连接命令截图示例](https://mc.qcloudimg.com/static/img/d31bfa612a295fd070ea5dd09c7ce6a3/cr_somedb.png)

### 使用 shell 进行数据导入和导出
上文所述的两种认证方式都可以在 shell 里进行数据导入和导出， [参见这里](https://cloud.tencent.com/doc/product/240/5321)。
