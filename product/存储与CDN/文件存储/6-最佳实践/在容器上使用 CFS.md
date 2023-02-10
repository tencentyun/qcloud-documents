## 操作场景

文件存储（Cloud File Storage，CFS）在容器环境如下主要适用于两类场景：

#### 场景一：POD/容器数据的持久化存储，推荐使用动态挂载 CFS

CFS 可提供一个持久化存储的空间，当 POD/容器销毁时，数据仍然保存；当 POD/容器再次启动时，可通过 PVC 快速挂载原空间，实现数据的读写操作。
相比于其他方案，单 FS 实例可同时支持多个 POD/容器的数据存储，并支持根据 CFS 实例中的不同子目录，分配给不同的 POD。CFS 通用标准型/性能型按照实际使用容量进行计费，且无最小购买容量要求，可降低用户大规模容器持久化数据存储的成本。

#### 场景二：多 POD/容器的数据共享，推荐使用静态挂载 CFS

CFS 通过 NFS/私有协议提供了一个共享访问的目录空间给多个 POD/容器，实现数据资源的高效共享，相比于其他方案，能提供更高的带宽和 IOPS 能力。

本文将重点介绍基于腾讯云控制台，部署容器 workload 的方法。具体的 YAML 写法，可参考通过控制台创建 StorageClass 后自动生成 YAML 文件。

>! 使用前，需确保容器服务 （Tencent Kubernetes Engine，TKE）集群的 CSI 组件在1.0.4版本以上。若版本不对，可在 TKE 控制台上进行更新，CSI 组件的更新不影响容器的正常使用。
>

## 操作步骤

### 动态挂载 CFS

>? POD/容器数据的持久化存储场景，推荐此方式进行挂载。
>

1. 创建 StorageClass，具体操作请参见 [通过控制台创建 StorageClass](https://cloud.tencent.com/document/product/457/44235#.E6.8E.A7.E5.88.B6.E5.8F.B0.E6.93.8D.E4.BD.9C.E6.8C.87.E5.BC.95) 文档。
![](https://qcloudimg.tencent-cloud.cn/raw/9df2dac9bc3c053599b610bf7c0e28d7.png)
相关的关键配置项如下：
<table>
	<tr><th>配置项</th><th>配置项.说明</th></tr>
	<tr><td>实例创建模式</td><td>此场景选择共享实例。</td></tr>
	<tr><td>可用区</td><td>建议选择与容器宿主机相同的可用区，以便获得更好的性能。</td></tr>
	<tr><td>存储类型</td><td>根据实际性能需求可选择通用标准型存储和通用性能型存储。</td></tr>
	<tr><td>协议版本</td><td>在非多个同时修改/编辑的场景下，建议使用 NFS V3协议，以便得到更好的性能。</td></tr>
	<tr><td>回收策略</td><td>可根据实际需要，选择删除和保留，为避免数据误删优先建议选择保留。</td></tr>
</table>
2. 创建 PVC，具体操作请参见 [创建 PVC](https://cloud.tencent.com/document/product/457/44236#.E5.88.9B.E5.BB.BA-pvc.3Ca-id.3D.22createpvc2.22.3E.3C.2Fa.3E) 文档。
![](https://qcloudimg.tencent-cloud.cn/raw/5365fcc6cf36ce365c05aa8bbd94cf6c.png)
相关的关键配置项如下：
<table>
	<tr><th>配置项</th><th>配置项说明</th></tr>
	<tr><td>命名空间</td><td>根据实际需要选择不同的命名空间。</td></tr>
	<tr><td>Storageclass</td><td>选择刚才创建的 StorgeClass。</td></tr>
	<tr><td>是否指定PersistentVolume</td><td>动态创建可不指定 PV。</br><b>说明</b>：基于 CFS 共享型实例的 StorgeClass，在创建 PVC 时，若不指定 PV，CSI 插件会在创建 PVC 的同时，自动创建一个按量付费的 CFS 实例，此实例会随着 PVC 的删除而删除，故需谨慎处理基于此方式创建的 PVC。</td></tr>
</table>
3. 创建 Deployment，具体操作请参见 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment) 文档。
![](https://qcloudimg.tencent-cloud.cn/raw/02c037f7ff27b2e6275bd548c99fb448.png)
相关的关键配置项如下：
<table>
	<tr><th>配置项</th><th>配置项说明</th></tr>
	<tr><td>数据卷</td><td>根据实际需求，对数据卷进行命名，并选中刚创建的 PVC。</td></tr>
	<tr><td>挂载点</td><td>选择对应的数据卷，指定在容器本地的挂载路径。在共享 CFS 实例的动态创建方式下，需要指定具体的环境变量，CSI 插件会基于配置的环境变量的变量值，在所选 PVC 对应的 CFS 实例里创建目录供容器挂载。</td></tr>
</table>
配置完成后，单击<b>创建Workload</b>，系统将基于此配置创建容器，并挂载 CFS。


### 静态挂载 CFS

>? 多 POD/容器的数据共享场景，推荐此方式进行挂载。
>

1. 创建 StorageClass，具体操作请参见 [通过控制台创建 StorageClass](https://cloud.tencent.com/document/product/457/44235#.E6.8E.A7.E5.88.B6.E5.8F.B0.E6.93.8D.E4.BD.9C.E6.8C.87.E5.BC.95) 文档。
![](https://qcloudimg.tencent-cloud.cn/raw/9df2dac9bc3c053599b610bf7c0e28d7.png)
相关的关键配置项如下：
<table>
	<tr><th>配置项</th><th>配置项.说明</th></tr>
	<tr><td>实例创建模式</td><td>此场景选择共享实例。</td></tr>
	<tr><td>可用区</td><td>建议选择与容器宿主机相同的可用区，以便获得更好的性能。</td></tr>
	<tr><td>存储类型</td><td>根据实际性能需求可选择通用标准型存储和通用性能型存储。</td></tr>
	<tr><td>协议版本</td><td>在非多个同时修改/编辑的场景下，建议使用 NFS V3协议，以便得到更好的性能。</td></tr>
	<tr><td>回收策略</td><td>可根据实际需要，选择删除和保留，为避免数据误删优先建议选择保留。</td></tr>
</table>
2. 创建 PV，具体操作请参见 [静态创建 PV](https://cloud.tencent.com/document/product/457/44236#.E9.9D.99.E6.80.81.E5.88.9B.E5.BB.BA-pv.3Ca-id.3D.22pv.22.3E.3C.2Fa.3E) 文档。
![](https://qcloudimg.tencent-cloud.cn/raw/6133f892b4c92eecb94eb8573d0d4bfc.png)
相关的关键配置项如下：
<table>
	<tr><th>配置项</th><th>配置项说明</th></tr>
	<tr><td>来源设置</td><td>选择静态创建，即指定某个 CFS 实例配置 PV。</td></tr>
	<tr><td>StorgeClass</td><td>选择刚才创建的 StorgeClass。</td></tr>
	<tr><td>选择CFS</td><td>选择一个指定的 CFS。</br><b>说明</b>：静态创建时需要保证已经有一个 CFS 实例，同时该 CFS 实例需与容器在同一个 VPC 网络环境。</td></tr>
	<tr><td>CFS子目录</td><td>CFS 可以允许挂载子目录，用户可根据实际需要选择不同的子目录绑定至一个或多个 PV 上，实现不同程度的数据共享。</td></tr>
</table>
3. 创建 PVC，具体操作请参见 [创建 PVC](https://cloud.tencent.com/document/product/457/44236#.E5.88.9B.E5.BB.BA-pvc.3Ca-id.3D.22createpvc2.22.3E.3C.2Fa.3E) 文档。
![](https://qcloudimg.tencent-cloud.cn/raw/cac0368da56c222a39c2e74179821695.png)
相关的关键配置项如下：
<table>
	<tr><th>配置项</th><th>配置项说明</th></tr>
	<tr><td>命名空间</td><td>根据实际需要选择不同的命名空间。</td></tr>
	<tr><td>Storageclass</td><td>选择刚才创建的 StorgeClass。</td></tr>
	<tr><td>是否指定PersistentVolume</td><td>选择指定，并选择刚才创建的 PV。</td></tr>
</table>
4. 创建 Deployment，具体操作请参见 [创建 Deployment](https://cloud.tencent.com/document/product/457/31705#.E5.88.9B.E5.BB.BA-deployment) 文档。
![](https://qcloudimg.tencent-cloud.cn/raw/391961269e4bdfc6f53d5c88fbfcbd51.png)
![](https://qcloudimg.tencent-cloud.cn/raw/d70a761711e767537545e9727a22c6ad.png)
相关的关键配置项如下：
<table>
	<tr><th>配置项</th><th>配置项说明</th></tr>
	<tr><td>数据卷</td><td>根据实际需求，对数据卷进行命名，并选中刚创建的 PVC。</td></tr>
	<tr><td>挂载点</td><td>选择对应的数据卷，指定在容器本地的挂载路径。对于自动创建子目录的场景，目前有两种方案可以使用。</br>方案一，挂载点选择subPath，直接填写希望挂载的路径名称如test，则CSI插件会自动在文件系统跟路径下创建test目录，并自动挂载至容器的指定目录下。</br>方案二，添加环境变量，并给环境变量赋值。挂载点选择subPathExpr，并选择对应的环境变量。则CSI 插件将会以该环境变量的变量值作为目录名，自动在文件系统的根路径下创建该目录，并自动挂载至容器的指定目录下。</td></tr>
</table>
配置完成后，单击<b>创建Workload</b>，系统将基于此配置创建容器，并挂载 CFS。

