## 操作场景

为提升函数上传效率，我们提供了默认使用 COS 上传函数的方式。您可在 SCF CLI 中开启“使用 COS 上传函数”功能，即可提升80%的上传效率，还能够领取 COS 代金券。



## 前提条件
- 请确保您当前使用的账户已完成了以下授权操作：
 1. 参考 [角色与授权](https://cloud.tencent.com/document/product/583/32389) 完成 SCF 默认角色配置。
 2. 新建角色 `QCS_SCFExcuteRole` ，并参考 [用户与权限](https://cloud.tencent.com/document/product/583/40142) 完成预设策略关联。
- 已完成 SCF CLI 的 [安装及配置](https://cloud.tencent.com/document/product/583/33449)。您可依次执行以下命令进行验证：
 1. 执行 `scf --version` 命令，确认是否安装。 
 2. 执行 `scf configure get` 命令，确认是否已完成配置。



## 操作步骤
### 开启 COS 上传
1. 执行以下命令，开启默认使用 COS 上传的功能。
```
scf configure set --using-cos y
```
2. 执行以下命令，查看是否开启默认使用 COS 上传功能。
```
scf configure get
```
返回类似如下信息，`using-cos` 为 `True` 则表示已开启。
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
1. 执行以下命令，在当前目录下创建 hello_world 函数。
>?如果您已经有创建好的云函数，请执行 [步骤2](#cd)。
>
```
scf init
```
2. [](id:cd)根据您的实际情况，执行以下命令进入对应的函数目录。
```
$ cd hello_world/
```
3. 执行以下命令，在您的腾讯云账号下创建 COS bucket ，并从该 bucket 拉取函数并部署。
```
$ scf deploy
```
>?成功部署函数后，SCF CLI 会在您的腾讯云账号下根据 CLI 配置信息自动创建 COS bucket。您可在返回信息中查看 bucket 名称，并前往对应地域下的 [存储桶列表](https://console.cloud.tencent.com/cos5/bucket) 查看。
>若 SCF CLI 未能自动创建 COS bucket，请您按照返回信息中的 bucket 名称，参考 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 在对应地域下创建同名 bucket，并再次执行命令部署函数。 



### 领取代金券

完成上述步骤后，即可前往 [SCF 控制台](https://console.cloud.tencent.com/scf/index?rid=16) 概览页顶部领取代金券。如下图所示：
![](https://main.qcloudimg.com/raw/31d5f34e82a7c8ff743c134641c3a296.png)
