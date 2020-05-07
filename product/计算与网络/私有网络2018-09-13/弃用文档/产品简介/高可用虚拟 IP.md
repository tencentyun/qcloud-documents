## 什么是高可用虚拟 IP
高可用虚拟 IP（HAVIP）是一个浮动的内网 IP，支持机器通过 ARP 宣告进行绑定，更新 IP 和 MAC 地址的映射关系。在高可用部署（如 keepalived）场景下，该 IP 可从 主服务器切换至备服务器，从而完成业务容灾。
### 特点介绍
1. HAVIP 是一个浮动的内网 IP，不会固定在指定机器上。后端云服务器通过 ARP 宣告可更改与 HAVIP 的绑定关系。
2. 不在控制台显式绑定，而是在后端云服务器的配置文件中配置，由后端云服务器发起绑定。
3. 需要在云服务器内配置该浮动 IP，完成高可用应用的配置，如 keepalived 等。
4. 有子网属性，只能被同一个子网下的机器宣告绑定。

### 针对问题
公有云厂商的普通内网 IP，出于安全考虑（如 ARP 欺骗等），不支持主机通过 ARP 宣告 IP 。当用户直接在 keepalived.conf 文件中指定一个普通内网 IP 为 virtual_address，系统无法完成迁移。
由此带来的问题是：如果用普通内网 IP，keepalived 将 virtual IP 从 MASTER 机器切换到 BACKUP 机器时，无法更新 IP 和 MAC 地址的映射，需要调 API 来进行 IP 切换。
以 keepalived 配置为例，IP 相关部分如下：
```

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

        172.17.16.3          #虚拟IP，其中这里需要一个浮动的IP，对外呈现这个IP在主备切换后重新映射IP与MAC地址的关系

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
```

virtual_ipaddress {

        172.17.16.3          #虚拟 IP，其中这里需要一个浮动的 IP，对外呈现这个 IP 在主备切换后重新映射 IP 与 MAC 地址的关系
    

}


```

针对以上问题，腾讯云创新性推出 HAVIP，满足客户对高可用的需求。
>!
1. 每个 VPC 的 HAVIP 默认配额为10个。
2. 由后端云服务器宣告占有该 HAVIP，不支持手动在控制台把 HAVIP 绑定指定机器（体验与传统物理机保持一致）。
3. 是否发生迁移由后端 RS 根据配置文件协商决定，不是由 HAVIP 决定。
4. 只支持 VPC 网络，不支持基础网络。
5. 心跳检测需要在云服务器中的应用来实现，不是靠 HAVIP 实现，HAVIP 仅作为一个被 ARP 宣告的浮动 IP（体验与传统物理机保持一致）。
6. 灰度阶段，请提工单申请开通。

## 计费方式
腾讯云 HAVIP 可免费使用。

## 使用申请
HAVIP 目前处于灰度阶段，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/ednylty94f) 。

## 常见使用场景
- **负载均衡的 HA**
用户自己部署负载均衡时，一般业务架构是：负载均衡之间做 HA，后端机器做集群。因此部署负载均衡的两台服务器间要部署 HA，用 HAVIP 作为 virtual Ip address。
- **关系型数据库主备**
两台数据库之间 keepalived 或 Windows Server Failover Cluster，需要 HAVIP 作为 virtual IP。详细操作请参见 [最佳实践-用 HAVIP + Windows Server Failover Cluster 搭建高可用 DB](https://cloud.tencent.com/document/product/215/20187)。
## 操作指南
控制台操作，详情请参见 [操作概述](https://cloud.tencent.com/document/product/215/20133)。
