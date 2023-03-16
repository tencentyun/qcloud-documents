TDSQL-C MySQL 版支持实例级独立 IP 地址，即您可以通过集群下读写实例或任一只读实例的 IP 地址连接访问对应实例。本文为您介绍，如何使用内网或外网地址通过 Windows 云服务器连接集群。

## 前提条件
已创建数据库集群账号，具体请参见 [创建数据库账号](https://cloud.tencent.com/document/product/1003/62730)。

## 步骤一：查询需要连接的实例内/外网 IP 地址[](id:SLIPDZ2)
1. 登录 [TDSQL-C MySQL 版控制台](https://console.cloud.tencent.com/cynosdb/mysql/ap-beijing/cluster/cynosdbmysql-fo7dcbse/detail)。
2. 在集群列表页，根据实际使用的视图模式进行操作：
<dx-tabs>
::: 页签视图
1. 在左侧集群列表，单击目标集群，进入集群管理页。
2. 在集群详情下，找到需要查询内/外网 IP 地址的实例，在其所属网络下方可查看该实例的内/外网 IP 地址。
![](https://qcloudimg.tencent-cloud.cn/raw/b3edce7cf890c03e1409b3c65bef4bb4.png)
:::
::: 列表视图
1. 在集群列表中，找到目标集群，单击**集群 ID** 或操作列的**管理**，进入集群管理页面。
2. 在集群管理页面，选择实例列表页，选择读写实例或只读实例，在**字段：内/外网地址**下查看对应实例的内/外网 IP 地址。
![](https://qcloudimg.tencent-cloud.cn/raw/4bb088d5a196ec6ea6d6d4c4baef7cd2.png)
:::
</dx-tabs>

## 步骤二：连接集群下的目标实例
1. 登录到 Windows 云服务器，请参见 [快速配置 Windows 云服务器](https://cloud.tencent.com/document/product/1003/79662)。
2. 下载一个标准的 SQL 客户端。
>?推荐您下载 MySQL Workbench，并根据您的系统来下载适配版本的安装程序，下载地址请参见 https://dev.mysql.com/downloads/workbench/。
>
![](https://main.qcloudimg.com/raw/851ab46468c554097a0cf742017157b7.png)
3. 界面将提示 **Login**、**Sign Up** 和 **No, thanks, just start my download.**， 选择 **No thanks, just start my download.** 来快速下载。
![](https://main.qcloudimg.com/raw/47b195fb37ff584f21038ee54342d362.png)
4. 在此台云服务器上安装 MySQL Workbench。
>?
>- 此电脑上需要安装 Microsoft .NET Framework 4.5 和 Visual C++ Redistributable for Visual Studio 2015。
>- 您可以单击 MySQL Workbench 安装向导中的 **Download Prerequisites**，跳转至对应页面下载并安装这两个软件，然后安装 MySQL Workbench。
>
![](https://main.qcloudimg.com/raw/1af292f989f03f3e02e1200b77cb70c1.png)
5. 打开 MySQL Workbench，选择 **Database** > **Connect to Database**，输入 TDSQL-C MySQL 数据库集群的内网（或外网）地址和用户名、密码，单击 **OK** 进行登录。
![](https://main.qcloudimg.com/raw/9c9e5dcc8a2bb9fa15fa4d98a18308f1.png)
<table>
<thead><tr><th>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>Hostname</td>
<td>输入 TDSQL-C MySQL 版集群下目标实例的内/外网地址，内/外网地址查询方法参见 <a href="#SLIPDZ2">步骤一</a>。若为外网地址，请确认是否已开启，如未开启，请参见 <a href="https://cloud.tencent.com/document/product/1003/79682">开启或关闭外网地址</a>。</td></tr>
<tr>
<td>Port</td>
<td>内网（或外网）对应端口。</td></tr>
<tr>
<td>Username</td>
<td>填写创建数据库账号时的账号名，此处以默认账号 root 为例。</td></tr>
<tr>
<td>Password</td>
<td>Username 对应的密码。如忘记密码可在控制台进行修改。</td></tr>
</tbody></table>
6. 登录成功的页面如图所示，在此页面上您可以看到数据库的各种模式和对象，您可以开始创建表，进行数据插入和查询等操作。
![](https://main.qcloudimg.com/raw/33f081e99c384258bbc5ed3683ed4d7d.png)

## 常见问题
#### 如果忘记账号名以及密码，怎么重置后登录集群？
您可以在 TDSQL-C MySQL 版控制台，集群管理页面的**账号管理**下查看您创建的用于连接集群的账号名，当您忘记密码时，可通过**重置密码**操作修改密码后再登录集群。
![](https://qcloudimg.tencent-cloud.cn/raw/aa0aebe262c7b0d2f26e4218cafeefed.png)

#### 通过内网或外网连接 TDSQL-C MySQL 版是否需要为集群配置安全组？
需要配置安全组，详细步骤请参见 [配置安全组](https://cloud.tencent.com/document/product/1003/62745)。注意，若开启外网，通过外网连接时，配置的安全组规则需放通内网的访问端口。

#### 如果云服务器实例的安全组规则匹配不当，导致无法登录 Linux 实例怎么办？
如果云服务器实例的安全组规则匹配不当，如未放通相应端口导致无法登录 Linux 实例，您可以通过 [安全组（端口）验通工具](https://console.cloud.tencent.com/vpc/helper) 检查实例当前配置的安全组连通性。
![](https://main.qcloudimg.com/raw/9fc46a7133fdb07b631876cd9fa4c253.png)
通过一键检测可得知登录失败的可能原因。
![](https://qcloudimg.tencent-cloud.cn/raw/f0eccdbd666a04e73de610d42d3e3b49.png)
然后在云服务器实例详情页，选择**安全组** > **编辑规则**，然后放通对应端口，详细操作请参见 [添加安全组规则](https://cloud.tencent.com/document/product/213/39740)。

#### 无法连接集群还与哪些设置有关？
当无法连接集群时，您可以检查云服务器 CVM 和 TDSQL-C MySQL 是否在同一腾讯云账号下，是否处于同一地域，是否为同一 VPC 网络。需确保以上三点设置相同，才可以正常连接集群。
