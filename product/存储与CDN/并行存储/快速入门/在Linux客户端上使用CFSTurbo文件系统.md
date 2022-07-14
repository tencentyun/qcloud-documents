## 操作场景
在计算节点上使用挂载命令将文件系统挂载到本地目录后，即可像使用本地文件系统一样使用 Turbo 文件系统。本文以标准登录方式（WebShell）登录实例为例，为您详细介绍如何在 Linux 客户端上使用 Turbo 文件系统。
更多登录 Linux 实例的方式请参见 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/16515)。


## 前提条件
为能够正常使用产品，请在使用前完成如下条件，并确保配置和安装成功，否则将影响您的正常使用。
- [创建文件系统及挂载点](https://cloud.tencent.com/document/product/1546/68774)。
- 在云联网内的某个私有网络 VPC 下 [创建实例](https://cloud.tencent.com/document/product/213/4855)。
- 待访问存储的计算节点**双向放通**云联网内 Turbo 所在 VPC 全部 IP 地址的988端口。


## 操作步骤

### 安装自动化工具
<dx-tabs>
::: 自动安装
1. 参考 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，登录云服务器实例。
2. 执行如下命令，下载自动化工具。
```
wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/tools/cfs_turbo_client_setup
```
3. 执行如下命令，设置自动化工具的权限。
```
chmod a+x cfs_turbo_client_setup
```
4. 执行如下命令，执行自动化工具。
```
sudo ./cfs_turbo_client_setup
```
   - 若返回如下信息，即表示安装成功。
![](https://main.qcloudimg.com/raw/71cc3fdd2e94887cf4976bb80692792c.png)
   - 若返回如下信息，即表示暂不支持该内核版本，请参考已支持的 [内核版本清单](#CVMKernelVersion) 进行调整。
![](https://main.qcloudimg.com/raw/cf1eb0ca5d9f5097099f472ae3ff7929.png)
<dx-alert infotype="explain" title="">
Ubuntu 16.04 版本因镜像原因，暂不支持自动下载。若需使用，请 [手动安装](#ManualInstallation)。
</dx-alert>

:::
::: 手动安装[](id:ManualInstallation)
1. 参考 [使用标准登录方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/5436)，登录云服务器实例。
2. 执行如下命令，查看实例的内核版本。
```
uname -a
```
3. 根据实例内核版本，依次执行相应命令，下载对应实例内核版本的两个安装包。
请确认如下列表中包含该实例内核版本。如果如下列表没有实例内核版本，请先进行升级再安装。
<span id="CVMKernelVersion"></span>
<table>
  <tr>
	<th>操作系统版本</th>
	<th>内核版本</th>
	<th>执行命令</th>
  </tr>
  <tr>
	<td rowspan="10">Ubuntu</td>
	<td>4.15.0-142 18.04.4 LTS (Bionic Beaver)</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-142/cfsturbo-client-modules.x86_64.deb</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-142/cfsturbo-client-utils.x86_64.deb</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>4.15.0-142 16.04.7 LTS (Xenial Xerus)</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.15.0-142/cfsturbo-client-modules.x86_64.deb</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.15.0-142/cfsturbo-client-utils.x86_64.deb</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>4.15.0-118</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-118/cfsturbo-client-modules.x86_64.deb</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-118/cfsturbo-client-utils.x86_64.deb</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>4.15.0-76</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-76/cfsturbo-client-modules.x86_64.deb</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-76/cfsturbo-client-utils.x86_64.deb</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>4.15.0-62</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-62/cfsturbo-client-modules.x86_64.deb</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-62/cfsturbo-client-utils.x86_64.deb</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>4.15.0-45</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-45/cfsturbo-client-modules.x86_64.deb</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-45/cfsturbo-client-utils.x86_64.deb</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>4.15.0-30</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-30/cfsturbo-client-modules.x86_64.deb</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/4.15.0-30/cfsturbo-client-utils.x86_64.deb</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>5.4.0-42</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/5.4.0-42/cfsturbo-client-modules.x86_64.deb</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/5.4.0-42/cfsturbo-client-utils.x86_64.deb</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>5.4.0-48</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/5.4.0-48/cfsturbo-client-modules.x86_64.deb</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/5.4.0-48/cfsturbo-client-utils.x86_64.deb</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>5.4.0-62</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/5.4.0-62/cfsturbo-client-modules.x86_64.deb</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu/5.4.0-62/cfsturbo-client-utils.x86_64.deb</code>
</pre>
	</td>
  </tr>
  <tr>
	<td rowspan="6">Centos</td>
	<td>3.10.0-1160</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-1160/kmod-cfsturbo-client.x86_64.rpm</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-1160/cfsturbo-client.x86_64.rpm</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>3.10.0-1127</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-1127/kmod-cfsturbo-client.x86_64.rpm</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-1127/cfsturbo-client.x86_64.rpm</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>3.10.0-1062</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-1062/kmod-cfsturbo-client.x86_64.rpm</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-1062/cfsturbo-client.x86_64.rpm</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>3.10.0-957</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-957/kmod-cfsturbo-client.x86_64.rpm</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-957/cfsturbo-client.x86_64.rpm</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>3.10.0-862</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-862/kmod-cfsturbo-client.x86_64.rpm</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-862/cfsturbo-client.x86_64.rpm</code>
</pre>
	</td>
  </tr>
  <tr>
	<td>3.10.0-693</td>
	<td>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-693/kmod-cfsturbo-client.x86_64.rpm</code>
</pre>
	  <pre>
<code>wget
https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos/3.10.0-693/cfsturbo-client.x86_64.rpm</code>
</pre>
	</td>
  </tr>
</table>
4. 根据实例的操作系统类型，执行相应命令，安装客户端。
   - Ubuntu 操作系统：
```
sudo dpkg -i
```
   - CentOS 操作系统：
```
yum install
```
:::
</dx-tabs>


### 挂载文件系统至实例
1. 登录文件存储控制台，进入 [文件系统](https://console.cloud.tencent.com/cfs/fs?rid=1) 管理页面。
2. 单击需要操作的 Turbo 文件系统 ID/名称，选择**挂载点信息**页签。
3. 在挂载点信息页签的“挂载命令”中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png"/>，复制所需命令。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/e66b83862958d4d7a915f7badd4fab52.png)
4. 切换至登录的实例，执行复制的挂载命令。
关于挂载指令的说明如下，请根据实际的业务情况使用合适的挂载指令：
   - 如果您希望支持扩展属性且所有操作默认为同步执行（机器重启不会丢数据，但性能会有损耗），请复制和执行第如下命令。
 例如：
```shell
sudo mount.lustre -o sync,user_xattrXXXXXXXXXXXXXXXXXXX
```
   - 如果您希望支持扩展属性且无需强制同步执行（机器重启有可能会丢少量尚缓存在内存中的数据，但性能好），请复制和执行如下命令。例如：
```shell
sudo mount.lustre -o user_xattrXXXXXXXXXXXXXXXXXXX
```
   - 如果您无需支持扩展属性且无需强制同步执行（机器重启有可能会丢少量尚缓存在内存中的数据，但性能好），请复制和执行如下命令。例如：
```shell
sudo mount.lustre XXXXXXXXXXXXXXXXXXX
```



