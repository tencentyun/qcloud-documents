## 简介

当您要快速了解日志服务（Cloud Log Service，CLS）的各项功能，但自己没有资源上手操作时，可通过 CLS 提供的 Demo 日志进行体验。

>? Demo 日志免收流量费用与存储费用，请放心体验。
>

| Demo 日志           | 说明                                                         |
| :----------------- | :----------------------------------------------------------- |
| 负载均衡 CLB        | 包含 CLB 访问日志 Demo，提供检索、仪表盘、告警模板              |
| Nginx 日志          | 包含 Nginx ingress 访问日志 Demo，提供检索、仪表盘、告警模板   |
| 容器服务 TKE        | 包含 TKE 审计日志 Demo、TKE事件日志Demo，提供检索、仪表盘、告警模板 |
| 内容分发网络 CDN    | 包含 CDN 访问日志 Demo，提供检索、仪表盘、告警模板              |
| 网络流日志 Flowlogs | 包含弹性网卡 ENI 网络流日志 Demo，云联网 CCN 网络流日志 Demo，提供检索、仪表盘、告警模板 |
| 对象存储 COS        | 包含 COS 访问日志 Demo，提供检索、仪表盘、告警模板              |


## 使用 Demo

### 开启 Demo

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls/overview)。
2. 在**概览**页面的**日志中心**中，找到想要体验的Demo，并单击**开启Demo**。
![](https://qcloudimg.tencent-cloud.cn/raw/4a7183864e49193ae76948b1539bc712.png)
3. 在弹出的提示框中，单击**确认**。
资源初始化过程需约等待2分钟。
![](https://qcloudimg.tencent-cloud.cn/raw/d451c8679b6e49f432ebdf914fc19c8f.png)
4. 初始化完成后，可以执行如下操作：
 - 单击 **Demo 内容 > 进入检索页**，查看检索分析详情。
 - 单击 **Demo 内容 > 查看仪表盘**，查看预置仪表盘。
 - 单击 **Demo 内容 > 查看告警**，查看监控告警详情。
 - 单击 **Demo 内容 > 查看日志主题**，查看日志主题详情。

### 重置 Demo

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls/overview)。
2. 在**概览**页面的**日志中心**中，找到对应Demo，并单击 **Demo 内容 > 重置 Demo**。当 Demo 日志过期时，可以通过重置再次启用。
![](https://qcloudimg.tencent-cloud.cn/raw/ebe535082785cef371518416f39f38f7.png)

### 关闭 Demo

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls/overview)。
2. 在**概览**页面的**日志中心**中，找到对应 Demo，并单击 **Demo 内容 > 删除 Demo**。
3. 在弹出的提示框中，单击**确认**，Demo 日志停止写入，且删除 Demo 资源。
