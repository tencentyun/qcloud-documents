CLI supports all cloud APIs. That is, any product with a cloud API can use CLI for operation and management. For more information about the command module and corresponding API, please see the following description and [Tencent Cloud API Documentation](https://cloud.tencent.com/doc/api).

## Basic Commands
| Command | Description | Parameters and Description |
| -------------------- | -----------------  |------ | 
| qcloudcli help | View help information about the main command | None |
| qcloudcli configure | Set specific user information | --profile XX: Set the user information for the user whose name is XX. If this parameter is empty, the default account information is set. |
| qcloudcli showconfigure | View current configuration information | None |
| qcloudcli addprofile | Add a user | --name XX: Add a user named XX. If this parameter is empty, you need to manually enter the user name |
| qcloudcli delprofile | Delete a user | --name XX: Delete the user named XX |
| qcloudcli useprofile | Switch the user | --name XX: Set the user named XX as a default user |

## Expandability
### Filtering Results      
```
qcloudcli <command> <operation> --filter XX 
```
Filter the returned results with XX as the condition [>> Details](https://cloud.tencent.com/document/product/440/10532) |

## Module Introduction
Tencent Cloud CLI is a product encapsulated based on Tencent Cloud APIs to make it easy for developers to use. Each command module corresponds to a different module for the API. The APIs of a command module are the same as the cloud APIs. For more information about APIs, please see [Tencent Cloud API Documentation](https://cloud.tencent.com/doc/api).

| Main Command Module | Description | Some APIs | More APIs |
|:----------------------| :-------------------|:----------------------------------------|:-------------------------------------------------------| 
| qcloudcli account | User account related commands | Add/view a project, view an user group | [View Details](https://cloud.tencent.com/doc/api/403/4368) |
| qcloudcli cbs | Cloud disk related commands | Create a cloud disk, create an elastic cloud disk | [View Details](https://cloud.tencent.com/doc/api/364/2446) |
| qcloudcli cdn | Content Delivery Network related commands | Add an accelerated domain, enable/disable a CDN domain | [View Details](https://cloud.tencent.com/doc/api/231/1723) |
| qcloudcli cns | Domain name related commands | Resolute/license a domain name | [Domain Name Licensing](https://cloud.tencent.com/doc/api/263/1213) |
| qcloudcli cvm | Cloud service related commands | View/create/terminate/launch/shut down an instance | [View Details](https://cloud.tencent.com/doc/api/229/569#2.-.E5.AE.9E.E4.BE.8B.E7.9B.B8.E5.85.B3.E6.8E.A5.E5.8F.A3)  
| qcloudcli dfw | Cloud service security group related commands | Add/delete/query/modify a security group | [View Details](https://cloud.tencent.com/doc/api/229/569#5.-.E5.AE.89.E5.85.A8.E7.BB.84.E7.9B.B8.E5.85.B3.E6.8E.A5.E5.8F.A3) |
| qcloudcli image | Cloud service image related commands | Create/delete a custom image | [View Details](https://cloud.tencent.com/doc/api/229/569#3.-.E9.95.9C.E5.83.8F.E7.9B.B8.E5.85.B3.E6.8E.A5.E5.8F.A3) |
| qcloudcli live | LVB related commands | Create/query/delete an LVB channel | [View Details](https://cloud.tencent.com/doc/api/258/4714) |
| qcloudcli monitor | Monitor related commands | Commands for Cloud Monitor and CCM |[Cloud Monitor](https://cloud.tencent.com/doc/api/405/4474) [CCM](https://cloud.tencent.com/doc/api/255/1786) |
| qcloudcli scaling | Auto scaling related commands | Commands for launching configuration, scaling group/alarm policy | [View Details](https://cloud.tencent.com/doc/api/372/3174) |
| qcloudcli tdsql | Cloud Database tdsql related commands | Commands for instance, account, backup and monitoring | [View Details](https://cloud.tencent.com/doc/api/309/5374) |        
| qcloudcli vod | VOD related commands | Create/ delete/view/modify a video category | [View Details](https://cloud.tencent.com/doc/api/257/1965) |
| qcloudcli wenzhi | NLP natural language processing related commands | Common APIs and download and extraction API | [View Details](https://cloud.tencent.com/doc/api/307/2050) |
| qcloudcli cdb | Cloud Database related commands | Commands for the instance, monitoring and log of the Cloud Database MYSQL | [View Details](https://cloud.tencent.com/doc/api/253/1210) |
| qcloudcli cmem | Cloud cache Memcached related commands | View/clear a CMEM instance | [View Details](https://cloud.tencent.com/doc/api/261/1763) |
| qcloudcli dayu | (Network Security) Dayu related commands | Purge URL, view traffic | [View Details](https://cloud.tencent.com/doc/api/361/2315) |
| qcloudcli eip | EIP related commands | Add/delete/modify/query an EIP | [View Details](https://cloud.tencent.com/doc/api/229/569#6.-.E5.BC.B9.E6.80.A7ip.E7.9B.B8.E5.85.B3.E6.8E.A5.E5.8F.A3) |
| qcloudcli lb | Load balance related commands | Add/delete/modify/query a load balancer | [View Details](https://cloud.tencent.com/doc/api/244) |
| qcloudcli redis | Cloud Redis related commands | Add/delete/modify/query a CRS instance | [View Details](https://cloud.tencent.com/doc/api/260) |
| qcloudcli snapshot | Snapshot related commands | Create/delete/roll back a snapshot | [View Details](https://cloud.tencent.com/doc/api/364/2446#3.-.E5.BF.AB.E7.85.A7.E7.9B.B8.E5.85.B3.E6.8E.A5.E5.8F.A3) |
| qcloudcli vpc | VPC related commands | Commands for VPCs, subnets, routers, network ACL and Direct Connect | [View Details](https://cloud.tencent.com/doc/api/245/909) |
| qcloudcli yunsou | Cloud search related commands | Commands for data operation and data retrieval | [View Details](https://cloud.tencent.com/doc/api/256/1990) |
