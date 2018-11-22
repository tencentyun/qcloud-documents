### 应用部署成功后，服务列表中没有出现服务？

检查部署压缩包中是否包含了 `spec.yaml` ，且 `spec.yaml` 的格式是否正确。如果不存在 `spec.yaml` 或者格式不对，TSF 无法将服务注册到服务注册中心。参考 [TSF Mesh 开发指引 >>](https://cloud.tencent.com/document/product/649/19049)。



### 服务实例显示离线状态？

在 Mesh 环境下，TSF sidecar 会定期通过调用服务的健康检查接口获取服务健康状态，然后将健康状态上报到服务注册中心。假如因为某些原因，比如用户健康检查接口信息配置错误、端口配置错误、或者服务实例出现访问失败，则会导致服务不健康。

#### 1. 排查配置是否正确

##### (1) 服务配置信息错误

查看应用的软件包，获取服务配置信息（spec.yaml），检查下服务名是否为期望暴露的服务名字、端口号是否为服务真实监听的端口号、健康检查接口是否存在、以及检查健康接口格式是否正确（记得是不含ip:port的，类似"/health"这种是符合的）

##### (2) 服务配置文件格式错误

将spec.yaml内容，拷贝到[yamllink](http://www.yamllint.com/)中，校验下yaml格式是否正确。假如正确的话，则可以检查下字段名称，是否与下面示例的格式一致。

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

##### (3) 服务配置没有挂载到正确的位置

在容器环境下，需要排查下，业务是否在容器的启动脚本中，把spec.yaml和apis目录，拷贝到挂载路径/opt/tsf/app_config下面。
在虚拟机环境下，需要排查下，业务程序包根目录下面，是否存在spec.yaml以及apis目录，如果没有，则需要修改。



#### 2. 排查健康检查是否返回正常

登录到应用所在的容器或者虚拟机，通过调用本地的健康检查路径，查看返回码是否200，如果不是200，证明服务存在健康问题。

```shell
curl -i http://127.0.0.1:<服务端口>/<healthCheck_path>
```



#### 3. 通过调用clusters接口来排查

登录到应用所在的容器或者虚拟机，调用envoy的clusters接口，查看本地cluster（格式为 in#port#serviceName）是否存在或者健康状态是否healthy。

```shell
curl http://127.0.0.1:15000/clusters
```

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

假如cluster不存在，则联系后台运维人员处理。
假如状态不为healthy，则可以接下来继续定位。



#### 4. 通过调用config_dump接口来排查

登录到应用所在的容器或者虚拟机，调用envoy的clusters接口，查看本地的路由配置信息

```shell
curl http://127.0.0.1:15000/config_dump -o config.json
```

vi打开config.json文件，并查找in#8080#reporttimeb（本地cluster，格式为in#port#serviceName），查看配置中的服务地址(address)、端口(port_value）是否正确。
健康检查信息health_checks、熔断配置circuit_breakers是否正确。假如不正确，而且确认服务没有被熔断，则联系后台运维人员处理。

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



### 联系后台运维人员

需要提供以下信息，方便运维人员快速定位问题。

问题: B服务注册失败，已初步定位，原因在于下发的配置与服务配置不相符。
服务节点信息: A调用B服务，B服务192.168.3.1，A服务192.168.2.1。
服务类型信息: A服务为springcloud，B服务为mesh。