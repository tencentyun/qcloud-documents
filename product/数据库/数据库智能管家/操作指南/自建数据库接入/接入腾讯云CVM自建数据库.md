本文为您介绍如何将腾讯云服务器 CVM 自建数据库接入数据库智能管家 DBbrain。通过接入自建数据库，使得自建数据库也能拥有 DBbrain 提供的监控告警、诊断优化、数据库管理等自治服务能力。

## 接入方式
- **agent 接入（推荐）**：部署 DBbrain agent 在数据库主机上，可以自动发现您的数据库，可支持 DBbrain 提供的全部自治服务。优势如下：
 - 数据传输加密。
 - agent 自动采集并暂存数据，即使与 Server 断开连接也不会丢失数据。
 - 服务端与 agent 通讯需经过认证，且发送给 agent 执行的 SQL 语句带有校验。
 - 能够采集主机资源信息及慢日志，支持慢日志分析。
- **直连接入**：无需部署 DBbrain agent，仅需要在网络连通前提下，通过输入数据库帐号和密码即可快速接入您的数据库，可支持部分 DBbrain 提供的自治服务，适合比较少的自建数据库接入。

>?
>- 两种接入方式的功能对比请参见 [功能对比](https://cloud.tencent.com/document/product/1130/54283#jrfsgndb)。
>- DBbrain 当前支持的腾讯云 CVM 自建数据库类型：MySQL。

## [agent 接入流程](id:ajrlc)
### 进入接入页面
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/instance)，在左侧导航选择**实例概览**页，在上方自建实例接入卡片中单击**快速接入**，进入自建数据库实例接入页面。
![](https://main.qcloudimg.com/raw/b329ffde59299d6d3990eea430d7eae0.png)
2. 在自建数据库实例接入页面的“腾讯云CVM自建数据库”模块，单击 **agent接入**，进入接入流程。
![](https://main.qcloudimg.com/raw/62573457ac7802000d4d2a5546d73d79.png)

### 接入 CVM 自建数据库
#### 步骤1：选择 CVM
在选择服务器实例页面，选择有自建数据库的 CVM，然后单击**下一步**，进行 agent 部署。
- **选择云服务器获取方式**：支持列表拉取和手动输入两种方式获取 CVM：
  - 选择**列表拉取**时，可以直接获取到该账号下 CVM 的实例列表。
  - 当选择**手动输入**时，用户可以通过输入实例 IP 的方式获取到 CVM。
- **选择接入DBbrain服务地域**：目前支持广州、北京、上海、成都四个地域，如果用户的数据库所在地域不在以上地域内，建议就近选择。
- **添加云服务器**：
 - 若获取方式选择**列表拉取**，则选择好地域后，可直接在列表获取选择一个或多个 CVM。
![](https://main.qcloudimg.com/raw/9aa0ff851abe1af2c8c1fb79e4c5f4d3.png)
 - 若获取方式选择**手动输入**，则用户可以在文本框输入一个或多个实例 IP 来添加 CVM。
![](https://main.qcloudimg.com/raw/08974b52498cfe20a916eb2c56ed5efb.png)

#### 步骤2：部署 agent 
在 agent 部署页面，展示了上一步已选择的 CVM 和其 agent 状态。
1. 在 agent 部署页面，选择一个 CVM，单击**操作**列的**部署**，或选择多个 CVM，单击列表左上方的**批量部署**，将 agent 部署在 CVM。
>?CVM 中未部署 agent 的情况下，agent 状态显示为**--**。
>
![](https://main.qcloudimg.com/raw/e5076c083d14f67f19b20e1ca0ae8f24.png)
2. 在弹出的对话框，选择 agent 端口后，单击**部署**，即可根据所选的端口号，生成 agent 部署命令。
![](https://main.qcloudimg.com/raw/f0ce129450d3dca87028bf0492275084.png)
3. 复制生成的 agent 部署命令，并在 CVM 上运行，出现 `Start agent successfully` 后，则表示 agent 部署成功，返回部署页面，可查看 agent 状态变为**连接正常**。
agent 状态及对应操作说明：
<table>
<thead><tr><th width=10%>agent 状态</th><th width=35%>状态说明</th><th width=10%>操作</th><th width=45%>操作说明</th></tr></thead>
<tbody><tr>
<td rowspan=1>--</td>
<td>CVM 中未部署 agent</td>
<td>部署</td><td>单击<b>部署</b>，可将 agent 部署在 CVM 中</td></tr>
<tr>
<td rowspan=2>部署中</td>
<td rowspan=2>CVM 中正在部署 agent</td>
<td>查看</td><td>单击<b>查看</b>，可查看正在部署的 agent 端口号及 agent 命令</td></tr>
<tr>
<td>重置</td><td>单击<b>重置</b>，可将 agent 状态恢复为<b>--</b>，以满足用户想换 agent 端口号的场景，重新部署 agent</td></tr>
<tr>
<td rowspan=3>连接正常</td>
<td rowspan=3>CVM 中已成功部署 agent 且 agent 处于正常监控采集中，该 CVM 中的自建数据库可正常使用 DBbrain 提供的自治服务</td>
<td>查看</td><td>单击<b>查看</b>，可查看已部署 agent 的端口号及 agent 命令</td></tr>
<tr>
<td>停止</td><td>单击<b>停止</b>，可将处于正常连接状态的 agent 暂停连接</td></tr>
<td>重置</td><td>单击<b>重置</b>，可将 agent 状态恢复为<b>--</b>，以满足用户想换 agent 端口号的场景，重新部署 agent</td></tr>
<tr>
<td rowspan=2>连接失败</td>
<td rowspan=2>CVM 中部署 agent 失败，请参见 <a href="https://cloud.tencent.com/document/product/1130/54288">agent 接入问题</a></td>
<td>查看</td><td>单击<b>查看</b>，可查看该 agent 的端口号及 agent 命令</td></tr>
<tr>
<td>重置</td><td>单击<b>重置</b>，可将 agent 状态恢复为<b>--</b>，以此可以更换 agent 端口号，重新部署 agent</td></tr>
<tr>
<td rowspan=3>暂停连接</td>
<td rowspan=3>CVM 中已成功部署 agent 但 agent 处于暂停监控采集中</td>
<td>查看</td><td>单击<b>查看</b>，可查看该 agent 的端口号及 agent 命令</td></tr>
<tr>
<td>重连</td><td>单击<b>重连</b>，可将处于暂停连接状态的 agent 进行启动，恢复为连接正常</td></tr>
<tr>
<td>重置</td><td>单击<b>重置</b>，可将 agent 状态恢复为<b>--</b>，以满足用户想换 agent 端口号的场景，重新部署 agent</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/b4ef69e3c9671f0083424b3201b83233.png"  style="margin:0;">
4. 待至少存在一个状态为**连接正常**的 agent，单击**下一步**，进行下一步添加数据库。

#### 步骤3：添加数据库
在添加数据库实例页面，展示了上一步已成功部署 agent 的 CVM 及其数据库状态。
1. 在添加数据库实例页面，选择数据库类型。
2. 选择一个 CVM，单击**操作**列的**添加**，或选择多个 CVM，单击列表左上方的**批量添加数据库**，向成功部署 agent 的 CVM 中添加数据库。
>?已成功部署 agent 的 CVM，在未添加数据库的情况下，数据库的状态显示为**--**。
>
![](https://main.qcloudimg.com/raw/c6773c68ca64a77dbcb4959cc85d4c68.png)
3. 在弹出的对话框，填写数据库端口号、帐号、密码及数据库配置，单击**确定**，即可完成数据库的添加。
>?若数据库帐号授权异常，请参见 [数据库帐号授权异常](https://cloud.tencent.com/document/product/1130/54289)。
> 
数据库帐号配置说明如下：
<table>
<thead><tr><th >参数名称</th><th >参数说明</th></tr></thead>
<tbody><tr>
<td>端口号</td><td>DBbrain agent 侦测到的数据库端口号（若 CVM 中存在多个数据库，可单击<b>添加端口</b>，手动添加数据库端口号，以此来同时接入多个 CVM 自建数据库）。</td></tr>
<tr>
<td >账号</td><td>CVM 自建数据库的帐号（若该帐号尚未创建，需先单击<b>生成授权命令</b>，生成授权命令后，复制在数据库上执行所生成的授权命令）。</td></tr>
<tr>
<td >密码</td><td>CVM 自建数据库对应的密码。</td></tr>
<tr>
<td >数据库配置</td><td>包含 CPU、内存、磁盘，此配置为主机分配给该 CVM 自建数据库的配置，DBbrain 将根据用户所填写的数据库配置计算相关性能。</td></tr>
</tbody></table>
数据库帐号授权说明如下：
<table>
<thead><tr><th >权限</th><th >权限说明</th></tr></thead>
<tbody><tr>
<td>PROCESS</td><td>查看所有连接进程，用于实时会话展示进程。</td></tr>
<tr>
<td>REPLICATION SLAVE, REPLICATION CLIENT</td><td>查看主备库状态，查看备库 relaylog 和 binlog 事件，用于诊断主备复制异常。</td></tr>
<tr>
<td>SHOW DATABASES, SHOW VIEW, RELOAD, SELECT</td><td>默认的库，表的读权限以及刷新权限。</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/60fac86f0b271710d61e388ec8a4d60b.png"  style="margin:0;">
4. 返回添加数据库实例页面，单击**完成**，状态为“连接正常”的数据库，即可成功接入 DBbrain 自治服务。
![](https://main.qcloudimg.com/raw/c6773c68ca64a77dbcb4959cc85d4c68.png)
5. 返回 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/instance)，进入实例管理页面，在上方选择对应的自建数据库类型，即可查看及管理接入的自建数据库。
![](https://main.qcloudimg.com/raw/dce74d82953dae117cb3d2201317ca9e.png)

## [直连接入流程](id:zljrlc)
### 进入接入页面
1.登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/instance)，在左侧导航选择**实例概览**页，在上方自建实例接入卡片中单击**快速接入**，进入自建数据库实例接入页面。
![](https://main.qcloudimg.com/raw/b329ffde59299d6d3990eea430d7eae0.png)
2. 在自建数据库实例接入页面的“腾讯云CVM自建数据库”模块，单击**直连接入**，进入接入流程。
![](https://main.qcloudimg.com/raw/8120dc796452f21c50e41a2d8ba0ddcd.png)

### 接入 CVM 自建数据库
#### 步骤1：选择 CVM
在选择服务器实例页面，选择有自建数据库的 CVM，然后单击**下一步**，进行下一步添加数据库。
- **选择云服务器获取方式**：支持列表拉取和手动输入两种方式获取 CVM：
  - 选择**列表拉取**时，可以直接获取到该账号下 CVM 的实例列表。
  - 当选择**手动输入**时，用户可以通过输入实例 IP 的方式获取到 CVM。
- **选择接入DBbrain服务地域**：目前支持广州、北京、上海、成都四个地域，如果用户的数据库所在地域不在以上地域内，建议就近选择。
- **添加云服务器**：
 - 若获取方式选择**列表拉取**，则选择好地域后，可直接在列表获取选择一个或多个 CVM。
![](https://main.qcloudimg.com/raw/9aa0ff851abe1af2c8c1fb79e4c5f4d3.png)
 - 若获取方式选择**手动输入**，则用户可以在文本框输入一个或多个实例 IP 来添加 CVM。
![](https://qcloudimg.tencent-cloud.cn/raw/579927a43ae7232f0e43aadcec38dcf6.png)

#### 步骤2：添加数据库
在添加数据库实例页面，展示了上一步选择的 CVM 及其数据库状态。
1. 在添加数据库实例页面，选择数据库类型。
2. 选择一个 CVM，单击**操作**列的**添加**，或选择多个 CVM，单击列表左上方的**批量添加数据库**，向 CVM 中添加数据库。
>?已成功部署 agent 的 CVM，在未添加数据库的情况下，数据库的状态显示为“--”。
>
![](https://main.qcloudimg.com/raw/b7af21c76def711875ea1f728178eeaf.png)
3. 在弹出的对话框，填写数据库端口号、帐号、密码及数据库配置，单击**确定**，即可完成数据库的添加。
>?若数据库帐号授权异常，请参见 [数据库帐号授权异常](https://cloud.tencent.com/document/product/1130/54289)。
> 
数据库帐号配置说明：
<table>
<thead><tr><th >参数名称</th><th >参数说明</th></tr></thead>
<tbody><tr>
<td >端口号</td><td>DBbrain agent 侦测到的数据库端口号（若 CVM 中存在多个数据库，可单击<b>添加端口</b>，手动添加数据库端口号，以此来同时接入多个 CVM 自建数据库）。</td></tr>
<tr>
<td >账号</td><td>CVM 自建数据库的帐号（若该帐号尚未创建，需先单击<b>生成授权命令</b>，生成授权命令后，复制在数据库上执行所生成的授权命令）。</td></tr>
<tr>
<td >密码</td><td>CVM 自建数据库对应的密码。</td></tr>
<tr>
<td >数据库配置</td><td>包含 CPU、内存、磁盘，此配置为主机分配给该 CVM 自建数据库的配置，DBbrain 将根据用户所填写的数据库配置计算相关性能。</td></tr>
</tbody></table>
数据库帐号授权说明如下：
<table>
<thead><tr><th >权限</th><th >权限说明</th></tr></thead>
<tbody><tr>
<td >PROCESS</td><td>查看所有连接进程，用于实时会话展示进程。</td></tr>
<tr>
<td >REPLICATION SLAVE, REPLICATION CLIENT</td><td>查看主备库状态，查看备库 relaylog 和 binlog 事件，用于诊断主备复制异常。</td></tr>
<tr>
<td >SHOW DATABASES, SHOW VIEW, RELOAD, SELECT</td><td>默认的库，表的读权限以及刷新权限。</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/60fac86f0b271710d61e388ec8a4d60b.png"  style="margin:0;">
4. 返回添加数据库实例页面，单击**完成**，状态为**连接正常**的数据库，即可成功接入 DBbrain 自治服务。
![](https://main.qcloudimg.com/raw/c6773c68ca64a77dbcb4959cc85d4c68.png)
5. 返回 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/instance)，进入实例管理页面，在上方选择对应的自建数据库类型，即可查看及管理接入的自建数据库。
![](https://main.qcloudimg.com/raw/dce74d82953dae117cb3d2201317ca9e.png)
