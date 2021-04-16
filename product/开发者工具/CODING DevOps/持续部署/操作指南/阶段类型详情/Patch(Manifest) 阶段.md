本文为您详细介绍 CODING 持续部署中部署流程的 Patch (Manifest) 阶段。

## 前提条件

使用 CODING 持续部署的前提是，您的腾讯云账号需要开通 CODING DevOps 服务，详情请参见 [开通服务](https://cloud.tencent.com/document/product/1159/44859)。 

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击工作台首页左侧的 <img src ="https://main.qcloudimg.com/raw/12230547b45d5eae85ad1c4fa86fba68.png" style ="margin:0" data-nonescope="true">，进入持续部署控制台。

### 功能说明

本文档将会介绍如何在 `Patch(Manifest)` 阶段更新 Kubernetes 资源对象。将会包含以下几个操作说明：

- 指定更新的 manifest
- 指定更新内容
- （可选）在更新内容里覆盖制品
- （可选）覆盖特定的选项

### 指定更新的资源

1. 在阶段下拉列表中选择【Patch(Manifest)】。
![](https://main.qcloudimg.com/raw/57092acf199afb377dc5ae93e30fdc0a.png)
2. 指定更新的 Kubernetes 资源，需要配置如下字段：
	- 云账号：管理 Kubernetes 资源的云账号。
	- Namespace：资源所在的命名空间。
	- 资源类型（如 Deployment、Service 等）。
	- 名称：资源名称。

### 指定更新的内容

更新内容与 [Deploy(Manifest)](https://cloud.tencent.com/document/product/1159/47747) 类似。与部署阶段不同的是，更新阶段的内容只需填写更新的资源清单即可，不必提供所有资源的清单。根据不同需求，Patch 内容有两种提供方式：

- 静态：直接在阶段配置中填写。
- 动态：运行时绑定制品。

### 指定静态内容

您可以在阶段配置中直接输入 YAML 配置。例如给 manifest 添加新标签：

```yaml
metadata:
  labels:
    foo: bar
```

![](https://main.qcloudimg.com/raw/d6eece554bd482e0e1c59e75ab9c2962.png)

### 动态绑定

与 [Deploy(Manifest)](https://cloud.tencent.com/document/product/1159/47747) 类似，您可以引用外部的 manifest 作为制品，制品必须是包含 patch 内容的文本文件。

假设您在部署流程中声明了 Patch(Manifest) 阶段需要引用的制品，那么在 Patch(Manifest) 阶段可以通过如下配置引用：
![](https://main.qcloudimg.com/raw/384d5ecd94a5616a57f6535c2fb1e185.png)

### 覆盖制品

当对 Kubernetes 资源对象使用 strategic 或 merge strategy 方式进行 Patch 操作时, Patch(Manifest) 阶段可以像部署阶段一样配置覆盖制品。

例如，假设部署流程中有如下 manifest 内容的更新阶段：

```groovy
spec:
  template:
    spec:
      containers:
        -   name: my-container
          image: lhkprod-docker.pkg.coding.net/cd-demo/release/nginx
```

假设您更新了 Docker 镜像 tag（my-image:2.0），并上传镜像至 Docker 仓库触发部署流程执行，Spinnaker 将会使用新版本的 Docker 镜像覆盖掉旧版本：

```dockerfile
#...rest of manifest
containers:
  - name: my-container
    image: lhkprod-docker.pkg.coding.net/cd-demo/release/nginx:2.0
```

### 指定更新选项

- 记录更新注解
默认是 `true`。此选项勾选后，Kubernetes 将会使用注解 `kubernetes.io/change-cause` 将更新的操作与内容记录至被更新的资源中。
- 策略合并
`strategic`：默认选项。它是自定义版本的 JSON 合并更新，允许 Kubernetes 对象基于结构标签替换或者合并。当您需要在 pod spec 列表中添加注解、标签或容器而不是替换时非常有用。

`json`：使用标准的 [RFC 6902 JSON patch](https://tools.ietf.org/html/rfc6902) 更新 manifest。
`merge`：使用 [RFC 7386 JSON Merge Patch](https://tools.ietf.org/html/rfc7386) 更新 manifest。


