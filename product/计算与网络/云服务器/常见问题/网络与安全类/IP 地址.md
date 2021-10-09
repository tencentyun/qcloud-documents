## 普通公网 IP 问题

### 云服务器没有公网 IP 如何实现公网访问？
如果您在购买机器时未购买公网 IP 或者已将公网 IP 退还，您可以在 [弹性公网 IP 控制台 ](https://console.cloud.tencent.com/cvm/eip)申请弹性公网 IP，然后绑定到您的机器，实现公网访问。

### 能否更换我的公网 IP 地址？

您可以为您的云服务器更换公网 IP，具体操作请参见 [更换实例公网 IP](https://cloud.tencent.com/document/product/213/16642)。

### 如何保持公网 IP 地址不变？

当您需要保留账户中的某个特定公网 IP 时，可将其先转换为弹性公网 IP，绑定设备后即可使用该 IP 进行公网访问。只要不进行**释放**操作，该弹性公网 IP 便会一直保留在您的账户中。
相关操作请参见 [弹性公网 IP](https://cloud.tencent.com/document/product/213/16586)。

### 公网 IP 地址是什么？
公网 IP 地址是 Internet 上的非保留地址，有公网 IP 地址的云服务器可以和 Internet 上的其他计算机互相访问。
如需了解更多详情，请参考 [公网服务](https://cloud.tencent.com/document/product/213/5224)。

### 如何获取实例的公网 IP 地址？
具体操作，请参考 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940)。

### 如何更换实例公网 IP？
具体操作，请参考 [更换公网 IP 地址](https://cloud.tencent.com/document/product/213/16642)。

### 公网网关和带有公网 IP 的云服务器有何区别？
公网网关在镜像里开通了公网流量路由转发功能，而带有公网 IP 的云服务器默认不具备流量转发功能。Windows 公共镜像云服务器无法做公网网关，因为 Windows 镜像中未开通流量转发功能。

### 为什么我的云服务器更换不了公网 IP？
可能原因如下：
- 云服务器实例已关机，并设置了关机不收费。
- 云服务器更换过公网 IP。


### 创建实例时未分配独立公网 IP（IPv4），创建成功后该如何获取公网 IP 地址？
您可以通过申请和绑定弹性公网 IP 方式进行获取。详细步骤，请参见 [弹性公网 IP](https://cloud.tencent.com/document/product/213/16586)。

## 内网 IP 问题

### 内网 IP 地址是什么？
内网 IP 地址是无法通过 Internet 访问的 IP 地址，是腾讯云内网服务的实现形式。
如需了解更多详情，请参考 [内网服务](https://cloud.tencent.com/document/product/213/5225)。

### 如何获取实例的内网 IP 地址？
具体操作，请参考 [获取实例的内网 IP 地址](https://cloud.tencent.com/document/product/213/17941#.E8.8E.B7.E5.8F.96.E5.AE.9E.E4.BE.8B.E7.9A.84.E5.86.85.E7.BD.91-ip-.E5.9C.B0.E5.9D.80)。

### 除了更换公网 IP 地址，我可以更换内网 IP 地址吗？
可以。具体操作，请参考 [修改内网 IP 地址](https://cloud.tencent.com/document/product/213/16561)。



