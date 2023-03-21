## 操作场景
本文以标准登录方式（WebShell）登录实例为例，为您详细介绍如何在 Linux 客户端上使用 CFS Turbo 文件系统。
更多登录 Linux 实例的方式请参见 [登录 Linux 实例](https://cloud.tencent.com/document/product/213/16515)。

## 前提条件

- 已 [创建文件系统及挂载点](https://cloud.tencent.com/document/product/582/9132)。
- 已在云联网内的某个 VPC 下 [创建实例](https://cloud.tencent.com/document/product/213/4855)。
- 需要和存储通信的计算实例，且已双向放通云联网内 Turbo 所在 VPC 全部 IP 地址的988端口。

## 操作步骤

### 自动安装

1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm)。
2. 在实例列表中找到刚购买的云服务器，在右侧操作栏中单击**登录**。
3. 在弹出的**登录 Linux 实例**窗口，选择**标准登录方式**，单击**立即登录**。
4. 在打开的 WebShell 登录页面，输入用户名和密码，单击**确定**。
5. 执行如下命令，下载自动化工具。
```
wget https://cfsturbo-client-1251013638.cos.ap-guangzhou.myqcloud.com/tools/cfs_turbo_client_setup
```
6. 执行如下命令，设置自动化工具的权限。
```
chmod a+x cfs_turbo_client_setup
```
7. 执行如下命令，执行自动化工具。
```
sudo ./cfs_turbo_client_setup
```
 - 若返回如下信息，即表示安装成功。
![](https://main.qcloudimg.com/raw/71cc3fdd2e94887cf4976bb80692792c.png)
 - 若返回如下信息，即表示暂不支持该内核版本，可 [提交工单与我们联系](https://cloud.tencent.com/online-service?source=PRESALE&from=console_bar_cvm|instance|index)
![](https://main.qcloudimg.com/raw/cf1eb0ca5d9f5097099f472ae3ff7929.png)


<span id="ManualInstallation"></span>

### 兼容性列表

<span id="CVMKernelVersion"></span>
<table>
<table>
    <tr>
        <th>操作系统类型</td>
        <th>操作系统版本</td>
    </tr>
    <tr>
        <td rowspan=8>CentOS</td>
        <td>7.9</td>
    </tr>
    <tr>
        <td>7.8</td>
    </tr>
    <tr>
        <td>7.7</td>
    </tr>
    <tr>
        <td>7.6</td>
    </tr>
    <tr>
        <td>7.5</td>
    </tr>
    <tr>
        <td>7.4</td>
    </tr>
    <tr>
        <td>7.3</td>
    </tr>
    <tr>
        <td>7.2</td>
    </tr>
    <tr>
        <td rowspan=3>Ubuntu</td>
        <td>20.04</td>
    </tr>
    <tr>
        <td>18.04</td>
    </tr>
    <tr>
        <td>16.04</td>
    </tr>
    <tr>
        <td rowspan=9>TencentOS</td>
        <td>3.1(TK4)</td>
    </tr>
    <tr>
        <td>2.4(TK4）</td>
    </tr>
    <tr>
        <td>2.2(TK3）</td>
    </tr>

</table>
 
>!客户端版本不仅与操作系统版本相关，更重要的是内核的对应关系。目前 Turbo 支持兼容性列表内云上默认公共镜像的内核，若有特殊内核的需求，可 [提交工单与我们联系](https://cloud.tencent.com/online-service?source=PRESALE)。

8. 登录文件存储控制台，进入 [文件系统](https://console.cloud.tencent.com/cfs/fs?rid=1) 管理页面。
9. 单击需要操作的 Turbo 文件系统 ID/名称，选择**挂载点信息**页签。
10. 在挂载点信息页签的“挂载命令”中，单击 <img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png" />，复制所需命令。
![](https://main.qcloudimg.com/raw/4133842c838460323fea754124bd8548.png)
11. 切换至登录的实例，执行刚复制的挂载命令。
关于挂载指令的说明如下，请根据实际的业务情况使用合适的挂载指令：
 - 如果您希望支持扩展属性且所有操作默认为同步执行（机器重启不会丢数据，但性能会有损耗），请复制和执行第如下命令。
 例如：
```shell
sudo mount.lustre -o sync,user_xattrXXXXXXXXXXXXXXXXXXX
```
 - 如果您希望支持扩展属性且无需强制同步执行（机器重启有可能会丢少量尚缓存在内存中的数据，但性能好），请复制和执行如下命令。
 例如：
```shell
sudo mount.lustre -o user_xattrXXXXXXXXXXXXXXXXXXX
```
 - 如果您无需支持扩展属性且无需强制同步执行（机器重启有可能会丢少量尚缓存在内存中的数据，但性能好），请复制和执行如下命令。
 例如：
```shell
sudo mount.lustre XXXXXXXXXXXXXXXXXXX
```
>? 
>- 若需要只读挂载，可在挂载时添加 -o ro 的指令。
>- 卸载与 NFS 协议的文件系统使用方式一致，使用 umount /path/to/umount，即可完成卸载操作。
