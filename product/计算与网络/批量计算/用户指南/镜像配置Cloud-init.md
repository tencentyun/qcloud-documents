## 概要信息

批量计算 Batch 依赖Cloud-init服务对云服务器进行初始化，所以使用 Batch 时填写的镜像必须已经成功安装和配置Cloud-init，否则作业执行或计算环境内云服务器创建将``失败``。

（Cloud-init 提供了一个云服务器首次初始化时的自定义配置的能力）

安装和配置Cloud-init请遵循下面指引，
* Linux ``新建``云服务器/自定义镜像：目前腾讯云CentOS、Ubuntu所有版本公有镜像已默认支持Cloud-init，从这些公有镜像再去创建云服务器和自定义镜像无需再手动去安装和配置Cloud-init
* Linux ``存量``云服务器/自定义镜像：如果是早前就创建的云服务器或自定义镜像，需要手动安装 Cloud-init，请参照 [linux手动安装Cloud-init>>>](https://cloud.tencent.com/document/product/213/12587)
* Windows：必须从Batch 官方提供的镜像市场镜像来创建云服务器或制作自定义镜像，请参照 [制作Batch可用的Windows自定义镜像>>>](https://cloud.tencent.com/document/product/599/13035)

已包含Cloud-init的常用操作系统镜像ID如下，
* img-31tjrtph（CentOS 7.2 64位）
* img-er9shcln（Windows Server 2012 R2 标准版 64位中文版）
* img-pyqx34y1（Ubuntu Server 16.04.1 LTS 64位）








