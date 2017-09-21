CMDB (Configuration Management Database) 即配置管理数据库。织云以业务为核心,提供全面的基础资源和应用资源模型，便于用户进行面向业务的资源管理。
## 服务器 ##
### 全量 ###
可以管理所有服务器。

- 展示所有设备信息，可自定义展示字段，最多展示九个字段，支持下载到 excel 表格；
- 支持列表视图、IDC 视图、运维负责人视图、机型视图、模块视图、运营状态视图；
- 支持高级搜索，可按负责人等进行搜索；
- 可查看单机监控数据，多机监控数据；
- 可修改服务器绑定的业务，可把服务器释放到未分配。

![](https://mc.qcloudimg.com/static/img/d3b7ed3a7ed2ecbe04bb198335e07665/CMDB1.png)
### 未分配 ###
展示未绑定业务的所有服务器，可进行服务器分配以及监控数据查看。
![](https://mc.qcloudimg.com/static/img/7187f524fbea49c714cc925bbe4e59f6/CMDB2.png)
## 业务 ##
可以管理所有的一级业务。
### 一级业务列表 ###
- 展示所有一级业务的信息，包括服务器数。可自定义展示字段，最多展示九个字段，支持下载到 excel 表格
- 支持高级搜索，可按负责人，IDC 等进行搜索
- 可新建一级业务，但只有管理员才有权限操作

![](https://mc.qcloudimg.com/static/img/5f5b48cd0f83ee2d2a32332c7bfb4d7b/CMDB3.png)
### 二级业务列表  ###
- 可以管理一个一级业务的所有二级业务；
- 展示所有二级业务的信息，包括服务器数，可自定义展示字段，最多展示九个字段，支持下载到 excel 表格；
- 支持高级搜索，可按负责人搜索；
- 可新建二级业务，但只有管理员或一级业务负责人才有权限操作。

![](https://mc.qcloudimg.com/static/img/aadc307cb74ab1a4c04203b88807aed3/CMDB4.png)
### 三级业务列表 ###
- 可以管理一个二级业务的所有三级业务
- 展示所有三级业务的信息，包括服务器数，可自定义展示字段，最多展示九个字段，支持下载到 excel 表格
- 支持高级搜索，可按负责人搜索
- 可新建三级业务，但只有管理员或一级业务负责人或二级业务负责人才有权限操作

![](https://mc.qcloudimg.com/static/img/7ba56e6496ff7a2124d6cd413220a47a/CMDB5.png)
## 我的 ##
### 设备 ###
展示所有我负责的服务器的信息，可自定义展示字段，最多展示九个字段，支持下载到 excel 表格，支持查看多机监控数据。
![](https://mc.qcloudimg.com/static/img/4603d52de7d50f598f1032bc20df289a/CMDB6.png)
### 业务 ###
展示所有我负责的一级业务、二级业务、三级业务的信息，包括服务器数，可自定义展示字段，最多展示九个字段，支持下载到 excel 表格。
![](https://mc.qcloudimg.com/static/img/87dee0d8fe91329675e6aee3e76e9790/CMDB7.png)
## 数据导入 ##
### 批量导入服务器 ###
用于批量导入服务器信息，请下载服务器导入模版填写服务器信息，并下载服务器导入规则与实例，注意查看字段规则说明。红色字段为必填项，类似下图:
![](https://mc.qcloudimg.com/static/img/cb3df5cadf9e076361e955755f79a300/CMDB8.png)
然后在织云界面导入已填好信息的服务器导入模版（excel 文件）。
![](https://mc.qcloudimg.com/static/img/bd843ecd239f288bda2a602583b237b1/CMDB9.png)
单击【导入】，便能在 CMDB-服务器-全量看到新增的服务器信息。
### 批量导入业务 ###
请下载业务导入模版填写业务信息，并下载业务导入规则与实例，注意查看字段规则说明。红色字段为必填项，类似下图：
![](https://mc.qcloudimg.com/static/img/9df14c0edf205ab2e386233c7fc9fd51/CMDB10.png)
然后在织云页面导入该 excel 表格。
![](https://mc.qcloudimg.com/static/img/7185b21205db770ea6bd229a03140d8d/CMDB11.png)
点击导入后，便能在 CMDB-业务-全量中看到新增的业务信息。
