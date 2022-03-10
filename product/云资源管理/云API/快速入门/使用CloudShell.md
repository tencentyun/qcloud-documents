CloudShell 是网页版命令行工具，帮助您通过命令行管理腾讯云资源。您可以通过浏览器启动 CloudShell，启动时将会自动为您分配一台 Linux 管理机供您免费使用，该实例上已经预装 TCCLI 及 Terraform 等多种云管理工具和 SSH 及 VIM 等系统工具。




## 功能特性
CloudShell 具备以下功能特性：
- **自动创建免费虚拟机**
CloudShell 启动时，会自动创建一台 Linux 虚拟机，供您独享使用。
当会话处于活跃状态时，CloudShell 实例长期有效。每个登录云账号所拥有的管理权限等同于其在访问管理 CAM 中被授予的操作权限。同时，CloudShell 会对所有的登录用户进行安全认证，并实现虚拟机按用户隔离，保障运行环境的安全。
- **持久性磁盘存储空间**
CloudShell 免费提供1GB的持久存储（ 数据将会在最近一次会话的120天后随机器销毁），作为您在 CloudShell 实例上的 `/home/cloudshell/data/` 目录。您存储在主目录中的所有文件在不同会话、实例之间保持不变。
- **语言及工具支持**
CloudShell 实例多种语言支持及预装工具如下：
<dx-accordion>
::: 语言支持
<table>
<thead>
  <tr>
	<th>语言</th>
	<th>版本</th>
  </tr>
</thead>
<tbody>
  <tr>
	<td>Java</td>
	<td>1.8.0</td>
  </tr>
  <tr>
	<td>Go</td>
	<td>1.13.8</td>
  </tr>
  <tr>
	<td>Python2</td>
	<td>2.7.17</td>
  </tr>
  <tr>
	<td>Python3</td>
	<td>3.6.9</td>
  </tr>
  <tr>
	<td>Node.js</td>
	<td>14.17.2</td>
  </tr>
  <tr>
	<td>PHP</td>
	<td>7.2.24</td>
  </tr>
  <tr>
	<td>Ruby</td>
	<td>2.5.1</td>
  </tr>
  <tr>
	<td>C++</td>
	<td>7.5.0</td>
  </tr>
  <tr>
	<td>C#</td>
	<td>5.0.205</td>
  </tr>
</tbody>
</table>
:::
::: 工具支持
<table>
<thead>
  <tr>
	<th>类型</th>
	<th>工具名</th>
	<th>版本号</th>
  </tr>
</thead>
<tbody>
  <tr>
	<td rowspan=7>Linux 实用工具</td>
	<td>telnet</td>
	<td>0.17</td>
  </tr>
  <tr>
	<td>tmux</td>
	<td>2.6</td>
  </tr>
  <tr>
	<td>wget</td>
	<td>1.19.4</td>
  </tr>
  <tr>
	<td>ssh</td>
	<td>7.6</td>
  </tr>
  <tr>
	<td>curl</td>
	<td>7.58.0</td>
  </tr>
  <tr>
	<td>bash</td>
	<td>4.4.20</td>
  </tr>
  <tr>
	<td>ping</td>
	<td>1.9.4</td>
  </tr>
  <tr>
	<td>腾讯云工具</td>
	<td>tccli</td>
	<td>3.0.469.1</td>
  </tr>
  <tr>
	<td rowspan=3>在线编辑器</td>
	<td>vim</td>
	<td>8.0</td>
  </tr>
  <tr>
	<td>nano</td>
	<td>2.9.3</td>
  </tr>
  <tr>
	<td>emacs</td>
	<td>26.3</td>
  </tr>
  <tr>
	<td>源代码管理</td>
	<td>git</td>
	<td>2.17.1</td>
  </tr>
  <tr>
	<td rowspan=8>构建和打包工具</td>
	<td>pip</td>
	<td>9.0.1</td>
  </tr>
  <tr>
	<td>nvm</td>
	<td>0.38.0</td>
  </tr>
  <tr>
	<td>gcc</td>
	<td>7.5.0</td>
  </tr>
  <tr>
	<td>dotnet</td>
	<td>5.0.205</td>
  </tr>
  <tr>
	<td>make</td>
	<td>4.1</td>
  </tr>
  <tr>
	<td>maven</td>
	<td>3.6.0</td>
  </tr>
  <tr>
	<td>cmake</td>
	<td>3.10.2</td>
  </tr>
  <tr>
	<td>npm</td>
	<td>6.14.13</td>
  </tr>
  <tr>
	<td rowspan=2>编排工具</td>
	<td>terraform</td>
	<td>1.0.3</td>
  </tr>
  <tr>
	<td>ansible</td>
	<td>2.11.2</td>
  </tr>
  <tr>
	<td rowspan=2>容器工具</td>
	<td>docker</td>
	<td>20.10.7</td>
  </tr>
  <tr>
	<td>kubectl</td>
	<td>1.21.3</td>
  </tr>
  <tr>
	<td>数据库工具</td>
	<td>mysql client</td>
	<td>14.14</td>
  </tr>
</tbody>
</table>


:::
</dx-accordion>


## 使用限制
在使用 CloudShell 前，请了解以下使用限制：
<table>
<thead>
  <tr>
	<th width="15%">限制项</th>
	<th>描述</th>
  </tr>
</thead>
<tbody>
  <tr>
	<td>虚拟机数量</td>
	<td>
	无论打开多少会话窗口，CloudShell 在同一时刻只会创建一台虚拟机，且所有会话窗口都会自动连接到此虚拟机上。</td>
  </tr>
  <tr>
	<td>会话窗口</td>
	<td>最多可以打开5个会话窗口。</td>
  </tr>
  <tr>
	<td>文件存储</td>
	<td>CloudShell 为您免费提供1
	GB的永久存储空间，您可以将您的文件存放在 <code>/home/cloudshell/data/</code> 目录，该数据将保留120天（在上一次会后结束后）。</td>
  </tr>
  <tr>
	<td>禁止使用</td>
	<td>
	长时间使用以及计算或网络密集型等恶意进程将不受支持，并可能会导致会话在没有任何警告的情况下被终止甚至禁用。</td>
  </tr>
	<tr>
	<td>机器销毁</td>
	<td>
当您30分钟无任何命令行会话操作即视为停止，停止30分钟后机器销毁。当您再次使用 CloudShell 时，会重新分配 Linux 机器。</td>
  </tr>
	<tr>
	<td>访问限制</td>
	<td>
CloudShell 为用户的调试工具，仅支持通过公网域名访问，不支持通过内网访问除云 API 以外的其他业务。</td>
  </tr>
</tbody>
</table>




## 使用方法

### 启动 CloudShell[](id:startCloudShell)
您可通过以下两种方式启动 CloudShell：
<dx-tabs>
::: 通过控制台运行[](id:startMethodOne)
登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance)，选择页面上方的**工具** > **CloudShell**，即可启动 CloudShell。如下图所示：
![](https://main.qcloudimg.com/raw/14b50cd7f1c261571fce41764c5c6025.png)
::: 
::: 独立运行[](id:startMethodTwo)
您可通过以下方式，独立运行 CloudShell：
 - 在浏览器中输入 `https://console.cloud.tencent.com/cloudshell`。
 - 进入 [API Explorer](https://console.cloud.tencent.com/api/explorer)，选择对应接口后单击**调试SDK示例代码**即可。如下图所示：
![](https://main.qcloudimg.com/raw/63f490b59e016ce0821a575d43f6398f.png)
 - 打开 API Inspector，单击 <img src="https://main.qcloudimg.com/raw/c355dd68f4d46b218bb1ca9dd8b268a3.png" style="margin:-3px 0px"> 即可。如下图所示：
![](https://main.qcloudimg.com/raw/3c782858de149931eea1304161bbc427.png)

:::
</dx-tabs>


<dx-alert infotype="explain" title="">
- 第一次连接 CloudShell 时会为您创建虚拟机，会消耗一些时间。打开多个 CloudShell 窗口时，所有窗口都会连接到同一台虚拟机。虚拟机数量不会因为您打开新的命令行窗口而增加。
- 您可以根据实际需要打开多个 CloudShell 窗口，但最多可同时打开5个。
</dx-alert>




### 使用 TCCLI 命令管理云资源
您参考以下示例，在 CloudShell 中腾讯云 TCCLI 命令管理云资源。TCCLI 更多使用方法介绍请参见 [使用 TCCCLI](https://cloud.tencent.com/document/product/440/34013)。

- 执行以下命令，查看云产品帮助信息。
```
tccli <ProductCode> help
```
以查看云服务器 CVM 支持的 API 接口为例，则执行以下命令。
```
tccli cvm help
```
- 执行以下命令，查看执行 API 帮助信息。
```
tccli <ProductCode> <ApiName> help
```
执行以下命令，查看云服务器 CVM 的 DescribeInstances 接口支持的参数。具体的参数说明和 API 的相关信息可以在腾讯云官网查看对应的 API 文档。
```
tccli cvm DescribeInstances help
```



## 相关操作
### 上传及下载文件
CloudShell 提供了文件的上传和下载功能。您可通过通过 CloudShell 界面传输文件，步骤如下：

1. 参考 [通过控制台](#startMethodOne) 启动 CloudShell，打开 CloudShell 界面。
2. 选择 CloudShell 界面上方的 <img src="https://main.qcloudimg.com/raw/ec8d0b471216407ba9afde40f54cfb73.png" style="margin:-3px 0px">。如下图所示：
![](https://main.qcloudimg.com/raw/507f98a47f077698a2f3f599eca0212d.png)
3. 在弹出的菜单中单击**上传**或**下载**，按需传输文件。
 - 上传文件：在弹出的窗口中选择文件后，单击**打开**。
 - 下载文件：在弹出的窗口中，输入需下载文件的绝对路径后，单击**确定**。
<dx-alert infotype="notice" title="">
上传文件功能会默认将您的文件上传到 CloudShell 实例的 `/home/cloudshell/data/` 目录下。并且您只能下载 CloudShell 实例中 `/home/cloudshell/data/` 目录下的文件。
</dx-alert>





 
