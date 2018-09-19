## 产品简介
高可用虚拟 IP（HAVIP）是一个浮动的内网 IP，支持机器通过 ARP 宣告进行绑定，更新 IP 和 MAC 地址的映射关系。在高可用部署（如 keepalived）场景下，该 IP 可从 主服务器切换至备服务器，从而完成业务容灾。
### 产品特点
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
>**注意：**
1. 每个 VPC 的 HAVIP 默认配额为 10 个。
2. 由后端云服务器宣告占有该 HAVIP，不支持手动在控制台把 HAVIP 绑定指定机器（体验与传统物理机保持一致）。
3. 是否发生迁移由后端 RS 根据配置文件协商决定，不是由 HAVIP 决定。
4. 只支持 VPC 网络，不支持基础网络。
5. 心跳检测需要在云服务器中的应用来实现，不是靠 HAVIP 实现，HAVIP 仅作为一个被 ARP 宣告的浮动 IP（体验与传统物理机保持一致）。
6. 灰度阶段，请提工单申请开通。

## 计费方式
腾讯云 HAVIP 可免费使用。

## 操作指南
<span id="chuangjian"></span>
### 创建 HAVIP
1. 打开 [HAVIP 控制台](https://console.cloud.tencent.com/vpc/havip)，单击【新建】。
 ![](https://main.qcloudimg.com/raw/80524d2e7953a62da7e5a1a061fc7a54.png)
2. 输入名称，选择所在地域、HAVIP 所在的 VPC 和子网，单击【创建】即可。
HAVIP 的地址可以自动分配，也可以手动指定（手动指定的合法校验跟普通内网 IP 一致）。

### 绑定和解绑 HAVIP
不是从控制台进行绑定，而是由后端云服务器根据心跳检测，协商和声明哪一设备绑定 HAVIP，此处跟传统模式一样。您也可以通过更改 HA 应用的配置文件来更改绑定关系。
如，在 keepalived 方案下，在 keepalived.conf 中指定 virtual_address。如果是其他方案，在对应的配置文件中指定virtual IP 为 HAVIP。

### 释放 HAVIP
1. 打开 [HAVIP 控制台](https://console.cloud.tencent.com/vpc/havip)，在列表中找到要释放的 HAVIP。
2. 单击【释放】>【删除】即可。
 ![](https://main.qcloudimg.com/raw/4b041dbf53ff01cf470ee58ac34dc6ad.png)

>**注意：**
>释放后请更改云服务器中的配置文件。

## 使用申请
HAVIP 目前处于灰度阶段，如需使用请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=168&source=0&data_title=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C%20VPC&level3_id=181&radio_title=%E7%A7%81%E6%9C%89%E7%BD%91%E7%BB%9C/%E5%9F%BA%E7%A1%80%E7%BD%91%E7%BB%9C&queue=81&scene_code=17116&step=2) 申请。

## 常见使用场景
- **负载均衡的 HA**
用户自己部署负载均衡时，一般业务架构是：负载均衡之间做 HA，后端机器做集群。因此部署负载均衡的两台服务器间要部署 HA，用 HAVIP 作为 virtual Ip address。
- **关系型数据库主备**
两台数据库之间 keepalived 或 Windows Server Failover Cluster，需要 HAVIP 作为 virtual IP。

## 最佳实践
**用 HAVIP + Windows Server Failover Cluster 搭建高可用 DB**
1. **创建 HAVIP**
打开 [HAVIP 控制台](https://console.cloud.tencent.com/vpc/havip) ，创建一个 HAVIP，具体方法请参见 [创建 HAVIP](#chuangjian)。
2. **绑定和配置**
此处跟传统模式配置一样，由后端机器声明和协商哪一设备绑定创建的 HAVIP。您只要在对应的配置文件中指定 virtual IP为 HAVIP。
在群集管理器里，将刚才创建的 HAVIP 配置进去。
 ![](https://main.qcloudimg.com/raw/960af4c34f05cf71432c0143176db3c2.png)
3. **验证**
等待配置完成后，直接切换节点进行测试。
 ![](https://main.qcloudimg.com/raw/528373c391c718451acab0db9594ec04.png)
正常情况下会看到只有短暂中断后网络又通了（若切换较快甚至看不到中断），业务不受影响。
 ![](https://main.qcloudimg.com/raw/de5e3fd284d55c38c0a134efc1badf23.png)
