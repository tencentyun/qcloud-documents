高可用虚拟 IP（HAVIP）是从 VPC 子网 CIDR 分配的一个内网 IP 地址，通常和高可用软件（如 keepalived 或 Windows Server Failover Cluster）配合使用，应用于搭建高可用主备集群场景。
>?
>- 目前 HAVIP 产品处于灰度优化中，切换的时延在10s左右，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/azh0w1qoavk)。
>- 为保证主备集群云服务器的高可用性，强烈建议通过 [置放群组](https://cloud.tencent.com/document/product/213/15486) 将不同云服务器分配到不同的宿主机上，更多关于置放群组的信息，请参考 [置放群组](https://cloud.tencent.com/document/product/213/15486)。
>- 高可用软件需要支持发送 ARP 报文。
>

## 特点介绍
1. 可以在 HAVIP 产品控制台申请 HAVIP 地址，每个 VPC 可以申请多个 HAVIP 地址。
2. 需要在云服务器的配置文件中绑定 HAVIP。
3. HAVIP 有子网属性，只能被同一个子网下的机器宣告绑定。

## 架构与实现原理
通常高可用主备集群包含2台服务器，一台主服务器处于某种业务的激活状态（即 Active 状态），另一台备服务器处于该业务的备用状态（即 Standby 状态），它们共享同一个 VIP（Virtual IP，一个内网 IP）。同一时刻，VIP 只在一台主设备上生效，当主服务器出现问题时，备用服务器接管 VIP 继续提供服务。
+ 在传统物理网络中，可以通过 keepalived 的 VRRP 协议协商主备状态。其原理为：主设备周期性发送免费 ARP 报文刷新上联交换机的 MAC 表或终端 ARP 表，触发 VIP 迁移到主设备上。
+ 在私有网络 VPC 中，同样通过在云服务器中部署 Keepalived 来实现高可用主备集群。与物理网络不同的是，出于安全考虑（如 ARP 欺骗等），通常不支持云服务器通过 ARP 宣告普通内网 IP，该 VIP 必须为从腾讯云申请的高可用虚拟 IP (HAVIP) ，且该 VIP 具有子网属性，只能在同一子网下的机器间宣告绑定。
>?Keepalived 是基于 VRRP 协议的一款高可用软件，Keepalived 配置通过 keepalived.conf 文件完成。
>


高可用虚拟 IP 的架构如下图所示。
![](https://main.qcloudimg.com/raw/6cf7f99f1cfad6a26da8b4734035b97b.png)
以上图举例，假设搭建 CVM1 和 CVM2 为一套高可用主备集群，实现原理如下：
1. CVM1 和 CVM2 均安装 keepalived 软件，配置 HAVIP 为 VRRP VIP，并设置主备服务器的优先级（priority 值），值越大优先级越高。
2. Keepalived 中的 VRRP 协议通过比对 CVM1 和 CVM2 的初始优先级大小，选举出 Master 服务器，即 CVM1 为 Master 服务器，CVM2 为 Backup 服务器。
3. Master 服务器向外发送 ARP 报文，宣告 VIP（该 VIP 为 HAVIP），并更新 VIP 和 MAC 的地址映射。此时，真正对外提供服务的服务器为 Master 服务器，通信的内网 IP 为 HAVIP 。同时，可在 HAVIP 控制台看到，HAVIP 绑定的服务器为 Master 服务器 CVM1。   
4. （可选）可以在控制台为 HAVIP 绑定 EIP，实现公网交互。
5. Master 服务器会周期性发送 VRRP 报文给 Backup 服务器。如果 Master 服务器异常，Backup 服务器在一定时间内没有收到 VRRP 报文，则会将自己设置为 Master，并对外发送 ARP更新，报文携带自己的 MAC 地址，此时 Backup 服务器 CVM2 将作为 Master 服务器对外提供通信服务，外部访问的报文将转发至 CVM2 处理。在 HAVIP 控制台可看到 HAVIP 绑定的云服务器变更为 CVM2。

## 常见使用场景
- **负载均衡的 HA**
  用户自己部署负载均衡时，一般业务架构是：负载均衡之间做 HA，后端机器做集群。因此部署负载均衡的两台服务器间要部署 HA，用 HAVIP 作为 virtual IP。
- **关系型数据库主备**
  两台数据库之间通过 keepalived 或 Windows Server Failover Cluster 搭建高可用主备集群，需要 HAVIP 作为 virtual IP。详细操作请参见 [最佳实践-用 HAVIP+Keepallved 搭建高可用主备集群 ](https://cloud.tencent.com/document/product/215/20186)和 [最佳实践-用 HAVIP + Windows Server Failover Cluster 搭建高可用 DB](https://cloud.tencent.com/document/product/215/20187) 。


## 常见问题

### 为什么在 VPC 环境，需要使用 HAVIP 配合 Keepalived？
公有云厂商的普通内网 IP，出于安全考虑（如 ARP 欺骗等），不支持主机通过 ARP 宣告 IP 。如果用户直接在 keepalived.conf 文件中指定一个普通内网 IP 为 virtual IP，当 keepalived 将 virtual IP 从 MASTER 机器切换到 BACKUP 机器时，将无法更新 IP 和 MAC 地址的映射，而需要调 API 来进行 IP 切换。
以 keepalived 配置为例，IP 相关部分如下：
```plaintext
vrrp_instance VI_1 {
    state BACKUP           #备
    interface eth0          #网卡名 
    virtual_router_id 51
    nopreempt                   #非抢占模式
    #preempt_delay 10
    priority 80
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    unicast_src_ip 172.17.16.7   #本机内网 IP
    unicast_peer {
        172.17.16.13           #对端设备的 IP 地址，例如：10.0.0.1
    }

    virtual_ipaddress {

        172.17.16.3  #高可用虚拟IP，填写控制台申请到的 HAVIP 地址。

    }

    garp_master_delay 1
    garp_master_refresh 5

    track_interface {
        eth0              
    }

    track_script {
        checkhaproxy
    }
}
```
若没有 HAVIP，以下这段配置文件不生效。
```plaintext
virtual_ipaddress {
   172.17.16.3 #高可用虚拟IP，填写控制台申请到的 HAVIP 地址。
}
```

## 后续操作
- 了解 HAVIP 的使用限制，请参见 [限制说明](https://cloud.tencent.com/document/product/215/36692)。
- 了解 HAVIP 的操作指南，请参见 [管理 HAVIP](https://cloud.tencent.com/document/product/215/36694)。
