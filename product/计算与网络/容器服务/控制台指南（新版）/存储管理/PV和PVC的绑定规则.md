## PV 状态介绍
<table>
	<tr>
	<th>PV 状态</th>	<th>描述</th>
	</tr>
	<tr>
	<td>Avaliable</td>
	<td>创建好的 PV 在没有和 PVC 绑定的时候处于 Available 状态。</td>
	</tr>
	<tr>
	<td>Bound</td>
	<td>当一个 PVC 与 PV 绑定之后，PVC 就会进入 Bound 的状态。</td>
	</tr>
	<tr>
	<td>Released</td>
	<td>一个回收策略为 Retain 的 PV，当其绑定的 PVC 被删除，该 PV 会由 Bound 状态转变为 Released 状态。<br><b>注意：</b>Released 状态的 PV 需要手动删除 YAML 配置文件中的 claimRef 字段才能与 PVC 成功绑定。 </td>
	</tr>
</table>


## PVC 状态介绍
<table>
	<tr>
	<th>PVC 状态</th>	<th>描述</th>
	</tr>
	<tr>
	<td>Pending</td>
	<td>没有满足条件的 PV 能与 PVC 绑定时，PVC 将处于 Pending 状态。</td>
	</tr>
	<tr>
	<td>Bound</td>
	<td>当一个 PV 与 PVC 绑定之后，PVC 会进入 Bound 的状态。</td>
	</tr>
</table>

## 绑定规则
当 PVC 绑定 PV 时，需考虑以下参数来筛选当前集群内是否存在满足条件的 PV。
<table>
	<tr>
	<th>参数</th>	<th>描述</th>
	</tr>
	<tr>
	<td>VolumeMode</td>
	<td>主要定义 volume 是文件系统（FileSystem）类型还是块（Block）类型，PV 与 PVC 的 VolumeMode 标签必须相匹配。</td>
	</tr>
	<tr>
	<td>Storageclass</td>
	<td>PV 与 PVC 的 storageclass 类名必须相同（或同时为空）。</td>
	</tr>
	<tr>
	<td>AccessMode</td>
	<td>主要定义 volume 的访问模式，PV 与 PVC 的 AccessMode 必须相同。 </td>
	</tr>
	<tr>
	<td>Size</td>
	<td>主要定义 volume 的存储容量，PVC 中声明的容量必须小于等于 PV，如果存在多个满足条件的 PV，则选择最小的 PV 与 PVC 绑定。 </td>
	</tr>
</table>

>? PVC 创建后，系统会根据上述参数筛选满足条件的 PV 进行绑定。如果当前集群内的 PV 资源不足，系统会动态创建一个满足绑定条件的 PV 与 PVC 进行绑定。

## StorageClass 的选择和 PV/PVC 的绑定关系
容器服务 TKE 的平台操作中，StorageClass 的选择与 PV/PVC 之间的绑定关系见下图：
![](https://main.qcloudimg.com/raw/211897efb0d69913a91844c0a27ff6f3.png)







