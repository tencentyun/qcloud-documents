## Secret 管理
### Secret 简介
Secret 可用于存储密码、令牌、密钥等敏感信息，降低直接对外暴露的风险。 Secret 是有key-value类型的键值对，您可以通过控制台会kubectl工具创建对应的 Secret 对象。 可通过挂载数据卷或环境变量或在容器的运行命令中使用 Secret. 修改 Secret 对象，使用该对象的工作负载配置也生效。

### Secret 控制台操作指引
#### 创建 Secret
1. 点击需要部署创建 Secret 的集群ID，进入集群详情页面。
2. 点击创建 Secret 选项，选择新建创建 Secret
3. 根据指引设置创建 Secret 参数，完成创建。

![][createSecret]

#### 使用 Secret
**方式一**： 数据卷使用 Secret 类型
1. 点击需要部署 workloads 的集群ID，进入集群详情页面。
2. 点击 任意workloads类型 ，选择新建。
3. 根据指引设置 Secret 类型数据卷参数，配置挂载点，完成创建。

![][MountSecret]

**方式二**： 环境变量中使用 Secret 类型
1. 点击需要部署 workloads 的集群ID，进入集群详情页面。
2. 点击 任意workloads类型 ，选择新建。
3. 根据指引设置 Secret 类型环境变量参数，完成创建。

![][EnvUseSecret]

#### 更新 Secret
**方式一**：Yaml更新
1. 点击需要部署的 Secret 的集群ID，进入集群详情页面。
2. 选择需要更新的 Secret 详情页，点击Yaml tab, 可编辑Yaml直接更新

**方式一**：更新Key-values
1. 点击需要更新的 Secret 的集群ID，进入集群详情页面。
2. 选择需要更新的 Secret, 点击更新操作。

### kubectl 操作 Secret 指引
#### 创建 Secret
**方式一：** 通过指定文件创建Secret
1. pod应使用的用户名和密码位于文件 ./username.txt和./password.txt本地计算机上。
```shell
$ echo -n 'username' > ./username.txt
$ echo -n 'password' > ./password.txt
```
2. 通过Kubectl命令创建Secret
```shell
$ kubectl create secret generic test-secret --from-file=./username.txt --from-file=./password.txt
secret "testSecret" created
```
3. 通过`kubectl describe secrets/ test-secret`查看Secret详情。

**方式二：** YAML文件手动创建. 注通过Yaml手动创建需提交把secret的data进行Bash64编码。
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

#### 使用 Secret
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
        name: secret-volume
        mountPath: /etc/config
   volumes:
        name: secret-volume
        secret:
          name:  test-secret ## 设置Csecret来源
          ## items:  ## 设置指定secret的Key挂载
          ##   key: username  ## 选择指定Key
          ##   path: group/user ## 挂载到指定的子路径
          ##   mode: 256  ## 设置文件权限
   restartPolicy: Never
```
**方式二**： 环境变量中使用secret类型
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
         - name: SECRET_USERNAME
           valueFrom:
             secretKeyRef:
               name: test-secret ## 设置来源ConfigMap文件名
               key: username  ## 设置该环境变量的Value来源项
   restartPolicy: Never
```

[createSecret]:https://main.qcloudimg.com/raw/59ff7b249f2baa37f118d969d1f11411.png
[MountSecret]:https://main.qcloudimg.com/raw/ead5a7a8afbc05719f9809253ee826b8.png
[EnvUseSecret]:https://main.qcloudimg.com/raw/4c9541782d6ac54a711f128d0ea7f859.png
