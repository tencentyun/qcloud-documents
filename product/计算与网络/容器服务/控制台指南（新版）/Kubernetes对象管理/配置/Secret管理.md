## 简介
Secret 可用于存储密码、令牌、密钥等敏感信息，降低直接对外暴露的风险。Secret 是 key-value 类型的键值对，您可以通过控制台的 Kubectl 工具创建对应的 Secret 对象，也可以通过挂载数据卷、环境变量或在容器的运行命令中使用 Secret。

## Secret 控制台操作指引

### 创建 Secret
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 选择需要创建 Secret 的集群 ID，进入待创建 Secret 的集群管理页面。
3. 选择左侧导航栏中的**配置管理** > **Secret**，进入 Secret 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/de4fcb50d53db97af9f1d6ede08be1e1.png)
4. 单击**新建**，进入“新建Secret”页面。
5. 在“新建Secret”页面，根据实际需求，进行如下参数设置。如下图所示：
![](https://main.qcloudimg.com/raw/a0c5ec51165aa0cfff4bfbfc303246b7.png)
 - **名称**：请输入自定义名称。
 - **Secret类型**：提供**Opaque**和**Dockercfg**两种类型，请根据实际需求进行选择。
        - **Opaque**：适用于保存密钥证书和配置文件，Value 将以 base64 格式编码。
        - **Dockercfg**：适用于保存私有 Docker Registry 的认证信息。
 - **生效范围**：提供以下两种范围，请根据实际需求进行选择。
        - **存量所有命名空间**：不包括 kube-system、kube-public 和后续增量命名空间。
        - **指定命名空间**：支持选择当前集群下一个或多个可用命名空间。 
 - **内容**：根据不同的 Secret 类型，进行配置。
    - 当 Secret 类型为**Opaque**时：根据实际需求，设置变量名和变量值。
    - 当 Secret 类型为**Dockercfg**时：
 		 - 仓库域名：请根据实际需求输入域名或 IP。
 		 - 用户名：请根据实际需求输入第三方仓库的用户名。
 		 - 密码：请根据实际需求设置第三方仓库的登录密码。
>?如果本次为首次登录系统，则会新建用户，相关信息写入 `~/.dockercrg` 文件中。
6. 单击**创建 Secret**，即可完成创建。

### 使用 Secret
#### 方式一：数据卷使用 Secret 类型[](id:Volume)
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 选择需要部署 Workload 的集群 ID，进入待部署 Workload 的集群管理页面。
3. 在**工作负载**下，任意选择 Workload 类型，进入对应的信息页面。
例如，选择**工作负载** >**DaemonSet**，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/743aa4292e75f58e92033ee829d44cbb.png)
4. 单击**新建**，进入 “新建Workload” 页面。
5. 根据页面信息，设置工作负载名、命名空间等信息。并在 “数据卷” 中，单击**添加数据卷**。如下图所示：
![](https://main.qcloudimg.com/raw/15e95703427ae44a8bae6b608ee34101.png)
6. 选择**使用Secret**方式，填写名称，并单击**选择Secret**。如下图所示：
![](https://main.qcloudimg.com/raw/9b560e9458c2253ad422a163d59e8532.png)
7. 在弹出的“设置Secret”窗口中，配置挂载点，并单击**确认**。如下图所示：
![](https://main.qcloudimg.com/raw/ec9c1f5055eb5ed8779777efe4ce6f03.png)
 - **选择Secret**：根据实际需求进行。
 - **选项**：提供**全部**和**指定部分 Key**两种选择。
 - **Items**：当选择**指定部分 Key**选项时，可以通过添加 Item 向特定路径挂载，如挂载点是 `/data/config`，子路径是 `dev`，最终会存储在 `/data/config/dev` 下。
8. 单击**创建Workload**，完成创建。

#### 方式二：环境变量中使用 Secret 类型[](id:Environment)
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 单击需要部署 Workload 的集群 ID，进入待部署 Workload 的集群管理页面。
3. 在**工作负载**下，任意选择 Workload 类型，进入对应的信息页面。
例如，选择**工作负载** > **DaemonSet**，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/743aa4292e75f58e92033ee829d44cbb.png)
4. 单击**新建**，进入 “新建Workload” 页面。
5. 根据页面信息，设置工作负载名、命名空间等信息。并在“实例内容器”的“环境变量”中，单击**引用ConfigMap/Secret**。如下图所示：
![](https://main.qcloudimg.com/raw/f9ca9039ce314fe65a302963c2ddf254.png)
6. 选择**Secret**环境变量方式，并根据实际需求选择资源。如下图所示：
![](https://main.qcloudimg.com/raw/5ae67cf051ed20a4c1e509c3f7ac6fb9.png)
7. 单击**创建Workload**，完成创建。

#### 方法三：使用第三方镜像仓库时引用[](id:ThirdRepository)
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 选择需要部署 Workload 的集群 ID，进入待部署 Workload 的集群管理页面。
3. 在**工作负载**下，任意选择 Workload 类型，进入对应的信息页面。
例如，选择**工作负载** > **DaemonSet**，进入 DaemonSet 信息页面。如下图所示：
![](https://main.qcloudimg.com/raw/743aa4292e75f58e92033ee829d44cbb.png)
4. 单击**新建**，进入 “新建Workload” 页面。
5. 根据页面信息，设置工作负载名、命名空间等信息。单击本页面左下角**显示高级设置** 。
6. 单击**添加**，请根据实际情况选择dockercfg类型的Secret 。如下图所示：
![](https://main.qcloudimg.com/raw/e744a226a75914f8cccaec30da86d213.png)
7. 单击**创建Workload**，完成创建。

### 更新 Secret
1. 登录容器服务控制台，选择左侧导航栏中的 **[集群](https://console.cloud.tencent.com/tke2/cluster)**。
2. 选择需要更新 YAML 的集群 ID，进入待更新 YAML 的集群管理页面。
3. 选择**配置管理** > **Secret**，进入 Secret 信息页面。如下图所示：
![Secret](https://main.qcloudimg.com/raw/de4fcb50d53db97af9f1d6ede08be1e1.png)
4. 在需要更新 YAML 的 Secret 行中，单击**编辑YAML**，进入更新 Secret 页面。
5. 在“更新Secret”页面，编辑 YAML，并单击**完成**即可更新 YAML。
>? 如需修改 key-values，则编辑 YAML 中 data 的参数值，并单击**完成**即可完成更新。

## Kubectl 操作 Secret 指引

### 创建 Secret

#### 方式一：通过指定文件创建 Secret[](id:SpecifyFile)
1. 依次执行以下命令，获取 Pod 的用户名和密码。
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

#### 方式二：YAML 文件手动创建[](id:YamlManual)

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

#### 方式一： 数据卷使用 Secret 类型[](id:KubectlVolume)

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

#### 方式二： 环境变量中使用 Secret 类型[](id:KubectlEnvironment)

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

#### 方法三：使用第三方镜像仓库时引用[](id:KubectlThirdRepository)

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
   imagePullSecrets:
   - name: test-secret ## 设置来源 Secret 文件名
   restartPolicy: Never
```



