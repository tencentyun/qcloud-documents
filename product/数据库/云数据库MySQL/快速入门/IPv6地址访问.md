腾讯云数据库现已支持 IPv6 网络协议，您可以通过 IPv6 地址访问数据库，实现 IPv6 的内外网通信。

## 注意事项
- 目前支持部署 IPv6 的腾讯云数据库：MySQL、MongoDB、MariaDB、TDSQL、PostgreSQL、Redis、CTSDB、TcaplusDB。
- 目前支持部署 IPv6 的区域：北京五区、广州四区、上海四区、成都一区、南京一区。
- 购买时需要选择支持 [IPv6 的私有网络](https://cloud.tencent.com/document/product/215/38109#ipv6-.E5.9C.B0.E5.9D.80)。
- 以下产品暂不支持外网访问功能，因此只支持内网 IPv6 地址访问：MongoDB、Redis、CTSDB、TcaplusDB。

## 操作步骤
### 步骤一：开启 IPv6 地址访问
1. 登录 [云数据库购买页](https://buy.cloud.tencent.com/cdb?regionId=8)，在上方导航栏选择对应数据库。
>?TcaplusDB 需在 [控制台](https://console.cloud.tencent.com/tcaplusdb/app) 集群列表购买。
2. 在购买页的“IP版本”处，勾选“支持IPv6地址访问”。
![](https://main.qcloudimg.com/raw/c89ee6950e10c1c50c2b7bfb478023e9.png)
>?数据库购买完成后，默认开启并分配内网 IPv6 地址。

### （可选）步骤二：开启 IPv6 外网地址
1. 登录 [云数据库控制台](https://console.cloud.tencent.com/cdb)，在左侧导航栏选择对应数据库。
2. 在实例列表，单击实例名进入详情页，在“外网IPv6地址”处，单击【开启】，即可开启并分配外网 IPv6 地址。
![](https://main.qcloudimg.com/raw/f4f38e65fd7985e04c92022318465408.png)

### 步骤三：使用 IPv6 地址访问数据库
#### 通过内网地址访问数据库
使用云服务器 CVM 直接访问云数据库的内网 IPv6 地址，这种访问方式使用内网高速网络，延迟低。
  - 云服务器和数据库须是同一账号，且同一个 VPC 内（保障同一个地域)。
  - 内网 IPv6 地址可在 [控制台](https://console.cloud.tencent.com/cdb) 的实例/集群列表或实例/集群详情页查看。

#### 通过外网地址访问数据库
对于支持外网地址的数据库，可直接通过外网 IPv6 地址访问云数据库。
  - 外网 IPv6 地址可在 [控制台](https://console.cloud.tencent.com/cdb) 的实例/集群详情页查看。
  - 云数据库外网访问适用于开发或辅助管理数据库，不建议正式业务访问使用，因为可能存在不可控因素会导致外网访问不可用（例如 DDOS 攻击、突发大流量访问等）。
