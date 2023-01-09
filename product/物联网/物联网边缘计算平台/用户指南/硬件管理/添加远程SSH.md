## 操作场景

本文介绍如何通过腾讯云边缘计算平台添加设备远程 SSH 连接

## 前提条件

已登录 [边缘计算平台](https://console.cloud.tencent.com/iecp)。

## 操作步骤

1. 单击左侧导航栏中**硬件管理** > **产品列表**，进入“硬件列表”页面。
![](https://qcloudimg.tencent-cloud.cn/raw/5b044bb737cb86f2052dc4e963079e8a.png)
2. 对于运行中的设备可单击**添加远程 SSH** ，输入配置开启时间及跳板机端口即可完成远程 SSH 添加，输入开启时长（秒为单位）和端口号，端口号建议使用100xx格式，避免端口冲突。
![](https://qcloudimg.tencent-cloud.cn/raw/9a050a82152ec2f1e0fddf520bd17e02.png)
3. 添加成功后，本地通过终端登录跳板机，执行：ssh ubuntu@1.13.163.188，跳板机密码为：tencent2022!!
4. 登录跳板机后，执行：ssh -p 端口号 设备用户名@127.0.0.1
5. 如提醒需要添加 ssh key，输入 yes 即可
6. 完成后即可登录到设备上。