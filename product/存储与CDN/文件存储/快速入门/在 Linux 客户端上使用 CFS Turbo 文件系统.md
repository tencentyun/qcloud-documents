## 简介
本文为您详细介绍如何在 Linux 客户端上使用 CFS Turbo 文件系统。

## 步骤1：创建文件系统及挂载点
详细步骤请参见 [创建文件系统及挂载点](https://cloud.tencent.com/document/product/582/9132) 文档。

## 步骤2：登录云联网内的实例
>? 本文以标准登录方式（WebShell）登录实例为例，更多登录方式请参见 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/16515)。
>
1. 在云联网内的某个 VPC 下创建一个实例，详情请参见云服务器的 [通过购买页创建实例](https://cloud.tencent.com/document/product/213/4855) 文档。
2. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)，在实例列表中找到刚购买的云服务器，在右侧操作栏中单击【登录】。
3. 在“登录Linux实例”窗口中选择【立即登录】后，输入云服务器的用户名和密码，并单击【确定】即可正常登录。

## 步骤3：下载私有客户端
1. 执行如下命令，查看实例的内核版本。
```
uname -a
```
2. 根据实例内核版本，依次执行相应命令，下载对应实例内核版本的两个安装包。
>! 请确认如下列表中包含该实例内核版本。如果如下列表没有实例内核版本，请先进行升级再安装。
>
<table>
	<tr><th>操作系统版本</th><th>内核版本</th><th>执行命令</th></tr>
	<tr><td rowspan="9">Ubuntu16.04</td><td>4.10.0-42-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-143-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-143-generic/cfsturbo-utils.deb<code></pre></td></tr>
	<tr><td>4.11.0-14-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.11.0-14-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.11.0-14-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>4.13.0-45-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.13.0-45-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.13.0-45-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>4.15.0-99-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.15.0-99-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.15.0-99-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>4.4.0-112-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-112-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-112-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>4.4.0-116-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-116-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-116-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>4.4.0-133-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-133-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-133-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>4.4.0-143-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-143-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-143-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>4.4.0-157-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-157-generic/cfsturbo-kernel-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu16.04/4.4.0-157-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td rowspan="5">Ubuntu18.04</td><td>4.15.0-30-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu18.04/4.15.0-30-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu18.04/4.15.0-30-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>4.15.0-45-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu18.04/4.15.0-45-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu18.04/4.15.0-45-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>4.15.0-62-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu18.04/4.15.0-62-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu18.04/4.15.0-62-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>4.15.0-76-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu18.04/4.15.0-76-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu18.04/4.15.0-76-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>4.15.0-118-generic</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu18.04/4.15.0-118-generic/cfsturbo-client-modules.deb</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/ubuntu18.04/4.15.0-118-generic/cfsturbo-utils.deb</code></pre></td></tr>
	<tr><td>CentOS 7.9</td><td>3.10.0-1160</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.9/3.10.0-1160/kmod-lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.9/3.10.0-1160/lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre></td></tr>
	<tr><td>CentOS 7.8</td><td>3.10.0-1127</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.8/3.10.0-1127/kmod-lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.8/3.10.0-1127/lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre></td></tr>
	<tr><td>CentOS 7.7</td><td>3.10.0-1062</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.7/3.10.0-1062/kmod-lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.7/3.10.0-1062/lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre></td></tr>
	<tr><td>CentOS 7.6</td><td>3.10.0-957</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.6/3.10.0-957/kmod-lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.6/3.10.0-957/lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre></td></tr>
	<tr><td>CentOS 7.5</td><td>3.10.0-862</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.5/3.10.0-862/kmod-lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.5/3.10.0-862/lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre></td></tr>
	<tr><td>CentOS 7.4</td><td>3.10.0-693</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.4/3.10.0-693/kmod-lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre>
	<pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.4/3.10.0-693/lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre></td></tr>
	<tr><td>CentOS 7.3</td><td>3.10.0-514</td>
	<td><pre><code>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.3/3.10.0-514/kmod-lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre>
	<pre>wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/2.12.4/centos7.3/3.10.0-514/lustre-client-2.12.4-1.el7.x86_64.rpm</code></pre></td></tr>
</table>

## 步骤4：安装客户端

根据实例的操作系统类型，执行相应命令，安装客户端。
- Ubuntu 操作系统：
```
sudo dpkg -i
```
- CentOS 操作系统：
```
yum install
```

## 步骤5：挂载 Turbo 文件系统

1. 登录文件存储控制台，在左侧导航栏中，选择【[文件系统](https://console.cloud.tencent.com/cfs/fs?rid=1)】，进入文件系统管理页面。
2. 单击需要操作的 Turbo 文件系统 ID/名称，选择【挂载点信息】页签。
3. 在挂载点信息页签的“挂载命令”中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" />，复制所需命令。
![](https://main.qcloudimg.com/raw/4133842c838460323fea754124bd8548.png)
4. 切换至登录的实例，执行刚复制的挂载命令。
通常情况下，建议使用第一条指令进行挂载。关于挂载指令的说明如下：
 - 如果您希望支持扩展属性且所有操作默认为同步执行（机器重启不会丢数据，但 IO 性能会稍有损耗），请复制和执行第一条命令。
 例如：
```
sudo mount.lustre -o sync,user_xattrXXXXXXXXXXXXXXXXXXX
```
 - 如果您希望支持扩展属性且无需强制同步执行（机器重启有可能会丢少量尚缓存在内存中的数据，但 IO 性能好），请复制和执行第二条命令。
 例如：
```
sudo mount.lustre -o user_xattrXXXXXXXXXXXXXXXXXXX
```
 - 如果您无需支持扩展属性且无需强制同步执行，请复制和执行第三条命令。
 例如：
```
sudo mount.lustre XXXXXXXXXXXXXXXXXXX
```



