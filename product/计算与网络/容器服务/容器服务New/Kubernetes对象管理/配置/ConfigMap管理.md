## ConfigMap 管理
### ConfigMap 简介
通过ConfigMap您可以把配置和运行的镜像解耦，使得应用程序有更强的移植性， ConfigMap是有key-value类型的键值对，您可以通过控制台会kubectl工具创建对应的ConfigMap对象。 可通过挂载数据卷或环境变量或在容器的运行命令中使用ConfigMap. 修改ConfigMap对象，使用该对象的工作负载配置也生效。

### ConfigMap 控制台操作指引
#### 创建 ConfigMap
1. 点击需要部署创建 ConfigMap 的集群ID，进入集群详情页面。
2. 点击创建 ConfigMap 选项，选择新建创建 ConfigMap
3. 根据指引设置创建 ConfigMap 参数，完成创建。

![][createConfigMap]

#### 使用 ConfigMap
**方式一**： 数据卷使用ConfigMap类型
1. 点击需要部署 workloads 的集群ID，进入集群详情页面。
2. 点击 任意workloads类型 ，选择新建。
3. 根据指引设置 ConfigMap 类型数据卷参数，配置挂载点，完成创建。


![][MountConfigMap]

**方式二**： 环境变量中使用ConfigMap类型
1. 点击需要部署 workloads 的集群ID，进入集群详情页面。
2. 点击 任意workloads类型 ，选择新建。
3. 根据指引设置 ConfigMap 类型环境变量参数，完成创建。


![][EnvUseConfigMap]

#### 更新 ConfigMap
**方式一**：Yaml更新
1. 点击需要更新的 ConfigMap 的集群ID，进入集群详情页面。
2. 选择需要更新的 ConfigMap 详情页，点击Yaml tab, 可编辑Yaml直接更新

**方式一**：更新Key-values
1. 点击需要部署的 ConfigMap 的集群ID，进入集群详情页面。
2. 选择需要更新的 ConfigMap, 点击更新操作。

### kubectl 操作 ConfigMap 指引
#### Yaml示例
```Yaml
apiVersion: v1
data:
  key1: value1
  key2: value2
  key3: value3
kind: ConfigMap
metadata:
  name: test-config
  namespace: default
```
- data：ConfigMap 的数据，Key-value形式
- kind: 标识该资源是 ConfigMap 类型
- metadata：该 ConfigMap 的名称、Label等基本信息
- metadata.annotations: 对 ConfigMap 的额外说明，腾讯云TKE额外增强能力可以通过该参数设置。
#### 创建 ConfigMap
**方式一**：直接通过Yaml示例文件创建
1. 准备 StatefulSet Yaml文件， 例如上述文件为web.yaml
2. kubectl安装完成，并且已连接上集群（可直接登录集群节点使用kubectl）
3. 执行命令创建：
```shell
kubectl create -f web.yaml
```
4. 执行命令验证创建情况：
```shell
kubectl get StatefulSet
```

**方式二**：通过`kubectl create configmap <map-name> <data-source>`从目录中创建， key为文件名，Value为文件的内容。更多详情可查阅[Kubernetes configMap官方文档](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#create-a-configmap)


#### 使用 ConfigMap
**方式一**： 数据卷使用ConfigMap类型
Yaml示例：
```Yaml
apiVersion: v1
 kind: Pod
 metadata:
   name: nginx
 spec:
   containers:
     - name: nginx
       image: nginx:latest
       volumeMounts:
        name: config-volume
        mountPath: /etc/config
   volumes:
        name: config-volume
        configMap:
          name: test-config ## 设置ConfigMap来源
          ## items:  ## 设置指定ConfigMap的Key挂载
          ##   key: key1  ## 选择指定Key
          ##   path: keys ## 挂载到指定的子路径
   restartPolicy: Never
```
**方式二**： 环境变量中使用ConfigMap类型
Yaml示例：
```Yaml
apiVersion: v1
 kind: Pod
 metadata:
   name: nginx
 spec:
   containers:
     - name: nginx
       image: nginx:latest
       env:
         - name: key1
           valueFrom:
             configMapKeyRef:
               name: test-config ## 设置来源ConfigMap文件名
               key: test-config.key1  ## 设置该环境变量的Value来源项
   restartPolicy: Never
```


[createConfigMap]:https://main.qcloudimg.com/raw/f31c544f6e4a0d813d5df7d033d882c2.png

[EnvUseConfigMap]:https://main.qcloudimg.com/raw/379d16ccf3ecc3a8c9ab90664b74168b.png
[MountConfigMap]:https://main.qcloudimg.com/raw/ef5f69e7c4c8112d21f1c9ae59d32363.png
