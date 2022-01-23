本文将介绍如何在腾讯云 VPC 内通过 keepalived 软件 + [高可用虚拟 IP (HAVIP)](https://cloud.tencent.com/document/product/215/36691) 搭建高可用主备集群。
>?目前 HAVIP 产品处于灰度优化中，切换的时延在10s左右，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/azh0w1qoavk)。
>

## 基本原理
通常高可用主备集群包含2台服务器，一台主服务器处于某种业务的激活状态（即 Active 状态），另一台备服务器处于该业务的备用状态（即 Standby 状态），它们共享同一个 VIP（Virtual IP）。同一时刻，VIP 只在一台主设备上生效，当主服务器出现问题时，备用服务器接管 VIP 继续提供服务。高可用主备模式有着广泛的应用，例如，MySQL 主备切换、Nginx Web 接入。

在 VPC 的云服务器间可以通过部署 Keepalived 来实现高可用主备集群。Keepalived 是基于 vrrp 协议的一款高可用软件，Keepalived 配置通过 keepalived.conf 文件完成。
![](//mc.qcloudimg.com/static/img/a5aa34fb87508284d9e7a07898085728/1.png)
- 在传统的物理网络中，可以通过 keepalived 的 VRRP 协议协商主备状态，其原理是：主设备周期性发送免费 ARP 报文刷新上联交换机的 MAC 表或终端 ARP 表，触发 VIP 迁移到主设备上。
- 在腾讯云 VPC 中，支持部署 keepalived 来搭建主备高可用集群。与物理网络相比，主要区别是：
   - 使用的 VIP 必须是从腾讯云申请的 [高可用虚拟 IP (HAVIP)](https://cloud.tencent.com/document/product/215/36691) 。
   - VIP 有子网属性，只能在同一个子网下的机器间宣告绑定。

## 注意事项
+ 推荐使用单播方式进行 VRRP 通信。
>?本文演示配置为单播模式，如果使用组播方式进行 VRRP 通信，需提交 [组播内测申请](https://cloud.tencent.com/apply/p/rkx852nifjh)，待内测申请通过后参考 [开启或关闭组播功能](https://cloud.tencent.com/document/product/215/53428) 打开 VPC 组播开关；同时在 keepalived 配置文件中无需配置对端设备的 IP 地址，即**不配置** “unicast_peer” 参数。
>
+ 推荐使用 Keepalived（**1.2.24版本及以上**）。
+ 确保已经配置以下 garp 相关参数。因为 keepalived 依赖 ARP 报文更新 IP 信息，如果缺少以下参数，会导致某些场景下，主设备不发送 ARP 导致通信异常。
	```plaintext
	garp_master_delay 1
	garp_master_refresh 5
	```
+ 确保同一 VPC 下的每个主备集群需要配置不同的 vrrp router id。
+ 确定没有采用 strict 模式，即需要删除“vrrp_strict” 配置。
+ 控制单个网卡上配置的 VIP 数量，建议目前在单个网卡绑定的高可用虚拟 IP 数量不超过5个。如果需要使用多个虚拟 IP，建议在 keepalived 配置文件的 global_defs 段落添加或修改配置 “vrrp_garp_master_repeat 1”。
+ 通过调节 adver_int 参数的大小，在抗网络抖动及灾害恢复速度进行平衡取舍。当 advert_int 参数过小，容易受网络抖动影响发生频繁倒换和暂时 **双主（脑裂）** 直到网络恢复。当 advert_int 参数过大，会导致主机器故障后，主备倒换慢（即服务暂停时间长）。**请充分评估双主（脑裂）对业务的影响！**
+ track_script 脚本的具体执行项（如 checkhaproxy ）中的 interval 参数请适当提高，避免脚本执行超时导致 FAULT 状态的发生。
+ 可选：注意日志打印导致的磁盘使用量上涨，可以通过 logrotate 等工具解决。


## 操作步骤
>!本文操作步骤均以如下环境条件为例，实际操作时，请您务必使用实际环境参数进行替换。
>+ 主节点云服务器：HAVIP-01，172.16.16.5
>+ 备节点云服务器：HAVIP-02，172.16.16.6
>+ 高可用HAVIP：172.16.16.12
>+ 弹性公网IP：81.71.14.118
>+ 镜像版本：CentOS 7.6 64位
>
### 步骤1：申请 VIP[](id:step1)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/)。
2. 在左侧导航栏中，选择 **IP 与网卡**> **高可用虚拟 IP**。 
3. 在 HAVIP 管理页面，选择所在地域，单击**申请**。
4. 在弹出的**申请高可用虚拟 IP** 对话框中输入名称，选择 HAVIP 所在的私有网络和子网等信息，单击**确定**即可。
>?HAVIP 的 IP 地址可以自动分配，也可以手动填写。如果您选择手动填写，请确认填写内网 IP 在所属子网网段内，且不属于系统保留 IP。例如，所属子网网段为：10.0.0.0/24，则可填的内网 IP 范围 为：10.0.0.2 - 10.0.0.254。
>
![](https://main.qcloudimg.com/raw/c0dfa6657293a92774d21b48d436a6e0.png)
申请成功的 HAVIP 如下图所示。
![](https://main.qcloudimg.com/raw/a3d894863e5405477aa9910487c5f198.png)

### 步骤2：在主服务器和备服务器上安装 keepalived 软件（推荐1.2.24版本及以上）
本文以 CentOS 7.6镜像类型服务器为例提供 keepalived 的安装方法。
1. 查看 keepalived 软件包版本号是否符合要求。
 ```plaintext
 yum list keepalived
 ```
 + 是 = 执行[2](#substep2)
 + 否 = 执行[3](#substep3)
2. <span id="substep2">使用 yum 方式安装软件包。
```plaintext
yum install -y keepalived
```
3. 使用源码方式安装软件包。[](id:substep3)
```plaintext
tar zxvf keepalived-1.2.24.tar.gz
cd keepalived-1.2.24
./configure --prefix=/
make; make install
chmod +x /etc/init.d/keepalived   //防止出现 env: /etc/init.d/keepalived: Permission denied
```

### 步骤3：配置 keepalived，绑定高可用 VIP 到主备云服务器
1. 登录主节点云服务器 HAVIP-01，执行 `vim /etc/keepalived/keepalived.conf`，修改相关配置。
<dx-alert infotype="explain" title="">
HAVIP-01 和 HAVIP-02 在本例中将被配置成“等权重节点”，即 state 均为 BACKUP，priority 均为 100。优点是可以减少抖动造成的倒换次数。
</dx-alert>
 ```plaintext
   ! Configuration File for keepalived
   global_defs {
      notification_email {
        acassen@firewall.loc
        failover@firewall.loc
        sysadmin@firewall.loc
      }
      notification_email_from Alexandre.Cassen@firewall.loc
      smtp_server 192.168.200.1   
      smtp_connect_timeout 30
      router_id LVS_DEVEL
      vrrp_skip_check_adv_addr
      vrrp_garp_interval 0
      vrrp_gna_interval 0
   }
   vrrp_script checkhaproxy
   {
        script "/etc/keepalived/do_sth.sh"   # 检测业务进程是否运行正常。其中“do_sth.sh”文件为用户自定义的业务进程检测脚本，请根据业务需要来执行，执行时“do_sth.sh”更换为实际的脚本名称。
        interval 5
   }
   vrrp_instance VI_1 {
   # 注意主备参数选择
   state BACKUP              # 设置初始状态均为“备“
       interface eth0          # 设置绑定 VIP 的网卡 例如 eth0  
       virtual_router_id 51    # 配置集群 virtual_router_id 值
       nopreempt               # 设置非抢占模式，
       # preempt_delay 10      # 仅 state MASTER 时生效    
       priority 100            # 两设备是相同值的等权重节点
       advert_int 5        
       authentication {
           auth_type PASS
           auth_pass 1111
       }
       unicast_src_ip 172.16.16.5  # 设置本机内网IP地址
       unicast_peer {
           172.16.16.6             # 对端设备的 IP 地址
       }
       virtual_ipaddress {
           172.16.16.12           # 设置高可用虚拟 VIP 
       }
       notify_master "/etc/keepalived/notify_action.sh MASTER"
       notify_backup "/etc/keepalived/notify_action.sh BACKUP"
       notify_fault "/etc/keepalived/notify_action.sh FAULT"
       notify_stop "/etc/keepalived/notify_action.sh STOP"
       garp_master_delay 1    # 设置当切为主状态后多久更新 ARP 缓存
       garp_master_refresh 5   # 设置主节点发送 ARP 报文的时间间隔

       track_interface {
                   eth0               # 使用绑定 VIP 的网卡 例如 eth0
           }
       track_script {
          checkhaproxy 
       }
   }
   ```
2. 按“esc”退出编辑状态，输入`:wq!`保存并退出。
3. 登录备节点云服务器 HAVIP-02，执行 `vim /etc/keepalived/keepalived.conf`，修改相关配置。
   ```plaintext
   ! Configuration File for keepalived
   global_defs {
      notification_email {
        acassen@firewall.loc
        failover@firewall.loc
        sysadmin@firewall.loc
      }
      notification_email_from Alexandre.Cassen@firewall.loc
      smtp_server 192.168.200.1
      smtp_connect_timeout 30
      router_id LVS_DEVEL
      vrrp_skip_check_adv_addr
      vrrp_garp_interval 0
      vrrp_gna_interval 0
   }
   vrrp_script checkhaproxy
   {
       script "/etc/keepalived/do_sth.sh"
        interval 5
   }
   vrrp_instance VI_1 {
   # 注意主备参数选择
   state BACKUP            # 设置初始状态均为“备“
       interface eth0          # 设置绑定 VIP 的网卡 例如 eth0  
       virtual_router_id 51    # 配置集群 virtual_router_id 值
       nopreempt               # 设置非抢占模式
       # preempt_delay 10      # 仅 state MASTER 时生效   
       priority 100            # 两设备是相同值的等权重节点
       advert_int 5       
       authentication {
           auth_type PASS
           auth_pass 1111
       }
       unicast_src_ip 172.16.16.6  # 设置本机内网 IP 地址
       unicast_peer {
           172.16.16.5             # 对端设备的 IP 地址
       }
       virtual_ipaddress {
           172.16.16.12           # 设置高可用虚拟 VIP 
       }
       notify_master "/etc/keepalived/notify_action.sh MASTER"
       notify_backup "/etc/keepalived/notify_action.sh BACKUP"
       notify_fault "/etc/keepalived/notify_action.sh FAULT"
       notify_stop "/etc/keepalived/notify_action.sh STOP"
       garp_master_delay 1    # 设置当切为主状态后多久更新 ARP 缓存
       garp_master_refresh 5   # 设置主节点发送ARP报文的时间间隔
       track_interface {
                   eth0               # 使用绑定 VIP 的网卡 例如 eth0
           }
       track_script {
          checkhaproxy 
       }
   }
   ```
4. 按“esc”退出编辑状态，输入`:wq!`保存并退出。
5. 重启 keepalived 进程使配置生效。
 ```plaintext
 systemctl start keepalived
 ```
6. 检查两台云服务器的主备状态，并确认 HAVIP 已经正确的绑定到主备服务器。
>?此示例中 HAVIP-01 先启动 keepalived 服务，所以正常情况下，HAVIP-01 将被选择为主节点。
>
登录 [高可用虚拟 IP](https://console.cloud.tencent.com/vpc/havip) 控制台，可以看到 HAVIP 绑定的云服务器为主节点云 HAVIP-01，如下图所示。
![](https://main.qcloudimg.com/raw/6c6755680da646ab26d5774873af82d5.png)


### 步骤4：**VIP 绑定弹性公网 IP（可选）**  
1. 在 [高可用虚拟 IP](https://console.cloud.tencent.com/vpc/havip) 控制台，单击 [步骤一 ](#step1)中申请的 HAVIP 所在行的**绑定**。
![](https://main.qcloudimg.com/raw/79e1e4c95b29f660997b987a8487bab4.png)
2. 在弹出的**绑定弹性公网 IP** 对话框中选择待绑定的 EIP，并单击**确定**。如果没有可用的 EIP，请先在 [弹性公网 IP](https://console.cloud.tencent.com/cvm/eip?rid=46)控制台申请。
![](https://main.qcloudimg.com/raw/c679a9d21a4e039ae46db333e0e50dcf.png)

### 步骤5：使用 notify_action.sh 进行简单的日志记录（可选）
keepalived 主要日志仍然记录在“/var/log/message”中，可以通过添加 notify 的脚本来进行简单的日志记录。
1. 登录云服务器，执行 `vim /etc/keepalived/notify_action.sh` 命令添加脚本“notify_action.sh”，脚本内容如下：
   ```plaintext
   #!/bin/bash
   #/etc/keepalived/notify_action.sh
   log_file=/var/log/keepalived.log
   log_write()
   {
       echo "[`date '+%Y-%m-%d %T'`] $1" >> $log_file
   }
   [ ! -d /var/keepalived/ ] && mkdir -p /var/keepalived/
   
   case "$1" in
       "MASTER" )
           echo -n "$1" > /var/keepalived/state
           log_write " notify_master"
           echo -n "0" /var/keepalived/vip_check_failed_count
           ;;
       "BACKUP" )
           echo -n "$1" > /var/keepalived/state
           log_write " notify_backup"
           ;;
       "FAULT" )
           echo -n "$1" > /var/keepalived/state
           log_write " notify_fault"
           ;;
       "STOP" )
           echo -n "$1" > /var/keepalived/state
           log_write " notify_stop"
           ;;
       *)
           log_write "notify_action.sh: STATE ERROR!!!"
           ;;
   esac
   ```
2. 执行 `chmod a+x /etc/keepalived/notify_action.sh` 修改脚本权限。

### 步骤6：验证主备倒换时 VIP 及外网 IP 是否正常切换
通过重启 keepalived 进程、重启子机等方式模拟主机故障，检测 VIP 是否能正常迁移。
- 如果完成了主备切换，则可以看到控制台的绑定主机已经切换为 backup 云服务器。
- 另外，也可以从 VPC 内 ping VIP 的方式，查看网络中断到恢复的时间间隔，每切换一次，ping 中断的时间大约为4秒。从公网侧 ping HAVIP 绑定的 EIP，可以查看网络中断到恢复的时间间隔，每切换一次，ping 中断的时间大致为4秒。
- 使用 ip addr show 检查 havip 是否出现主设备网卡上。
