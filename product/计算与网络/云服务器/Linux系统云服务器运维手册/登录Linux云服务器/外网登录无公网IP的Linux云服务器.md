除去使用[VNC登录](http://www.qcloud.com/doc/product/213/%E6%8E%A7%E5%88%B6%E5%8F%B0VNC%E7%99%BB%E5%BD%95Linux%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)外，无公网IP的机器（可能有带宽也可能无带宽）需要在外网登录时，请按以下步骤操作。

如果您从公网登录访问CVM，这台CVM需具备两个必要条件： 
1) 公网IP；——如无公网IP，可申请【弹性公网IP】，进行绑定 
2) 网络带宽（或者网络流量）；——如无带宽或者流量，可对该CVM进行【调整网络】 

## 1. 绑定弹性公网IP
登录[腾讯云CVM控制台](https://console.qcloud.com/cvm)，对于需要登录的CVM，点击【更多】→【绑定弹性IP】。
![](//mccdn.qcloud.com/img56a5f53d4b3fe.png)

如无弹性公网IP，可以到[弹性公网IP控制台](https://console.qcloud.com/cvm/eip)，点击【申请】按钮申请一个弹性公网IP（EIP），申请完成后再进行绑定。
![](//mccdn.qcloud.com/img56a5f57c55398.png)

## 2. 调整网络带宽（可选）
若您的机器选择的是0Mbps的带宽或带宽上限，由于无带宽/流量不能进行外网通信，是不能由外网登录这台Linux云服务器的。此时需要调整带宽。
登录[腾讯云CVM控制台](https://console.qcloud.com/cvm)，对于需要登录的CVM，点击【更多】→【调整网络】。

![](//mccdn.qcloud.com/img56a5f697497f3.png)

选择目标带宽，完成购买。
![](//mccdn.qcloud.com/img56a5f6cf0c6b6.png)

即可使用刚刚绑定的弹性公网IP，通过密码或SSH密钥等方式来登录这台Linux云服务器。 
