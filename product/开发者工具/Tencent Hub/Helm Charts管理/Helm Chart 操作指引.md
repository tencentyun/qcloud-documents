## 控制台操作指引
### 新建 Helm Chart
1. 前往 Tencent Hub 控制台。
2. 选择 Helm 仓库。
3. 单击新建，填写相关信息。
4. 完成。

### 上传 Helm Chart

>!上传的 Chart 包的以下描述文件决定 Chart 包上传到哪个仓库。
- Chart.yaml 是 Chart 的关键元数据描述文件，有几个关键的字段需要关注下：
  - name : Chart 的名称，Chart 上传后会使用该字段作为 Chart 的名称。
  - version : Chart 的版本，Chart 上传后会使用该字段作为 Chart 的版本号，如果有相同的版本号已经上传，将会覆盖之前上传的。
  - description : Chart 的简短描述。
- README.md 是 Chart 的说明文档，markdown 格式。

1. 前往 Tencent Hub 控制台。
2. 选择 Helm 仓库。
3. 单击上传，选择需要上传的 Chart 包。
4. 完成。



## 命令行操作指引
### 前置条件
1. 本地安装 Helm 客户端，更多可查看 [安装 Helm](https://docs.helm.sh/using_helm/#installing-helm)。
```shell
$ curl https://raw.githubusercontent.com/helm/helm/master/scripts/get > get_helm.sh
$ chmod 700 get_helm.sh
$ ./get_helm.sh
```

2. 本地 Helm 客户端添加 Tencent Hub 的 repo。
```shell
helm repo add mycharts https://hub.tencentyun.com/charts/mycharts --username myname --password mypassword
```
   - `mycharts` 替换为自己仓库的命名空间 (用户名或组织名)
   - `myname` 替换为 Tencent Hub 账号用户名
   - `mypassword` 替换为 Tencent Hub 账号密码

3. 安装 Tencent Hub 的 helm-push 插件。
```shell
helm plugin install https://github.com/imroc/helm-push
```

### 上传 Helm Chart
1. 上传 （文件夹）
```shell
helm push ./myapp mycharts
```

2. 上传 （压缩包）
```shell
helm push myapp-1.0.1.tgz mychart
```

### 下载 Helm Chart
1. 下载最新版
```shell
helm fetch mycharts/myapp
```

2. 下载指定版本
```shell
helm fetch mycharts/myapp --version 1.0.1
```










