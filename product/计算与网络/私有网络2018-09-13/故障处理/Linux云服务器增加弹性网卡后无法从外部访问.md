## 现象描述
某用户云服务器主网卡无公网 IP，主要用于内网通信，因有公网业务的需求，故绑定了一个弹性网卡（辅助网卡），并在弹性网卡上绑定了弹性公网 IP，但无法从外部正常访问。
![](https://qcloudimg.tencent-cloud.cn/raw/fed18ecde25765b8227a9d3ec509e305.png)

## 可能原因
云服务器绑定弹性网卡后，如需从外部访问，需要为弹性网卡绑定弹性公网 IP（EIP），并配置正确的网卡策略路由，该问题可从如下原因逐个排查定位：
+ 弹性网卡未正确绑定到云服务器上
+ 弹性网卡内网 IP 未正确配置到弹性网卡上
+ 路由表中默认路由内网网卡路由优先级高于外网网卡
+ 未配置网卡的策略路由表
+ 策略路由表中未添加网卡的默认网关
+ 未配置弹性网卡的策略路由规则


## 处理步骤
### 步骤一：检查弹性网卡是否已正确绑定到了云服务器上
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=16) ，单击云服务器实例 ID，进入实例详情页。
![](https://qcloudimg.tencent-cloud.cn/raw/a4f18b41f8b9f84df5a5d587931a5374.png)
2. 单击**弹性网卡**页签，查看云服务器是否有弹性网卡，以及是否绑定了 EIP。
  + 如有弹性网卡，且正确绑定了 EIP，如下图所示，则继续排查 [步骤二](#step2)。
  + 如没有，请参考 [绑定并配置弹性网卡](https://cloud.tencent.com/document/product/576/59351) 和 [绑定弹性公网 IP](https://cloud.tencent.com/document/product/576/18539) 配置后，再尝试外网访问，问题解决则结束，未解决则继续排查。
![](https://qcloudimg.tencent-cloud.cn/raw/15a33575cc81970f7bcaff623cb32591.png)

### 步骤二：检查弹性网卡内网 IP 是否正确配置到弹性网卡上[](id:step2)
1. 单击云服务器详情页**弹性网卡**页签下的弹性网卡 ID，进入弹性网卡详情页。
  	![](https://qcloudimg.tencent-cloud.cn/raw/5ea336de830e69b40e810261b85a014e.png)
2. 记录弹性网卡的 MAC 地址，并单击**IPv4 地址管理**页签，记录弹性网卡的内网 IP 地址。[](id:jilu2)
  + **MAC 地址**：
  ![](https://qcloudimg.tencent-cloud.cn/raw/1c2cf84f00b1bd936ef974575e497e13.png)
   + **弹性网卡内网 IP**：
  ![](https://qcloudimg.tencent-cloud.cn/raw/9900d50217c89687170b25a002b37b71.png)
3. 返回 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=16) ，单击云服务器右侧的**登录**，按照界面提示输入密码或密钥，以 [标准方式登录云服务器](https://cloud.tencent.com/document/product/213/5436)。
   ![](https://qcloudimg.tencent-cloud.cn/raw/e0ad83a474a5355b9adfb58a3071a5b7.png)
4. 执行如下命令，查看弹性网卡的内网 IP 和 MAC 地址与 [步骤2](#jilu2) 记录的是否一致。
   ``` plaintext
ip address
```
![](https://qcloudimg.tencent-cloud.cn/raw/dc1ea97fd1ce7333b886c839d7940e59.png)
   - 如一致，请继续排查[ 步骤三](#step3)。
   - 如不一致或缺失，请执行 [步骤5](#s5) 进行修改。
5. 执行如下命令重新修改弹性网卡的配置文件。[](id:s5)
>?此处以 Centos7.8 为例，Centos7 系统网卡配置文件一般存放在“/etc/sysconfig/network-scripts”目录，保存在“ ifcfg-网卡名称”文件。
>
   1. 执行如下命令，进入配置文件。
   ``` plaintext
 cd /etc/sysconfig/network-scripts/   #进入配置文件所在目录
 vim ifcfg-eth1  #编辑弹性网卡配置文件
```
 2. 按`i`开始编辑。
  ```plaintext
DEVICE='eth1'               #弹性网卡的网卡名
HWADDR=20:90:6F:63:98:CC     #弹性网卡的 MAC 地址
NM_CONTROLLED='yes'
ONBOOT='yes'
IPADDR='10.0.0.14'  # 此处填写弹性网卡上的内网 IP 地址，请根据实际填写   
NETMASK='255.255.255.0'  # 此处填写子网掩码，请根据实际填写
GATEWAY='10.0.0.1    # 填写网卡所在子网的网关 IP 地址，请根据实际填写
```
 3. 按“ESC”，并输入“:wq!”保存并退出。
 4. 执行如下命令，重启网络，使配置生效。
``` plaintext
systemctl restart network 
```
 5. 再次执行 `ip address`，确认内网 IP 已经配置到弹性网卡上，如下图所示。
  ![](https://qcloudimg.tencent-cloud.cn/raw/589b4dece75f0990dcc1c8b4e1115085.png)

### 步骤三（可选）：检查路由表中默认路由内网网卡的路由优先级是否高于外网网卡的优先级[](id:step3)
>?
>+ 本例 eth0 无弹性公网 IP，主要用于内网通信，为内网网卡；eth1 配置了弹性公网 IP，为外网网卡。
>+ 如路由表中无内网明细路由（如下图中10.0.0.0/24的路由条目），调整外网网卡路由优先级，有可能导致内网流量被转发到外网网卡，可能会对业务有影响，如担心此风险，可跳过该步骤，直接按照 [步骤四](#step4) 开始排查，即排查每个网卡，确保配置了独立的策略路由表，策略路由表的优势在于保证流量源进源出。
>+ 如路由表中有明细路由，可按照此方法排查并修复故障效率会更高。
>
1. 在云服务器登录界面，执行`route`命令查看当前云服务器的路由表，可以看到有两条“default”路由，这两条默认路由出接口分别为“eth0”内网和“eth1”外网，其中“eth0”这条“default”对应 metric 为100，“eth1”的 metric 为101，路由优选了“eth0”（metric 数值越小越优）走了内网卡，导致数据返回 Internet 失败，因此需要将“eth1”对应的路由优先级调高。
![](https://qcloudimg.tencent-cloud.cn/raw/4a37018a8f16d6bfe4d5423639bfa4b8.png)
2. 执行如下命令调整外网网卡路由优先级比内网网卡路由优先级高（metric 值越小优先级越高），然后再尝试外网访问，问题解决则结束，未解决请联系 [在线支持](https://cloud.tencent.com/online-service) 进一步定位处理。
```
ip route add default dev eth1 via 10.0.0.1 metric 10    #10.0.0.1请更换为弹性网卡的网关 IP，metric 值修改为比内网网卡的 metric 值100小即可，此处举例设置为10
```

### 步骤四：检查是否配置了网卡的策略路由表[](id:step4)
1. 在云服务器登录界面，执行如下命令查看是否已创建策略路由表。
```plaintext
cat /etc/iproute2/rt_tables
```
无策略路由表如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/74cf5b1c87466569cbf1b3ea911a98b6.png)
 - 如无，请执行 [步骤2](#s2) 创建策略路由表。
 - 如有，请继续排查 [步骤五](#step5)。
2. 创建两张策略路由表。[](id:s2)
```plaintext
echo "10 t1" >> /etc/iproute2/rt_tables    #10为自定义的路由ID，t1为自定义的路由表名称，请根据实际填写。
echo "20 t2" >> /etc/iproute2/rt_tables   #20为自定义的路由ID，t2为自定义的路由表名称，请根据实际填写。
```
 已配置好策略路由表如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/48425391ecb7a233d691b9030c4bcc7f.png)

### 步骤五：检查是否将每个网卡的默认网关配置到策略路由表中[](id:step5)
>?配置好策略路由表后，需要针对每个网卡配置网卡的默认路由到策略路由表中。
>
1. 在云服务器登录界面，执行如下命令，可看到默认路由表中已经有弹性网卡的内网路由信息。
``` plaintext
ip route show
```
![](https://qcloudimg.tencent-cloud.cn/raw/44598f6f19ad80b2d048b71cbe8b01cf.png)
2. 依次执行如下命令，查看 table  10和 table 20 路由表是否已配置默认网关。
```plaintext
ip route show table 10
ip route show table 20
```
 + 如下图所示，无返回信息，表示未配置默认网关，请执行 [步骤3](#s3) 为策略路由表添加默认网关。
 + 如有返回信息，且正确，则继续排查[ 步骤六](#step6)。
![](https://qcloudimg.tencent-cloud.cn/raw/711642e9a180f5d2f7f843cce0b03fbe.png)
3. 执行如下命令为两个路由表分别配置默认网关。[](id:s3)
``` plaintext
ip route add default dev eth0 via 10.0.1.1 table 10   #10.0.1.1为eth0的默认网关，请根据实际情况填写
ip route add default dev eth1 via 10.0.0.1 table 20   #10.0.0.1为eth1的默认网关，请根据实际情况填写
```
>!
>+ 每个 table 都需要检查，因为不同的 table 设置了不同网卡的默认路由。
>+ 请一定确认网关与网卡名对应一致，此处经常出现将 eth0 的网关配置到 eth1 上而导致配置问题，因此请务必做好检查。
>+ 此处配置为临时路由，重启网络后路由会消失，如需配置永久路由，请参见 [配置永久路由](https://cloud.tencent.com/document/product/576/59353#pzyjly)。
>
配置后可查询到两个路由表中配置的默认路由条目：
![](https://qcloudimg.tencent-cloud.cn/raw/09d21f25ad332cc8e107126558de6d2e.png)

### 步骤六：检查是否配置了正确的策略路由规则[](id:step6)
>?配置好默认路由后，目前系统已经知道哪个路由表走哪个网关出去，但还不知道某个网卡来的流量，要到哪个路由表上，因此需要查看是否为每个网卡配置了策略规则。
>
1. 执行 `ip rule list` 命令，查看是否有策略路由规则。
  - 如仅有0、32766、32767三条默认规则，表示弹性网卡未配策略路由规则，请执行[ 步骤2 ](#buzhou2)配置。
  - 如已配置如红框所示的策略规则，且仍然无法 ping 通，请联系 [在线支持](https://cloud.tencent.com/online-service) 进一步定位处理。
 ![](https://qcloudimg.tencent-cloud.cn/raw/11c5109e0495780c5c883814916ddd6e.png)
2. 按照如下步骤配置策略路由规则。[](id:buzhou2)
``` plaintext
ip rule add from 10.0.1.3 table 10     # IP为主网卡的 IP，10为主网卡的策略路由表代号，请根据实际情况填写。
ip rule add from 10.0.0.14 table 20     #  IP为弹性网卡的 IP，20为弹性网卡的策略路由表代号，请根据实际情况填写。
```
3. 配置后，在外网 ping 弹性网卡的EIP验证问题是否解决。
  - 如返回如下报文，表示已 ping 通，问题解决，结束。
  - 如依然无法 ping 通，请记录问题信息，并联系 [在线支持](https://cloud.tencent.com/online-service) 进一步定位处理。
 	![](https://qcloudimg.tencent-cloud.cn/raw/461b62ee3bc52d8a426afe9a7ba2a046.png)
