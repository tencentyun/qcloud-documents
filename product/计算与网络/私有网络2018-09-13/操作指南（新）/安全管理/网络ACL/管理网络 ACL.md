您可通过如下视频了解配置网络 ACL 实现访问控制的相关信息。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2355-35415?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 创建网络 ACL
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 单击左侧目录中的**安全** > **网络 ACL**，进入管理页面。
3. 在列表上方，选择地域和私有网络，单击**+新建**。
4. 在弹出框中，输入名称，选择所属的私有网络，单击**确定**即可。
![](https://main.qcloudimg.com/raw/7140c40f01c09ba07a900a39a0e5a49a.png)
5. 在列表页中，单击对应的 ACL ID 即可进入详情页，添加 ACL 规则、关联子网。

## 增加网络 ACL 规则
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 单击左侧目录中的**安全** > **网络 ACL**，进入管理页面。
3. 在列表中，找到需要修改的网络 ACL，单击其 ID，进入详情页。
4. 新增出/入站规则，单击**出站规则**或**入站规则** > **编辑** > **新增一行**，选择协议类型并输入端口、源 IP，以及选择策略。
 - 协议类型：选择 ACL 规则允许/拒绝的协议类型，如 TCP、UDP 等。
 - 端口：流量的来源端口，支持单个端口或端口段，如80或90 - 100。
 - 源 IP：流量的源 IP 或源网段，支持 IP 或 CIDR，如`10.20.3.0`或`10.0.0.2/24`。
 - 策略：允许或拒绝。
![](https://main.qcloudimg.com/raw/e24739da05d191661024a92d3738a3d4.png)
5. 单击**保存**即可。

## 删除网络 ACL 规则
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 单击左侧目录中的**安全** > **网络 ACL**，进入管理页面。
3. 在列表中，找到需要删除的网络 ACL，单击其 ID，进入"基本信息"页面。
4. 单击**入站规则**或**出站规则**选项卡，进入"规则列表"页面。
5. 单击**编辑**，删除入站规则与删除出站规则步骤一致，本文以删除入站规则为例。
![](https://main.qcloudimg.com/raw/2cfa0c2dea110d2f2fe830e6b4208430.png)
6. 在列表中，找到需要删除的规则所在行，单击操作栏下的**删除**。
>?此时本条 ACL 规则置灰。若本次删除属于误操作，您可单击操作栏下的**恢复删除**，将其恢复。
>
![](https://main.qcloudimg.com/raw/2870ab49970f82e80e06846f61d1d4fc.png)
7. 单击**保存**，保存上述操作。
>!ACL规则的删除或恢复删除操作，必须保存后才会生效。
>

## 子网关联网络 ACL
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 单击左侧目录中的**安全** > **网络 ACL**，进入管理页面。
3. 在列表中，找到需要关联的网络 ACL，单击其 ID，进入详情页。
4. 在“基本信息”页面的“关联子网”模块，单击**新增关联**。
![](https://main.qcloudimg.com/raw/a6113f7b3c76b6b1be07d6edd26f3530.png)
5. 在弹出框中，选择需要关联的子网，单击**确定**即可。
![2](https://main.qcloudimg.com/raw/a7a608ebaf447a6fc24a6f9f313d14e6.png)

## 子网解除关联网络 ACL
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 单击左侧目录中的**安全** > **网络 ACL**，进入管理页面。
3. 在列表中，找到需要解除关联的网络 ACL，单击其 ID，进入详情页。
4. 解除关联子网有以下方法：
 - 方法一：在“基本信息”页面的“关联子网”模块，找到需要解除关联的子网，单击**解绑**。
![1](https://main.qcloudimg.com/raw/beb96d3bea157af5f5c9c76c85b1cc7f.png)
 - 方法二：在“基本信息”页面的“关联子网”模块，勾选所有需要解除关联的子网，单击**批量解绑**。
![2](https://main.qcloudimg.com/raw/ab35d623e1d61749dcb6594b8de21901.png)
5. 在弹出框中单击**确定**即可。
![3](https://main.qcloudimg.com/raw/93c7ebc3980f072d1194e87538ab1a79.png)

## 删除网络 ACL
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc)。
2. 单击左侧目录中的**安全** > **网络 ACL**，进入管理页面。
3. 选择地域和私有网络。
4. 在列表中，找到需要删除的网络 ACL，单击**删除**并确定操作，即可删除该网络 ACL 及该网络 ACL 的所有规则。
>?若**删除**置灰，如下图中的网络 ACL`testEg`，表示该网络 ACL 正与子网相关联，您需要先解除子网关联后，才能进行删除操作。
>
![](https://main.qcloudimg.com/raw/52d13aac33e609dc59d132ffa4c71171.png)



