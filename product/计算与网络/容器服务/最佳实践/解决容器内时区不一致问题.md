## 操作场景
腾讯云容器服务（TKE）集群中容器系统时间默认为 UTC 协调世界时间 （Universal Time Coordinated），与节点本地所属时区 CST （上海时间）相差8个小时。在容器使用过程中，当需要获取系统时间用于日志记录、数据库存储等相关操作时，容器内时区不一致问题将会带来一系列困扰。

默认时间不支持直接以集群为单位进行修改，但可在单个容器内进行修改。本文提供了容器内时区不一致问题的多种解决方案，请选择合适的方案进行操作：
- [方案1：Dockerfile 中创建时区文件（推荐）](#createDockerFile)
- [方案2：挂载主机时区配置到容器](#mount)

## 操作环境

本文中所有操作步骤均在 TKE 集群节点上完成，相关操作环境如下所示，请对应您实际情形结合文档解决问题：

| 角色 | 地域 | 配置 | 操作系统 | Kubernetes 版本信息 |
|---|---|---|---|---|
| 节点 | 华南地区（广州）| CPU：1核，内存:：1GB，带宽：1 Mbps<br>系统盘：50 GB（普通云硬盘） | CentOS Linux 7（Core）| 1.16.3 |


## 问题定位

1. 参考 [使用标准登录方式登录 Linux 实例（推荐）](https://cloud.tencent.com/document/product/213/5436)，登录目标节点。
2. 执行以下命令，查看本地时间。
```
date
```
返回结果如下图所示：
![](https://main.qcloudimg.com/raw/7c1572281bd2a07a6f98df1bb2bfe10e.png)
3. 依次执行以下命令，查看容器内 CentOS 系统默认时区。
```
docker run -it centos /bin/sh
```
```
date
```
返回结果如下图所示：
![](https://main.qcloudimg.com/raw/7c4dd6596c82992c209187eece347367.png)
对比发现，本地时间与容器内时区不一致。
4. 执行以下命令，退出容器。
```
exit
```

## 操作步骤

### 方案1：Dockerfile 中创建时区文件（推荐）<span id="createDockerFile"></span>

在构建基础镜像或在基础镜像的基础上制作自定义镜像时，在 Dockerfile 中创建时区文件即可解决单一容器内时区不一致问题，且后续使用该镜像时，将不再受时区问题困扰。

1. 执行以下命令，新建 Dockerfile.txt 文件。
```
vim Dockerfile.txt
```
2. 按 **i** 切换至编辑模式，写入以下内容，配置时区文件。
```
FROM centos
RUN rm -f /etc/localtime \
&& ln -sv /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
&& echo "Asia/Shanghai" > /etc/timezone
```
3. 按 **Esc**，输入 **:wq**，保存文件并返回。
4. 执行以下命令，构建容器镜像。
```
docker build -t centos7-test:v1 -f Dockerfile.txt .
```
返回结果如下图所示：
![](https://main.qcloudimg.com/raw/9e6594183e3f645eb90add73b9b99d50.png)
5. 依次执行以下命令，启动容器镜像并查看容器内时区。
```
date
```
```
docker run -it centos7-test:v1 /bin/sh
```
```
date
```
此时，容器内时区已与本地时间一致。如下图所示：
![](https://main.qcloudimg.com/raw/ecfd7efc0a235b1d3e0c996a618d79f4.png)
6. 执行以下命令，退出容器。
```
exit
```

### 方案2：挂载主机时区配置到容器<span id="mount"></span>
解决容器内时区不一致问题，还可以通过挂载主机时间配置到容器的方式进行解决。该方式可以在容器启动时进行设置，也可以在 YAML 文件中使用主机路径挂载数据卷到容器。



#### 容器启动时挂载主机时间配置到容器
挂载主机时间到容器内覆盖配置时，有以下两种选择：
- 挂载本地 `/etc/localtime`：需确保该主机时区配置文件存在且时区正确。
- 挂载本地 `/usr/share/zoneinfo/Asia/Shanghai`：当本地 `/etc/localtime` 不存在或者时区不正确时，可选择直接挂载该配置文件。

请对应实际情况，选择以下方式，进行挂载主机时间配置到容器：

- 方式1：挂载本地 `/etc/localtime`：
 1. 依次执行以下命令，查看本地时间并挂载本地 `/etc/localtime` 到容器内。
```
date
```
```
docker run -it -v /etc/localtime:/etc/localtime centos /bin/sh
```
```
date
```
返回结果如下图所示，容器内时区已与本地时间一致：
![](https://main.qcloudimg.com/raw/0387facb9f0fba5784a6d7e23ff8624a.png)
 2. 执行以下命令，退出容器。
```
exit
```

- 方式2： 挂载本地 `/usr/share/zoneinfo/Asia/Shanghai`：
 1. 依次执行以下命令，查看本地时间并挂载本地 `/usr/share/zoneinfo/Asia/Shanghai` 到容器内。
```
date
```
```
docker run -it -v /usr/share/zoneinfo/Asia/Shanghai:/etc/localtime centos /bin/sh
```
```
date
```
返回结果如下图所示，容器内时区已与本地时间一致：
![](https://main.qcloudimg.com/raw/d5c1e5507b768aa415badfce5d8c8faa.png)
 2. 执行以下命令，退出容器。
```
exit
```

#### YAML 文件使用主机路径挂载数据卷到容器

本节内容以 `mountPath:/etc/localtime` 为例，介绍在 YAML 文件中如何通过数据卷挂载主机时区配置到容器内，解决容器内时区不一致的问题。

1. 在节点上执行以下命令，创建 pod.yaml 文件。
```
vim pod.yaml
```
2. 按 **i** 切换至编辑模式，写入以下内容。
```yaml
apiVersion: v1
kind: Pod
metadata:
     name: test
     namespace: default
spec:
     restartPolicy: OnFailure
     containers:
     - name: nginx
       image: nginx-test
       imagePullPolicy: IfNotPresent
       volumeMounts:
       - name: date-config
         mountPath: /etc/localtime
       command: ["sleep", "60000"]
     volumes:
     - name: date-config
       hostPath:
         path: /etc/localtime
```
3. 按 **Esc**，输入 **:wq**，保存文件并返回。
4. 执行以下命令，新建该 Pod。
```
kubectl create -f  pod.yaml
```
返回结果如下图所示：
![](https://main.qcloudimg.com/raw/e4b977a6f370d3ea83f403bb30c7ae2c.png)
5. 依次执行以下命令，查看该容器内时区。
```
date
```
```
kubectl exec -it test date
```
返回结果如下图所示，与本地系统时区一致即为成功：
![](https://main.qcloudimg.com/raw/416b050b83d4888bb1a202aff234c39e.png)



　


