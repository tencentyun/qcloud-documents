本文将介绍如何在腾讯云 VPC 内通过 keepalived软件 + [高可用虚拟 IP (HAVIP)](https://cloud.tencent.com/document/product/215/36691) 搭建高可用主备集群。
## 基本原理
通常高可用主备集群包含2台服务器，一台主服务器处于某种业务的激活状态（即 Active 状态），另一台备服务器处于该业务的备用状态（即 Standby 状态），它们共享同一个 VIP（Virtual IP）。同一时刻，VIP 只在一台主设备上生效，当主服务器出现问题时，备用服务器接管 VIP 继续提供服务。高可用主备模式有着广泛的应用，例如，MySQL 主备切换、Nginx Web 接入。
![](//mc.qcloudimg.com/static/img/a5aa34fb87508284d9e7a07898085728/1.png)
- 在传统的物理网络中，可以通过 keepalived 的 VRRP 协议协商主备状态，其原理是：主设备周期性发送免费 ARP 报文刷新上联交换机的 MAC 表或终端 ARP 表，触发 VIP 迁移到主设备上。
- 在腾讯云 VPC 中，支持部署 keepalived 来搭建主备高可用集群。与物理网络相比，主要区别是：
   - 使用的 VIP 必须是从腾讯云申请的 [高可用虚拟 IP (HAVIP)](https://cloud.tencent.com/document/product/215/36691) 。
   - VIP 有子网属性，只能在同一个子网下的机器间宣告绑定。

## 注意事项

+ 推荐使用单播方式进行VRRP通信。
+ 强烈推荐使用Keepalived（**1.2.24版本及以上**），并确保已配置如下参数：
    ```plaintext
  garp_master_delay 1
  garp_master_refresh 5
    ```
由于 keepalived 依赖 ARP 报文更新 IP 信息，如果缺少以上参数，则会导致在某些场景下主设备不发送 ARP，进而导致通信异常。
+ 推荐使用 vmac 模式，并且同一 VPC 下的每个主备集群需要配置不同的 vrrp router id。
+ 控制单个网卡上配置的 VIP 数量，建议单个网卡绑定的高可用虚拟 IP 数量不超过5个。
+ 为了虚拟 IP 的切换更顺畅，腾讯云平台对单个网卡发送免费 ARP 宣告，并对虚拟 IP 的频率会进行一定限制。如果需要使用多个虚拟 IP，建议在 keepalived 配置文件的 global_defs 段落添加或修改配置。
   ```plaintext
  vrrp_garp_master_repeat 1
  ```
+ 腾讯云目前已经支持组播，但仍处于内测阶段。如需要通过组播方式进行 VRRP 通信，可通过 [工单申请](https://console.cloud.tencent.com/workorder/category) 内测。另外，网卡推荐使用默认路由所在的网卡，否则 vrrp 组播报文在其他网卡上的收发可能存在异常。

## 操作流程
1.  申请 VIP，该 VIP 仅支持在子网内迁移（因此需要保证主备服务器位于同一个子网）。
2.  主备服务器安装及配置 keepalived (**1.2.24版本及以上**），并修改配置文件。
3.  编辑使用 keepalived  的 notify 机制，借助 notify_action.sh 进行简单的日志记录。
4.  验证主备倒换时 VIP 是否正常切换。

## 操作步骤
### <span id="step1">步骤1：申请 HAVIP
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/)，在左侧导航栏中，选择【IP 与网卡】>【高可用虚拟 IP】。 
2. 在 HAVIP 管理页面，选择所在地域，单击【申请】。
3. 在弹出的【申请高可用虚拟IP】对话框中输入名称，选择 HAVIP 所在的私有网络和子网等信息，单击【确定】即可。
> ?HAVIP 的 IP 地址可以自动分配，也可以手动指定（手动指定的合法校验跟普通内网 IP 一致）。
> 
![](https://main.qcloudimg.com/raw/036b8d78f4b0de150fbd2d1bb2ae143d.png)
申请成功的HAVIP如下图所示。
![](https://main.qcloudimg.com/raw/57535230c79fe83966efa50c64c7f976.png)

### 步骤2：在主服务器和备服务器上分别安装 keepalived 软件包
本文提供常用镜像类型 CentOS 服务器的安装方法，如有其他需求，请联系技术支持人员。
1. 执行如下命令查看 keepalived 软件包的版本号是否为**1.2.24版本及以上**。
   ```plaintext
   yum list keepalived
   ```
 + 是 = 执行[步骤3](#step3)
 + 否 = 执行[2](#substep2)
2. <span id="substep2">安装相应版本软件包，您可根据实际情况选择如下安装方式。
 + yum 安装方式：
     ```plaintext
     yum install -y keepalived
     ```
 + 源码包安装方式：
     ```plaintext
     tar zxvf keepalived-1.2.24.tar.gz
     cd keepalived-1.2.24
     ./configure --prefix=/
     make; make install
     chmod +x /etc/init.d/keepalived
	//防止出现 env: /etc/init.d/keepalived: Permission denied
     ```

### <span id="step3">步骤3：修改配置 keepalived.conf
需要同时修改主服务器和备服务器上的 keepalived.conf 配置，主要配置摘要如下：
 ```plaintext
0) state            初始角色，均填写 BACKUP
1) interface        改成本机网卡名 例如 eth0
2) priority         两台设备配置大小相同的整数，如 50
3) unicast_src_ip   改成本机内网 IP
4) unicast_peer     改成对端机器内网 IP
5) virtual_ipaddress    改成内网 VIP  
6) track_interface  改成本机网卡名 例如 eth0
 ```
**配置示例参考：**
1. 登录云服务器，执行如下命令修改配置文件。
   ```plaintext
   vim /etc/keepalived/keepalived.conf
   ```
2. 配置文件修改如下：
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
   # vrrp_script checkhaproxy
   {
       script "/etc/keepalived/do_sth.sh"
        interval 5
   }
   vrrp_instance VI_1 {
   #注意主备参数选择
   state BACKUP                # 设置初始状态为“备“
       interface eth0          # 设置绑定VIP的网卡 例如 eth0  
       virtual_router_id 51    # 配置集群virtual_router_id值
       nopreempt               # 设置非抢占模式
       preempt_delay 10
       priority 30              # 设置优先级，值越大优先级越高
       advert_int 1        
       authentication {
           auth_type PASS
           auth_pass 1111
       }
       unicast_src_ip 172.16.0.16  # 设置本机内网IP地址
       unicast_peer {
           172.16.0.14             # 对端设备的IP地址
       }
       virtual_ipaddress {
           172.16.0.135           # 设置高可用虚拟VIP 
       }
       notify_master "/etc/keepalived/notify_action.sh MASTER"
       notify_backup "/etc/keepalived/notify_action.sh BACKUP"
       notify_fault "/etc/keepalived/notify_action.sh FAULT"
       notify_stop "/etc/keepalived/notify_action.sh STOP"
       garp_master_delay 1    # 设置当切为主状态后多久更新ARP缓存
       garp_master_refresh 5   # 设置主节点发送ARP报文的时间间隔
   
       track_interface {
                   eth0               # 使用绑定VIP的网卡 例如 eth0
           }
       track_script {
          checkhaproxy 
       }
   }
   ```
3. 修改完成后，在键盘按“esc”，执行`:wq!`保存配置并退出。

### 步骤4：**VIP绑定弹性公网IP（可选）**  
1. 在【高可用虚拟IP】控制台中，单击[步骤一](#step1)中申请的HAVIP所在行的【绑定】。
![](https://main.qcloudimg.com/raw/92f60018db711b55ca6c6a9531b1fa86.png)
2. 在弹出的【绑定弹性公网IP】对话框中选择待绑定的EIP，并单击【确定】。如果没有可用的EIP，请先在[弹性公网IP](https://console.cloud.tencent.com/cvm/eip?rid=46)控制台申请。
![](https://main.qcloudimg.com/raw/e8973f6d16020379f0a695c2fd35b948.png)

### 步骤5：验证主备倒换时 VIP 及外网 IP 是否正常切换
1. 执行如下命令，启动 keepalived。
   ```plaintext
   systemctl start keepalived
   ```
2. 验证主备切换容灾效果。
通过重启 keepalived 进程、重启子机等方式模拟主机故障，检测 VIP 是否能正常迁移。通过 ping VIP 的方式，可以查看网络中断到恢复的时间间隔，每切换一次，ping 中断的时间大致为4秒。
3. 脚本日志将会写到“keepavlied.log”文件中，可以通过日志确认是否存在异常。
   ```plaintext
   /var/log/keealived.log
   ```
keepalived 进程的日志仍会写到message文件中。
   ```plaintext
   /var/log/message
   ```
日志会占用您的磁盘空间，您可以自行借助 logrotate 等工具处理日志累积的问题。

### 步骤6：使用 notify_action.sh 进行简单的日志记录
keepalived 主要日志仍然记录在 /var/log/message。
```
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
        echo -n "0" > /var/keepalived/vip_check_failed_count
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
