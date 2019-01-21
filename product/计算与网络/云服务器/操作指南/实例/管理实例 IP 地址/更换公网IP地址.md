## 操作场景

实例更换公网 IP 可以通过执行绑定弹性 IP 和解绑弹性 IP 的操作来进行。本文档指导您如何更换公网 IP 地址。

> **注意：**
> 解绑后的弹性 IP 如果不再使用请尽快释放，否则会收取闲置费用，同时释放后的弹性 IP 将无法找回。详情参考 [弹性公网 IP 计费模式](https://cloud.tencent.com/document/product/215/11145)。

## 操作步骤

### 转换为弹性 IP

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。
2. 在 “云主机” 中，选择待转换为弹性 IP的服务器，单击【更多】>【IP操作】>【绑定弹性IP】。如下图所示：
![](https://main.qcloudimg.com/raw/d9c315bdbc0ddb0355794b2bf255ab2c.png)
3. 在弹出的 “转换为弹性公网IP” 窗口中，单击【确定转换】。如下图所示：
![](https://main.qcloudimg.com/raw/21abc599d29d3408a3813860338d116c.png)
成功转换成弹性 IP 的状态如下图：
![](https://main.qcloudimg.com/raw/7dfeb52aaf8d2378678e902813cd8644.png)
>! 弹性 IP 申请后建议立即绑定服务器使用，否则会收取闲置费用。计费详情参考 [弹性公网 IP 计费模式](https://cloud.tencent.com/document/product/215/11145)。

### 解绑/释放弹性 IP
1. 在 “云主机” 中，选择待解绑 IP 的服务器，单击【更多】>【IP 操作】>【解绑弹性IP】。如下图所示：
![](https://main.qcloudimg.com/raw/9caabaf86b4b0a8ce5531c00feb3f96c.png)
2. 在弹出的 “解绑弹性公网IP” 窗口中， 单击两次【确定】，解绑弹性 IP。如下图所示：
![](https://main.qcloudimg.com/raw/81cdd6e3cd4cef10c162f09e09d473db.png)
3. 在左侧导航栏中，选择【弹性公网IP】，进入 “弹性公网IP” 页面。如下图所示：
![](https://main.qcloudimg.com/raw/ba657c5b7f5051b51470f5528035a22a.png)
4. 在待释放弹性 IP的服务器行中，单击【释放】，弹出 “释放弹性公网IP” 窗口。如下图所示：
![](https://main.qcloudimg.com/raw/ae239d7d3e66214bfd1516f9933bb829.png)
5. 单击两次【确定】，即可成功释放弹性 IP。

### 绑定弹性 IP/分配公网 IP

请根据实际需求，选择不同的方式为主机绑定新的 IP。
- 通过[ “绑定弹性 IP” 方式](#BindingEIP)
- 通过 [“在解绑弹性IP时，分配公网 IP” 方式](#AssignPublicIP)

<span id="BindingEIP"></span>
####  “绑定弹性 IP” 方式

1. 在 “弹性公网IP” 页面中，选择需绑定弹性 IP 的服务器，单击【绑定】。如下图所示：
![](https://main.qcloudimg.com/raw/97d4a2acd3813a42584615a531593b84.png)
2. 在弹出的 “绑定资源” 窗口中，根据实际需求，选择需要绑定的实例和主机 ID，单击两次【确定】。如下图所示：
![](https://main.qcloudimg.com/raw/de2d879345c646e565744bfe5af8bf97.png)
返回如下图所示信息，即表示绑定成功。
![](https://main.qcloudimg.com/raw/d5bf01a819e552afa41ffbfe373d0675.png)

<span id="AssignPublicIP"></span>
#### “在解绑弹性 IP 时，分配公网 IP” 方式

1. 在左侧导航栏中，选择【云主机】，进入 “云主机” 页面。
3. 在 “云主机” 页面中，选择待解绑 IP 的服务器，单击【更多】>【IP 操作】>【解绑弹性IP】，弹出的 “解绑弹性公网IP” 窗口。
2. 在弹出的 “解绑弹性公网IP” 窗口中， 勾选 “解绑后免费分配公网IP”，单击两次【确定】，即可通过 “在解绑弹性 IP 时，分配公网 IP” 方式完成绑定。
![](https://main.qcloudimg.com/raw/5716fd9089304b68d9fec588a5694852.png)




