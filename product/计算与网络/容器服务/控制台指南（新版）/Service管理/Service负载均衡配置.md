
## TkeServiceConfig
TkeServiceConfig 是腾讯云容器服务提供的自定义资源 CRD， 通过 TkeServiceConfig 能够帮助您更灵活的配置 LoadBalancer 类型的 Service ，及管理其中负载均衡的各种配置。

### 使用场景
Service YAML 的语义无法定义的负载均衡的参数和功能，可以通过 TkeServiceConfig 进行配置。


### 配置说明
使用 TkeServiceConfig 能够帮您快速进行负载均衡器的配置。通过 Service 注解 **service.cloud.tencent.com/tke-service-config:&lt;config-name&gt;**，您可以指定目标配置并应用到 Service 中。
>!TkeServiceConfig 资源需要与 Service 处于同一命名空间。

TkeServiceConfig 并不会帮您直接配置并修改协议和端口，您需要在配置中描述协议和端口以便指定配置下发的监听器。在一个 TkeServiceConfig 中可以声明多组监听器配置，目前主要针对负载均衡的健康检查以及对后端访问提供配置。
通过指定协议和端口，配置能够被准确的下发到对应监听器：
  * `spec.loadBalancer.l4Listeners.protocol`：四层协议
  * `spec.loadBalancer.l4Listeners.port`：监听端口

## Service 与 TkeServiceConfig 关联行为
1. 创建 Loadbalancer 模式 Service 时，设置注解 **service.cloud.tencent.com/tke-service-config-auto: "true"**，将自动创建 &lt;ServiceName&gt;-auto-service-config。 您也可以通过 **service.cloud.tencent.com/tke-service-config:&lt;config-name&gt;** 直接指定您自行创建的 TkeServiceConfig。两个注解不可同时使用。 
2. 其中自动创建的 TkeServiceConfig 存在以下同步行为：
  - 更新 Service 资源时，新增若干四层监听器时，如果该监听器或转发规则没有对应的 TkeServiceConfig 配置片段。 Service-Controller 将主动添加 TkeServiceConfig 对应片段。
  - 删除若干四层监听器时，Service-controller 组件将主动删除 TkeServiceConfig 对应片段。
  - 删除 Service 资源时，联级删除该 TkeServiceConfig。
  - 用户修改 Service 默认的 TkeServiceConfig，TkeServiceConfig 内容同样会被应用到负载均衡。
3. 您也可以参考下列 TkeServiceConfig 完整配置参考自行创建需要的 CLB 配置，Service 通过注解：**service.cloud.tencent.com/tke-service-config:&lt;config-name&gt;** 引用该配置。
4. 其中您手动创建的 TkeServiceConfig 存在以下同步行为：
  - 当用户在 Service 中添加配置注解时，负载均衡将会立即进行设置同步。
  - 当用户在 Service 中删除配置注解时，负载均衡将会保持不变。
  - 修改 TkeServiceConfig 配置时，引用该配置 Service 的负载均衡将会根据新的 TkeServiceConfig 进行设置同步。
  - Service 的监听器未找到对应配置时，该监听器将不会进行修改。
  - Service 的监听器找到对应配置时，若配置中没有声明的属性，该监听器将不会进行修改。


## 完整配置参考  
```yaml
apiVersion: cloud.tencent.com/v1alpha1
kind: TkeServiceConfig
metadata:
     name: sample # 配置的名称
     namespace: default # 配置的命名空间
spec:
     loadBalancer:
       l4Listeners: # 四层规则配置，适用于Service的监听器配置。
       - protocol: TCP # 协议端口锚定Service的四层规则。必填，枚举值：TCP|UDP。
         port: 80 # 必填，可选值：1~65535。
         session: # 会话保持相关配置。选填
           enable: true # 是否开启会话保持。必填，布尔值
           sessionExpireTime: 100 # 会话保持的时间。选填，默认值：30，可选值：30~3600，单位：秒。
         healthCheck: # 健康检查相关配置。选填
           enable: true # 是否开启健康检查。必填，布尔值
           intervalTime: 10 # 健康检查探测间隔时间。选填，默认值：5，可选值：5~300，单位：秒。
           healthNum: 2 # 健康阈值，表示当连续探测几次健康则表示该转发正常。选填，默认值：3，可选值：2~10，单位：次。
           unHealthNum: 3 # 不健康阈值，表示当连续探测几次健康则表示该转发异常。选填，默认值：3，可选值：2~10，单位：次。
           timeout: 10 # 健康检查的响应超时时间，响应超时时间要小于检查间隔时间。选填，默认值：2，可选值：2~60，单位：秒。
         scheduler: WRR # 请求转发方式配置。WRR、LEAST_CONN、IP_HASH分别表示按权重轮询、最小连接数、按IP哈希。选填，枚举值：WRR|LEAST_CONN。
       internetMaxBandwidthOut: 100 # 最大出带宽，仅对公网属性的LB生效。选填，可选值：0~2048，单位Mbps。
```


## 示例

### Deployment 示例：jetty-deployment.yaml
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
   labels:
     app: jetty
   name: jetty-deployment
   namespace: default
spec:
   progressDeadlineSeconds: 600
   replicas: 3
   revisionHistoryLimit: 10
   selector:
     matchLabels:
       app: jetty
   strategy:
     rollingUpdate:
       maxSurge: 25%
       maxUnavailable: 25%
     type: RollingUpdate
   template:
     metadata:
       creationTimestamp: null
       labels:
         app: jetty
     spec:
       containers:
       - image: jetty:9.4.27-jre11
         imagePullPolicy: IfNotPresent
         name: jetty
         ports:
         - containerPort: 80
           protocol: TCP
         - containerPort: 443
           protocol: TCP
         resources: {}
         terminationMessagePath: /dev/termination-log
         terminationMessagePolicy: File
       dnsPolicy: ClusterFirst
       restartPolicy: Always
       schedulerName: default-scheduler
       securityContext: {}
       terminationGracePeriodSeconds: 30
```

### Service 示例：jetty-service.yaml
```yaml
apiVersion: v1
kind: Service
metadata:
   annotations:
     service.cloud.tencent.com/tke-service-config: jetty-service-config 
     # 指定已有的 tke-service-config
     # service.cloud.tencent.com/tke-service-config-auto: true 
     # 自动创建 tke-service-config
   name: jetty-service
   namespace: default
spec:
   ports:
   - name: tcp-80-80
     port: 80
     protocol: TCP
     targetPort: 80
   - name: tcp-443-443
     port: 443
     protocol: TCP
     targetPort: 443
   selector:
     app: jetty
   type: LoadBalancer
```
该示例中包含以下配置：
- Service 为公网 LoadBalancer 类型。声明了两个 TCP 服务，一个在80端口，一个在443端口。
- 使用了 `jetty-service-config` 负载均衡配置。

### TkeServiceConfig 示例：jetty-service-config.yaml
```yaml
apiVersion: cloud.tencent.com/v1alpha1
kind: TkeServiceConfig
metadata:
   name: jetty-service-config
   namespace: default
spec:
   loadBalancer:
     l4Listeners:
     - protocol: TCP
       port: 80
       healthCheck:
         enable: false
     - protocol: TCP
       port: 443
       session:
         enable: true
         sessionExpireTime: 3600
       healthCheck:
         enable: true
         intervalTime: 10
         healthNum: 2
         unHealthNum: 2
         timeout: 5
       scheduler: WRR
```
该示例中包含以下配置：
名称为 `jetty-service-config`。且在四层监听器配置中，声明了以下两段配置：
 1. 80端口的 TCP 监听器将会被配置。
 关闭健康检查。
 2. 443端口的 TCP 监听器将会被配置。
  - 打开健康检查，健康检查间隔调整为10s，健康阈值2次，不健康阈值2次，超时5s。
  - 打开会话保持功能，会话保持的超时时间设置为3600s。
  - 转发策略配置为：按权重轮询。

### kubectl 配置命令
```
➜ kubectl apply -f jetty-deployment.yaml
➜ kubectl apply -f jetty-service.yaml
➜ kubectl apply -f jetty-service-config.yaml
  
➜ kubectl get pods
NAME                                READY   STATUS    RESTARTS   AGE
jetty-deployment-8694c44b4c-cxscn   1/1     Running   0          8m8s
jetty-deployment-8694c44b4c-mk285   1/1     Running   0          8m8s
jetty-deployment-8694c44b4c-rjrtm   1/1     Running   0          8m8s
  
➜ kubectl get service jetty
NAME    TYPE           CLUSTER-IP       EXTERNAL-IP       PORT(S)                      AGE
jetty   LoadBalancer   10.127.255.209   150.158.220.237   80:31338/TCP,443:32373/TCP   2m47s
  
# 获取TkeServiceConfig配置列表
➜ kubectl get tkeserviceconfigs.cloud.tencent.com
NAME                   AGE
jetty-service-config   52s
 
# 更新修改TkeServiceConfig配置
➜ kubectl edit tkeserviceconfigs.cloud.tencent.com jetty-service-config
TkeServiceConfig.cloud.tencent.com/jetty-service-config edited
```

