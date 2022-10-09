
## 操作背景

通过 DIP 连接 CVM 自建的服务时，根据腾讯云网络团队制定的标准跨 VPC 资源访问方案，需要先将自建服务挂载到 CLB（负载均衡）上，才能实现跨 VPC 的资源访问。

即当在 CVM 上自建 MySQL、Mongo 服务作为数据源接入 DIP 时，需要通过挂载 CLB（负载均衡）的方式接入，本文描述相关的操作流程。

## 操作流程

### 步骤1：购买 CLB（负载均衡） 实例（可选）

**如果客户账号下已有内网 CLB 实例，为了节省成本，可以直接复用该 CLB 实例**。也可以新建单独的 CLB 实例提供服务。下面描述新建内网负载均衡(CLB)的操作过程。

>!购买 CLB 实例时，需要与 CVM 集群在同一地域，同一 VPC，这样 CLB 才能够正常挂载 CVM 实例。同时选择购买内网的 CLB 实例。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ed053be6180ee62d69091160f46a6b6b.png" width="50%"> 

### 步骤2：配置 CLB 实例

1. 创建 TCP 监听器：进入 **CLB 控制台** > [**实例管理**](https://console.cloud.tencent.com/clb/instance)页面。找到需要配置的实例，在该实例详情页面单击 **监听器管理**，单击新建 **TCP 监听器**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/45dd5c54860b7bceb75e2a32f0cad993.png" width="50%"> 
此处配置的端口为访问 CLB 的端口。健康检查和会话保持可根据实际需求进行配置。
2. 绑定自建服务：新建监听器成功后，单击相应的监听器，然后单击右侧的绑定，对 CVM 实例进行绑定。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ad1e6265f22208fca56e80337b5d37ba.png" width="50%"> 
选择需要绑定的 CVM 实例，并填写服务的端口号：
<img src="https://qcloudimg.tencent-cloud.cn/raw/b8741456ca1b3ae0bb19c8ac38f4017d.png" width="50%"> 
>!自建 MySQL 集群建议只挂载 **1台** CVM 实例（1台主节点或1台从节点），因为 MySQL 主从库的 binlog 同步存在延迟，connector 的请求被转发到不同 MySQL 服务时可能会发生读取 binlog 错误。因此自建集群建议只挂载单个 MySQL 服务。
3. 查看服务健康状态：创建完成后可看到对应的服务及健康状态。
<img src="https://qcloudimg.tencent-cloud.cn/raw/b30231340248ca97cd49185e8334ca3d.png" width="50%"> 

### 步骤3：创建连接
进入 CKafka 控制台，单击 **数据接入平台** > [**连接列表**](https://console.cloud.tencent.com/ckafka/datahub-connect)，单击**创建连接**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/5a301ed930e2e0fb2950c44e164a7f12.png" width="50%"> 
>?其中 CLB 实例选择挂载了 CVM 服务的实例，端口为相应的 CLB 监听端口，用户名和密码为相应的服务对应的用户名和密码。
