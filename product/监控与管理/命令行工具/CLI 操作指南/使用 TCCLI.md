## 操作场景
命令行工具集成了腾讯云所有支持云 API 的产品，可以在命令行下完成对腾讯云产品的配置和管理。包括使用 TCCLI 创建云服务器，操作云服务器，通过 TCCLI 创建 CBS 盘、查看 CBS 盘使用情况，通过 TCCLI 创建 VPC 网络、往 VPC 网络中添加资源等，所有在控制台页面能完成的操作，均能在命令行工具上执行命令实现。
- 通过 `tccli cvm DescribeInstances` 命令查看当前账号有哪些云服务器。
- 通过 `tccli cbs DescribeDisks` 命令查看有 CBS 盘列表。

## 操作示例
>!请注意 demo 中非简单类型的参数必须为标准 json 格式。

以创建一台 CVM 为例，执行以下命令。
```bash
tccli cvm RunInstances --InstanceChargeType POSTPAID_BY_HOUR --InstanceChargePrepaid '{"Period":1,"RenewFlag":"DISABLE_NOTIFY_AND_MANUAL_RENEW"}'
 --Placement '{"Zone":"ap-guangzhou-2"}' --InstanceType S1.SMALL1 --ImageId img-8toqc6s3 --SystemDisk '{"DiskType":"CLOUD_BASIC", "DiskSize":50}'
--InternetAccessible '{"InternetChargeType":"TRAFFIC_POSTPAID_BY_HOUR","InternetMaxBandwidthOut":10,"PublicIpAssigned":true}' --InstanceCount 1
--InstanceName TCCLI-TEST --LoginSettings '{"Password":"isd@cloud"}' --SecurityGroupIds '["sg-0rszg2vb"]' --HostName TCCLI-HOST-NAME1
```
>?更多功能，您可以通过`tccli help`查看支持的产品，通过`tccli cvm help`（以 CVM 举例）查看产品支持的接口。通过`tccli cbs DescribeDisks help`（以 CBS 产品的 DescribeDisks 接口为例） 查看接口支持的参数。
