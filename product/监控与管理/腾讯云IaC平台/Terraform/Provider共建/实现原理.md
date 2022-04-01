
本文介绍 Terraform Tencentcloud Provider 的目录结构及生命周期。

## 目录结构
```
├─terraform-provider-tencentcloud                    根目录
│  ├─main.go                                         程序入口文件
│  ├─AUTHORS                                         作者信息
│  ├─CHANGELOG.md                                    变更日志
│  ├─LICENSE                                         授权信息
│  ├─debug.tf.example                                调试配置文件示例
│  ├─examples                                        示例配置文件目录
│  │  ├─tencentcloud-eip                             EIP示例tf文件
│  │  ├─tencentcloud-instance                        CVM示例tf文件
│  │  ├─tencentcloud-nat                             NAT网关示例tf文件
│  │  ├─tencentcloud-vpc                             VPC示例tf文件
│  │  └─ ...                                         更多examples目录
│  ├─tencentcloud                                    Provider核心目录
│  │  ├─basic_test.go                                基础单元测试
│  │  ├─config.go                                    公共配置文件
│  │  ├─data_source_tc_availability_zones.go         可用区查询
│  │  ├─data_source_tc_availability_zones_test.go
│  │  ├─data_source_tc_nats.go                       NAT网关列表查询
│  │  ├─data_source_tc_nats_test.go
│  │  ├─data_source_tc_vpc.go                        VPC查询
│  │  ├─data_source_tc_vpc_test.go
│  │  ├─...                                          更多Data Source
│  │  ├─helper.go                                    一些公共函数
│  │  ├─provider.go                                  Provider核心文件
│  │  ├─provider_test.go
│  │  ├─resource_tc_eip.go                           EIP资源管理程序
│  │  ├─resource_tc_eip_test.go
│  │  ├─resource_tc_instance.go                      CVM实例资源管理程序
│  │  ├─resource_tc_instance_test.go
│  │  ├─resource_tc_nat_gateway.go                   NAT网关资源管理程序
│  │  ├─resource_tc_nat_gateway_test.go
│  │  ├─resource_tc_vpc.go                           VPC网关资源管理程序
│  │  ├─resource_tc_vpc_test.go
│  │  ├─...                                          更多资源管理程序
│  │  ├─service_eip.go                               封装的EIP相关Service
│  │  ├─service_instance.go                          封装的CVM实例相关Service
│  │  ├─service_vpc.go                               封装的VPC相关Service
│  │  ├─...
│  │  ├─validators.go                                公共的参数校验函数
│  ├─vendor                                          依赖的第三方库
│  ├─website                                         Web相关文件
│  │  ├─tencentcloud.erb                             文档左侧菜单栏
│  │  ├─docs                                         文档markdown源文件目录
│  │  │  ├─d                                         data相关文档（data_source_*）
│  │  │  │  ├─availability_zones.html.md
│  │  │  │  ├─nats.html.markdown
│  │  │  │  ├─vpc.html.markdown
│  │  │  │  ├─...
│  │  │  ├─index.html.markdown
│  │  │  ├─r                                         resource相关文档(resource_*)
│  │  │  │  ├─instance.html.markdown
│  │  │  │  ├─nat_gateway.html.markdown
│  │  │  │  ├─vpc.html.markdown
│  │  │  │  └─...
```
结构主要分五部分：

- **main.go**：插件入口。
- **examples**：示例目录，其中包含的示例可直接使用。
- **tencentcloud**：插件目录，存放的业务代码。其中：
    - `provider.go`：插件的根源，用于描述插件的属性。例如，配置的密钥、支持的资源列表及回调配置等。
    - `data_source_*.go`：定义一些用于读调用的资源，主要是查询接口。
    - `resource_*.go`：定义一些写调用的资源，包含资源增删改查接口。
    - `service_*.go`：按资源大类划分的一些公共方法。
- **vendor**：依赖的第三方库。
- **website**：文档，重要性同 examples。

## Provider 生命周期

Terraform 执行过程如下图所示：
![生命周期](https://qcloudimg.tencent-cloud.cn/raw/b0a1ac2b36b2addb227c9da911760adb.png)

- `1 - 4`：寻找 Provider，此时加载 tencentcloud 插件。
- `5`：读取用户的配置文件，通过配置文件，可以获得分别属于哪种资源，以及每个资源的状态。
- `6`：根据资源的状态，调用不同的函数（Create/Update/Delete/Update）。
 - **Create**
当在 `.tf` 文件增加一个新的资源配置时，Terraform 判断为 Create。
 - **Update**
当修改 `.tf` 文件中已经创建好的资源一个或多个参数时，Terraform 判断为 Update。
 - **Delete**
当把 `.tf` 文件中已经创建好的资源配置删掉后，或执行 `terraform destroy` 命令时，Terraform 判断为 Delete。
 - **Read**
Read 是一个查询资源的操作，实际作用就是检查资源是否存在，以及更新资源属性到本地。
 - **tencentcloud-sdk-go**
tencentcloud-sdk-go 是基于 Tencent Cloud API 的 Go 版 SDK，其作用为调用 Tencent Cloud API 来实现资源管理。
