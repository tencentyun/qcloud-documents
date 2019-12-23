## 适用场景
已创建但未开启 COS 的集群，因业务需要需开启 COS 时。

## 操作说明
### 步骤一：查看 COS 访问密钥
在 [密钥管理](https://console.cloud.tencent.com/cam/capi) 获取 SecretId 和 SecretKey。
![](https://main.qcloudimg.com/raw/5dd2c7f85e2c4de158e7a7ed369c96d7.png)

### 步骤二：获取存储桶内文件下载路径
在 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket) 创建一个新存储桶或选择一个已有的存储桶，进入存储桶文件管理页。EMR 控制台自助开启 COS 时需要提供一个测试验证地址，用于检测 SecretId 和 SecretKey 的正确性，因此应该保证填写的 SecretId 和 SecretKey 对应账号下存在至少一个可下载的真实文件。

例如，存储桶根目录下有一个`t1.txt`文件，可将该文件的对象地址填写到测试验证地址处。进入存储桶文件列表，单击某一文件的【详情】进入文件详情页，复制文件对象地址。
![](https://main.qcloudimg.com/raw/b8be82043b35f7943c1917d7d15e9047.png)![](https://main.qcloudimg.com/raw/47de70f74612f574ef23f38149d83281.png)

### 步骤三：在集群中设置 COS
1. 进入 [EMR 控制台](https://console.cloud.tencent.com/emr)，在【集群列表】中单击集群 ID 进入集群实例详情页。
![](https://main.qcloudimg.com/raw/e4805873879b968bee6de910387d489d.png)
2. 在【软件信息】>【COS 访问】中单击【设置】。
![](https://main.qcloudimg.com/raw/0a5a7388df63bb6b12c0762c933bb150.png)
3. 在弹出框中填写前两步获取的 SecretId、SecretKey 和测试验证地址，然后单击【确认】。
![](https://main.qcloudimg.com/raw/56bc66c8fe93ad6515b97de3cc53270d.png)

### 步骤四：测试
在 master 节点命令行执行以下命令查看存储桶文件。
```
[root@172 ~]# su hadoop
[hadoop@172 root]$ hadoop fs -ls cosn://{bucket-name}/
Found 8 items
-rw-rw-rw-   1 hadoop hadoop       1366 2019-07-17 18:51 cosn://{bucket-name}/README.txt
drwxrwxrwx   - hadoop hadoop          0 1970-01-01 08:00 cosn://{bucket-name}/emr
drwxrwxrwx   - hadoop hadoop          0 1970-01-01 08:00 cosn://{bucket-name}/flume
drwxrwxrwx   - hadoop hadoop          0 1970-01-01 08:00 cosn://{bucket-name}/hive
-rw-rw-rw-   1 hadoop hadoop   95169691 2019-06-25 20:28 cosn://{bucket-name}/spark-test.jar
drwxrwxrwx   - hadoop hadoop          0 1970-01-01 08:00 cosn://{bucket-name}/test
drwxrwxrwx   - hadoop hadoop          0 1970-01-01 08:00 cosn://{bucket-name}/test2
drwxrwxrwx   - hadoop hadoop          0 1970-01-01 08:00 cosn://{bucket-name}/usr
```
