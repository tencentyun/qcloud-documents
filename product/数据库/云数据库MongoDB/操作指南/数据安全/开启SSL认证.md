## 操作场景

SSL（Secure Sockets Layer）认证是指客户端到云数据库服务器端的认证访问，对用户和服务器进行认证，对传送的数据进行加密或隐藏，保障数据传输过程的安全，防止数据在网络传输过程中被截取、篡改、窃听， 满足数据安全敏感客户的合规需求 。

## 计费说明

开启SSL，不收费任何费用，您可免费使用。

## 使用前须知

- 开启SSL过程中，需要重启实例，请在业务低峰期进行，或确保应用有重连功能。
- 开启SSL访问，保障数据访问及传输的安全，可能会略影响实例性能。
- 开启SSL之后， 证书过期前30天、15天、3天发送过期事件告警，请注意及时刷新SSL证书，否则无法通过SSL证书认证访问。

## 版本说明

 支持副本集与分片集群4.0、4.2、4.4版本。

## 前提条件

- 数据库实例状态：运行中，无其他任务执行。
- 当前为业务低峰时刻，或客户端具有自动重连机制。

## 操作步骤

1. 登录 [MongoDB 控制台](https://console.cloud.tencent.com/mongodb)。

2. 在左侧导航栏 **MongoDB** 的下拉列表中，选择**副本集实例**或者**分片实例**。副本集实例与分片实例操作类似。

3. 在右侧实例列表页面上方，选择地域。

4. 在实例列表中，找到目标实例。

5. 在目标实例的 **实例 ID / 名称** 列，单击蓝色字体的实例ID，进入**实例详情**页面。

6. 单击**数据安全**页签，再选择**访问加密**页签。

7. 在**开启SSL**后面，单击<img src="https://qcloudimg.tencent-cloud.cn/raw/84853fe19aa340a98cc138f8d951ddb9.png" style="zoom: 25%;" />。

8. 在**提示**对话框，了解开启SSL的影响，单击**确定**。

   ![](https://qcloudimg.tencent-cloud.cn/raw/b46c6404a27d3b9a361484b34c0fb60a.png)

9. 等待**开启SSL**的状态为**已开启**，单击**下载证书**。

   如果收到证书到期的告警信息，证书已经到期无效，请先单击**刷新证书**，更新证书文件。

   <img src="https://qcloudimg.tencent-cloud.cn/raw/459637e4bd877c2fe738b54d4b909d72.png" style="zoom:67%;" />

10. 在页面左下角，将获取到的证书**MongoDB-CA.crt**放在客户端。

11. 通过Shell方式或SDK访问数据库，可参见[连接 MongoDB 数据库](https://cloud.tencent.com/document/product/240/7092)。

    ```
    ./bin/mongo -umongouser -plxh***** 172.xx.xx.xx:27017/admin --ssl --sslCAFile MongoDB-CA.crt --sslAllowInvalidHostnames
    ```

    
