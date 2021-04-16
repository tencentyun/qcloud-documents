本文为您详细介绍 CODING 持续部署中的部署（Manifest）阶段。

## 前提条件

使用 CODING 持续部署的前提是，您的腾讯云账号需要开通 CODING DevOps 服务，详情请参见 [开通服务](https://cloud.tencent.com/document/product/1159/44859)。 

## 进入项目

1. 登录 [CODING 控制台](https://console.cloud.tencent.com/coding)，单击团队域名进入 CODING 使用页面。
2. 单击工作台首页左侧的 <img src ="https://main.qcloudimg.com/raw/12230547b45d5eae85ad1c4fa86fba68.png" style ="margin:0" data-nonescope="true">，进入持续部署控制台。

### 功能介绍

该阶段包含两个主要的步骤：

- 指定要部署的 manifest。
- 在 manifest 中指定需要覆盖的制品（如 Docker 镜像）。该步骤为可选项，您可以在阶段执行时指定需要覆盖的制品。

### 配置 manifest

根据实际的生产需求，有两个方法可以指定 manifest：

- 静态：直接在部署流程中指定。
- 动态：运行时使用绑定的制品。

不管使用何种方式，都需要先选择【部署（Manifest）】阶段：
![](https://main.qcloudimg.com/raw/2e04335f135cbfae3070063a02b5051d.png)

### 配置静态的 manifest

如果您预知即将部署的资源所对应的 manifest，那么可以在 Deployment(Manifest) 阶段配置中直接提供 manifest 纯文本内容。选择【输入内容】选项后，可以在文本框直接编辑 YAML 文件内容。

![](https://main.qcloudimg.com/raw/9042a19577770aff9e8fef1bc0237e8b.png)

如果使用了 JSON 定义的部署流程，则对应的内容如下：

```json
{
  "name": "Deploy my manifest",   // human-readable name
  "type": "deployManifest",       // tells orchestration engine what to run
  "account": "nudge",             // account (k8s cluster) to deploy to
  "cloudProvider": "kubernetes",
  "source": "text",
  "manifest": {
                                  // manifest contents go here
  }
}
```

### 配置动态的 manifests

如果需要引用外部仓库的 manifest，或者当部署阶段需要同时部署多个制品时，可以通过绑定制品来配置 manifest。

CODING 持续部署的制品允许您引用任何远程的可部署资源。部署（Manifest） 阶段所引用的制品必须是 manifest 文件，一般存储于 Git 仓库（如 CODING 代码仓库）。如果您已经在上游阶段声明了「启动所需制品」，那么可以在 部署（Manifest） 阶段进行引用。

上游阶段可能会匹配到多个制品，例如配置正则表达式 .*\yml，将所有 yml 文件作为制品，部署（Manifest） 阶段执行时会部署所有匹配到的 yml 文件。
![](https://main.qcloudimg.com/raw/86fca63feca1affb8cdacf2b0cadf4fa.png)

>! 制品来源勾选使用制品后，您可以自行选择部署上游所提供的制品，请确保云账号拥有下载制品的权限。

### 覆盖制品

通常情况下，当我们对 Kubernetes 资源进行部署更新操作时，大多数的变更都会涉及到 Docker 镜像或 ConfigMap 中的 flag。因此，CODING CD 针对这些资源类型的变更提供了优秀的适配性支持。

- Docker 镜像
- Kubernetes ConfigMap
- Kubernetes Secret

如果上游阶段的部署流程中存在这些资源对象，CODING CD 将会尝试自动将它们注入到正在部署的 manifest 文件中。

例如，假设 Docker 镜像仓库类型的触发器触发部署流程执行，并且触发器携带了镜像`lhkprod-docker.pkg.coding.net/cd-demo/release/nginx`，其 digest 值为`sha256:c81e41ef5e...`。在部署流程中，您配置了内容如下的部署阶段。

```dockerfile
# ... rest of manifest
  containers:
  - name: my-container
    image: lhkprod-docker.pkg.coding.net/cd-demo/release/nginx
# rest of manifest ...
```

因为部署流程是由 Docker 镜像内容变更所触发，所以部署流程编排引擎会将 Docker 镜像制品连同部署阶段中的 manifest 一起派发给`clouddriver`组件处理。最终得到部署的 manifest 内容如下。

```dockerfile
# ... rest of manifest
  containers:
  - name: my-container
    image: lhkprod-docker.pkg.coding.net/cd-demo/release/nginx@:sha256:c81e41ef5e...
# rest of manifest ...
```

为了确保部署阶段获取到正确的制品，您可以强制阶段绑定所有需要的制品，如果绑定失败，阶段将执行失败。以下配置的含义是 Docker 镜像`lhkprod-docker.pkg.coding.net/cd-demo/release/nginx`必须被绑定到 manifest，否则阶段将会执行失败。
![](https://main.qcloudimg.com/raw/d4099adb8f05dbf171fc19fbaaf0e4a2.png)

