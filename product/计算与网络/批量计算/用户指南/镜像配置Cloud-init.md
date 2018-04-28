## 概要信息

Cloud-init 提供了一个云主机首次初始化时的自定义配置的能力，Batch 依赖Cloud-init服务对云主机进行初始化，所以使用 Batch 时填写的镜像必须已经成功安装和配置Cloud-init，否则作业执行或计算环境内云主机创建将``失败``。

安装和配置Cloud-init请遵循下面指引，
* Linux ``新建``云主机/自定义镜像：目前腾讯云CentOS、Ubuntu所有版本公有镜像已默认支持Cloud-init，从这些公有镜像再去创建云主机和自定义镜像无需再手动去安装和配置Cloud-init
* Linux ``存量``云主机/自定义镜像：如果是早前就创建的云主机或自定义镜像，需要手动安装 Cloud-init，请参照 [linux手动安装Cloud-init>>>](https://cloud.tencent.com/document/product/213/12587)
* Windows：必须从Batch 官方提供的镜像市场镜像来创建云主机或制作自定义镜像，请参照 [制作Batch可用的Windows自定义镜像>>>](https://cloud.tencent.com/document/product/599/13035)








