本文为您详细介绍如何通过 Xshell 实现密钥直连和单点登录资源。

## 准备工作

本文演示机器及相关准备工作，请参见概述文档 [准备工作](https://cloud.tencent.com/document/product/1025/38514#.E5.87.86.E5.A4.87.E5.B7.A5.E4.BD.9C) 章节。

## 操作步骤

### 步骤1：生成密钥对
1. 打开 Xshell5 工具，并选择【工具】>【新建用户密钥生成向导】。
2. 设置密钥类型及密钥长度，并单击【下一步】。
<img src="https://main.qcloudimg.com/raw/775864b9c383ab562f4523fdd7615162.png"  width="70%">
3. 公约对已生成后，单击下一步输入用户密钥的名称和密码。
<img src="https://main.qcloudimg.com/raw/4de09cdaf6af8589dc3079738f44e352.png"  width="70%">
4. 生成公钥信息后，选择 SSH2-OpenSSH 格式，可复制或保存为指定文件，单击【完成】。
<img src="https://main.qcloudimg.com/raw/f9e18f15b66b3516ef46fabb5167f977.png"  width="70%">

### 步骤2：实现密钥直连登录

1. 打开 Xshell 工具，并选择【工具】>【用户密钥管理者】。
2. 导入对应的私钥文件后关闭即可生效。
<img src="https://main.qcloudimg.com/raw/3f4229e93ba09786d69718409507843b.png"  width="70%">
3. 导入后，进行 ssh 直连目标机操作，若未设置密钥对密码则直接回车即可，如设置了密钥对密码，则输入设置的密码回车即可。
<img src="https://main.qcloudimg.com/raw/4a142043ea93d280d1467ff8fb6c9c83.png"  width="70%">
4. 登录成功如下。

 <img src="https://main.qcloudimg.com/raw/f2b7f2af00745af54c81de0748f194b4.png"  width="70%">

### 步骤3：实现密钥单点登录
1. 打开 Xshell 工具，并选择【文件】>【属性】。
2. 使用 Xshell 工具单点登录时，必须将用户身份验证选项中的方法设置为 Password。
 <img src="https://main.qcloudimg.com/raw/563b5d26de10afb67eb37a9a08271dca.png"  width="70%">
3. 设置 SSH 选项，使用 SSH 代理服务，单击【确定】。
 <img src="https://main.qcloudimg.com/raw/aa1f1cf7abb1c970eaf9d06bb68f0afe.png"  width="70%">
4. 选择【工具】>【Xagent 开始】，配置 Xagent 服务，设置启动 Xagent 时启动服务器，设置 Xagent 服务端口。
	- 登录 Windows 时自动运行 Xagent（可选）：勾选时随 Windows 系统自启服务。
	- 确认 SSH 代理转发（可选）：勾选时使用单点登录需要确认弹出框提示使用 SSH 转发。
 <img src="https://main.qcloudimg.com/raw/47cd5f9daf3ed620d8e4c5bf8ac5c3b2.png"  width="70%">
5. 设置完成后开启状态为：正在端口5435中运作，即为 Xagent 服务开启（5435为Xagent 服务默认端口）。
 <img src="https://main.qcloudimg.com/raw/a338bb9a3f2364da4ca12472fb7ede36.png"  width="70%">
6. 配置完成后即可进行 Xshell 单点登录。打开浏览器，登录堡垒机，在登录界面，账号选择 tom，登录工具选择 Xshell，单击【连接】，即可调用 Xshell 实现单点登录。
 <img src="https://main.qcloudimg.com/raw/0f2cf78920eb78f780a3f27300746e6d.png"  width="70%">
