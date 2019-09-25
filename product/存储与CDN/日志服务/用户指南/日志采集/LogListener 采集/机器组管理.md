机器组是腾讯云日志服务中 LogListener 所采集日志的服务器对象，通过机器组的方式来配置 LogListener 采集日志的服务器。一般而言，根据不同业务场景来划分不同的机器组，可以方便您管理日志服务。

## 创建机器组
通过日志服务控制台可以快速创建机器组，具体操作步骤如下：
1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中，单击【机器组管理】。
3. 选择您日志服务所在的地域，例如广州，单击【创建机器组】。
![](https://main.qcloudimg.com/raw/95220e6cb971a91ac4e490b39f6e5068.png)
4. 填写机器组名称及其服务器对应的 IP 地址，确认信息无误后，单击【确认】，完成机器组创建。
![](https://main.qcloudimg.com/raw/5a5372e04930018fb1a1a51653d5eab8.png)
>!
> - 每行填写一个 IP 地址，暂不支持 Windows 系统机器。
> - 同园区内，腾讯云服务器填写内网 IP 即可，分行隔开。


## 查看机器状态
机器组与日志服务系统之间采用心跳机制保持连接，成功安装过 LogListener 的机器组会定时向日志服务发送心跳。
1. 您可以通过单击【查看】，查看机器组的状态来识别当前该机器是否工作正常。
![](https://main.qcloudimg.com/raw/b1b9f577f6ca595c5a6aaffd8169fd40.png)
2. 若状态显示为正常，则说明您的服务器可以与腾讯云日志服务正常通信。
![](https://main.qcloudimg.com/raw/69d87f0aa09637c03f58190a366178ce.png)

## 删除机器组
1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 选择需要删除的机器组，单击【删除】。
![](https://main.qcloudimg.com/raw/c5cb4b37df17cc3b01f15e363d7dacd2.png)
3. 单击【确认】，完成机器组删除。
![](https://main.qcloudimg.com/raw/d94ecda2fd201698859dd9eee5bfd5c4.png)
>!机器组一旦删除，所关联的日志主题将无法继续采集日志。
