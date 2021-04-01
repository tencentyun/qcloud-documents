本文介绍如何将腾讯云服务器 CVM 自建数据库接入数据库智能管家 DBbrain。

接入方式支持：直连接入和将 DBbrain agent 部署在用户主机上接入，通过接入自建数据库，使得多种类型的自建数据库也能拥有 DBbrain 提供的监控告警、诊断优化、数据库管理等自治服务能力。

两种接入方式的说明及功能请参见 [接入方式说明](https://cloud.tencent.com/document/product/1130/54283#jrfssm) 及 [功能对比](https://cloud.tencent.com/document/product/1130/54283#jrfsdgndb)。

>?DBbrain 当前支持的腾讯云 CVM 自建数据库实例类型：MySQL。

## agent 接入流程
### 进入接入页面
1. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/instance)，在左侧导航选择【实例概览】页，在上方自建实例接入卡片中单击【快速接入】，进入自建数据库实例接入页面。
![](https://main.qcloudimg.com/raw/b329ffde59299d6d3990eea430d7eae0.png)
2. 在自建数据库实例接入页面的“腾讯云CVM自建数据库”模块，单击【agent接入】，进入接入流程。
![](https://main.qcloudimg.com/raw/62573457ac7802000d4d2a5546d73d79.png)

### 接入 CVM 自建数据库
#### 步骤1：选择服务器实例
在选择服务器实例页面，选择 CVM，来向所选的 CVM 中添加接入 DBbrain 自治服务的自建数据库，然后单击【下一步】，进行 agent 部署。
- **选择云服务器获取方式**：支持列表拉取和手动输入两种方式获取 CVM：
  - 选择【列表拉取】时，可以直接获取到该账号下 CVM 的实例列表。
  - 当选择【手动输入】时，用户可以通过输入实例 IP 的方式获取到 CVM。
- **选择接入DBbrain服务地域**：当前 DBbrain 服务在广州、北京、上海、成都这四个地域进行了部署，如果用户的数据库所在地域不在以上部署地域内，建议就近选择。
- **添加云服务器**：
 - 若获取方式选择【列表拉取】：则选择好 CVM 地域后，可直接在列表选择一个或多个 CVM。
![](https://main.qcloudimg.com/raw/9aa0ff851abe1af2c8c1fb79e4c5f4d3.png)
 - 若获取方式选择【手动输入】：用户可以在文本框输入一个或多个实例 IP 来添加 CVM。
![](https://main.qcloudimg.com/raw/4d4143756cb4f0a742c7a802bbfe15d6.png)

#### 步骤2：部署 agent 
在 agent 部署页面，展示了已添加的 CVM 和 agent 的状态，列表中展现了 CVM 的实例ID/名称、IP 地址、agent 端口号、agent 状态。
1. 在 agent 部署页面，选择一个 CVM，单击“操作”列的【部署】，或选择多个 CVM，单击列表左上方的【批量部署】，将 agent 部署在 CVM。
>?CVM 中未部署 agent 的情况下，agent 状态显示为“--”。
>
![](https://main.qcloudimg.com/raw/109788aa05f7a8e08938c593ca08978b.png)
2. 在弹出的对话框，选择 Agent端口后，单击生成部署命令后的【部署】，即可根据用户所选的 agent 端口号，生成 agent 部署命令。
![](https://main.qcloudimg.com/raw/db9b57afc4eb96eeb3f533abe6d1e1dc.png)
3. 复制生成的 agent 部署命令，并在 CVM 上运行，出现 `Start agent successfully` 后，则表示 agent 部署成功，返回至腾讯云控制台，可查看 agent 状态变为“连接正常”。
![](https://main.qcloudimg.com/raw/96acbd799593579c5da43a2054078d24.png)
4. 待至少存在一个状态为连接正常的 agent，单击【下一步】，即可向成功部署 agent 的 CVM 中添加接入 DBbrain 自治服务的数据库。
<table>
<thead><tr><th width=10%>agent 状态</th><th width=35%>状态说明</th><th width=10%>操作</th><th width=45%>操作说明</th></tr></thead>
<tbody><tr>
<td rowspan=1>--</td>
<td>CVM 中未部署 agent</td>
<td>部署</td>
<td>单击【部署】，可将 agent 部署在 CVM 中</td></tr>
<tr>
<td rowspan=2>部署中</td>
<td rowspan=2>CVM 中正在部署 agent</td>
<td>查看</td>
<td>单击【查看】，可查看正在部署的 agent 端口号及 agent 命令</td></tr>
<tr>
<td>重置</td>
<td>单击【重置】，可将 agent 状态恢复为“--”，以满足用户想换 agent 端口号的场景，重新部署 agent</td></tr>
<tr>
<td rowspan=3>连接正常</td>
<td rowspan=3>CVM 中已成功部署 agent 且 agent 处于正常监控采集中，该 CVM 中的自建数据库可正常使用 DBbrain 提供的自治服务</td>
<td>查看</td>
<td>单击【查看】，可查看已部署 agent 的端口号及 agent 命令</td></tr>
<tr>
<td>停止</td>
<td>单击【停止】，可将处于正常连接状态的 agent 暂停连接</td></tr>
<td>重置</td>
<td>单击【重置】，可将 agent 状态恢复为“--”，以满足用户想换 agent 端口号的场景，重新部署 agent</td></tr>
<tr>
<td rowspan=2>连接失败</td>
<td rowspan=2>CVM 中部署 agent 失败，具体请参见 [agent接入问题及排查指引]()</td>
<td>查看</td>
<td>单击【查看】，可查看该 agent 的端口号及 agent 命令</td></tr>
<tr>
<td>重置</td>
<td>单击【重置】，可将 agent 状态恢复为“--”，以此可以更换 agent 端口号，重新部署 agent</td></tr>
<tr>
<td rowspan=3>暂停连接</td>
<td rowspan=3>CVM 中已成功部署 agent 但 agent 处于暂停监控采集中</td>
<td>查看</td>
<td>单击【查看】，可查看该 agent 的端口号及 agent 命令</td></tr>
<tr>
<td>重连</td>
<td>单击【重连】，可将处于暂停连接状态的 agent 进行启动，恢复为连接正常</td></tr>
<tr>
<td>重置</td>
<td>单击【重置】，可将 agent 状态恢复为“--”，以满足用户想换 agent 端口号的场景，重新部署 agent</td></tr>
</tbody></table>

#### 步骤三：添加数据库实例
在添加数据库实例页面，展现了步骤二中已成功部署 agent 的 CVM及数据库的状态，列表展现了 CVM 的实例ID/名称、IP 地址、数据库端口号、数据库配置、数据库状态。
1. 选择数据库引擎的类型。
2. 已成功部署 agent 的CVM，在未添加数据库的情况下，数据库的状态显示为“--”，用户可以选择一个 CVM，单击“操作”列的【添加】，或选择多个 CVM，单击列表左上方的【批量添加数据库】，向成功部署 agent 的 CVM 中添加接入 DBbrain 自治服务的数据库实例。
![](https://main.qcloudimg.com/raw/c6773c68ca64a77dbcb4959cc85d4c68.png)
3. 在弹出的对话框，填写数据库端口号、帐号、密码及数据库配置，单击【确定】，即可完成数据库的添加。
>?若数据库账号授权异常，请参见 [数据库账号授权异常排查指引](xx)
> 
数据库帐号配置说明如下：
<table>
<thead><tr><th >参数名称</th><th >参数说明</th></tr></thead>
<tbody><tr>
<td rowspan=1>端口号</td>
<td>DBbrain Agent侦测到的数据库端口号。（注：若云服务器CVM中存在多个数据库，可单击【添加端口】，手动添加数据库端口号，以此来同时接入多个CVM自建数据库实例）</td></tr>
<tr>
<td rowspan=1>账号</td>
<td>CVM自建数据库的账号。（注：若该账号尚未创建，需先点击“生成授权命令”文字链，生成授权命令后，复制后在数据库上执行所生成的授权命令）</td></tr>
<tr>
<td >密码</td>
<td>CVM自建数据库对应的密码</td></tr>
<tr>
<td >数据库配置</td>
<td>数据库配置包含CPU、内存、磁盘，此配置为主机分配给该CVM自建数据库的配置，DBbrain将根据用户所填写的数据库配置计算相关性能</td></tr>
</tbody></table>
数据库帐号授权说明如下：
<table>
<thead><tr><th >权限</th><th >权限说明</th></tr></thead>
<tbody><tr>
<td rowspan=1>PROCESS</td><td>查看所有连接进程，用于实时会话展示进程</td></tr>
<tr>
<td rowspan=1>REPLICATION SLAVE, REPLICATION CLIENT</td>
<td>查看主备库状态，查看备库relaylog和binlog事件，用于诊断主备复制异常</td></tr>
<tr>
<td rowspan=1>SHOW DATABASES, SHOW VIEW, RELOAD, SELECT</td>
<td>默认的库，表的读权限以及刷新权限。</td></tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/68437d3f10b0df66f15ca1840a572568.png"  style="margin:0;">
4. 在【添加数据库实例】页面中，单击【完成】按钮，数据库状态为【连接正常】的数据库实例，即可成功接入DBbrain自治服务。
![](https://main.qcloudimg.com/raw/c6773c68ca64a77dbcb4959cc85d4c68.png)
5. 登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/instance)，在左侧导航选择【实例管理】页，进入到实例管理页面，在上方选择对应的自建数据库类型，即可查看及管理接入的自建数据库。
![](https://main.qcloudimg.com/raw/dce74d82953dae117cb3d2201317ca9e.png)

## 直连接入流程
### 进入接入页面
1.登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/instance)，在左侧导航选择【实例概览】页，在上方自建实例接入卡片中单击【快速接入】，进入自建数据库实例接入页面。
![](https://main.qcloudimg.com/raw/b329ffde59299d6d3990eea430d7eae0.png)
2.在自建数据库实例接入页面的【腾讯云CVM自建数据库】模块，单击【直连接入】按钮，进入接入流程。
![](https://main.qcloudimg.com/raw/8120dc796452f21c50e41a2d8ba0ddcd.png)

### 接入 CVM 自建数据库
#### 步骤一：选择服务器实例
在选择服务器实例页面中，选择云服务器，以此来向所选择的云服务器中添加接入DBbrain自治服务的自建数据库实例。
1. 选择云服务器获取方式
用户可以通过【列表拉取】和【手动输入】两种方式获取云服务器。当选择【列表拉取】方式时，可以直接获取到该账号下云服务器CVM的实例列表；当选择【手动输入】方式时，用户可以通过输入实例IP的方式获取到云服务器CVM。
2. 选择接入DBbrain服务地域
当前DBbrain服务在广州、北京、上海、成都这四个地域进行了部署，如果用户的数据库所在地域不在以上DBbrain服务部署地域内，建议就近选择。
3. 添加云服务器
若上面选择【列表拉取】方式获取云服务器CVM实例，则选择好云服务器CVM所在地域后，可直接在列表中勾选一个或多个云服务器CVM，单击【下一步】，进行agent部署。
![](https://main.qcloudimg.com/raw/9aa464c20a0f963d8b97bf9a46bf1b56.png)
若上面选择【手动输入】方式获取云服务器CVM实例，用户可以在文本框中输入一个或多个实例IP，以此来添加云服务器CVM，单击【下一步】，进行agent部署。
![](https://main.qcloudimg.com/raw/8fbd53ae2967bdc42838094a94eec79d.png)

#### 步骤二：添加数据库实例
在添加数据库实例页中，展现了步骤一中已勾选的云服务器CVM及数据库的状态，列表中展现了云服务器CVM的实例ID/名称、IP地址、数据库端口号、数据库配置、数据库状态、数据库的操作。
添加数据库实例的步骤具体如下：
1. 选择数据库引擎的类型
2. 在列表中，云服务器CVM在未添加数据库的情况下，数据库的状态显示为【--】，用户可以勾选一个云服务器CVM，单击操作列中的【添加】，或勾选多个云服务器CVM，单击列表左上方的【批量添加数据库】按钮，向云服务器CVM中添加接入DBbrain自治服务的数据库实例。
![](https://main.qcloudimg.com/raw/b7af21c76def711875ea1f728178eeaf.png)
3. 在添加数据库的弹窗中，填写数据库端口号、账号、密码及数据库配置，单击【确定】按钮，即可完成数据库的添加。
> 若数据库账号授权异常，则参见[数据库账号授权异常排查指引](xx)
> 
![](https://main.qcloudimg.com/raw/68437d3f10b0df66f15ca1840a572568.png)
数据库帐号及配置说明如下：
<table>
<thead><tr><th >参数名称</th><th >参数说明</th></tr></thead>
<tbody><tr>
<td rowspan=1>端口号</td>
<td>CVM自建数据库的端口号。（注：若云服务器CVM中存在多个数据库，可单击【添加端口】，添加多个数据库端口号，以此来同时接入多个CVM自建数据库实例）</td></tr>
<tr>
<td rowspan=1>账号</td>
<td>CVM自建数据库的账号。（注：若该账号尚未创建，需先点击“生成授权命令”文字链，生成授权命令后，复制后在数据库上执行所生成的授权命令）</td></tr>
<tr>
<td rowspan=1>密码</td>
<td>CVM自建数据库对应的密码</td></tr>
<tr>
<td rowspan=1>数据库配置</td>
<td>数据库配置包含CPU、内存、磁盘，此配置为主机分配给该CVM自建数据库的配置，DBbrain将根据用户所填写的数据库配置计算相关性能</td></tr>
</tbody></table>
数据库帐号授权说明如下：
<table>
<thead><tr><th >权限</th><th >权限说明</th></tr></thead>
<tbody><tr>
<td >PROCESS</td><td>查看所有连接进程，用于实时会话展示进程</td></tr>
<tr>
<td >REPLICATION SLAVE, REPLICATION CLIENT</td>
<td>查看主备库状态，查看备库relaylog和binlog事件，用于诊断主备复制异常</td></tr>
<tr>
<td >SHOW DATABASES, SHOW VIEW, RELOAD, SELECT</td>
<td>默认的库，表的读权限以及刷新权限。</td></tr>
</tbody></table>
4.在【添加数据库实例】页面中，单击【完成】按钮，数据库状态为【连接正常】的数据库实例，即可成功接入DBbrain自治服务。
![](https://main.qcloudimg.com/raw/b7af21c76def711875ea1f728178eeaf.png)
5.登录 [DBbrain 控制台](https://console.cloud.tencent.com/dbbrain/instance)，在左侧导航选择【实例管理】页，进入到实例管理页面，在上方选择对应的自建数据库类型，即可查看及管理接入的自建数据库。
![](https://main.qcloudimg.com/raw/dce74d82953dae117cb3d2201317ca9e.png)



