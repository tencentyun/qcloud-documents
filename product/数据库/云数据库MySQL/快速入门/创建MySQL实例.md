
本文为您介绍如何通过控制台创建 MySQL 实例。

## 前提条件
已注册腾讯云账号并完成实名认证。
- 如需注册腾讯云账号：
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.3128.btn1">点此注册腾讯云账号</a></div>
- 如需完成实名认证：
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/developer" target="_blank"  style="color: white; font-size:16px;"  hotrep="document.guide.3128.btn2">点此完成实名认证</a></div>

## 操作步骤
1. 登录 [MySQL 购买页](https://buy.cloud.tencent.com/cdb)，根据实际需求选择各项配置信息，确认无误后，单击**立即购买**。
 - **计费模式**：支持包年包月和按量计费。
    - 若业务量有较稳定的长期需求，建议选择包年包月。
    - 若业务量有瞬间大幅波动场景，建议选择按量计费。
 - **地域**：选择您业务需要部署 MySQL 的地域。建议您选择与云服务器同一个地域，不同地域的云产品内网不通，购买后不能更换。
 - **数据库版本**：云数据库 MySQL 目前支持以下版本：MySQL 8.0、MySQL 5.7、MySQL 5.6、MySQL 5.5，各个版本相关特性，请参见 [官方文档](https://dev.mysql.com/doc/refman/5.7/en/)。
  - **架构**：提供双节点、三节点、单节点，各架构介绍请参见 [数据库架构](https://cloud.tencent.com/document/product/236/17136)。
  - **数据复制方式**：提供异步复制、半同步复制、强同步复制三种方式，请参见 [数据库实例复制](https://cloud.tencent.com/document/product/236/7913)。
 - **主可用区和备可用区**：选择主备可用区不同时（即 [多可用区部署](https://cloud.tencent.com/document/product/236/8459)），可保护数据库以防发生故障或可用区中断。
>?
>- 主备机处于不同可用区，可能会增加2ms - 3ms的同步网络延迟。
>- 购买云服务时建议选择最靠近您的地域，可降低访问时延、提高下载速度。
>
 - **实例类型**：提供通用型与独享型两种实例类型，详情请参见 [实例类型](https://cloud.tencent.com/document/product/236/53253)。
 - **实例规格**：根据业务需要选择对应规格。
 - **硬盘**：硬盘空间用于存放 MySQL 运行时所必须文件。
 - **网络**：云数据库 MySQL 所属网络，建议您选择与云服务器同一个地域下的同一私有网络，否则无法通过内网连接云服务器和数据库，缺省设置为 Default-VPC（默认）。
 - **自定义端口**：数据库的访问端口，默认为3306。
 - **安全组**：安全组创建与管理请参见 [云数据库安全组](https://cloud.tencent.com/document/product/236/9537)。
>?安全组入站规则需要放通 MySQL 实例的3306端口。MySQL 内网默认端口为3306，同时支持自定义端口，若修改过默认端口号，安全组中需放通 MySQL 新端口信息。
 - **参数模版**：除提供的系统参数模板外，您也可以创建自定义参数模板，请参见 [使用参数模板](https://cloud.tencent.com/document/product/236/30304)。
  - **字符集**：支持 LATIN1 、GBK、UTF8 、UTF8MB4 字符集，默认字符集编码格式是 UTF8。购买完成后，亦可在控制台实例详情页修改字符集，更多说明请参见 [字符集说明](https://cloud.tencent.com/document/product/236/7259#.E5.AD.97.E7.AC.A6.E9.9B.86.E8.AF.B4.E6.98.8E)。
 - **表名大小写敏感**：表名是否大小写敏感，默认为开启。
 - **root密码**：新创建的 MySQL 数据库的用户名默认为 root，此处用来设置该 root 帐号的密码。选择**自动生成密码**时，可在创建完实例后再 [重置密码](https://cloud.tencent.com/document/product/236/10305)。
 - **告警策略**：创建告警用于在云产品状态改变时触发警报并发送相关消息，请参见 [告警策略](https://cloud.tencent.com/document/product/236/8457)。
 - **指定项目**：选择数据库实例所属的项目，缺省设置为默认项目。
 - **标签**：便于分类管理实例资源，请参见 [标签概述](https://cloud.tencent.com/document/product/236/30971)。
 - **实例名**：可选择创建后命名或立即命名。
 - **购买数量**：每个用户在每个可用区可购买按量计费实例的总数量为10个。
 - **购买时长**：根据业务需要选择对应时长，包年包月计费模式，购买时长越长，折扣越大。
 - **自动续费**：在包年包月计费模式下，账户余额足够时，设备到期后按月自动续费。
 - **服务条款**：[云数据库服务条款](https://cloud.tencent.com/document/product/236/39102)。
2. 支付完成后，返回实例列表，会看到实例显示**发货中**（大概需要3min - 5min中，请耐心等待），待实例状态变为**运行中**，即可进行正常操作。

## 后续操作
通过 Windows 云服务器或 Linux 云服务器，以内外网两种不同的方式连接云数据库 MySQL，请参见 [连接 MySQL 实例](https://cloud.tencent.com/document/product/236/3130)。

