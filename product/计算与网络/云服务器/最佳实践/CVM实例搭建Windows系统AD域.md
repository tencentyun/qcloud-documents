## 操作场景
活动目录 AD（Active Directory）是微软服务的核心组件。AD 能实现高效管理，例如批量管理用户、部署应用和更新补丁等。许多微软组件（例如 Exchange）和故障转移群集也需要 AD 域环境。本文以 Windows Server 2012 R2 数据中心版64位操作系统为例，介绍如何搭建 AD 域。

## 前提条件

- 已创建两台 Windows 云服务器 CVM 实例，分别作为域控制器（DC）和客户端（Client）。如您未购买实例，请参见 [快速配置 Windows 云服务器](https://cloud.tencent.com/document/product/213/2764)。
- 创建的实例需满足以下条件：
	- 分区为 NTFS 分区。
	- 实例支持 DNS 服务。
	- 实例支持 TCP/IP 协议。

## 实例网络环境
- 组网信息：网络类型采用私有网络 VPC，交换机的私有网段为10.0.0.0/16。
- 域名信息：示例域名为 `example.com`。作为 DC 的 CVM 实例 IP 地址为10.0.5.102，作为客户端的 CVM 实例 IP 地址为10.0.5.97。
<dx-alert infotype="notice" title="">
搭建 AD 域后，请确保 CVM 实例始终使用相同的 IP 地址，否则 IP 地址变化会导致访问异常。
</dx-alert>



## 相关概念
活动目录 AD（Active Directory）是微软服务的核心组件，相关名词概念如下：
- **DC**：Domain Controllers，域控制器。
- **DN**：Distinguished Name，识别名。
- **OU**：Organizational Unit，组织单位。
- **CN**：Canonical Name，正式名称。
- **SID**：Security Identifier，安全标识符。


## 操作步骤

<dx-alert infotype="explain" title="">
不推荐使用已有的域控制器通过创建自定义镜像部署新的域控。如必须使用，请确保新建实例的主机名（hostname）和创建自定义镜像之前实例的主机名必须保持一致，否则可能会报错“服务器上的安全数据库没有此工作站信任关系”。您也可以在创建实例后修改成相同的主机名，解决此问题。
</dx-alert>



### 部署 AD 域控制器[](id:Step1)
1. 登录作为 DC 的实例，详情参见 [使用标准方式登录 Windows 实例](https://cloud.tencent.com/document/product/213/57778)。
2. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f779581f1ce3edfead8c725ce1504009.png" style="margin:-3px 0px"> ，打开服务器管理器。
3. 单击**添加角色和功能**，弹出 “添加角色和功能向导” 窗口。
4. 在“选择安装类型”界面，选择**基于角色或基于功能的安装**，并连续单击2次下一步。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/413f2376200fe7a64d56035206ac2c21.png)
5. 在 “选择服务器角色” 界面，勾选如下图所示的  “Active Directory 域服务”及 “DNS 服务器”，并在弹出窗口中单击**添加功能**及**继续**。
该步骤以将 AD 域服务和 DNS 服务部署在同一台实例上为例。
![](https://qcloudimg.tencent-cloud.cn/raw/a9f62f646661dc1c3559b12328ed8077.png)
6. 保持默认配置，连续单击4次**下一步**。
7. 在确认信息页面中，单击**安装**。
安装完成后，关闭“添加角色和功能”对话框。
8. 在操作系统界面，单击 <img src="https://main.qcloudimg.com/raw/f779581f1ce3edfead8c725ce1504009.png" style="margin:-3px 0px"> ，打开服务器管理器。
9. 在服务器管理器窗口中，单击 <img src="https://main.qcloudimg.com/raw/b7b26ebdfecb3b158adac1a37d7a23f3.png" style="margin:-3px 0px"> ，选择**将此服务器提升为域控制器**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/bc6e02bf64866c4458ec6599babe09a2.png)
10. 在打开的 “Active Directory 域服务配置向导”窗口中，将“选择部署操作”设置为**添加新林**，输入根域名，本文以 `example.com` 为例，单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b91884139c592c76cf3547fa7c5de711.png)
11. 设置目录服务还原模式（DSRM）密码，单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/192ba48444d9fef4faf46a2c5eb73983.png)
12. 保持默认配置，连续4次单击**下一步**。
13. 在“先决条件检查”中，单击**安装**开始安装 AD 域服务器。
安装完成后将自动重启实例，重新连接实例后可在**控制面板** > **系统和安全** > **系统**中查看安装结果。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/32475970bbb3c6ff99a6ced08c3e72e1.png)

### 修改客户端 SID
参考 [修改 SID 操作说明](https://cloud.tencent.com/document/product/213/4829)，修改作为客户端实例的 SID。


### 将客户端加入 AD 域
1. 登录作为客户端的实例，详情参见 [使用标准方式登录 Windows 实例](https://cloud.tencent.com/document/product/213/57778)。
2. 修改 DNS 服务器地址。
  1. 打开**控制面板** > **网络和 Internet** > **网络和共享中心**，在“网络和共享中心”窗口中，单击**以太网**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ecbcc37005bc2924ab9cb76055fd0666.png)
  2. 在“以太网 状态”窗口中，单击**属性**。
  3. 在“以太网 属性”窗口中选择 “Internet 协议版本4（TCP/IPv4）”，并单击**属性**。
  4. 在“Internet 协议版本4（TCP/IPv4）属性”窗口中，选择“使用下面的 DNS 服务器地址”，并将首选 DNS 服务器地址设置为 DC 实例的 IP 地址，本文以 `10.0.5.102` 为例。如下图所示：
  ![](https://qcloudimg.tencent-cloud.cn/raw/2201da4809892efa26558b3a99e6d324.png)
  在 [部署 AD 域控制器](#Step1) 中已将 AD 域服务和 DNS 服务部署在同一台 CVM 实例上（IP地址为10.0.5.102），故此处指定 DNS 服务器的地址为10.0.5.102。
 5. 单击**确定**，保存修改。
3. 在 cmd 窗口中，执行以下命令，检查是否能 Ping 通 DNS 服务器 IP 地址。
```
ping example.com
```
返回结果如下图所示，说明可 Ping 通 DNS 服务器 IP 地址。
![](https://qcloudimg.tencent-cloud.cn/raw/cfd1ab27a7aaaeb42f9a78c67e476a53.png)
4. 打开**控制面板** > **系统和安全** > **系统**，并单击“系统”窗口中的**更改设置**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6fb71866831646df81ed08c47e10843a.png)
5. 在弹出的“系统属性”窗口中，单击**更改**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/dbfe2df50797ee5fc07cb2ede72dc7ba.png)
6. 在弹出的“计算机名/域更改”窗口中，按需修改计算机名，并设置隶属于“域”为 `example.com`。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/52b3f11a0347a93eb52d47069d3def1a.png)
7. 单击**确定**。
8. 在弹出的 “Windows 安全”窗口中，输入 DC 实例的用户名及登录密码，单击**确定**。
弹出如下图所示确认窗口，表示已成功加入域。
![](https://qcloudimg.tencent-cloud.cn/raw/80856c8d02b87e6b00ef44df88941e89.png)
9. 单击**确定**，重启实例使配置生效。
<dx-alert infotype="explain" title="">
对于作为客户端的 CVM 实例，不推荐使用已加入域的客户端实例来创建自定义镜像，否则新镜像创建的实例会报错“服务器上的安全数据库没有此工作站信任关系”。如果确实需要，建议您在创建新的自定义镜像前先退出域。
</dx-alert>


