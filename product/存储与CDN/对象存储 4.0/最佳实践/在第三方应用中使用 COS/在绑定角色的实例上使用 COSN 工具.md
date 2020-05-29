## 简介

目前，腾讯云的 [云服务器 CVM](https://cloud.tencent.com/document/product/213) 和 [黑石物理服务器 CPM](https://cloud.tencent.com/document/product/386) 都支持角色绑定，运行在 CVM 或 CPM 实例上的应用可以通过请求绑定的角色，来获取云资源的访问证书。本文以腾讯云对象存储 COS 为例，介绍 [Hadoop-COS](https://cloud.tencent.com/document/product/436/6884) 通过 CVM 和 CPM 的绑定角色，获取访问 COS 的访问证书，实现无明文密钥配置的大数据计算。

## 创建角色

1. 登录 [访问管理](https://console.cloud.tencent.com/cam/role) 控制台。
2. 单击【新建角色】，选择角色载体类别为【腾讯云产品服务】。
3. 指定角色的实例载体为【云服务器】或【黑色物理服务器1.0】，单击【下一步】。
   ![](https://main.qcloudimg.com/raw/ae804f5c09faeaf117f3513c8c0c5ae3.png)
4. 搜索并勾选 COS 存储桶的全读写访问策略 QcloudCOSFullAccess，为角色赋予权限，单击【下一步】。
   ![](https://main.qcloudimg.com/raw/ddcf92bae85927721f2941b7840db7c7.png)
5. 输入自定义指定角色名，单击【完成】，即可完成角色的创建。
   ![](https://main.qcloudimg.com/raw/48a97e242246c30a5eeb85cafc1b589e.png)

## 角色绑定实例

当角色创建完成，即可调用 [云 API](https://console.cloud.tencent.com/api/explorer)，将角色绑定到指定的云服务器 CVM 或黑石物理服务器 CPM 实例上。下面介绍 CVM 和 CPM 的绑定操作。

### 将角色绑定到 CPM 实例

1. 进入 [云 API](https://console.cloud.tencent.com/api/explorer) 页面。
2. 选择【黑石物理服务器】>【黑石物理服务器接口】> 【服务器绑定 CAM 角色】，然后依次填入 secretId，secretKey，以及待绑定的实例 ID、地域和角色名称。
![](https://main.qcloudimg.com/raw/c9a491a19ff10e3d213d8485f452c957.png)
3. 在右侧单击【在线调用】页签，进入在线调用页面。
4. 单击【发送请求】，即可绑定成功。

#### 验证角色绑定结果

1. 登录上述步骤申请的 [黑石物理服务器 CPM](https://console.cloud.tencent.com/cpm/cpm?rid=1)。
2. 执行`curl http://bm.metadata.tencentyun.com/meta-data/cam/security-credentials/$RoleName`，若返回如下结果，则说明绑定成功。如果绑定失败，通常会返回`404`错误。
![](https://main.qcloudimg.com/raw/319eb1e0dc7a2aa2983aaf0640338d2e.jpg)

### 将角色绑定到 CVM 实例

目前云服务器 CVM 还未正式对外发布角色绑定的 API 和控制台，因此在附件中提供了一个 CVM 角色绑定的 Python 脚本。用户依次填入鉴权密钥、实例 ID 以及角色名即可完成绑定。

#### 验证角色绑定结果

1. 登录 [云服务器 CVM](https://console.cloud.tencent.com/cvm/instance/index?rid=1)。
2. 执行`curl http://metadata.tencentyun.com/meta-data/cam/security-credentials/$RoleName`，如果正常返回密钥信息，则说明绑定成功。否则，返回`404`错误。

## Hadoop-COS 访问 COS 证书

此步骤介绍 Hadoop-COS 使用实例绑定的角色获取访问 COS 的证书。在已经绑定了角色的集群节点上，指定 hadoop-cos 的`fs.cosn.credentials.provider`的配置选项为：`org.apache.hadoop.fs.auth.CVMInstanceCredentialsProvider`或`org.apache.hadoop.fs.auth.CPMInstanceCredentialsProvider`，即可使得 Hadoop 在运行期间可以通过 CVM 或 CPM 绑定的角色来获取访问 COS 的证书信息，而无需再显式地指定明文密钥，配置如下所示。

```xml
...
    <property>
        <name>fs.cosn.credentials.provider</name>
        <value>org.apache.hadoop.fs.auth.CVMInstanceCredentialsProvider</value>
    </property>
...
```

执行`hadoop fs -ls -R cosn://<BucketName-APPID>/<路径>`即可测试 COS 访问是否正常。下面以名称为 examplebucket-1250000000 的存储桶为例演示：

```shell
hadoop fs -ls -R cosn://examplebucket-1250000000/
-rw-rw-rw-   1 root root       1087 2018-06-11 07:49 cosn://examplebucket-1250000000/LICENSE
drwxrwxrwx   - root root          0 1970-01-01 00:00 cosn://examplebucket-1250000000/hdfs
drwxrwxrwx   - root root          0 1970-01-01 00:00 cosn://examplebucket-1250000000/hdfs/2018
-rw-rw-rw-   1 root root       1087 2018-06-12 03:26 cosn://examplebucket-1250000000/hdfs/2018/LICENSE
-rw-rw-rw-   1 root root       2386 2018-06-12 03:26 cosn://examplebucket-1250000000/hdfs/2018/ReadMe
drwxrwxrwx   - root root          0 1970-01-01 00:00 cosn://examplebucket-1250000000/hdfs/test
-rw-rw-rw-   1 root root       1087 2018-06-11 07:32 cosn://examplebucket-1250000000/hdfs/test/LICENSE
-rw-rw-rw-   1 root root       2386 2018-06-11 07:29 cosn://examplebucket-1250000000/hdfs/test/ReadMe
```



