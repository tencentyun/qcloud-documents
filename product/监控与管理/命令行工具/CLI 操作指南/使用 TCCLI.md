

## 操作场景

命令行工具集成了腾讯云所有支持云 API 的产品，可以在命令行下完成对腾讯云产品的配置和管理。包括使用 TCCLI 创建云服务器、操作云服务器、通过 TCCLI 创建 CBS 盘、查看 CBS 盘使用情况、通过 TCCLI 创建 VPC 网络、往 VPC 网络中添加资源等，所有在控制台页面能完成的操作，均能在命令行工具上执行命令实现。例如：

* 通过 `tccli cvm DescribeInstances` 命令查看当前账号有哪些云服务器。
* 通过 `tccli cbs DescribeDisks` 命令查看有 CBS 盘列表。

## 操作示例

>! 以下以 Linux 操作系统为例，示例中非简单类型的参数，必须为标准 JSON 格式。

1. 以创建一台 CVM 为例，执行以下命令。
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
2. 如果调用接口参数是复杂类型时，可以加 `--cli-unfold-argument`参数，进行参数补全，使用复杂类型点(`.`)展开的方式调用，降低输入难度。
```bash
tccli cvm RunInstances --cli-unfold-argument \
--Placement.Zone ap-guangzhou-3 \
--ImageId img-8toqc6s3 \
--DryRun True
```
>?
>- `--cli-unfold-argument` 命令可通过 Tab 键进行补全，详情请参见 [命令补全](https://cloud.tencent.com/document/product/440/34011#.E5.91.BD.E4.BB.A4.E8.A1.A5.E5.85.A8)。
>- `--cli-unfold-argument` 命令需`3.0.273.1` 版本及以上。
3. 如果您不清楚接口入参，可加`--generate-cli-skeleton`参数输出一份 JSON 格式入参骨架。
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
>- `--generate-cli-skeleton` 命令可通过 Tab 键进行补全，详情请参见 [命令补全](https://cloud.tencent.com/document/product/440/34011#.E5.91.BD.E4.BB.A4.E8.A1.A5.E5.85.A8)。
>- `--generate-cli-skeleton` 命令需`3.0.273.1`版本及以上。
4. 如果接口入参比较多，可加 `--cli-input-json` 参数，该参数支持 JSON 文件输入（后面需要加上 `file://+文件路径`）。
```bash
tccli cvm DescribeInstances --cli-input-json file:///home/test.json
```
>?
>- `--cli-input-json` 命令可通过 Tab 键进行补全，详情请参见 [命令补全](https://cloud.tencent.com/document/product/440/34011#.E5.91.BD.E4.BB.A4.E8.A1.A5.E5.85.A8)。
>- `--cli-input-json` 命令需`3.0.250.2`版本及以上。



## 更多命令
- `tccli help`
查看支持的产品。您也可以在 [产品简介](https://cloud.tencent.com/document/product/440/6176) 文档中查看。
- `tccli cvm help`
以 CVM 为例，查看产品支持的接口。
- `tccli cbs DescribeDisks help`
以 CBS 中的 DescribeDisks 接口为例，查看接口支持的参数。具体的参数说明和 API 的相关信息可以在腾讯云官网查看对应的 API 文档。
