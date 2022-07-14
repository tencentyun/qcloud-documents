流日志功能需要将采集的日志数据上报到日志服务 CLS，因此需要授权流日志访问 CLS 的读写权限，否则将无法在 CLS 上查询到日志数据。本文指导您如何配置流日志访问 CLS 的资源访问权限。

## 操作步骤
1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/overview) 。
2. 单击“**角色**”，进入角色管理界面。
![](https://qcloudimg.tencent-cloud.cn/raw/2601db878fbe2d6f98f2ff4d9c3b3a91.png)
3. 单击“**新建角色**”，并选择角色载体为“腾讯云账户”。
![](https://qcloudimg.tencent-cloud.cn/raw/f2b4449713b9410459786a82b5b88924.png)
4. 在“输入角色载体信息”界面，选择“其他主账号”并输入流日志公共账户“91000000202”，单击“**下一步**”。
![](https://qcloudimg.tencent-cloud.cn/raw/01f0793ea02241643ec6019c59244a0a.png)
5. 在“配置角色策略”界面，输入“日志服务”进行检索，勾选“QcloudCLSFullAccess”，授权流日志公共账户访问 CLS 的读写权限，单击“**下一步**”。
![](https://qcloudimg.tencent-cloud.cn/raw/40dc564001aa7e19c861b58d55503c64.png)
6. 在“审阅”界面，输入角色名称“FlowLogClsRole”。
![](https://qcloudimg.tencent-cloud.cn/raw/58136c77357c8a935bcb0b7d43677560.png)
7. 单击“**完成**”，角色创建并授权成功如下图所示。
![](https://qcloudimg.tencent-cloud.cn/raw/8d4cf9dca5a370723c64f094ce078456.png)
