## 现象描述
Windows 资源访问异常，提示 wait active error，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/22016494ac69ded7f4736fff0dde8144.png)



## 可能原因
远程桌面授权未激活，用户未加入 Remote Desktop Users 组。


## 解决思路
激活远程桌面服务，将用户加入 Remote Desktop Users 组。


## 处理步骤
1. 参考文档 [设置允许多用户远程登录 Windows 云服务器](https://cloud.tencent.com/document/product/213/36267) 进行配置。
2. 在操作系统界面，单击![](https://qcloudimg.tencent-cloud.cn/raw/0614d9150e988643275e37cdf4b0cdf9.png)，输入 `gpedit.msc`，按 Enter，打开 “本地组策略编辑器”。
3. 依次打开**运行** > **gpedit.msc** > **计算机配置** > **管理模板** > **Windows 组件** > **远程桌面服务** > **远程桌面会话主机** > **会话时间限制**，找到“设置已中断会话的时间限制”，启用并将“结束已断开连接的会话”设置为1分钟。
![](https://qcloudimg.tencent-cloud.cn/raw/0290e11fb6f59f62a2959d631a76c213.png)
4. 将用户添加到 Remote Desktop Users 组。
