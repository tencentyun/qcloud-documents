Apache Livy 是一个可以通过 REST 接口与 Spark 集群进行交互的服务，它可以提交 Spark 作业或者 Spark 代码片段，同步或者异步的进行结果检索以及 Spark Context 上下文管理，Apache Livy 简化 Spark 和应用程序服务器之间的交互，从而使 Spark 能够用于交互式 Web/移动应用程序。

**其他功能包括：**
- 由多个客户端长时间运行可用于多个 Spark 作业的 Spark 上下文。
- 跨多个作业和客户端共享缓存的 RDD 或数据帧。
- 可以同时管理多个 Spark 上下文，并且 Spark 上下文运行在群集（YARN/Mesos）而不是 Livy 服务器，以实现良好的容错性和并发性。
- 作业可以作为预编译的 jar，代码片段或通过 java/scala 客户端 API 提交。
- 通过安全的认证通信确保安全。

![](https://main.qcloudimg.com/raw/4dc71e49b36d1790760e97cdd54543b6.png)

## 使用 Livy
1. 访问`http://IP:8998/ui` 可以进入 Livy 的 UI 页面（**IP 为外网 IP，请自行为安装有 Livy 的机器申请外网 IP，并编辑设置安全组策略来开通对应的端口以进行访问**）。
2. 创建一个交互式会话。
```
curl -X POST --data '{"kind":"spark"}' -H "Content-Type:application/json" IP:8998/sessions
```
3. 查看 Livy 上存活的 sessions。
```
curl IP:8998/sessions
```
4. 执行代码片段，简单的加法操作（这里相当于指定的 session 0，如果有多个 session，也可以指定其他 session）。
```
curl -X POST IP:8998/sessions/0/statements -H "Content-Type:application/json" -d '{"code":"1+1"}'
```
5. 计算圆周率（执行 jar 包）。
```
curl -H "Content-Type: application/json" -X POST -d '{ "file":"/usr/local/service/spark/examples/jars/spark-examples_2.11-2.4.3.jar", "className":"org.apache.spark.examples.SparkPi" }' IP:8998/batches
```
6. 查询代码片段执行是否成功，也可以直接在 UI 页面`http://IP:8998/ui/session/0`查看。
```
curl IP:8998/sessions/0/statements/0
```
7. 删除 session。
```
curl -X DELETE IP:8998/sessions/0
```

## 注意事项
###  开放的配置文件
目前开放的配置文件包括`livy.conf`和`livy-env.sh`，这两个配置文件均可以通过配置下发的方式来修改配置。具体开放了哪几个配置文件，请以 EMR 控制台实际为准。

### Livy 端口修改方法
目前的默认端口是8998，用户可以自行修改。修改配置文件`livy.conf`的`livy.server.port`属性即可。

若集群装有 Hue，由于 Hue 与 Livy 之间涉及联通性，因此 Hue 对应的配置端口也需要修改。其对应的配置文件为`pseudo-distributed.ini`，路径为`/usr/local/service/hue/desktop/conf`，对应的配置项为 `livy_server_port=8998`。修改后要重启对应的服务。

**如非必要，建议不要修改 Livy 的端口，如涉及安全要求，可以通过安全组的方式来进行控制。修改后可能会导致一些其他的潜在问题。**

### Livy 部署方式
目前 Livy 默认会在所有 master 节点上部署，用户也可以通过扩容 router 的方式在 router 上进行部署。
