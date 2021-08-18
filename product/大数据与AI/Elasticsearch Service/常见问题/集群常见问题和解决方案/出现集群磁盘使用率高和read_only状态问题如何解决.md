## 问题现象
当磁盘使用率超过85%，或者达到100%，会导致 Elasticsearch 集群或 Kibana 无法正常提供服务，可能会出现以下几种问题场景：
- 在进行索引请求时，返回类似 `{[FORBIDDEN/12/index read-only/allow delete(api)];","type":"cluster_block_exception"}` 的报错。
2. 在对集群进行操作时，返回类似 `[FORBIDDEN/13/cluster read-only / allow delete (api)]` 的报错。
3. 集群处于 Red 状态，严重情况下存在节点未加入集群的情况（可通过 `GET _cat/allocation?v` 命令查看），并且存在未分配的分片（可通过 `GET _cat/allocation?v` 命令查看）。
4. 通过 Elasticsearch 控制台的节点监控页面，集群节点磁盘使用率曾达到或者接近100%。

## 问题分析
上述问题是由于磁盘使用率过高所导致。数据节点的磁盘使用率存在以下三个水位线，超过水位线可能会影响 Elasticsearch 或 Kibana 服务。
- 当集群磁盘使用率超过85%：会导致新的分片无法分配。
- 当集群磁盘使用率超过90%：Elasticsearch 会尝试将对应节点中的分片迁移到其他磁盘使用率比较低的数据节点中。
- 当集群磁盘使用率超过95%：系统会对 Elasticsearch 集群中对应节点里每个索引强制设置 read_only_allow_delete 属性，此时该节点上的所有索引将无法写入数据，只能读取和删除对应索引。

## 解决方案
### 清理集群过期数据
1. 用户可以通过访问【Kibana】>【Dev Tools】删除过期索引释放磁盘空间。步骤如下：
>=数据删除后将无法恢复，请谨慎操作。您也可以选择保留数据，但需进行磁盘扩容。
>
第一步：开启集群索引批量操作权限。
```
PUT _cluster/settings
 {
			"persistent": {
			 "action.destructive_requires_name": "false"
			}
}
```
第二步：删除数据，例如 `DELETE NginxLog-12*`。
```
DELETE index-name-*
```
2. 执行完上述步骤后，如果用户腾讯云 Elasticsearch 的版本是7.5.1以前的版本，还需要在 Kibana 界面的【Dev Tools】中执行如下命令：
 - 关闭索引只读状态，执行如下命令：
```
PUT _all/_settings
{
			"index.blocks.read_only_allow_delete": null
}
```
 - 关闭集群只读状态，执行如下命令：
```
PUT _cluster/settings
{
			"persistent": {
				"cluster.blocks.read_only_allow_delete": null
			}
}
```
3. 查看集群索引是否依然为`read_only`状态，索引写入是否恢复正常。
4. 若集群是否依然为 Red 状态，执行以下命令，查看集群中是否存在未分配的分片。
```
GET /_cluster/allocation/explain
```
5. 等待分片下发完成后，查看集群状态。如果集群状态依然为 Red，请通过 [售后支持](https://cloud.tencent.com/online-service?from=connect-us) 联系腾讯云技术支持。
6. 为避免磁盘使用率过高影响 Elasticsearch 服务，建议开启磁盘使用率监控报警，及时查收报警短信，提前做好防御措施，具体可参考 [监控告警配置建议](https://cloud.tencent.com/document/product/845/35572)。

### 扩容云盘空间
若用户不想清理集群数据，也可以在腾讯云 [ES 控制台](https://console.cloud.tencent.com/es) 的集群配置界面，扩容磁盘空间。步骤如下：
1. 在集群列表中单击要配置的实例【ID/名称】，进入实例详情页，在【基础配置】页签中单击【调整配置】。
![](https://main.qcloudimg.com/raw/2efb62516f0db1aabf4df16deb237739.png)
2. 进入调整配置页面，【单节点数据盘】选择您需要扩容的磁盘空间，单击【下一步】，提交任务即可。
![](https://main.qcloudimg.com/raw/33d809a66201d21343d19f17646439fa.png)
3. 如果用户腾讯云 Elasticsearch 的版本是7.5.1以前的版本，还需要在 Kibana 界面的【Dev Tools】中执行如下命令：
 - 关闭索引只读状态，执行如下命令：
```
PUT _all/_settings
  {
			"index.blocks.read_only_allow_delete": null
  }
```
 - 关闭集群只读状态，执行如下命令：
```
PUT _cluster/settings
{
			"persistent": {
			"cluster.blocks.read_only_allow_delete": null
			}
}
```
