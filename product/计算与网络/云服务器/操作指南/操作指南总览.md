您在使用云服务器时，可能碰到诸如登录云服务器、重装操作系统、调整配置、重置密码等问题。本文将介绍云服务器实例以及跟云服务器相关的产品使用过程中的常用操作，供您参考。

## 实例

[CVM 实例](https://cloud.tencent.com/document/product/213/495) 即云服务器（Cloud Virtual Machine）实例。腾讯云 CVM 实例支持用户自定义一切资源：CPU、内存、硬盘、网络、安全等等，并可在访问量和负载等需求发生变化时轻松地调整它们。下面列举 CVM 实例目前支持的常见功能。

### 常用操作

- [创建实例](https://cloud.tencent.com/document/product/213/4855)
- 登录实例
 - [登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)
 - [登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435)
- [搜索实例](https://cloud.tencent.com/document/product/213/15519)
- [重启实例](https://cloud.tencent.com/document/product/213/4928)
- [关闭实例](https://cloud.tencent.com/document/product/213/4929)
- [销毁实例](https://cloud.tencent.com/document/product/213/4930)
- [回收实例](https://cloud.tencent.com/document/product/213/4931)

### 修改实例属性

- [重置密码](https://cloud.tencent.com/document/product/213/16566)
- 调整配置
 - [调整实例配置](https://cloud.tencent.com/document/product/213/2178)
 - [调整网络配置](https://cloud.tencent.com/document/product/213/15517)
 - [调整项目配置](https://cloud.tencent.com/document/product/213/16514)
- [修改实例名称](https://cloud.tencent.com/document/product/213/16562)
- 修改IP
 - [修改内网 IP](https://cloud.tencent.com/document/product/213/16561)
 - [修改公网 IP](https://cloud.tencent.com/document/product/213/16642)
- [更换实例子网](https://cloud.tencent.com/document/product/213/16565)
- [更换安全组](https://cloud.tencent.com/document/product/213/16564)
- [重装操作系统](https://cloud.tencent.com/document/product/213/4933)

### 计费相关

- [续费实例](https://cloud.tencent.com/document/product/213/6143)
- [按量计费转包年包月](https://cloud.tencent.com/document/product/213/2762)

## 镜像

[镜像](https://cloud.tencent.com/document/product/213/4940) 提供启动云服务器实例所需的所有信息。通俗的说，镜像就是云服务器的“装机盘”。目前腾讯云提供四种类型的镜像：公有镜像、服务市场镜像、自定义镜像以及共享镜像。下面介绍镜像目前支持的常见操作。

### 常用操作

- [创建自定义镜像](https://cloud.tencent.com/document/product/213/4942)
- [删除自定义镜像](https://cloud.tencent.com/document/product/213/6036)
- [导入镜像](https://cloud.tencent.com/document/product/213/4945)
- [复制镜像](https://cloud.tencent.com/document/product/213/4943)

### 共享镜像

- [共享镜像](https://cloud.tencent.com/document/product/213/4944)
- [取消共享镜像](https://cloud.tencent.com/document/product/213/7148)

## 安全组

[安全组](https://cloud.tencent.com/document/product/213/12452) 是腾讯云提供的重要的网络安全隔离手段，是一种有状态的包过滤功能虚拟防火墙，用于设置单台或多台云服务器的网络访问控制。下面介绍安全组目前支持的常见操作以及典型场景下，如何设置安全组以满足业务需要。最后提供常见端口作用的说明，供您参考。

### 常用操作

- [创建安全组](https://cloud.tencent.com/document/product/213/18197#.E5.88.9B.E5.BB.BA.E5.AE.89.E5.85.A8.E7.BB.84)
- [删除安全组](https://cloud.tencent.com/document/product/213/18197#.E5.88.A0.E9.99.A4.E5.AE.89.E5.85.A8.E7.BB.84)
- [克隆安全组](https://cloud.tencent.com/document/product/213/18197#.E5.85.8B.E9.9A.86.E5.AE.89.E5.85.A8.E7.BB.84)
- [向安全组中添加规则](https://cloud.tencent.com/document/product/213/18197#.E5.90.91.E5.AE.89.E5.85.A8.E7.BB.84.E4.B8.AD.E6.B7.BB.E5.8A.A0.E8.A7.84.E5.88.99)
- [实例关联安全组](https://cloud.tencent.com/document/product/213/18197#.E9.85.8D.E7.BD.AE-cvm-.E5.AE.9E.E4.BE.8B.E5.85.B3.E8.81.94.E5.AE.89.E5.85.A8.E7.BB.84)
- [导入/导出安全组规则](https://cloud.tencent.com/document/product/213/18197#.E5.AF.BC.E5.85.A5.E5.AF.BC.E5.87.BA.E5.AE.89.E5.85.A8.E7.BB.84.E8.A7.84.E5.88.99)

### 典型场景配置
[安全组应用案例](https://cloud.tencent.com/document/product/213/34601)


## 弹性公网 IP

[弹性公网 IP 地址（EIP）](https://cloud.tencent.com/document/product/213/5733)，简称弹性 IP 地址或弹性 IP。是专为动态云计算设计的静态 IP 地址。它是某地域下一个固定不变的公网 IP 地址。借助弹性公网 IP 地址，您可以快速将地址重新映射到账户中的另一个实例（或 NAT 网关实例 ），从而屏蔽实例故障。下面列举弹性公网 IP 常见的操作。

### 常用操作

- [申请弹性公网 IP](https://cloud.tencent.com/document/product/213/16586#.E7.94.B3.E8.AF.B7.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip)
- [释放弹性公网 IP](https://cloud.tencent.com/document/product/213/16586#.E9.87.8A.E6.94.BE.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip)
- [绑定实例](https://cloud.tencent.com/document/product/213/16586#.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip-.E7.BB.91.E5.AE.9A.E4.BA.91.E4.BA.A7.E5.93.81)
- [解绑实例](https://cloud.tencent.com/document/product/213/16586#.E5.BC.B9.E6.80.A7.E5.85.AC.E7.BD.91-ip-.E8.A7.A3.E7.BB.91.E4.BA.91.E4.BA.A7.E5.93.81)
- [调整带宽](https://cloud.tencent.com/document/product/213/16586#.E8.B0.83.E6.95.B4.E5.B8.A6.E5.AE.BD)
- [公网 IP 转弹性 IP](https://cloud.tencent.com/document/product/213/16586#.E5.85.AC.E7.BD.91ip.E8.BD.AC.E5.BC.B9.E6.80.A7ip)

## SSH 密钥

### 常用操作

- [创建 SSH 密钥](https://cloud.tencent.com/document/product/213/16691#.E5.88.9B.E5.BB.BA-ssh-.E5.AF.86.E9.92.A5)
- [删除 SSH 密钥](https://cloud.tencent.com/document/product/213/16691#.E5.88.A0.E9.99.A4-ssh-.E5.AF.86.E9.92.A5)
- [绑定/解绑实例](https://cloud.tencent.com/document/product/213/16691#.E5.AF.86.E9.92.A5.E7.BB.91.E5.AE.9A.2F.E8.A7.A3.E7.BB.91.E6.9C.8D.E5.8A.A1.E5.99.A8)
- [修改名称/描述](https://cloud.tencent.com/document/product/213/16691#.E4.BF.AE.E6.94.B9-ssh-.E5.AF.86.E9.92.A5.E5.90.8D.E7.A7.B0.2F.E6.8F.8F.E8.BF.B0)
- [使用密钥登录 Linux 实例](https://cloud.tencent.com/document/product/213/16691#.E4.BD.BF.E7.94.A8-ssh-.E5.AF.86.E9.92.A5.E7.99.BB.E5.BD.95-linux-.E4.BA.91.E6.9C.8D.E5.8A.A1.E5.99.A8)
