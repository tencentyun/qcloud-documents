
本文介绍 TDSQL-C MySQL 版性能测试所使用的环境。

## 测试对象：TDSQL-C MySQL 版
- 地域/可用区：北京-北京六区
- 客户端
 - 客户端类型：云服务器 CVM
 - 客户端规格：S5.4XLARGE32（标准型S5，16核32GB）
 - 客户端操作系统：centos 7
 - 客户端数量：2个（超过1000并发后增加1个客户端，以此类推）
- 测试的 TDSQL-C MySQL 版实例信息：
 - 可用区部署：单可用区
 - 数据库版本：MySQL 5.7
 - 参数模板：使用默认模板，并对以下几个参数调整如下：
   - log_bin=off
   - thread_handling=pool-of-threads
   - innodb_log_sync_method=async
 - VPC 网络时延：0.6ms
 - 实例类型/规格：
 
<table>
<tr><th>实例类型</th>
<th>实例规格</th></tr>
<tr><td rowspan = "11"  width="40%">独享型</td><td>2核16G</td></tr>
<tr><td>4核16GB</td></tr>
<tr><td>4核32GB</td></tr>
<tr><td>8核32GB</td></tr>
<tr><td>8核64GB</td></tr>
<tr><td>16核64GB</td></tr>
<tr><td>16核96GB</td></tr>
<tr><td>16核128GB</td></tr>
<tr><td>32核128GB</td></tr>
<tr><td>32核256GB</td></tr>
<tr><td>64核256GB</td></tr>
</table>

## 测试对象：腾讯云 MySQL 
- 地域/可用区：广州-广州六区
- 客户端
 - 客户端类型：云服务器 CVM
 - 客户端规格：S5.4XLARGE32（标准型S5，16核32GB）
 - 客户端操作系统：centos 7
 - 客户端数量：2个（超过1000并发后增加1个客户端，以此类推）
- 测试的云数据库 MySQL 实例信息：
 - 存储类型：本地 SSD
 - 可用区部署：单可用区
 - 数据库版本：MySQL 5.7
 - 架构：双节点
 - 复制方式：异步复制
 - 参数模板：高性能参数模板
 - VPC 网络时延：0.5ms
 - 实例类型/规格：与上表一致

