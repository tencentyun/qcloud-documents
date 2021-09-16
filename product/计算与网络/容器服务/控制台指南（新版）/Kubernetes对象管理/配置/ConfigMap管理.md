## 简介

通过 ConfigMap 您可以将配置和运行的镜像进行解耦，使得应用程序有更强的移植性。ConfigMap 是有 key-value 类型的键值对，您可以通过控制台的 Kubectl 工具创建对应的 ConfigMap 对象，也可以通过挂载数据卷、环境变量或在容器的运行命令中使用 ConfigMap。


## ConfigMap 控制台操作指引

### 创建 ConfigMap
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击**集群**，进入集群列表页。
3. 单击需要创建 ConfigMap 的集群 ID，进入集群管理页面。
4. 选择 **配置管理** > **ConfigMap**，进入 ConfigMap 信息页面。
5. 单击**新建**，进入 “新建ConfigMap” 页面。
6. 根据实际需求，设置 ConfigMap 参数。关键参数信息如下：
 - 名称：自定义。
 - 命名空间：根据实际需求进行选择命名空间类型，定义变量名和变量值。
7. 单击**创建ConfigMap**，完成创建。

### 使用 ConfigMap

#### 方式一：数据卷使用 ConfigMap 类型
1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中单击**集群**，进入集群列表页。
3. 单击需要部署 Workload 的集群 ID，进入集群管理页面。
4. 在 “工作负载” 下，任意选择 Workload 类型，进入对应的信息页面。例如，选择**工作负载** > **DaemonSet**，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/71e5e1f1c03b60792c9c3232ab6bc088.png)
5. 单击**新建**，进入 “新建Workload” 页面。
6. 根据页面信息，设置工作负载名、命名空间等信息。并在 “数据卷” 中，单击**添加数据卷**，添加数据卷。如下图所示：
![添加数据卷](https://main.qcloudimg.com/raw/2e036dc898bd3fecfc59edd8742ff18a.png)
7. 选择 “使用ConfigMap” 方式，填写名称，单击**选择配置项**。如下图所示：
![](https://main.qcloudimg.com/raw/2647c950bda4780a0e254acc9fe10f94.png)
8. 在弹出的 “设置ConfigMap” 窗口中，参考以下信息配置挂载点，并单击**确认**。如下图所示：
 - **选择ConfigMap**：根据实际需求进行选择。
 - **选项**：提供“全部”和“指定部分Key”两种选择。
 - **Items**：当选择“指定部分Key”选项时，可以通过添加 item 向特定路径挂载，如挂载点是 /data/config，文件名是 filename，最终会该键值对的值会存储在 /data/config/filename 下。
![](https://main.qcloudimg.com/raw/0983836264d6d6434eb501adba7ba906.png)
9. 单击**创建Workload**，完成创建。

#### 方式二： 环境变量中使用 ConfigMap 类型

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击**集群**，进入集群列表页。
3. 单击需要部署 Workload 的集群 ID，进入待部署 Workload 的集群管理页面。
4. 在 “工作负载” 下，任意选择 Workload 类型，进入对应的信息页面。例如，选择**工作负载** > **DaemonSet**，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/71e5e1f1c03b60792c9c3232ab6bc088.png)
5. 单击**新建**，进入 “新建Workload” 页面。
6. 根据页面信息，设置工作负载名、命名空间等信息。并在 “实例内容器” 的 “环境变量” 中，单击**新增变量**。如下图所示：
![](https://main.qcloudimg.com/raw/48f6735d3be0ec6aa426dc78a317418e.png)
7. 选择 “ConfigMap” 环境变量方式，并根据实际需求选择资源。
9. 单击**创建Workload**，完成创建。

### 更新 ConfigMap

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击**集群**，进入集群列表页。
3. 单击需要更新 ConfigMap 的集群 ID，进入集群管理页面。
4. 选择 **配置管理** > **ConfigMap**，进入 ConfigMap 信息页面。
5. 在需要更新的 ConfigMap 行中，单击右侧的**更新配置**，进入更新 ConfigMap 页面。
![](https://main.qcloudimg.com/raw/2bfb0d32ab85682548a598175e1bbe19.png)
7. 在 “更新配置” 页面，编辑 key-value 类型的键值对，单击**完成**。
![](https://main.qcloudimg.com/raw/91790cab3cb4ebd35c0354cd555ae60a.png)





## Kubectl 操作 ConfigMap 指引

### YAML 示例
<dx-codeblock>
::: Yaml
apiVersion: v1
data:
  key1: value1
  key2: value2
  key3: value3
kind: ConfigMap
metadata:
  name: test-config
  namespace: default
:::
</dx-codeblock>

- **data**：ConfigMap 的数据，以 key-value 形式呈现。
- **kind**：标识 ConfigMap 资源类型。
- **metadata**：ConfigMap 的名称、Label等基本信息。
- **metadata.annotations**：ConfigMap 的额外说明，可通过该参数设置腾讯云 TKE 的额外增强能力。

### 创建 ConfigMap

#### 方式一：通过 YAML 示例文件方式创建

1. 参考 [YAML 示例](#YAMLSample)，准备 ConfigMap YAML 文件。
2. 安装 Kubectl，并连接集群。操作详情请参考 [通过 Kubectl 连接集群](https://cloud.tencent.com/document/product/457/8438)。
3. 执行以下命令，创建 ConfigMap YAML 文件。
```shell
kubectl create -f ConfigMap YAML 文件名称
```
 例如，创建一个文件名为 web.yaml 的 ConfigMap YAML 文件，则执行以下命令：
```shell
kubectl create -f web.yaml
```
4. 执行以下命令，验证创建是否成功。
```shell
kubectl get configmap
```
 返回类似以下信息，即表示创建成功。
```
NAME          DATA      AGE
test          2         39d
test-config   3         18d
```


#### 方式二：通过执行命令方式创建

执行以下命令，在目录中创建 ConfigMap。
```
kubectl create configmap <map-name> <data-source>
```
- &lt;map-name&gt;：表示 ConfigMap 的名字。
- &lt;data-source&gt;：表示目录、文件或者字面值。

更多参数详情可参见 [Kubernetes configMap 官方文档](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/#create-a-configmap)。

### 使用 ConfigMap

#### 方式一：数据卷使用 ConfigMap 类型

YAML 示例如下：
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
          name: test-config ## 设置 ConfigMap 来源
          ## items:  ## 设置指定 ConfigMap 的 Key 挂载
          ##   key: key1  ## 选择指定 Key
          ##   path: keys ## 挂载到指定的子路径
   restartPolicy: Never
```

#### 方式二：环境变量中使用 ConfigMap 类型

YAML 示例如下：
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
               name: test-config ## 设置来源 ConfigMap 文件名
               key: test-config.key1  ## 设置该环境变量的 Value 来源项
   restartPolicy: Never
```
