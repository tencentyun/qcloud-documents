## 实例改名
用户可根据业务需要修改实例名称，具体操作如下所示：
![](https://main.qcloudimg.com/raw/0cffc15e8492c67596768921c809f5ee.png)
![](https://main.qcloudimg.com/raw/50f948972ab3b5fdf9950780dddc49e7.png)
## Oplog容量调整
实例购买时默认Oplog容量是整个实例存储容量的10%，在使用过程中，为防止Oplog被冲导致回档失败，可根据需要调整Oplog大小,最大可扩容至实例容量的90%。具体操作如下所示：<br>
![](https://main.qcloudimg.com/raw/cbea67ae9f7f158ca3227932c4025022.png)
![](https://main.qcloudimg.com/raw/960b2ebc7da3c4dec5b1a8c4218df8d0.png)
## 实例扩容
随着业务的发展，现有MongoDB的实例配置可能无法满足业务需求，用户可在控制台扩容实例。扩容包括计算资源扩容和存储扩容。用户可选择扩容至更高的节点规格和更大的节点容量。由于Oplog是Capped Collections，过小容易被冲，所以建议，实例扩容时同时扩容Oplog容量。具体操作如下所示：
![](https://main.qcloudimg.com/raw/1431188010f656c90d2e11b32a56ef5f.png)
![](https://main.qcloudimg.com/raw/1dd06176d8544498d331cbfd985ccbb5.png)
## 实例重启 
实例重启包括mongos重启和mongod重启。重启mongod的同时如果正在数据写入，可能会造成rollback进而丢失数据。重启mongos和mongod均会出现连接闪断，均为高危操作，建议停止业务后进行操作。用户如需重启实例操作，请提工单操作或者申请白名单。
## 实例销毁 
按量计费MongoDB实例支持自助销毁，具体操作如下所示：
![](https://main.qcloudimg.com/raw/7fb099ff4aa63a1160b055cfdca31144.png)
![](https://main.qcloudimg.com/raw/794a7d20867d683e9899a00c71876b18.png)
## 账号管理
进入实例管理页面，点击进入“账号管理”子页，具体操作如下所示：
![](https://main.qcloudimg.com/raw/5e7458e70608b906fb3c60b61d46c5f1.png)
### 账号列表 
账号列表页会列举出所有的账号详细信息，包括账号名、认证方式、创建时间、修改时间和可以进行的操作，具体操作如下所示：
![](https://main.qcloudimg.com/raw/e7f782bcf58ed15deb14d0c8790d879c.png)
### 新建账号 
可新建一个账号并对库表授权。具体操作如下所示：
![](https://main.qcloudimg.com/raw/81e67382632e8771bdcb0a83360233d4.png)
![](https://main.qcloudimg.com/raw/a9b9f75e2ebdb951fc53f8d03d1b7fdc.png)
### 修改账号密码 
具体操作如下所示：
![](https://main.qcloudimg.com/raw/44216a3a917742837d0abdf10ee1b530.png)
![](https://main.qcloudimg.com/raw/f0f9f6022ee8d1b5b2c5b8600340a2d1.png)
### 删除账号 
具体操作如下所示：
![](https://main.qcloudimg.com/raw/201f5cdfc8f83e2fffcca39c6d99ed10.png)
![](https://main.qcloudimg.com/raw/8fd633ef85ba6823645334083a3ccc1c.png)
### 修改账号授权 
具体操作如下所示：
![](https://main.qcloudimg.com/raw/5ffadc9ab1b93d6d3f474f1e2ad418b8.png)
![](https://main.qcloudimg.com/raw/e326bacaa202e1de6614c4396b3afce8.png)
