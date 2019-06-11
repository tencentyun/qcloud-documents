>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

### INSTANCE_STATE

>描述了一个实例的整个生命周期。

|ID | 描述|
|---------|---------|
|PENDING| 准备中|
|RUNNING| 运行中|
|STOPPED| 已停止|
|REBOOTING| 重启中|
|STARTING| 启动中|
|STOPPING| 停止中|


### REGION

> 地域表

|ID | 描述|
|---------|---------|
| ap-guangzhou| 广州 |
| ap-shanghai| 上海 |
| ap-hongkong| 香港 |
| ap-beijing| 北京 |
| ap-shanghai-fsi| 上海金融 |
| ap-chengdu| 成都 |
| ap-shenzhen-fsi| 深圳金融 |
| ap-guangzhou-open| 广州Open |
| ap-seoul| 首尔 |
| ap-singapore| 新加坡 |
| eu-frankfurt| 法兰克福 |
| na-siliconvalley| 硅谷 |
| na-toronto| 多伦多 |


### ZONE

> 描述了地域下属的可用区

|ID |描述|
|---------|---------|
| ap-guangzhou-1| 广州一区 |
| ap-guangzhou-2| 广州二区 |
| ap-guangzhou-3| 广州三区 |
| ap-guangzhou-4| 广州四区 |
| ap-shanghai-1| 上海一区 |
| ap-shanghai-2| 上海二区 |
| ap-hongkong-1| 香港一区 |
| ap-beijing-1| 北京一区 |
| ap-beijing-2| 北京二区 |
| ap-beijing-3| 北京三区 |
| ap-shanghai-fsi-1| 上海金融一区 |
| ap-shanghai-fsi-2| 上海金融二区 |
| ap-chengdu-1| 成都一区 |
| ap-chengdu-2| 成都二区 |
| ap-shenzhen-fsi-1| 深圳金融一区 |
| ap-shenzhen-fsi-2| 深圳金融二区 |
| ap-guangzhou-open-1| 广州Open专区 |
| ap-seoul-1| 首尔一区 |
| ap-singapore-1| 新加坡一区 | 
| eu-frankfurt-1| 法兰克福一区 |
| na-siliconvalley-1| 硅谷一区 |
| na-toronto-1| 多伦多一区 |


### BLOCK_DEVICE

>磁盘类型

|ID | 描述|
|---------|---------|
| LOCAL_BASIC| 本地硬盘| 
| LOCAL_SSD| 本地SSD硬盘| 
| CLOUD_BASIC| 普通云硬盘| 
| CLOUD_PREMIUM| 高性能云硬盘| 
| CLOUD_SSD| SSD云硬盘| 


### AUTO_RENEW

>标明了自动续费的方式

|ID | 描述|
|---------|---------|
| NOTIFY_AND_MANUAL_RENEW| 通知且不自动续费。（通知即将过期，但不自动续费)
| NOTIFY_AND_AUTO_RENEW| 通知且自动续费 (通知即将过期，而且自动续费)
| DISABLE_NOTIFY_AND_MANUAL_RENEW| 不通知且不自动续费 (不通知即将过期，也不自动续费)


### INSTANCE_PAID

>实例计费模式

|ID | 描述|
|---------|---------|
| PREPAID| 预付费，即包年包月|
| POSTPAID_BY_HOUR| 后付费，即按量计费|
| CDHPAID| `CDH`付费，即只对`CDH`计费，不对`CDH`上的实例计费|


### NETWORK_PAID

>网络计费模式

|ID | 描述|
|---------|---------|
| BANDWIDTH_POSTPAID_BY_MONTH| 按月后付费方式|
| BANDWIDTH_PREPAID| 按带宽计费方式|
| TRAFFIC_POSTPAID_BY_HOUR| 按流量计费方式|
| BANDWIDTH_POSTPAID_BY_HOUR| 按带宽使用时长计费方式|
| BANDWIDTH_PACKAGE| 带宽包计费方式|


### IMAGE_SOURCE

>标注镜像来源

|ID | 描述|
|---------|---------|
|OFFICIAL| 官方提供的镜像。
|IMAGE_CREATE|通过创建实例镜像等方式从官方镜像所派生出的镜像。 |
|EXTERNAL_IMPORT|外部导入的镜像所派生出的镜像。 |



### ZONE_STATE

>可用区状态

|ID | 描述|
|---------|---------|
| AVAILABLE| 可用|
| UNAVAILABLE| 不可用|


### IMAGE_TYPE

>镜像类型

|ID | 描述|
|---------|---------|
|PRIVATE_IMAGE|私有镜像 (本帐户创建的镜像) 
|PUBLIC_IMAGE|公共镜像 (腾讯云官方镜像)
|MARKET_IMAGE|服务市场 (服务市场提供的镜像) 
|SHARED_IMAGE|共享镜像(其他账户共享给本帐户的镜像)


### IMAGE_STATE

>镜像状态

|ID |描述|
|---------|--------|
|CREATING| 创建中
|NORMAL| 正常
|USING| 使用中
|SYNCING| 同步中
|IMPORTING| 导入中
|DELETING| 删除中


### EIP_STATE

> EIP状态

|ID |描述|
|---------|--------|
|CREATING| 创建中
|BINDING| 绑定中
|BIND| 已绑定
|UNBINDING| 解绑中
|UNBIND| 未绑定
|OFFLINING| 下线中
|CREATE_FAILED| 创建失败
|BIND_ENI| 绑定在网卡上，且该网卡没有挂载到实例上
