本文为您详细介绍 CODING 持续部署中 Kubernetes 场景下的制品。

## 前提条件

使用 CODING 持续部署的前提是，您的腾讯云账号需要开通 CODING DevOps 服务，详情请参见 [开通服务](https://cloud.tencent.com/document/product/1159/44859)。 

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击工作台首页左侧的 <img src ="https://main.qcloudimg.com/raw/12230547b45d5eae85ad1c4fa86fba68.png" style ="margin:0" data-nonescope="true">，进入持续部署控制台。

### 功能介绍

制品在 Kubernetes 资源对象的部署中扮演中重要的角色，您在 manifest 文件中引用的如 Docker 镜像或 ConfigMap 都可以通过制品来进行绑定部署。

### 将 Manifest 作为制品

有两种方法可以部署 manifest：

- manifest 以静态的方式（text格式）提供给部署流程
- manifest 作为制品提供给部署流程

下图展示了在 Deploy 阶段中部署存储于 CODING 代码仓库的 manifest：
![](https://main.qcloudimg.com/raw/e7216428ebf188a368db0c4866756229.png)

### 在 manifest 中绑定制品

通常来说，制品表示用户在部署流程部署中需要更新的资源。诸如 Docker 镜像和 ConfigMaps 这类通过 manifest 更新的资源类型，CODING 部署控制台（Spinnaker）提供了一种简单的方式将其注入到 manifest 文件中。

在 manifest 中绑定制品的过程中，CODING 部署控制台使用了一个便捷的规则实现。即当 manifest 中资源对象的 `type` 和 `value` 与制品的 `type` 和 `name` 分别匹配时，manifest 中的 `value` 将会被制品的 `reference` 替换。

`manifest 中资源对象的 type` 具体来说就是 `spec.template.spec.containers.*.image` 中所引用的 Docker 镜像，因此将匹配 `docker/image` 类型的制品。

`spec.template.spec.volumes.*.configMap.name` 引用 `ConfigMap`，因此将匹配 `kubernetes/configMap` 类型的制品。 

它们的实现过程原理如下：

首先在部署流程中定义了需要部署的 manifest 内容：

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - image: lhkprod-docker.pkg.coding.net/cd-demo/release/nginx # possible artifact
          name: nginx
          ports:
            - containerPort: 80
          volumeMounts:
            - mountPath: /opt/config
              name: my-config-map
      volumes:
        - configMap:
            name: configmap             # possible artifact
          name: my-config-map
```

当部署阶段执行时，如果执行上下文中有如下的制品（制品可能来自触发器或之前的部署过程），代码如下：

```
[
  {
    "type": "docker/image",
    "name": "lhkprod-docker.pkg.coding.net/cd-demo/release/nginx",
    "reference": "lhkprod-docker.pkg.coding.net/cd-demo/release/nginx@sha256:0cce25b9a55"
  },
  {
    "type": "kubernetes/configMap",
    "name": "configmap",
    "version": "v001",
    "location": "default",
    "reference": "configmap-v001"
  }
]
```

则 ConfigMap 和 Docker 镜像将会被上下文中的制品替换，最终被部署到集群的 manifest 内容为：

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: nginx
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - image: lhkprod-docker.pkg.coding.net/cd-demo/release/nginx@sha256:0cce25b9a55    # bound by spinnaker
          name: nginx
          ports:
            - containerPort: 80
          volumeMounts:
            - mountPath: /opt/config
              name: my-config-map
      volumes:
        - configMap:
            name: configmap-v001                              # bound by spinnaker
          name: my-config-map
```

