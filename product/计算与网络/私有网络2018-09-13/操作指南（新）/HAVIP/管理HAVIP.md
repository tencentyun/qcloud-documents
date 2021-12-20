本章节介绍如何在控制台创建高可用虚拟 IP（HAVIP），以及 HAVIP 创建后，在第三方软件中如何进行配置等后续操作。
>?目前 HAVIP 产品处于灰度优化中，如有需要，请提交 [内测申请](https://cloud.tencent.com/apply/p/azh0w1qoavk)。


## 操作步骤
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/)，在左侧导航栏中，选择**IP 与网卡** > **高可用虚拟 IP**。 
2. 在 HAVIP 管理页面，选择所在地域，单击**申请**。
3. 在弹出的**申请高可用虚拟 IP** 对话框中，配置 HAVIP 的参数。
 + 名称：填写 HAVIP 的名称。
 + 私有网络：选择待创建 HAVIP 所在的私有网络。
 + 子网：HAVIP 具有子网属性，请选择所在子网。
 + IP 地址：支持自动分配和手动填写。选择自动分配系统将从子网中分配一个 IP 地址；选择手动填写，需填写子网网段范围内的可用 IP 地址，且不能为系统保留 IP，例如，所属子网网段为：10.0.0.0/24，则可填的内网 IP 范围为：10.0.0.2 - 10.0.0.254。
  ![](https://main.qcloudimg.com/raw/036b8d78f4b0de150fbd2d1bb2ae143d.png)
4. 单击**确定**，创建成功的 HAVIP 展示在列表中，状态为**未绑定云服务器**。
    ![](https://main.qcloudimg.com/raw/eced960b793c2897d3267b7a7a3c8ccb.png)

## 后续操作
HAVIP 用于配合第三方 HA 软件使用，创建后还需要在第三方 HA 软件中操作（HAVIP 只是被操作的对象，作为可被声明绑定的内网 IP，操作的发起方为第三方 HA 软件，不在 HAVIP 的控制台实现绑定和解绑）。即：在第三方 HA 软件中，将 HAVIP 指定为可漂移的 VIP（Virtual IP Address），然后由第三方 HA 软件通过 ARP 协议指定 HAVIP 要绑定的网卡。示意图如下：
![](https://main.qcloudimg.com/raw/8417b0708ad72c76fce8662a66132928.png)
传统物理设备环境下，所有内网 IP 默认都是可以通过 ARP 协议绑定到网卡上的，都可以在 HA 软件中指定为可漂移的 IP。而在公有云环境下普通内网 IP 禁止 ARP 协议，若在 HA 软件中指定普通内网 IP 为可漂移的 IP，会导致漂移失败，因此在云服务器内的 HA 软件中，需要将 HAVIP 指定为可漂移的 VIP。该操作与第三方 HA 软件在非云平台的操作完全一样。
>?常见的 HA 软件有：Linux 下的 HeartBeat、keepalived、pacemaker，Windows下的 MSCS 等。
>
在 HA 软件指定 VIP 时（配置文件），填入您创建的 HAVIP 即可，配置示例如下：
<pre><code class="language-html">
vrrp_instance VI_1 {
#注意主备参数选择
    state MASTER               #设置初始状态为"备"。
    interface eth0             #设置绑定 VIP 的网卡，例如 eth0
    virtual_router_id 51       #配置集群 virtual_router_id 值
		nopreempt                  #设置非抢占模式
		preempt_delay 10           #抢占延时10分钟
    priority 100               #设置优先级，值越大优先级越高
    advert_int 1               #检查间隔，默认1秒
    authentication {           #设置认证
        auth_type PASS          #认证方式
        auth_pass 1111          #认证密码
    }
		unicast_src_ip 172.16.16.5 #设置本机内网IP地址
		unicast_peer{
		172.16.16.6                #对端设备的 IP 地址
		}
    virtual_ipaddress {     
		172.16.16.12               #<font color="red">设置“高可用虚拟IP”为可漂移的IP</font>
    }
	}
</code></pre>

在云服务器的 HA 软件中配置了 HAVIP 后，控制台中该 HAVIP 的状态将变更为【已绑定云服务器】。
![](https://main.qcloudimg.com/raw/f22aaa2b2b9aeb72e445c27f8702e089.png)

常见配置案例请参考：
+ [最佳实践 - 用 HAVIP+Keepallved 搭建高可用主备集群](https://cloud.tencent.com/document/product/215/20186)
+ [最佳实践 - 用 HAVIP + Windows Server Failover Cluster 搭建高可用 DB](https://cloud.tencent.com/document/product/215/20187) 

## 相关文档
高可用虚拟 IP 与普通内网 IP 类似，均支持在控制台绑定或解绑 EIP，如果您有公网通信的需求，可参考 [绑定或解绑 EIP](https://cloud.tencent.com/document/product/215/53706)，如无，可不绑定 EIP。
