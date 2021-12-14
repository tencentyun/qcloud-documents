若单个 CVM 可绑定的公网 IP 的限额不满足您的需求时，可以添加辅助网卡来绑定多个公网 IP，以实现流量转移，提高 CVM 的利用率。本文将为您介绍如何为 Linux 云服务器和 Windows 云服务器添加辅助网卡并绑定多个 EIP。

## 前提条件
- 您已购买 Linux 云服务器和 Windows 云服务器，并且所属安全组开放了 ICMP 协议。
- 请确保您的公网 IP 在限额数内，具体限额请参见 [使用限制](https://cloud.tencent.com/document/product/1199/41648)。
- 请确保您的辅助网卡绑定内网 IP 数在限额数内，具体限额请参见 [弹性网卡-使用限制](https://cloud.tencent.com/document/product/576/18527)。

## 操作步骤
### 步骤一：添加辅助网卡[](id:add)
1. 登录 [CVM 控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=4)。
2. 在实例列表中，单击您的 CVM ID，在详细信息页面选择**弹性网卡**。
![](https://main.qcloudimg.com/raw/44111f021a232564c8a9502ae51e3445.png)
3. 在“弹性网卡”页面，单击**绑定弹性网卡**。
4. 在弹出的“绑定弹性网卡”窗口中，选择待绑定的弹性网卡。若您未创建弹性网卡，请单击**新建弹性网卡并绑定**，填写名称，选择弹性网卡的所属子网后，选择分配的内网 IP （可自动分配也可手动填写）。
>?
>- 若需分配多个 IP 请单击**增加一个辅助 IP**。
>- 若选择手动填写要分配的内网 IP，请确认填写的内网 IP 在所属子网网段内，且不属于系统保留 IP。
>例如，所属子网网段为：`10.0.0.0/24`，则可填的内网 IP 范围 为：`10.0.0.2 - 10.0.0.254`，本次操作以手动填写 `10.0.0.7` 为主 IP，`10.0.0.8`为辅助 IP 为例。
>
![](https://main.qcloudimg.com/raw/99c25b7fd0708218cd385fd06a459643.png)

### 步骤二：绑定 EIP
1. 在“弹性网卡”页面，单击 <img src="https://main.qcloudimg.com/raw/57a0c76b72cd97bd80bf857cd30c867a.png" style="margin: 0;">，以展开绑定的辅助网卡信息。
![](https://main.qcloudimg.com/raw/5032fdfa89ef927aadf89ef03fe997ba.png)
2. 在分配的 IP 的“已绑定公网 IP”栏下，单击**绑定**，分别为分配的 IP 绑定 EIP。
3. 在弹出的“绑定弹性公网IP”窗口中：
 - 若有可选的 EIP，选中并单击**确定**即可。
 - 若无可选的 EIP，可单击弹框上方的**新建**进行申请，详情请参见 [申请 EIP](https://cloud.tencent.com/document/product/1199/41698)，申请成功后返回弹出框并单击**刷新**，即可看见申请的 EIP，选中并单击**确定**即可。
![](https://main.qcloudimg.com/raw/a31ebe5ad4ac8bc6924af36279e2eb63.png)
4. 在辅助网卡的列表中，即可查看相关内网 IP 绑定公网 IP 的信息。
![](https://main.qcloudimg.com/raw/6768e7a3ce6052cbc4439459da9b764b.png)

### 步骤三：配置网卡
请根据您的云服务器操作系统类型，选择对应的配置网卡操作：
- [Linux 云服务器](#Linux)
- [Windows 云服务器](#Win)

#### Linux 云服务器[](id:Linux)
如下操作以 CentOS 7 云服务器为例：
1. 登录 [CVM 控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=4)。
2. 在实例列表中单击您的 CVM ID，在详细信息页面，选择**弹性网卡**。
3. 单击辅助网卡 ID，进入辅助网卡详情页，根据所属子网记录如下信息：
 - **子网掩码：**如下图所示，所属子网的 CIDR 位数为/24，即子网掩码为 `255.255.255.0`。
 CIDR 位数与子网掩码的对应关系如下表所示：
<table style="width:400px;important!">
<thead>
<tr>
<th width="150px">CIDR 位数</th>
<th width="250px">子网掩码</th>
</tr>
</thead>
<tbody><tr>
<td>/28</td>
<td>255.255.255.240</td>
</tr>
<tr>
<td>/27</td>
<td>255.255.255.224</td>
</tr>
<tr>
<td>/26</td>
<td>255.255.255.192</td>
</tr>
<tr>
<td>/25</td>
<td>255.255.255.128</td>
</tr>
<tr>
<td>/24</td>
<td>255.255.255.0</td>
</tr>
<tr>
<td>/23</td>
<td>255.255.254.0</td>
</tr>
<tr>
<td>/22</td>
<td>255.255.252.0</td>
</tr>
<tr>
<td>/21</td>
<td>255.255.248.0</td>
</tr>
<tr>
<td>/20</td>
<td>255.255.240.0</td>
</tr>
<tr>
<td>/19</td>
<td>255.255.224.0</td>
</tr>
<tr>
<td>/18</td>
<td>255.255.192.0</td>
</tr>
<tr>
<td>/17</td>
<td>255.255.128.0</td>
</tr>
<tr>
<td>/16</td>
<td>255.255.0.0</td>
</tr>
</tbody></table>
 - **网关：**如果您未更改其他设置，则网关为子网网段的首个 IP，如下图中的所属子网网段的首个 IP 即为 `10.0.0.1`。
![](https://main.qcloudimg.com/raw/130af7fd24d0c052661bec7679545112.png)
4. 登录云服务器，具体操作请参见 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)。执行如下命令，查看需配置（未显示 IP）的网卡信息，如图所示，需配置的网卡名称为 `eth1`：
```
ip addr
```
![](https://main.qcloudimg.com/raw/37c65397f52bce5702edb4b594bf708a.png)
5. 执行如下命令，进入`/etc/sysconfig/network-scripts/`文件夹：
```
cd /etc/sysconfig/network-scripts/
```
6. 根据实际情况创建新网卡的配置文件，如下以创建命名为 `ifcfg-eth1` 的配置文件为例 ：
   1. 输入命令：
```
cp ifcfg-eth0 ifcfg-eth1
```
   2. 输入命令修改配置文件内容：
```
	vim ifcfg-eth1
```
   3. 按 “i” 切换至编辑模式，把配置文件内容修改为以下内容：
```
DEVICE='eth1' # 此处填写步骤1中查看到的需配置的弹性网卡名称，请根据实际填写
 NM_CONTROLLED='yes'
 ONBOOT='yes'
 # 配置主ip
IPADDR0=10.0.0.7 # 此处填写步骤一：添加辅助网卡中手动填写的主 IP，请根据实际填写
NETMASK0=255.255.255.0 # 此处填写步骤三中所记录的子网掩码，请根据实际填写
 # 配置辅助 ip1
IPADDR1=10.0.0.8 # 此处填写步骤一：添加辅助网卡中手动填写的辅助 IP，请根据实际填写
NETMASK1=255.255.255.0 # 此处填写步骤三中所记录的子网掩码，请根据实际填写
 #GATEWAY='192.168.1.1'  # 因为 eth0 文件定义了网关，这里不再写网关，避免网关冲突，请根据实际填写
```
修改后，示例如下：
![](https://main.qcloudimg.com/raw/14c849d0031c859e2f65abc1f7862d02.png)
  4. 修改后保存配置文件并退出（在 vim 的末行模式下按 “Esc”，输入 “`wq!`” 并回车）。
7. 输入如下命令重启网络服务。
```
systemctl restart network
```
8. 检查和确认 IP 配置正确。
    1. 输入如下查看 IP 的命令。
```
ip addr
```
    2. 确认辅助网卡和辅助网卡上的 IP 可见，如下图所示。
     ![](https://main.qcloudimg.com/raw/d99d81a7bd973cb0a748d785c326cd22.png)
      如果 IP 配置不正确，请执行如下检查：
      1. 检查配置文件是否正确，如不正确请重新配置。
      2. 检查网络是否重启，如未重启，请执行如下命令重启网络，使配置生效。
``` 
systemctl restart network
```
9. 根据业务实际情况配置路由策略。
    按照上述步骤配置好后，Linux 镜像依旧默认从主网卡发包。您可通过策略路由来指定报文从某个网卡进，并从该网卡返回。
 1. 创建两张路由表<span id="6.1">。
``` 
echo "10 t1" >> /etc/iproute2/rt_tables
echo "20 t2" >> /etc/iproute2/rt_tables 
```
<dx-alert infotype="explain" title="">
此处10、20为自定义的路由 ID，t1、t2为自定义的路由表名称，请根据实际填写。
</dx-alert>
 2. 给两个路由表添加默认路由。
```
ip route add default dev eth0 via 192.168.1.1 table 10
ip route add default dev eth1 via 192.168.1.1 table 20 
```
<dx-alert infotype="explain" title="">
此处两个命令中，192.168.1.1要分别替换成主网卡所属子网的网关，以及辅助网卡所属子网的网关。
</dx-alert>
 3. 配置策略路由。
```
ip rule add from 192.168.1.5 table 10
ip rule add from 192.168.1.62 table 20 
```
<dx-alert infotype="explain" title="">
     - 此处两个命令中，IP 要分别替换成主网卡上的 IP，以及辅助网卡上的 IP；10和20为 [步骤6.1 ](#6.1)中自定义的路由 ID，请根据实际情况填写。
     - 配置完成后，可用同一个子网下的 CVM，来 Ping 内网地址，能 Ping 通即说明配置成功。如无其他 CVM，可以给辅助网卡的内网 IP 绑定公网 IP，Ping 该公网 IP 来验证。
     - 此处配置的是临时静态路由，网络重启后需要重新配置路由，如希望网络重启后路由不丢失，可再执行 [步骤7](#ste7_centos7) 将路由配置持久化。
</dx-alert>
10. <span id="step7_centos7">（可选）配置永久静态路由，即：将路由配置持久化写入文件，可确保网络重启后路由不丢失。
   1. 执行如下命令，进入配置文件。
```
vi /etc/sysconfig/network-scripts/route-eth1   
``` 
   2. 按 “i” 切换至编辑模式，并进行如下配置。
```
0.0.0.0/0 via 192.168.1.1 dev eth0 table 10
0.0.0.0/0 via 192.168.1.1 dev eth1 table 20
```
   3. 按 “Esc”，输入 “`:wq`”，保存文件并返回。


#### Windows 云服务器[](id:Win)
如下操作以 Windows 2012 云服务器为例：
1. 登录云服务器，具体操作请参见 [使用 RDP 文件登录 Windows 实例](https://cloud.tencent.com/document/product/213/5435)。
2. [](id:step2)执行如下步骤，查看云服务器辅助网卡的 IP 地址、子网掩码和默认网关和 DNS 服务器：
 1. 在操作系统界面，选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width:25px">，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: -3px 0px;">，打开 “Windows PowerShell” 窗口，执行如下命令：
```
ipconfig /all
```
 2. 记录输出的“以太网适配器 以太网 2”信息中的 IPv4 地址、子网掩码、默认网关和 DNS 服务器值。
 ![](https://main.qcloudimg.com/raw/c12ee37a6aee579326275f1f02bc3416.png)
3. 进入操作系统的**控制面板** > **网络和 Internet** > **网络和共享中心**，单击命名为“以太网 2”的网卡进行编辑。
4. 在 “以太网 2 状态” 弹窗中，单击**属性**。
![](https://main.qcloudimg.com/raw/663f2c94b7c1fca7605b770affb249c8.png)
5. 在“以太网 2 属性”弹窗中，双击**Internet 协议版本4（TCP/IPv4）**。
![](https://main.qcloudimg.com/raw/6f5ad88fd6bdbea09ac206b587fd868a.png)
6. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，填写如下信息：
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数值</th>
</tr>
</thead>
<tbody><tr>
<td>IP 地址</td>
<td>上述 <a href="#step2">步骤2</a> 中的 IPv4 地址。</td>
</tr>
<tr>
<td>子网掩码</td>
<td>上述 <a href="#step2">步骤2</a> 中的子网掩码。</td>
</tr>
<tr>
<td>默认网关</td>
<td>上述 <a href="#step2">步骤2</a> 中的默认网关地址。</td>
</tr>
<tr>
<td>首选 DNS 服务器</td>
<td>上述 <a href="#step2">步骤2</a> 中的 DNS 服务器。</td>
</tr>
<tr>
<td>备用 DNS 服务器</td>
<td>上述 <a href="#step2">步骤2</a> 中的备用 DNS 服务器。如果未列出备用 DNS 服务器，则无需填写此参数。</td>
</tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/baa33bf96c2fc833006f5b17e0347c9b.png" />
7. 单击**高级**，配置辅助内网 IP。
8. 在“高级 TCP/IP 设置”弹窗中的 “IP 地址”模块下，单击**添加**。
9. 在 “TCP/IP 地址”弹窗中，填写 [步骤一：添加辅助网卡](#add) 配置的辅助内网 IP，上述 [步骤2](#step2) 中的子网掩码，单击**添加**。若有多个辅助 IP，请重复上一步与当前步骤。
![](https://main.qcloudimg.com/raw/28de15eed49b374969340748ea615a50.png)
10. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，单击**确定**。
11. 在“以太网 2 属性”弹窗中，单击**确定**即可完成配置。
12. 在“以太网 2 状态”弹窗中，单击**详细信息**，可查看已配置的 IP 信息，如下图所示。
![](https://main.qcloudimg.com/raw/23f9f5bd806787314efa7f8ec28ab5af.png)

### 步骤四：结果验证
登录其他云服务器，执行 `ping <辅助网卡公网地址>`命令，若显示以下信息证明绑定成功。
>?若执行命令未得到以下结果，请检查 CVM 安全组配置是否开放 ICMP 协议。
>
![](https://main.qcloudimg.com/raw/aa70b56e1c53fa94bfdb828f00c15b78.png)
