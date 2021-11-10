>? HTTP 函数功能在全新升级中，后期会开放申请使用，您可以前往 [云函数介绍页](https://cloud.tencent.com/product/scf) 来了解最新进展。
>
## 操作场景
本文档介绍了如何快速创建一个 HTTP 函数，您可通过此教程了解 HTTP 函数创建过程及云函数控制台基本操作。



## 前提条件
已注册腾讯云账户。若未注册腾讯云账户，可 [点此](https://cloud.tencent.com/register) 进入注册页面。

## 操作步骤

### 创建函数
1. 登录 [SCF 控制台](https://console.cloud.tencent.com/scf/index?rid=1)，选择**广州**。
>!HTTP 函数目前仅支持**广州**地区。
>
2. 选择左侧导航栏**函数服务**，单击**新建**。如下图所示：
![img](https://main.qcloudimg.com/raw/3336661866d7dd0fce459b0d49fb9ee3.png)
3. 在“新建函数”页面，填写函数基础信息，单击**下一步**。如下图所示：
 - **函数类型**：选择 “HTTP”。
 - **函数名称**：填写 express-helloworld。
 - **运行环境**：选择 “Nodejs 8.9”。
 - **创建方式**：选择“模版函数”。
 - **模板搜索**：输入 Express 后按 “Enter” 进行搜索，选择 “Express” 模版。
![](https://main.qcloudimg.com/raw/f5758f5dc63b1527793edb3899177e43.png)
4. 函数配置保持默认，并单击**完成**。如下图所示：
![](https://main.qcloudimg.com/raw/0fa5b842f20ad3a48360b94a40ca19e8.png)
函数创建完成后，自动进入创建成功函数的“访问控制”页面，即可查看 HTTP 函数的访问路径 URL。如下图所示：
![](https://main.qcloudimg.com/raw/586eb7de3cb672c359fb9852b60d7031.png)

### 云端测试
在浏览器里打开该访问路径，显示 “hello from Express”，则说明函数创建成功。如下图所示：
![](https://main.qcloudimg.com/raw/688e56210f56513a9eeeddc0174d08b6.png)
您也可以使用其他 HTTP 测试工具，如 CURL、POSTMAN 等测试您已创建成功的 HTTP 函数。

### 查看日志
在已创建函数的详情页面，选择**运行日志**，即可查看函数详细日志。如下图所示：
![](https://main.qcloudimg.com/raw/6af3b878cd0f7d5a66bb3242f3f9f5e4.png)
更多关于日志信息请参见 [函数日志](https://cloud.tencent.com/document/product/583/36143)。

### 查看监控
在已创建函数的详情页面，选择**监控信息**，即可查看函数调用次数/运行时间等情况。
>!监控统计的粒度最小为1分钟。您需要等待1分钟后，才可查看当次的监控记录。
>
![](https://main.qcloudimg.com/raw/354cdde5c43ef17b60c0f7024451fd26.png)
更多关于监控信息请参见 [监控指标说明](https://cloud.tencent.com/document/product/583/32686)。
