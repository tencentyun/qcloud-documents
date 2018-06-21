实例更换公网 IP 可以通过执行绑定弹性 IP 和解绑弹性 IP 的操作来进行。在绑定弹性 IP 后原有公网 IP 会丢失，且不可找回；接着释放弹性 IP 后会重新分配新的免费公网 IP，以此来达到更换公网 IP 的目的。

> **注意：**
> 解绑后的弹性 IP 如果不再使用请尽快释放，否则会收取闲置费用，同时释放后的弹性 IP 将无法找回。详情参考 [弹性公网 IP 计费模式](https://cloud.tencent.com/document/product/215/11145)。

## 绑定弹性IP
1. 登录腾讯云，进入 CVM 控制台的云主机 [管理页面](https://console.cloud.tencent.com/cvm/index)，单击【更多】>【IP操作】>【绑定弹性IP】。
![](https://main.qcloudimg.com/raw/d9c315bdbc0ddb0355794b2bf255ab2c.png)
2. 在弹出框中确认信息后单击【确定转换】。
![](https://main.qcloudimg.com/raw/1dee2e6fae92713aec29669c8b13e63d.png)
3. 成功转换成弹性 IP 的状态如下图：
![](https://main.qcloudimg.com/raw/7dfeb52aaf8d2378678e902813cd8644.png)

> **注意：**
> 弹性 IP 申请后建议立即绑定服务器使用，否则会收取闲置费用。计费详情参考 [弹性公网 IP 计费模式](https://cloud.tencent.com/document/product/215/11145)。

## 解绑弹性IP
1. 重新转换为公网IP，单击【更多】>【IP操作】>【解绑弹性IP】。
![](https://main.qcloudimg.com/raw/9caabaf86b4b0a8ce5531c00feb3f96c.png)
2. 在弹出框中勾选“解绑后免费分配公网IP”，单击【确定】后即可解绑弹性IP。
![](https://main.qcloudimg.com/raw/0bd483df02504e6bb5eeb6e08e70aa20.png)

## 释放弹性IP
1. 单击左侧导航栏【弹性公网IP】切换到弹性公网IP管理页面，选择目标弹性IP后在操作选项下单击【释放】。
![](https://main.qcloudimg.com/raw/ed50aea2f759bfc0b687770f1fffaba5.png)
2. 在弹出框中确认信息后单击【确定】即可成功释放弹性IP。
![](https://main.qcloudimg.com/raw/7dfded2b053f6def4aa9292076c0e019.png)
