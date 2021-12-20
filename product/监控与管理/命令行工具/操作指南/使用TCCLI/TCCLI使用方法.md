

## 操作场景
本文介绍如何使用命令行工具 TCCLI 的基础功能。

TCCLI 集成了腾讯云所有支持云 API 的产品，您可以在命令行下完成对腾讯云产品的配置和管理。包括使用 TCCLI 创建云服务器、操作云服务器、通过 TCCLI 创建云硬盘、查看云硬盘使用情况、通过 TCCLI 创建私有网络、往私有网络中添加资源等，所有在控制台页面能完成的操作，均能在 TCCLI 上执行命令实现。例如：

* 通过 `tccli cvm DescribeInstances` 命令查看当前账号有哪些云服务器。
* 通过 `tccli cbs DescribeDisks` 命令查看有云硬盘列表。



## 操作步骤

>! 以下以 Linux 操作系统为例，示例中非简单类型的参数，必须为标准 JSON 格式。

- 执行以下命令，创建一台 CVM。
```bash
tccli cvm RunInstances
--InstanceChargeType POSTPAID_BY_HOUR
--InstanceChargePrepaid '{"Period":1,"RenewFlag":"DISABLE_NOTIFY_AND_MANUAL_RENEW"}'
--Placement '{"Zone":"ap-guangzhou-2"}'
--InstanceType S1.SMALL1
--ImageId img-8toqc6s3
--SystemDisk '{"DiskType":"CLOUD_BASIC", "DiskSize":50}'
--InternetAccessible '{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":10,"PublicIpAssigned":true}' 
--InstanceCount 1
--InstanceName TCCLI-TEST
--LoginSettings '{"Password":"TCCLI"}'
--SecurityGroupIds '["sg-0rszg2vb"]'
--HostName TCCLI-HOST-NAME1
```
- TCCLI 支持调用 octet-stream 类型的接口，如果调用的接口使用的是 octet-stream 协议，您可以使用标准输入`< /path/to/file`来传输您的二进制文件
```bash
# 以 cls 的 UploadLog 接口为例，上传日志可使用如下命令
tccli cls UploadLog --TopicId xxx < /path/to/file
```
- 若调用接口参数为复杂类型时，可以增加 `--cli-unfold-argument` 参数，并进行参数补全，使用复杂类型点(`.`)展开的方式调用，降低输入难度。
```bash
tccli cvm RunInstances --cli-unfold-argument \
--Placement.Zone ap-guangzhou-3 \
--ImageId img-8toqc6s3 \
--DryRun True
```
>?
>- `--cli-unfold-argument` 命令可通过 Tab 键进行补全，详情请参见 [使用命令行自动补全功能](https://cloud.tencent.com/document/product/440/60834)。
>- `--cli-unfold-argument` 命令需`3.0.273.1` 版本及以上。
- 可增加 `--generate-cli-skeleton` 参数，输出 JSON 格式入参骨架。
```bash
# 可将 json 格式入参骨架直接输入到 json 文件中
# $ tccli cvm DescribeInstances --generate-cli-skeleton > /home/test.json
tccli cvm DescribeInstances --generate-cli-skeleton
{
    "Limit": "Integer", 
    "Filters": [
        {
            "Values": [
                "String"
            ], 
            "Name": "String"
        }
    ], 
    "InstanceIds": [
        "String"
    ], 
    "Offset": "Integer"
}
```
>?
>- `--generate-cli-skeleton` 命令可通过 Tab 键进行补全，详情请参见  [使用命令行自动补全功能](https://cloud.tencent.com/document/product/440/60834)。
>- `--generate-cli-skeleton` 命令需`3.0.273.1`版本及以上。
- 若接口入参较多，可增加 `--cli-input-json` 参数，该参数支持 JSON 文件输入（参数后需增加 `file://+文件路径`）。您可以使用 `--generate-cli-skeleton` 生成相应的 JSON 文件，填写参数后即可直接使用该 JSON 文件调用接口。
```bash
tccli cvm DescribeInstances --cli-input-json file:///home/test.json
```
>?
>- `--cli-input-json` 命令可通过 Tab 键进行补全，详情请参见 [使用命令行自动补全功能](https://cloud.tencent.com/document/product/440/60834)。
>- `--cli-input-json` 命令需`3.0.250.2`版本及以上。
