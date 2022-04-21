本文指导您如何配置初始化 TCCLI，包括如何使用交互模式、命令行模式进行初始化，以及如何进行账户切换。


## 前提条件
已安装 TCCLI，详情请参见 [安装 TCCLI](https://cloud.tencent.com/document/product/440/34011)。

## 操作步骤

使用 TCCLI 前您需要进行一些初始化配置，使其完成使用云 API 的必要前提条件。


<dx-alert infotype="explain" title="">
下文中 secretId、secretKey、地域等信息仅作为实例，请以实际情况为准。
</dx-alert>


#### 交互模式

您可以通过执行 `tccli configure` 命令进入交互模式快速配置。
```bash
$ tccli configure
TencentCloud API secretId [*afcQ]:AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******
TencentCloud API secretKey [*ArFd]:Gu5t9xGARNpq86cd98joQYCN3*******
region: ap-guangzhou
output[json]:
```
- **secretId**：云 API 密钥 SecretId，前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取。
- **secretKey**：云 API 密钥 SecretKey，前往 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 获取。
- **region**： 云产品地域，请前往对应云产品的 [API 文档](https://cloud.tencent.com/document/api) 获取可用的 region。例如云服务器的 [地域列表](https://cloud.tencent.com/document/api/213/15692#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。
-	**output**： 可选参数，请求回包输出格式，支持 [json table text] 三种格式，默认为 json。
	更多信息请执行 `tccli configure help` 查看。
	

	
#### 命令行模式
通过命令行模式您可以在自动化脚本中配置您的信息。
```bash
# set 子命令可以设置某一配置，也可同时配置多个
$ tccli configure set secretId AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******
$ tccli configure set region ap-guangzhou  output json
# get 子命令用于获取配置信息
$ tccli configure get secretKey
secretKey = Gu5t9xGARNpq86cd98joQYCN3*******
# list 子命令打印所有配置信息
$ tccli configure list
credential:
secretId =  AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******
secretKey =  Gu5t9xGARNpq86cd98joQYCN3*******
configure:
region =  ap-guangzhou
output =  json
# 在命令行中直接指定secretId和secretKey的值，如查询cvm实例信息：
$ tccli cvm DescribeInstances --secretId AKIDz8krbsJ5yKBZQpn74WFkmLPx3****** --secretKey Gu5t9xGARNpq86cd98joQYCN3*******
```

#### 多账户支持
TCCLI 支持多账户，方便您多种配置同时使用。
```bash
# 在交互模式中指定账户名 test
$ tccli configure --profile test
TencentCloud API secretId [*BCDP]:AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******
TencentCloud API secretKey [*ArFd]:Gu5t9xGARNpq86cd98joQYCN3*******
region: ap-guangzhou
output[json]:
# set/get/list 子命令指定账户名 test
$ tccli configure set region ap-guangzhou  output json  --profile test
$ tccli configure get secretKey      --profile test
$ tccli configure list      --profile test
# remove 子命令删除指定账户的配置文件。当 remove 子命令不指定账户名时，会删除 default 配置文件。
$ tccli configure remove -profile test
# 在调用接口时指定账户（以 cvm DescribeZones 接口为例）
$ tccli cvm DescribeZones --profile test
```

#### TCCLI 配置文件
 - 使用 `tccli configure` 命令后，TCCLI 会在 `~/.tccli` 目录下生成对应的 `default.configure` 和 `default.credential` 文件，这两个文件记录均为 JSON 格式的内容。
 `default.configure` 记录对应产品调用的版本（默认最新版）和 endpoint（默认为最近接入点），以及默认的输出格式和指定的地域。 `default.credential` 则记录的是用户的密钥信息。 示例如下：
```bash
# default.configure文件格式，cvm产品默认调用版本 2017-03-12 的接口，默认的请求域名为 cvm.tencentcloudapi.com
{
	...
	"cvm": {
	"endpoint": "cvm.tencentcloudapi.com",
	"version": "2017-03-12"
	},
	...
	"output": "json",
	"region": "ap-guanzhou",
	...
}
# default.credential的文件格式
{
  "secretId": "AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******",
  "secretKey": "Gu5t9xGARNpq86cd98joQYCN3*******"
}
```
 - 若用户在使用配置命令时指定了账户名，则会生成账户名对应的配置文件。例如，用户使用了 `tccli configure --profile test` 命令，则会生成 `test.configure` 和 `test.credential` 文件。
 - 若需修改配置文件内容，您可以直接编辑文件或者使用 `set` 子命令修改。例如 `tccli configure set cvm.version 2017-03-12`，将调用的 cvm 的版本指定为默认 2017-03-12 版本。


#### 配置环境变量
TCCLI 支持配置云 API 密钥对到环境变量，让您的信息更安全。下文以 Linux 系统配置为例，您可以通过如下两种方式进行配置：
<dx-tabs>
::: 使用 export 命令（临时性）
```bash
# 设置云 API 密钥 SecretId
$ export TENCENTCLOUD_SECRET_ID=AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******
# 设置云 API 密钥 SecretKey
$ export TENCENTCLOUD_SECRET_KEY=Gu5t9xGARNpq86cd98joQYCN3*******
# 设置云产品地域
$ export TENCENTCLOUD_REGION=ap-guangzhou
```

:::
::: 写入 profile 文件（永久性）
```bash
# 编辑 /etc/profile 文件，写入如下内容
export TENCENTCLOUD_SECRET_ID=AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******
export TENCENTCLOUD_SECRET_KEY=Gu5t9xGARNpq86cd98joQYCN3*******
export TENCENTCLOUD_REGION=ap-guangzhou
# 写入后需执行如下命令使环境变量生效
$ source /etc/profile
```
:::
</dx-tabs>

<dx-alert infotype="explain" title="">
如果您在命令、配置文件和环境变量都指定了相同的内容，TCCLI 执行的优先级为：命令 > 配置文件 > 环境变量。
</dx-alert>

## 其他配置
- TCCLI 支持通过 CAM 角色的方式进行认证，您可以参考 [角色概述](https://cloud.tencent.com/document/product/598/19420) 查看相关信息。
```bash
# cam 角色的配置不支持交互模式，您可以使用非交互模式的方式进行配置：
$ tccli configure set role-arn qcs::cam::uin/***********/**** role-session-name ****
```
`role-arn` 和 `role-session-name` 字段支持 configure 的 get 和 list 操作，可以写入配置文件、直接在命令行指定，操作方式与 `secretId` 和 `secretKey` 的配置类似。如下所示：
```bash
# get 子命令获取配置信息
$ tccli configure get role-arn
role-arn = qcs::cam::uin/***********/****
# list 子命令打印所有配置信息
$ tccli configure list
credential:
role-arn = qcs::cam::uin/***********/****
role-session-name = ****
# 将配置信息写入环境变量
$ export TENCENTCLOUD_ROLE_ARN=qcs::cam::uin/***********/****
$ export TENCENTCLOUD_ROLE_SESSION_NAME=****
# 直接在命令行中指定 role-arn 和 role-session-name 信息，如调用 DescriZones 接口
$ tccli cvm DescribeZones --role-arn qcs::cam::uin/***********/**** --role-session-name ****
```
- 如果您的实例绑定了角色，您可以直接通过实例角色的方式进行认证，无需 secretId 和 secretKey 等信息。您可以使用 `--use-cvm-role` 来使用实例角色的方式调用。
```bash
#  使用实例角色的方式调用 DescribeZones 的接口
$ tccli cvm DescribeZones --use-cvm-role
```
<dx-alert infotype="notice" title="">
该方式仅支持在已绑定角色的实例上使用，具体方式请参见 [管理实例角色](https://cloud.tencent.com/document/product/213/47668)。
</dx-alert>


