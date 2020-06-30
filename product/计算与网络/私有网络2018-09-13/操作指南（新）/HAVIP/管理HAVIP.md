## 创建 HAVIP
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/)，在左侧导航栏中，选择【IP 与网卡】>【高可用虚拟 IP】。 
2. 在 HAVIP 管理页面，选择所在地域，单击【申请】。
3. 输入名称，选择 HAVIP 所在的私有网络和子网，单击【确定】即可。
>?HAVIP 的 IP 地址可以自动分配，也可以手动指定（手动指定的合法校验跟普通内网 IP 一致）。
>
![](https://main.qcloudimg.com/raw/036b8d78f4b0de150fbd2d1bb2ae143d.png)

## 绑定和解绑 HAVIP
HAVIP 用于配合第三方 HA 软件使用，与 CVM 的绑定与解绑不在腾讯云控制台进行，您需要在第三方 HA 软件中操作，将 HAVIP 指定为可漂移的 VIP（Virtual IP Address）即可，然后由第三方 HA 软件通过 ARP 协议指定 HAVIP 要绑定的网卡。示意图如下，具体操作请参见第三方 HA 软件：
![](https://main.qcloudimg.com/raw/8417b0708ad72c76fce8662a66132928.png)
- 传统物理设备环境下，所有内网 IP 默认都是可以通过 ARP 协议绑定到网卡上的，都可以在 HA 软件中指定为可漂移的 IP。
- 公有云环境下普通内网 IP 禁止 ARP 协议，若在 HA 软件中指定为可漂移 IP 的话，会导致漂移失败，因此需要用 HAVIP。

### 操作说明
1. HAVIP 只是被操作的对象，作为可被声明绑定的内网IP。操作的发起方为第三方 HA 软件，不在 HAVIP 的控制台实现绑定和解绑。
2. 在云服务器内的 HA 软件中，将 HAVIP 指定为可漂移的 VIP。此操作与第三方 HA 软件在非云平台的操作完全一样，不同 HA 软件的操作请参见对应软件的操作指南。
>?常见的 HA 软件有：Linux 下的 HeartBeat、keepalived、pacemaker，Windows下的 MSCS 等。

### 操作示例
HA 软件中指定 VIP 时（配置文件或操作界面均可），填入您创建的 HAVIP 即可，示例如下：
```
vrrp_instanceVI_1 {    
    state MASTER   
    interface eth0     
    virtual_router_id 51   
    priority 100    
    advert_int 1    
    authentication {   
        auth_type PASS
        auth_pass 1111   //密码
    }
    virtual_ipaddress {     //设置可漂移IP时，输入HAVIP
       172.16.2.8
    }
}
```

## 释放 HAVIP
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/)，在左侧导航栏中，选择【IP 与网卡】>【高可用虚拟 IP】，在列表中找到需要释放的 HAVIP。
2. 单击操作栏下的【释放】，在弹出框中选择【确认】即可。
>!释放后请更改云服务器中的配置文件。
>
![](https://main.qcloudimg.com/raw/8d39420e157104bb7974f70bfc878687.png)
