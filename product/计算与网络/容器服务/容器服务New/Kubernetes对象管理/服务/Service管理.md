## Service 管理
### Service 简介
Service 定义了访问后端Pod的访问策略，由Label Selector选中后端的Pod, Service不因后端Pod变化而变化，提供的固定虚拟的访问IP。 可以通过Service 负载均衡地访问到后端的Pod.
Serivce支持以下类型：
- 公网访问： 自动创建公网CLB， 通过公网IP可直接访问到后端Pod， 对应Service的loadbalance模式
- VPC内网访问：自动创建内网CLB， VPC内可通过内网IP直接访问到后端Pod， 也对应Service的Loadbalance模式，但需额外指定 `annotations:service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxxxxx`
- 集群内访问：会自动分配Serivce网段中的IP用于集群内访问，对应Service的ClusterIP模式。

### Service 控制台操作指引
#### 创建 Service
1. 点击需要部署 Service 的集群ID，进入集群详情页面。
2. 点击 Service 选项，选择新建 Service。
3. 根据指引设置 Service 参数，完成创建。


![][createService]
>注意：
1. 不建议您容器业务和CVM业务共用一个CLB。
2. 不建议您直接在CLB控制台操作TKE自动管理的CLB。
2. 使用已有的CLB时容器服务TKE会自动覆盖CLB已有的后端RS。
3. TKE会自动覆盖和更新名称为TKE_Dedicated_Listener的监听器，其他监听器不覆盖。

#### 更新 Service
**Yaml更新**
1. 点击需要部署的 Service 的集群ID，进入集群详情页面。
2. 选择需要更新的 Service , 进入 Service 详情页，点击Yaml tab, 可编辑Yaml直接更新


### kubectl 操作 Service 指引
#### Yaml模板
```Yaml
kind: Service
apiVersion: v1
metadata:
  ## annotations:
  ##   service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxxxxx ##若是创建内网访问的Service需指定该条annotation
  name: my-service
spec:
  selector:
    app: MyApp
  ports:
  - protocol: TCP
    port: 80
    targetPort: 9376
  type: LoadBalancer
```
##### annotations: 使用已有负载均衡器来创建公网/内网访问的Service
当您已有包年包月的传统型CLB空闲时， 希望TKE创建的Service能够使用已有的CLB， 您可以通过以下annotations进行设置：
```Yaml
metadata:
  annotations:
    service.kubernetes.io/tke-existed-lbid: lb-6swtxxxx
```
>注意：
1. 不建议您容器业务和CVM业务共用一个CLB。
2. 不建议您直接在CLB控制台操作TKE自动管理的CLB。
2. 使用已有的CLB时容器服务TKE会自动覆盖CLB已有的后端RS。
3. TKE会自动覆盖和更新名称为TKE_Dedicated_Listener的监听器，其他监听器不覆盖。

##### annotations: 指定节点绑定Loadbalances
当您的集群规模较大时， 入口类型的应用设置亲和性调度到部分节点， 你可以配置Servce的Loadbalance只绑定指定节点， annotations如下：
```yaml
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-backends-label: `key in (value1, value2) ` ## LabelSelector格式
```
1. 建议配合工作负载的亲和性调度使用。
2. 前提条件是Node已根据业务需求设置Label。
2. 采用原生LabelSelector格式如：
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key1=values1, key2=values2
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key1 in (value1),key2 in (value2)
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key in (value1, value2)
  - service.kubernetes.io/qcloud-loadbalancer-backends-label: key1, key2 notin (value2)
4. 增量的节点若匹配，将自动绑定到该Loadbalance。
5. 修改存量节点的Label， 根据匹配规则将动态绑定和解绑Loadbalance。

>注：如果是带宽上移账号，在创建公网访问方式的服务时需要指定如下两个 annotations 项：
- `service.kubernetes.io/qcloud-loadbalancer-internet-charge-type`.公网带宽计费方式， 可选值有：TRAFFIC_POSTPAID_BY_HOUR（按使用流量计费），BANDWIDTH_POSTPAID_BY_HOUR（按带宽计费）
- `service.kubernetes.io/qcloud-loadbalancer-internet-max-bandwidth-out`.带宽上限，范围：[1,2000] Mbps。
如：
```Yaml
metadata:
  annotations:
    service.kubernetes.io/qcloud-loadbalancer-internet-charge-type: TRAFFIC_POSTPAID_BY_HOUR
    service.kubernetes.io/qcloud-loadbalancer-internet-max-bandwidth-out: "10"
```

- kind: 标识该资源是 service 类型
- metadata：该 service 的名称、Label等基本信息
- metadata.annotations: 对 service 的额外说明，腾讯云TKE额外增强能力可以通过该参数设置。
- spec.type：标识该Service的被访问形式：
  - ClusterIP：在集群内部公开服务， 可用于集群内不访问。
  - NodePort：使用节点的端口映射到后端Service，集群外可以通过节点IP：NodePort 访问。
  - LoadBalancer: 使用腾讯云提供的负载均衡器公开服务，默认创建公网CLB， 指定annotations可创建内网CLB。
  - ExternalName：ExternalName类型的服务将服务映射到DNS。注： ExternalName服务仅适用于kube-dns1.7及更高版本

#### 创建Service
1. 准备service Yaml文件， 例如上述文件为my-service.Yaml （请先创建好工作负载）
2. kubectl安装完成，并且已连接上集群（可直接登录集群节点使用kubectl）
3. 执行命令创建：
```shell
kubectl create -f my-service.yaml
```
4. 执行命令验证创建情况：
```shell
kubectl get services
```
#### 更新Service
**方法一**：直接通过`kubectl edit  service/[name]`更新
**方法二**：删除旧的Service， 重新通过kubectl create/apply 创建Service.

#### 删除Service
1. 执行命令`kubectl delete service [NAME]`


[createService]:https://main.qcloudimg.com/raw/33058be22f681ad732e5d9dd51ddbb8f.png
