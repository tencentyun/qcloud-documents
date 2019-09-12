## 操作场景

为提升函数上传效率，我们提供了默认使用 COS 上传函数的方式。您可在 SCF CLI 中开启“使用 COS 上传函数”功能，即可提升80%的上传效率，还能够领取 COS 代金券。



## 前提条件
已完成 SCF CLI 的 [安装及配置 ](https://cloud.tencent.com/document/product/583/33449) 。您可依次执行以下命令进行验证：
- 执行 `scf --version` 命令，确认是否安装 
- 执行 `scf configure get` 命令，确认是否已完成配置。



## 操作步骤
### 开启 COS 上传
1. 执行以下命令，开启默认使用 COS 上传的功能
```
scf configure set --using-cos y
```
2. 执行以下命令，查看是否开启默认使用 COS 上传功能。
```
scf configure get
```
查看输出信息中的 `using-cos` 是否为 `True`，显示如下，则已开启。
```bash
$ scf configure get
[>] USER_1
[>] appid = 1255721742
[>] region = ap-guangzhou
[>] secret-id = ********************************cEr7
[>] secret-key = ****************************mkYA
[>] using-cos = True (By default, it is deployed by COS.)
[>] python2-path = None
[>] python3-path = None
[>] no-color = False
```

### 部署函数
>?如果您已经有创建好的云函数，请执行 [步骤2](#cd)。
>
1. 执行以下命令，初始化示例项目 hello_world。
```
scf init
```
2. <span id="cd"></span>执行以下命令，根据您的实际情况进入对应的项目目录。
```
$ cd hello_world/
```
3. 执行以下命令，CLI 会默认在您的腾讯云账号下创建 COS bucket ，并从该 bucket 拉取函数并部署。
```
$ scf deploy
```


### 领取代金券

完成上述步骤后，即可前往 [SCF 控制台](https://console.cloud.tencent.com/scf/index?rid=16) 概览页顶部领取代金券。如下图所示：
![](https://main.qcloudimg.com/raw/31d5f34e82a7c8ff743c134641c3a296.png)
