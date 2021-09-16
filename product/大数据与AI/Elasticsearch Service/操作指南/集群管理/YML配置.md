您可以通过修改腾讯云 Elasticsearch Service（ES）实例的 YML 参数配置，配置常用的参数。

## 使用步骤
### 查看配置项
登录 [Elasticsearch Service 控制台](https://console.cloud.tencent.com/es)，单击需要修改配置的【集群ID/名称】，进入集群详情页，然后单击【高级配置】，即可查看配置项参数。
![](https://main.qcloudimg.com/raw/a3fa8eb4b0378692c91ab76a968c6d53.png)

### 修改配置项
单击【修改配置】，可对相应的配项进行修改，配置项的输入限制，见表格最后一列“取值说明”。【更多配置】支持 YML 语法，可以自定义其他配置项的设置。
![](https://main.qcloudimg.com/raw/72762fa7534da65f2eeda8d2f13bd61c.png)
单击【确定修改】，新的配置项参数将会应用到您的集群，勾选“已了解风险，仍然强制重启”会滚动重启集群。如果您集群中的索引有副本，重启后不会对您的业务造成影响，但建议在业务低峰期操作。
> !如果集群健康状态为 YELLOW 或 RED，或集群存在无副本索引时，修改集群配置项对话框会有强制重启的提示和选项框，此时进行更新配置操作有较大风险，建议修复集群状态，为所有索引添加副本，再进行修改配置操作。
> 
如果用户已了解该操作风险，仍要进行更新配置操作，可以勾选强制重启选项框，单击【确定】进行重启。详情参考下图：
![](https://main.qcloudimg.com/raw/33e9357644d3f99fc38d2d9160e94a30.jpg)
确定后，腾讯云 ES 实例会进行重启，重启过程中可在集群变更记录中查看进度。重启成功后即可完成 YML 文件的配置。

## 支持的参数

| 参数                                | 说明                                       | 默认值 |
| ----------------------------------- | ------------------------------------------ | ------ |
| indices.fielddata.cache.size        | 指定分配到字段数据的 Java 堆空间的百分比   | 15%    |
| indices.query.bool.max_clause_count | 指定 Lucene 布尔查询中允许的子句的最大数量 | 1024   |

## 支持的热更参数

| 参数                             | 说明                           | 取值范围                       |
| -------------------------------- | ------------------------------ | ------------------------------ |
| action.destructive_requires_name | 删除索引时是否需要明确索引名称 | true 或者 false，默认值为 true |

## 配置 reindex 白名单

| 参数                     | 说明                     | 默认值 |
| ------------------------ | ------------------------ | ------ |
| reindex.remote.whitelist | 远程 ES 集群访问地址白名单 | `[]`   |

## 自定义队列大小

| 参数                          | 说明                                    | 默认值 |
| ----------------------------- | --------------------------------------- | ------ |
| thread_pool.bulk.queue_size   | 文档写入队列大小，适用于5.6.4版本       | 1024   |
| thread_pool.write.queue_size  | 文档写入队列大小，适用于6.4.3及以上版本 | 1024   |
| thread_pool.search.queue_size | 文档搜索队列大小                        | 1024   |

## 自定义 CORS 访问配置

| 参数                        | 说明                                                         | 默认值                                         |            
| --------------------------- | ------------------------------------------------------------ | ---------------------------------------------- | 
| http.cors.enabled           | 跨域资源共享配置项，`true`表示启用跨域资源访问，`false`表示不启用 | false                        |                          
| http.cors.allow-origin      | 域资源配置项，可设置接受来自哪些域名的请求                   | `""`                                           | 
| http.cors.max-age           | 获取的 CORS 配置信息在浏览器中的缓存时间                       | 1728000（20天）                                | 
| http.cors.allow-methods     | 跨域允许的请求方法                                           | `OPTIONS,HEAD,GET,POST,PUT,DELETE`             |              
| http.cors.allow-headers     | 跨域允许的请求头信息                  | `X-Requested-With,Content-Type,Content-Length` |                          
| http.cors.allow-credentials | 是否允许响应头中返回 Access-Control-Allow-Credentials 信息     | false                               |                   

## 配置 Watcher

| 参数                  | 说明                              | 默认值 |
| --------------------- | --------------------------------- | ------ |
| xpack.watcher.enabled | `true`表示开启 X-Pack 的 Watcher 功能 | true   |

具体配置项详细含义，可参见 [Elasticsearch 官方文档](https://www.elastic.co/guide/en/elasticsearch/reference/5.6/index.html)。如果有其他配置项自定义设置需求，可通过 [售后支持](https://cloud.tencent.com/online-service?from=connect-us) 进行反馈。
