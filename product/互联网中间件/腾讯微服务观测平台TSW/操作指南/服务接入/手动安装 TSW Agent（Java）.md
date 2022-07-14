## 操作场景
使用官方提供的 TSW Agent 可快速接入 Java 应用。TSW Agent 提供三种安装方式，您可依据自身需求及应用环境选择适合的接入形式。本文介绍手动安装 TSW Agent（Java）的操作流程。

| 安装方式 | 适用场景 | 预计耗时 |
| ----- |---- |--- |
| [脚本接入](https://cloud.tencent.com/document/product/1311/51599#脚本接入) | 新手用户 | 1分钟 |
| [简单手动接入](https://cloud.tencent.com/document/product/1311/51599#简单手动接入) | 本机网络与公网不通的新手用户 | 3分钟 |
| [手动安装](#手动安装) | 对链路追踪、Opentracing 类链路追踪产品有一定理解的用户 | 5分钟 |


## 前提条件[](id:手动安装)
已安装 JDK，建议升级至1.8.X最新版本使用。

## 操作流程
1. 下载 TSW Agent（[下载链接](https://tsw-agent-1300555551.cos.ap-guangzhou.myqcloud.com/tsw-client-package.zip)）。建议下载到用户 PC 上快速操作配置。
2. 解压 tsw-client-package.zip 压缩包。
3. 进入 tsw-client-package\config，打开 agent.conf 以编辑。
4. 修改 agent.service_name、sender.etl_ip、sender.etl_port、sender.token。其中，agent.service_name 需要修改为应用程序包名。
私网接入点的，可通过 Skywalking 接入方式中的私网接入点获取。sender.etl_ip 使用域名，sender.etl_port 使用端口号。
sender.token 可通过 TSW 控制台【[接入服务](https://console.cloud.tencent.com/tsw/service-access?rid=1) 】界面中的脚本复制，token 的位置如下图所示。
![](https://main.qcloudimg.com/raw/b36ce10a1b150814749e3b1f029ccab4.png)
5. 完成修改后，将 tsw-client-package 复制/SCP 到主机的应用程序目录下。启动/重启应用同时，启动 agent。启动脚本可参考：
`nohup java -javaagent:{absolute_path}/tsw-client-package/tsw-agent.jar -jar {absolute_path}/Order-Service.jar &`

## 接入验证
向应用发送请求，在收到响应后，在 TSW 控制台查看调用数据。
您可以在1分钟内通过【链路追踪】>【调用链查询】>【[Span查询](https://console.cloud.tencent.com/tsw/trace?rid=1&tab=span)】查找调用详情。监控曲线与统计数据将在1分钟后开始正常显示。
