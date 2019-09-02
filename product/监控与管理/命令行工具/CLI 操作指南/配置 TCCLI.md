## 操作场景
本文指导您如何配置 TCCLI。

## 前提条件

[安装 TCCLI](https://cloud.tencent.com/document/product/440/34011)

## 操作步骤
要使用腾讯云命令行工具，您还需要进行一些初始化配置，使其完成使用云 API 的必要前提条件。
1. 交互模式，您可以通过 tccli configure 命令进入交互模式快速配置。
```bash
$ tccli configure
TencentCloud API secretId [*afcQ]:AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
TencentCloud API secretKey [*ArFd]:OxXj7khcV1234dQSSYNABcdCc1LiArFd
region: ap-guangzhou
output[json]:
```
 - **secretId**：云 API 密钥 SecretId。
 - **secretIKey**：云 API 密钥 SecretKey。
 - **region**： 云产品地域，请移驾对应产品页面获取可用的 region。
 - **output**： 可选参数，请求回包输出格式，支持 [json table text] 三种格式，默认为 json。
更多信息请执行 `tccli configure help` 查看。
2. 命令行模式，通过命令行模式您可以在自动化脚本中配置您的信息。
```bash
# set子命令可以设置某一配置，也可同时配置多个。
tccli configure set secretId AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
tccli configure set region ap-guangzhou  output json
# get子命令用于获取配置信息。
tccli configure get secretKey
secretKey = OxXj7khcV1234dQSSYNABcdCc1LiArFd
# list子命令打印所有配置信息。
tccli configure list
credential:
secretId =  AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
secretKey =  OxXj7khcV1234dQSSYNABcdCc1LiArFd
configure:
region =  ap-guangzhou
output =  json
```
更多信息请执行 `tccli configure [list get set] help` 查看。
3. 多账户支持，TCCLI 支持多账户，方便您多种配置同时使用。
```sh
在交互模式中指定账户名 test。
$ tccli configure --profile test
TencentCloud API secretId [*BCDP]:AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
TencentCloud API secretKey [*ArFd]:OxXj7khcV1234dQSSYNABcdCc1LiArFd
region: ap-guangzhou
output[json]:
# set/get/list子命令指定账户名 test。
tccli configure set region ap-guangzhou  output json  --profile test
tccli configure get secretKey      --profile test
tccli configure list      --profile test
在调用接口时指定账户（以 cvm DescribeZones 接口为例）。
tccli cvm DescribeZones --profile test
```
