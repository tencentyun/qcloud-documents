## Helm Charts操作指引
### 控制台操作指引
#### 新建Helm Chart
1. 前往TencentHub控制台
2. 选择Helm仓库
3. 点击新建, 填写相关信息
4. 完成

#### 上传Helm Chart

>注:上传的Chart包的以下描述文件决定Chart包上传到哪个仓库。
- Chart.yaml 是 Chart 的关键元数据描述⽂文件，有⼏几个关键的字段需要关注下：
  - name : Chart 的名称，Chart 上传后会使⽤用该字段作为 Chart 的名称
  - version : Chart 的版本，Chart 上传后会使⽤用该字段作为 Chart 的版本号，如果有相同的版本号已经上传，将会覆盖之前上传的
  - description : Chart 的简短描述
- README.md 是 Chart 的说明⽂文档，markdown 格式

1. 前往TencentHub控制台
2. 选择Helm仓库
3. 点击上传，选择需要上传的Chart包。
4. 完成



### 命令行操作指引
#### 前置条件
1. 本地安装Helm 客户端, 更多可查看[Helm官方文档-安装Helm](https://docs.helm.sh/using_helm/#installing-helm)
```shell
$ curl https://raw.githubusercontent.com/helm/helm/master/scripts/get > get_helm.sh
$ chmod 700 get_helm.sh
$ ./get_helm.sh
```

2. 本地Helm客户端添加TencentHub的repo
```shell
helm repo add mycharts https://hub.tencentyun.com/charts/mycharts --username myname --password mypassword
```
   - `mycharts` 替换为自己仓库的命名空间 (用户名或组织名)
   - `myname` 替换为 tencenthub 账号用户名
   - `mypassword` 替换为 tencenthub 账号密码

3. 安装 tencenthub 的 helm-push 插件
```shell
helm plugin install https://github.com/imroc/helm-push
```

#### 上传Helm Chart
1. 上传 (文件夹)：
```shell
helm push ./myapp mycharts
```

2. 上传 (压缩包)：
```shell
helm push myapp-1.0.1.tgz mychart
```

#### 下载Helm Chart
1. 下载最新版：
```shell
helm fetch mycharts/myapp
```

2. 下载指定版本：
```shell
helm fetch mycharts/myapp --version 1.0.1
```
