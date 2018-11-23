### 应用部署成功后，服务列表中为何没有出现服务？
请检查部署压缩包中是否包含了 `spec.yaml` ，且 `spec.yaml` 的格式是否正确。
如果不存在 `spec.yaml` 或者格式不对，TSF 无法将服务注册到服务注册中心。详情参考 [TSF Mesh 开发指引](https://cloud.tencent.com/document/product/649/19049)。


### 服务实例显示离线状态如何解决？
在 Mesh 环境下，TSF Sidecar 会定期通过调用服务的健康检查接口获取服务健康状态，并将健康状态上报到服务注册中心。由于某些原因，比如用户健康检查接口信息配置错误、端口配置错误、或者服务实例出现访问失败，则会导致服务不健康。
您可以通过以下步骤进行排查：
#### 1. 查看服务配置信息
- 服务配置信息错误
查看应用的软件包，获取服务配置信息（spec.yaml），检查服务名是否为期望暴露的服务名、端口号是否为服务真实监听的端口号、健康检查接口是否存在、检查健康接口格式是否正确（不含 ip:port，类似`/health`是符合的）。

- 服务配置文件格式错误
将 spec.yaml 内容，拷贝到 [yamllink](http://www.yamllint.com/) 中，校验 yaml 格式是否正确。如过格式正确，则继续检查字段名称，是否与下面示例的格式一致。
```yaml
apiVersion: v1
kind: Application
metadata:
  name: service1
  namespace: nsTester
spec:
  services:
    - name: user
      healthCheck:
        path: /health
      ports:
        - targetPort: 8089
          protocol: http
```

-  服务配置没有挂载到正确的位置
  - 在容器环境下，排查业务是否在容器的启动脚本中，把 spec.yaml 和 apis 目录，拷贝到挂载路径`/opt/tsf/app_config`下面。
 - 在虚拟机环境下，排查业务程序包根目录下面，是否存在 spec.yaml 以及 apis 目录，如果没有，则需要修改。

#### 2. 查看健康检查返回
登录应用所在的容器或者虚拟机，通过调用本地的健康检查路径，查看返回码是否为200，如果不是200，证明服务存在健康问题。
```shell
curl -i http://127.0.0.1:<服务端口>/<healthCheck_path>
```

#### 3. 调用 clusters 接口
登录应用所在的容器或者虚拟机，调用 envoy 的 clusters 接口，查看本地 cluster（格式为 in#port#serviceName）是否存在或者健康状态是否 healthy。
输入：
```shell
curl http://127.0.0.1:15000/clusters
```
输出：
```
in#8080#reporttimeb::default_priority::max_connections::1024
in#8080#reporttimeb::default_priority::max_pending_requests::1024
in#8080#reporttimeb::default_priority::max_requests::1024
in#8080#reporttimeb::default_priority::max_retries::3
in#8080#reporttimeb::high_priority::max_connections::1024
in#8080#reporttimeb::high_priority::max_pending_requests::1024
in#8080#reporttimeb::high_priority::max_requests::1024
in#8080#reporttimeb::high_priority::max_retries::3
in#8080#reporttimeb::added_via_api::true
in#8080#reporttimeb::9.77.7.132:8080::cx_active::0
in#8080#reporttimeb::9.77.7.132:8080::cx_connect_fail::0
in#8080#reporttimeb::9.77.7.132:8080::cx_total::4
in#8080#reporttimeb::9.77.7.132:8080::rq_active::0
in#8080#reporttimeb::9.77.7.132:8080::rq_error::0
in#8080#reporttimeb::9.77.7.132:8080::rq_success::4
in#8080#reporttimeb::9.77.7.132:8080::rq_timeout::0
in#8080#reporttimeb::9.77.7.132:8080::rq_total::4
in#8080#reporttimeb::9.77.7.132:8080::health_flags::healthy
in#8080#reporttimeb::9.77.7.132:8080::weight::1
in#8080#reporttimeb::9.77.7.132:8080::region::
in#8080#reporttimeb::9.77.7.132:8080::zone::
in#8080#reporttimeb::9.77.7.132:8080::sub_zone::
in#8080#reporttimeb::9.77.7.132:8080::canary::false
in#8080#reporttimeb::9.77.7.132:8080::success_rate::-1
```
- 如果 cluster 不存在，则需要通过通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系后台运维人员处理。
- 如果状态不为 healthy，则执行后续步骤。



#### 4. 调用 config_dump 接口
登录应用所在的容器或者虚拟机，调用 envoy 的 clusters 接口，查看本地的路由配置信息：
```shell
curl http://127.0.0.1:15000/config_dump -o config.json
```

通过 vi 打开 config.json 文件，并查找 in#8080#reporttimeb（本地 cluster，格式为 in#port#serviceName），查看配置中的服务地址(address)、端口(port_value）是否正确。
健康检查信息 health_checks、熔断配置 circuit_breakers 是否正确。如果不正确，且确认服务没有被熔断，则需要通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 联系后台运维人员处理。
```json
"dynamic_active_clusters": [
    {
     "version_info": "2018-10-17T11:31:50+08:00",
     "cluster": {
      "name": "BlackHoleCluster",
      "connect_timeout": "1s"
     },
     "last_updated": "2018-10-16T19:31:41.792Z"
    },
    {
     "version_info": "2018-10-17T11:31:50+08:00",
     "cluster": {
      "name": "in#8080#reporttimeb",
      "connect_timeout": "5s",
      "hosts": [
       {
        "socket_address": {
         "address": "9.77.7.132",
         "port_value": 8080
        }
       }
      ],
      "health_checks": [
       {
        "timeout": "5s",
        "interval": "10s",
        "unhealthy_threshold": 2,
        "healthy_threshold": 2,
        "http_health_check": {
         "path": "/health"
        }
       }
      ]
```



### 如何联系后台运维人员？
您可以通过 [提交工单](https://console.cloud.tencent.com/workorder/category) 的方式联系后台运维人员。
您需要提供以下信息，方便运维人员快速定位问题。
- 问题：B 服务注册失败，已初步定位，原因在于下发的配置与服务配置不相符。
- 服务节点信息：A 调用 B 服务，B 服务192.168.3.1，A 服务192.168.2.1。
- 服务类型信息：A 服务为 springcloud，B 服务为 Mesh。
