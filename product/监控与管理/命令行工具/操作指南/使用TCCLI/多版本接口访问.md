
TCCLI 默认访问产品最新版本的接口，而某些产品可能存在多个版本的接口，若您需访问特定旧版本的接口，可参考本文进行实现。

## 操作步骤
- 以云服务器 CVM 为例，执行以下命令，设置默认使用版本为 `2017-03-12`。
```
tccli configure set cvm.version 2017-03-12
```
- 执行以下命令，在实时使用时指定版本号。
```
tccli cvm help --version 2017-03-12
tccli cvm DescribeZones help --version 2017-03-12
tccli cvm DescribeZones --version 2017-03-12
```
