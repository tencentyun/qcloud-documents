
本文将为您介绍如何为 Prometheus 监控配置公网地址。

## 实践步骤

### 步骤1：购买 Prometheus 实例

1. 登录 [Prometheus 监控服务控制台](https://console.cloud.tencent.com/monitor/prometheus)。
2. 单击左上角的**新建**，进入 Prometheus 购买页，可根据自己的实际情况购买对应的实例，详情请参见 [创建实例](https://cloud.tencent.com/document/product/1416/55982)。
3. 成功购买后，单击**实例名称**，进入实例基础信息页，获取 Prometheus IPV4 地址。
![](https://qcloudimg.tencent-cloud.cn/raw/1726226e2764f8e6beaa0f5a6c7d08dd.png)  


### 步骤2：申请 CLB 跨 VPC 功能（内测功能）
1. 进入 [负载均衡跨地域绑定2.0及混合云部署内测申请页](https://cloud.tencent.com/apply/p/y72ehzwbwzk)。
2. 根据填好资料，填写完后提交申请。
3. 提交完内测申请后，提单给 CLB，给账号特殊加白 CLB VPCGW 类型。


### 步骤3：新建公网 CLB 实例

1. 进入 [负载均衡控制台](https://console.cloud.tencent.com/clb/instance?rid=1)，新建 CLB 实例。
2. 根据提示选择并填写信息，具体操作说明可参考 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)（如已有公网的 CLB 实例，可不新建）。
3. 创建完后进入实例基本信息页，开启跨 VPC 功能。
![](https://qcloudimg.tencent-cloud.cn/raw/7289e37feb0fff32491b2314044d7114.png)


### 步骤4：绑定后端服务

1. 进入 [负载均衡实例详情页> 监听器管理](https://console.cloud.tencent.com/clb/detail?rid=1&id=lb-8kehv70k&tab=listener)。
2. 单击 TCP/UDP/TCP SSL/QUIC 监听器下的**新建**，可参考 [负载均衡监听器](https://cloud.tencent.com/document/product/214/6096) 操作指引新建监听器。
![](https://qcloudimg.tencent-cloud.cn/raw/c8a9ed5f3f51771bb259117f6c9b6221.png)
![](https://qcloudimg.tencent-cloud.cn/raw/ecaa41e8f931068db128783e40f51432.png)
3. 新建完监听器后，点击监听器名称。在子窗口中单击**绑定**，绑定后端服务。
 - 目标类型：选择其他内网 IP。
 - 默认端口：9090。
 - IP 地址：需填写步骤1获取的 Prometheus IPV4 地址。
![](https://qcloudimg.tencent-cloud.cn/raw/0f93ab155d3acabc8a0bbd2884a0055a.png)
![](https://qcloudimg.tencent-cloud.cn/raw/b9a3b7f29fa0455ae06083740cd7b397.png)
4. 单击**监听器名称**，查看是否监听正常监听正常。
![](https://qcloudimg.tencent-cloud.cn/raw/dc927c67c4c98d4f0251e7a12f47f6ec.png)


### 步骤5：测试是否配置成功

1. 查看公网 CLB 的地址，这里假设查看的地址为：192.168.1.1 。
![](https://qcloudimg.tencent-cloud.cn/raw/0c4d3286a3d4aac7343b0ef2276e62b9.png)
2. 查看监听配置端口。如下列端口为：8080。
![](https://qcloudimg.tencent-cloud.cn/raw/d1602a1bbba3a0e950d083e019b9d6bb.png)
根据上述两个信息，确定 Prometheus 转发的公网地址为如下新 IP:PORT 地址为：`192.168.1.1:8080` 。
3. 到浏览器或者机器上查看是否可以通过这个 IP 获取 UP 数据。
HTTP API 地址：
```
http://IP:PORT/api/v1/query?query=up
```
替换 IP:PORT  后如下：
```
http://81.71.21.123:9090/api/v1/query?query=up
```
4. 进入链接地址  `http://81.71.21.123:9090/api/v1/query?query=up` 。
 - 用户名：填写您的主账号 ID (APPID)。 
 - 密码：为身份临时访问凭证 Token，可通过 [GetFederationToken](https://cloud.tencent.com/document/product/1312/48195) 获取。
![](https://qcloudimg.tencent-cloud.cn/raw/d9a84c7fe94a880e0f8a4b1d9d428356.png)
如下图所示，Prometheus 配置公网地址成功。
![](https://qcloudimg.tencent-cloud.cn/raw/59d032eaf3593d9ab9c421d3d68ad73d.png)
