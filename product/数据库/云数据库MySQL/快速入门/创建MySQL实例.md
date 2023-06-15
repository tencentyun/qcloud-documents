本文为您介绍如何通过控制台创建 MySQL 实例。

## 前提条件
已注册腾讯云账号并完成实名认证。
- 如需注册腾讯云账号：
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.3128.btn1">点此注册腾讯云账号</a></div>
- 如需完成实名认证：
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/developer" target="_blank"  style="color: white; font-size:16px;"  hotrep="document.guide.3128.btn2">点此完成实名认证</a></div>

>?新版购买页支持一键**导入已有配置**，当登录的账号有已创建的云数据库 MySQL 实例时，通过此功能可自动配置好实例购买页的各项参数，便于您基于已有配置进行快捷调整或直接购买，操作指引如下。
>1. 在购买页单击右上角的**导入已有配置**。
>![](https://qcloudimg.tencent-cloud.cn/raw/3358386fc4f0c7154ee2453ebf9b6909.png)
>2. 在弹窗里，勾选对应地域的已有目标实例，单击**确定**。
>![](https://qcloudimg.tencent-cloud.cn/raw/86a0e328a0a181acc81c455a05bf90dd.png)

## 控制台购买
1. 登录 [MySQL 购买页](https://buy.cloud.tencent.com/cdb)，根据实际需求完成**基础配置**和**实例配置**，单击**下一步：设置网络和数据库**。
**基础配置**
 - **计费模式**：支持包年包月和按量计费。
    - 若业务量有较稳定的长期需求，建议选择包年包月。
    - 若业务量有瞬间大幅波动场景，建议选择按量计费。
 - **地域**：选择您业务需要部署 MySQL 的地域。建议您选择与云服务器同一个地域，不同地域的云产品内网不通，购买后不能更换。
 - **数据库版本**：云数据库 MySQL 目前支持以下版本：MySQL 8.0、MySQL 5.7、MySQL 5.6、MySQL 5.5，各个版本相关特性，请参见 [官方文档](https://dev.mysql.com/doc/refman/5.7/en/)。
 - **引擎**：支持选择 InnoDB 和 RocksDB 引擎。
    - InnoDB：最常用的 OLTP 存储引擎，拥有完整的事务支持与强大的读写高并发能力。
    - RocksDB：key-value 存储引擎，以高效写入能力与高压缩存储著称，选择 RocksDB 引擎后架构为双节点。
 - **架构**：支持双节点、三节点、单节点，各架构介绍请参见 [数据库架构](https://cloud.tencent.com/document/product/236/17136)。
 - **硬盘类型**：硬盘，用于存放 MySQL 运行时所必须的文件，云数据库 MySQL 支持本地盘和云盘两种硬盘类型。
    - 双节点、三节点硬盘类型为本地 SSD 盘。
    - 单节点硬盘类型为云盘。
 - **可用区**：双节点、三节点架构可选择主可用区和备可用区，选择主备可用区不同时（即 [多可用区部署](https://cloud.tencent.com/document/product/236/8459)），可保护数据库以防发生故障或可用区中断。
 >?
>- 主备机处于不同可用区，可能会增加2ms - 3ms的同步网络延迟。
>- 购买云服务时建议选择最靠近您的地域，可降低访问时延、提高下载速度。
>

 **实例配置**
 - **筛选**：快捷筛选所需实例的 CPU 和内存，默认选中全部 CPU、全部内存。
 - **类型**：提供通用型与独享型两种实例类型，详情请参见 [隔离策略](https://cloud.tencent.com/document/product/236/53253)。
 - **实例规格**：根据业务需要选择对应规格。
 - **硬盘**：用于存放 MySQL 运行时所必须的文件，选择硬盘空间大小。
    - 单节点架构为云盘，支持 SSD 云硬盘和增强型 SSD 云硬盘，了解硬盘类型请参见 [硬盘类型](https://cloud.tencent.com/document/product/362/2353)。可选硬盘容量：20 - 32000GB。
 ![](https://qcloudimg.tencent-cloud.cn/raw/0df5359b3c84ce92b2c2fe19ae1fcb6c.png)
2. 完成**网络和其他**、**数据库设置**配置，单击**下一步：确认配置信息**。
**网络和其他**
 - **网络**：支持私有网络环境，可选择实例的所属网络和子网，如现有的网络不合适，您可以 [新建私有网络](https://console.cloud.tencent.com/vpc/vpc?rid=4) 或 [新建子网](https://console.cloud.tencent.com/vpc/subnet?rid=4)。[](id:HXBZ)
>?
>- 子网是私有网络的一个网络空间，为逻辑概念，同一私有网络下可以创建不同可用区的子网，同一私有网络下不同可用区的子网默认可以内网互通。
>- 选择网络后，子网默认展示为所选实例同一可用区的子网 IP，您也可以自定义选择同地域其他可用区的子网 IP，实际业务连接访问为就近逻辑，不会增加网络时延。
>- 建议您选择与云服务器同地域下的同一私有网络，否则无法通过内网连接云服务器和数据库，缺省设置为 Default-VPC（默认）。
 - **自定义端口**：数据库的访问端口，默认为3306。
 - **安全组**：安全组创建与管理请参见 [云数据库安全组](https://cloud.tencent.com/document/product/236/9537)。
>?安全组入站规则需要放通 MySQL 实例的3306端口。MySQL 内网默认端口为3306，同时支持自定义端口，若修改过默认端口号，安全组中需放通 MySQL 新端口信息。
 - **指定项目**：选择数据库实例所属的项目，缺省设置为默认项目。
 - **标签**：便于分类管理实例资源，请参见 [标签概述](https://cloud.tencent.com/document/product/236/30971)。
 - **告警策略**：创建告警用于在云产品状态改变时触发警报并发送相关消息，请参见 [告警策略](https://cloud.tencent.com/document/product/236/8457)。
 
 **数据库设置**
 - **实例名**：可选择创建后命名或立即命名。
 - **数据复制方式**：提供异步复制、半同步复制、强同步复制三种方式，请参见 [数据库实例复制](https://cloud.tencent.com/document/product/236/7913)。
 - **参数模板**：除提供的系统参数模板外，您也可以创建自定义参数模板，请参见 [使用参数模板](https://cloud.tencent.com/document/product/236/30304)。
 - **字符集**：支持 LATIN1 、GBK、UTF8 、UTF8MB4 字符集，默认字符集编码格式是 UTF8。购买完成后，亦可在控制台实例详情页修改字符集，更多说明请参见 [字符集说明](https://cloud.tencent.com/document/product/236/7259#.E5.AD.97.E7.AC.A6.E9.9B.86.E8.AF.B4.E6.98.8E)。
 - **排序规则**：实例字符集为系统数据提供的排序规则，即区分大小写属性和重音属性。
 - **表名大小写敏感**：表名是否大小写敏感，MySQL 8.0 指定表名大小写设置后无法更改，请谨慎设置。
 - **密码复杂度**：支持设置密码复杂度以提升数据库安全性，默认为关闭。更多说明请参见 [设置密码复杂度](https://cloud.tencent.com/document/product/236/77620)。
 - **root 密码**：新创建的 MySQL 数据库的用户名默认为 root，此处用来设置该 root 账号的密码。选择**创建后设置**时，可在创建完实例后再 [重置密码](https://cloud.tencent.com/document/product/236/10305)。
3. 确认所选配置（如需修改，可单击**编辑**回到对应步骤进行调整），阅读并勾选服务条款，确认购买时长和数量后单击立即购买。
4. 支付完成后，返回实例列表，会看到实例显示**发货中**（大概需要3min - 5min中，请耐心等待），待实例状态变为**运行中**，即可进行正常操作。
![](https://qcloudimg.tencent-cloud.cn/raw/35e6e0a371d82923a09aa731826c243b.png)

## 后续操作
通过 Windows 云服务器或 Linux 云服务器，以内外网两种不同的方式连接云数据库 MySQL，请参见 [连接 MySQL 实例](https://cloud.tencent.com/document/product/236/3130)。
