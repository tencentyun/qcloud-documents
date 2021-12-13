## 操作场景
云联网可以实现不同 VPC（私有网络间）之间，VPC 与 IDC（本地数据中心间）之间的互联互通。使用云联网接入方式，需要用户提前通过云联网建立各 VPC 之间、VPC 与 IDC 的互通。

本场景中，已通过云联网建立了vpc-广州、vpc-南京、vpc-上海三个网络之间的互通，计划备份广州地域的数据库到腾讯云 DBS，则云联网关联 VPC 选择南京或者上海。

<img src="https://main.qcloudimg.com/raw/61f515040e4072a5815522cabbd1fb0b.png" style="zoom:67%;" />

## 操作步骤
请参考 [通过云联网建立不同网络之间的互通](https://cloud.tencent.com/document/product/877/30804)。

> ?云联网仅提供所有地域间 10Kbps 以下的免费带宽，使用 DBS 数据备份时需要更高带宽，所以链接中的配置带宽是必选操作。

## 后续步骤
1. 在 [DBS 配置备份计划页面](https://console.cloud.tencent.com/dbs) 选择**云联网**，关键参数配置说明如下：
![](https://qcloudimg.tencent-cloud.cn/raw/698a750e0af1ef9688bab596634d7cb8.png)
<table>
<thead><tr><th><strong>参数</strong></th><th><strong>说明</strong></th><th><strong>参数示例</strong></th></tr></thead>
<tbody><tr>
<td>私有网络云联网</td><td>云联网实例名称。</td><td>ccn6-xxxx7d</td></tr>
<tr>
<td>云联网关联 VPC</td>
<td>选择和源数据库地域、VPC 名称都不同的其他 VPC。例如广州地域数据库作为源数据库，则云联网关联 VPC 选择南京 VPC 或者上海 VPC。此处选择南京 VPC。</td>
<td>vpc-南京</td></tr>
<tr>
<td>子网</td>
<td>已选择 VPC 网络的子网名称。<br>如果无法拉取子网，则可能是账号问题，“云联网关联 VPC”所属账号和备份操作账号需要一致。</td>
<td>vpc-南京-子网</td></tr>
<tr>
<td>主机地址</td><td>源数据库的主机 IP 地址。</td><td>172.16.0.0</td></tr>
<tr>
<td>端口</td>
<td>源数据库使用的端口。常见数据库默认端口如下：（如用户修改了默认端口，请按实际情况填写）<ul><li>MySQL：3306</li><li>SQL Server：1433</li><li>PostgreSQL：5432</li><li>MongoDB：27017</li><li>Redis：6379</li></ul></td>
<td>3306</td></tr>
</tbody></table>

2. 单击**测试连通性**。如果出现测试不通过，请按照如下指导进行排查。
   - Telnet 测试不通过。
     在云联网关联 VPC 中（本例中为 vpc-南京）购买一个云服务器 CVM，在 CVM 上 ping 源数据库主机地址：
     - 如果不能 ping 通。
       - 源数据库所在服务器设置了安全组或防火墙。
       - 源数据库对 DBS IP 地址进行了限制。
       - 源数据库端口设置问题。
       - 云联网实例的路由表中，网段冲突导致部分路由表未被启用。
     - 如果可以 ping 通，则源数据库和云联网之间路由没有问题。 
       - 云联网关联 VPC 选择有误。
         云联网关联 VPC 与主机地址不能在同一地域（源库所在网络环境为广州某个 VPC，则云联网关联 VPC 不能选择广州的其他 VPC）；云联网关联 VPC 与主机地址不能在同一 VPC（源库所在网络环境为 VPC-A，则云联网关联 VPC 不能选择 VPC-A）。 
      -  请 [提交工单](https://console.cloud.tencent.com/workorder/category) 处理。
 - Telnet 测试通过，Database Connect 失败。
     - 备份帐号授权问题。
     - 帐号或密码不正确。

