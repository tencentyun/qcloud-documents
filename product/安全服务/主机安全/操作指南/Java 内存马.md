本文档将为您介绍如何使用 Java 内存马功能。

## 概述
主机安全支持实时监控、捕捉 JavaWeb 服务进程内存中存在的未知 Class，结合腾讯云攻防经验及专家知识自动识别内存木马。若检测到 Java 内存马，系统会向您提供实时告警通知。

## 前提条件
Java 内存马属于主机安全旗舰版功能，须 [升级旗舰版](https://buy.cloud.tencent.com/yunjing) 才可使用该功能。
 

## 操作步骤
1. 登录 [主机安全控制台](https://console.cloud.tencent.com/cwp/defend/memShell)，在左侧导航栏，选择**高级防御** > **Java 内存马**，进入 Java 内存马页面。
2. 选择**插件配置**，插件配置是监测 Java 内存马的前提，您可对旗舰版主机进行插件的开启和关闭，并观测插件的具体运行状态。 
>?
>- 启用 Java 内存马插件后，主机安全会自动检测主机上 JavaWeb 服务进程，并注入检测探针到服务进程中，实时监控黑客通过漏洞、Shell 等注入的 Java 内存马。
>- 已成功注入 Java 内存马插件的主机，将实时监控、捕捉 JavaWeb 服务进程内存中存在的未知 Class，结合腾讯云攻防经验及专家知识自动识别内存木马。若检测到 Java 内存马，系统会向您提供实时告警通知。
>
![](https://qcloudimg.tencent-cloud.cn/raw/345008c8773f79fda6cd73f83b8ebe1d.png)
**字段说明：**
 - **启用/关闭插件**：Java 内存马插件默认关闭，支持用户手动设置开关，可单主机设置，也可多选主机批量设置。
 - **插件状态**：全部正常、存在异常、未开启。 
 - **首次开启时间**：指首次启用插件的时间。
 - **更新时间**：指近期启用或关闭插件的时间。
 - **详情**：可查看当前已注入的 Java 内存马插件运行状态，包括进程 PID、进程主类名、插件状态（注入中、注入成功、插件超时、插入退出、注入失败）、错误日志。
3.  启用 Java 内存马插件后，您可选择**事件列表**，可查看检测到的 Java 内存马事件，并进行相关处理操作。
![](https://qcloudimg.tencent-cloud.cn/raw/7ac0c40f76d2c15debcf44e75fdd57b4.png)
**字段说明：**
 - **Java 内存马类型**：包括 Filter 型、Listener 型、Servlet 型、Interceptors 型、Agent 型、其他。
 - 说明：归纳说明 Java 内存马的概况。
 - **首次发现时间**：该 Java 内存马首次被检测到的时间。
 - **最近检测时间**：近期检测发现该 Java 内存马仍存在的时间。
 - **状态**：待处理、已处理、已忽略。
 - **操作**：
     - 单击**详情**可查看该内存马事件详情。
![](https://qcloudimg.tencent-cloud.cn/raw/530c20d062821aadf9bd312a6a5c52a0.png)
     - 单击 Java 内存马详情中的**查看文件**，可查看落地文件的反编译 Java 文件，支持复制，支持下载反编译 Java 文件或原 Class 文件。
![](https://qcloudimg.tencent-cloud.cn/raw/71b8348c6454d7d4bda95430c8ed0d22.png)
     - 单击**处理**可对事件进行标记已处理、忽略、删除记录操作，可单事件处理，也可多选事件批量处理。
![](https://qcloudimg.tencent-cloud.cn/raw/0b7cd596e68935036a1fd65d77816fe8.png)


