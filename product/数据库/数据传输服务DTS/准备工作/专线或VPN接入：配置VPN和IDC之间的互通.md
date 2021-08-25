## 操作场景
使用 VPN 网关接入方式，需要用户新建 VPC 和 VPN，然后建立 VPN 和 IDC 之间的通道，实现 VPN 和 IDC 之间的互通。

本场景中，用户所属的 VPC 网络为“TomVPC”，子网为“子网A”，子网A的网段为`192.168.1.0/24`。新建 VPN 网关为“TomVPNGW”，VPN 网关的公网 IP 为`203.195.147.82`。用户 IDC 中的子网网段为`10.0.1.0/24`，IDC 中 VPN 网关的公网 IP 为`202.108.22.5`，源端数据库的主机IP地址为`10.0.1.8`。

![](https://main.qcloudimg.com/raw/4a66ef79cd81a25f5ddafdc6a5d27d3d.png)

## 操作步骤
请参考 [建立 VPC 到 IDC 的连接](https://cloud.tencent.com/document/product/554/18988)。

## 后续步骤
1. VPN 与 IDC 连通后，在 [DTS 任务页面](https://console.cloud.tencent.com/dts/migration) 选择**VPN 接入**，关键参数配置说明如下：
![](https://main.qcloudimg.com/raw/ad3d1aad26532abe25bc461f92d91038.png)
<table>
<thead><tr><th><strong>参数</strong></th><th><strong>说明</strong></th><th><strong>参数示例</strong></th></tr></thead>
<tbody><tr>
<td>VPN 网关</td>
<td>在 VPC 网络中新建的 VPN 网关名称。</td>
<td>TomVPNGW</td></tr>
<tr>
<td>私有网络</td>
<td>用户所属的 VPC 网络名称。</td>
<td>TomVPC</td></tr>
<tr>
<td>子网</td>
<td>用户 VPC 网络的子网名称。</td>
<td>子网 A</td></tr>
<tr>
<td>主机地址</td>
<td>源数据库的主机 IP 地址。</td>
<td>10.0.1.8</td></tr>
<tr>
<td>端口</td>
<td>源数据库使用的端口。常见数据库默认端口如下：（如用户修改了默认端口，请按实际情况填写）<br><ul><li>MySQL：3306</li><li>SQL Server：1433</li><li>PostgreSQL：5432</li><li>MongoDB：27017</li><li>Redis：6379</li></ul></td>
<td>3306</td></tr>
</tbody></table>
2. 单击**测试连通性**。如果出现测试不通过，请按照如下指导进行排查。
   - Telnet 测试不通过。
     在新建的 VPC 网络中（本例中为 TomVPC）购买一个云服务器 CVM，在 CVM 上 ping 源数据库主机地址：
      - 如果不能 ping 通。
        - [源数据库设置了安全组或防火墙](https://cloud.tencent.com/document/product/571/58685)。
        - [源数据库对 SNAT IP 地址进行了限制](https://cloud.tencent.com/document/product/571/58685)。
        - 源数据库端口设置问题。     
      - 如果可以 ping 通。
        请 [提交工单](https://console.cloud.tencent.com/workorder/category) 处理。
   - Telnet 测试通过，Datebase Connect 失败。
     - 迁移帐号授权问题。请参考 [数据迁移](https://cloud.tencent.com/document/product/571/58688)、[数据同步](https://cloud.tencent.com/document/product/571/56516) 中的对应场景，重新对迁移帐号授权。
     - 帐号密码不正确。
     
 <img src="https://main.qcloudimg.com/raw/55f1738e5ea18c881182ae5efc9a8b08.png" style="zoom:50%;" />

 
