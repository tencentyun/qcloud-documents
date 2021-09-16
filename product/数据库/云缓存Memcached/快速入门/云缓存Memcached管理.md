
## 实例扩容
云数据库 Memcached 的扩容包括存储扩容、 接口扩容和端口扩容。
- **存储扩容**
云数据库 Memcached 会自动为每个实例每日预留约20%的空间作为数据增长 buffer。例如，实例的使用空间为80GB，则会分配96GB作为实例的占用空间。如果实例的数据日增长量超过20%，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 进行存储扩容申请。云数据库 Memcached 扩容过程是数据搬迁过程，不会影响业务访问。 
- **接口/端口扩容**
请 [提交工单](https://console.cloud.tencent.com/workorder/category)，填写接口/端口扩容进行申请。

## 实例缩容
实例缩容指的是减少实例的占用空间，即存储缩容。因为需要预留缓冲空间，缩容后实例使用率不会超过80%。实例缩容的最小粒度是1GB，如果缩容会造成使用率超过80%，则不能进行缩容。

目前云数据库 Memcached 的实例暂不支持自动缩容，如实例需要缩容则可提交工单申请，之后需运维人员操作缩容。
在申请缩容之前，计费时仍然会按照原占用空间（包括在原使用空间的基础上自动扩容的缓冲空间）的峰值进行计算。

## 数据清理
云数据库 Memcached 支持通过控制台手动清理实例数据，单个实例每天只能清理累计50GB的占用空间。如果超过50GB，请提交工单联系技术支持。
>!数据被清空后，不可以再恢复，请在清空前确认实例中的数据已经备份或不再使用。
>
登录 [云数据库 Memcached 控制台](https://console.cloud.tencent.com/memcached)，选择需要清空的实例，在操作列选择【更多】>【清空】，确认清空后，后台开始清空操作。清空完成后，页面会提示清空成功。
![](https://main.qcloudimg.com/raw/d17c28d3702e65f5aa46a65e9f6ede41.png)

## 实例销毁
>!实例销毁后，不可再恢复，请在销毁前确认实例中的数据已经备份或不再使用。

在 Memcached 实例列表，选择需要销毁的实例，在操作列选择【更多】>【销毁】，后台开始清理实例数据并删除表。
![](https://main.qcloudimg.com/raw/2db049178eaa5f603bebc2e0eb81eb42.png)

## 实例淘汰
云数据库 Memcached 支持通过开启控制台的淘汰功能来每天定期自动清理实例数据，清理后的数据将无法恢复。
1. 在 Memcached 实例列表，选择所需实例，单击【开启淘汰】打开淘汰开关。
![](https://main.qcloudimg.com/raw/ec7adbcf346b0d3582b55a1db10fcc8b.png)
2. 开启淘汰功能后，需要在代码里设置 key 的有效期，具体请参考各语言 Memcached 设置方法。
>?
>- 开启淘汰功能前设置的 key 是不会自动过期的。
>- expire 值与传统 Memcache 用法略有不同，范围为(0,2592000)，超出则无效。


## 实例监控
在 Memcached 实例列表，单击如下监控图标，或单击实例名进入【实例监控】页面可查看实例监控信息。
![](https://main.qcloudimg.com/raw/eabba956635c2d95482e3e90bfcf325c.png)

## 数据回档
请 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系我们。

## 连接诊断
请参见 [Memcached 连接诊断](https://cloud.tencent.com/doc/product/241/3247)。
