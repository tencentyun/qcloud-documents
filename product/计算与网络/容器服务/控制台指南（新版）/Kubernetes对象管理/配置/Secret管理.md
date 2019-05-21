## 简介
Secret 可用于存储密码、令牌、密钥等敏感信息，降低直接对外暴露的风险。 Secret 是有 key-value 类型的键值对，您可以通过控制台的 Kubectl 工具创建对应的 Secret 对象，也可以通过挂载数据卷、环境变量或在容器的运行命令中使用 Secret。

## Secret 控制台操作指引

### 创建 Secret

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要创建 Secret 的集群 ID，进入待创建 Secret 的集群管理页面。
4. 选择 “配置管理” > “Secret”，进入 Secret 信息页面。如下图所示：
![Secret](https://main.qcloudimg.com/raw/d532285897995fb337682512b875ffb9.png)
5. 单击【新建】，进入 “新建Secret” 页面。如下图所示：
![新建Secret](https://main.qcloudimg.com/raw/6c416a0e29de03e7a2057eafda2ca282.png)
6. 根据实际需求，设置 Secret 参数。关键参数信息如下：
 - 名称：自定义。
 - 命名空间：根据实际需求进行选择命名空间类型。
 - 内容：根据实际需求，设置变量名和变量值。
7. 单击【创建Secret】，完成创建。

### 使用 Secret

#### 方式一：数据卷使用 Secret 类型

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要部署 Workload 的集群 ID，进入待部署 Workload 的集群管理页面。
4. 在 “工作负载” 下，任意选择 Workload 类型，进入对应的信息页面。例如，选择 “工作负载” > “DaemonSet”，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/73b214fcb0cf26e569310894dd44c512.png)
5. 单击【新建】，进入 “新建Workload” 页面。
6. 根据页面信息，设置工作负载名、命名空间等信息。并在 “数据卷” 中，单击【添加数据卷】，添加数据卷。如下图所示：
![添加数据卷](https://main.qcloudimg.com/raw/2e036dc898bd3fecfc59edd8742ff18a.png)
7. 选择 “使用Secret” 方式，填写名称，单击【选择Secret】。如下图所示：
![使用Secret](https://main.qcloudimg.com/raw/f4274791b9d489b1543935ef7cc01985.png)
8. 在弹出的 “设置Secret” 窗口中，配置挂载点，单击【确认】。
9. 单击【创建Workload】，完成创建。

#### 方式二：环境变量中使用 Secret 类型

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要部署 Workload 的集群 ID，进入待部署 Workload 的集群管理页面。
4. 在 “工作负载” 下，任意选择 Workload 类型，进入对应的信息页面。例如，选择 “工作负载” > “DaemonSet”，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/73b214fcb0cf26e569310894dd44c512.png)
5. 单击【新建】，进入 “新建Workload” 页面。
6. 根据页面信息，设置工作负载名、命名空间等信息。并在 “实例内容器” 的 “环境变量” 中，单击【引用ConfigMap/Secret】。如下图所示：
![引用ConfigMap/Secret](https://main.qcloudimg.com/raw/0422b13b4b4d547799d643a34f466340.png)
7. 选择 “Secret” 环境变量方式，并根据实际需求选择资源。如下图所示：
![](https://main.qcloudimg.com/raw/e9df219376365ad32a78bff58b82cf8f.png)
9. 单击【创建Workload】，完成创建。

### 更新 Secret

1. 登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)。
2. 在左侧导航栏中，单击【集群】，进入集群管理页面。
3. 单击需要更新 YAML 的集群 ID，进入待更新 YAML 的集群管理页面。
4. 选择 “配置管理” > “Secret”，进入 Secret 信息页面。如下图所示：
![Secret](https://main.qcloudimg.com/raw/d532285897995fb337682512b875ffb9.png)
5. 在需要更新 YAML 的 Secret 行中，单击【编辑YAML】，进入更新 Secret 页面。
6. 在 “更新Secret” 页面，编辑 YAML，单击【完成】，即可更新 YAML。
 >? 如需修改 key-values，编辑 YAML 中 data 的参数值，单击【完成】，即可完成更新。

## Kubectl 操作 Secret 指引

### 创建 Secret

#### 方式一：通过指定文件创建 Secret

1. 执行以下命令，获取 Pod 的用户名和密码。
```shell
$ echo -n 'username' > ./username.txt
$ echo -n 'password' > ./password.txt
```
2. 执行 Kubectl 命令，创建 Secret。
```shell
$ kubectl create secret generic test-secret --from-file=./username.txt --from-file=./password.txt
secret "testSecret" created
```
3. 执行以下命令，查看 Secret 详情。
```
kubectl describe secrets/ test-secret
```

#### 方式二：YAML 文件手动创建

>? 通过 YAML 手动创建 Secret，需提前将 Secret 的 data 进行  Base64 编码。

```Yaml
apiVersion: v1
kind: Secret
metadata:
  name: test-secret
type: Opaque
data:
  username: dXNlcm5hbWU=  ## 由echo -n 'username' | base64生成
  password: cGFzc3dvcmQ=  ## 由echo -n 'password' | base64生成
```

### 使用 Secret

#### 方式一： 数据卷使用 Secret 类型

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
        name: secret-volume
        mountPath: /etc/config
   volumes:
        name: secret-volume
        secret:
          name:  test-secret ## 设置 secret 来源
          ## items:  ## 设置指定 secret的 Key 挂载
          ##   key: username  ## 选择指定 Key
          ##   path: group/user ## 挂载到指定的子路径
          ##   mode: 256  ## 设置文件权限
   restartPolicy: Never
```

#### 方式二： 环境变量中使用 Secret 类型

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
         - name: SECRET_USERNAME
           valueFrom:
             secretKeyRef:
               name: test-secret ## 设置来源 Secret 文件名
               key: username  ## 设置该环境变量的 Value 来源项
   restartPolicy: Never
```
