SCF 默认是部署在公共网络中，如果您想让 SCF 可以访问到内网中的资源，如 TencentDB、CVM 等，在创建或编辑云函数时，您可以通过更改网络配置，来为云函数的运行环境增加至 VPC 网络的访问能力。需要注意的是：
* 部署在 VPC 中的云函数默认是和外网隔离开的，如果您想让云函数同时具备内网访问和外网访问能力，您可以参考另外一篇文章 [《函数在 VPC 网络中访问外网》](https://cloud.tencent.com/document/product/583/19704)，给 VPC 添加 NAT 网关。
* 云函数当前不支持对接到基础网络里的资源，如果您确实需要访问到基础网络，可以 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=668&source=0&data_title=%E6%97%A0%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%BA%91%E5%87%BD%E6%95%B0%20SCF&step=1) 联系我们。

## 使用场景
* 内网服务访问：访问内网的数据库、Redis、Kafka 等产品或服务，确保数据安全，连接安全。
* 访问控制：外网访问统一收敛至同一地址，通过 VPC 外网出口可控制出口地址唯一。

## 编辑网络配置
在创建函数的过程中，或针对创建后的函数进行编辑时，可在函数配置页里找到 VPC 网络配置，选择需接入的 VPC 网络和所需要使用的子网。
通过选择网络选项中的 `无`，可重新切换云函数的网络环境至当前所属的独立网络环境。

## 查看网络配置

在配置好云函数的网络项后，可通过查看云函数的函数配置，通过 **所属网络** 和 **所在子网** 了解到具体配置。

## 使用 VPC 网络

在配置完成并开始使用 VPC 网络后，此云函数的运行网络环境，将从当前独立的网络环境中切换至用户的 VPC 中。云函数启动时，将占用用户 VPC 子网中的 IP 地址作为云函数运行环境的 IP 地址。
>! 请确保子网中有足够的可用空闲的 IP 地址。如果由于无空闲 IP 导致的 IP 分配失败，将使得云函数启动运行失败。您可以更改子网的掩码长度来扩充子网 IP 的数量。
>

云函数启动后，可通过代码访问 VPC 内的其他各产品，例如 [云数据库 TencentDB for Redis](https://cloud.tencent.com/product/crs?idx=1)、[云关系型数据库](https://cloud.tencent.com/product/cdb-overview)、用户配置在 VPC 中的 CVM 等等各种访问入口位于 VPC 中的产品或服务，直接通过内网 IP 地址即可访问。如下为访问 [云数据库 TencentDB for Redis](https://cloud.tencent.com/product/crs?idx=1) 的示例代码，其中 Redis 实例在 VPC 内的 IP 地址为 `10.0.0.86`。
```
# -*- coding: utf8 -*- 
import redis

def main_handler(event,context):
    r = redis.StrictRedis(host='10.0.0.86', port=6379, db=0,password="crs-i4kg86dg:abcd1234")
    print(r.set('foo', 'bar'))
    print(r.get('foo'))
    return r.get('foo')
```

云函数切换至 VPC 网络环境后，将失去原有独立网络环境中的外网访问能力，如需继续访问外网，在 VPC 上通过配置 [公网网关](https://cloud.tencent.com/document/product/215/20078)、配置 [ NAT 网关](https://cloud.tencent.com/document/product/552) 等方式，打通 VPC 访问外网的能力，具体可以参考另外一篇文章 [《函数在 VPC 网络中访问外网》](https://cloud.tencent.com/document/product/583/19704)，给 VPC 添加 NAT 网关。

### VPC 网络中的 Name server 配置
在配置云函数到 VPC 网络中后，如果需要在 VPC 网络内仍然使用域名方式访问 VPC 网络内的自建服务，通常需要使用自定义 name server 实现域名解析。
为了支持云函数环境内的自定义 name server 配置，目前可以通过配置 `OS_NAMESERVER` 环境变量来实现自定义 name server。

| 环境变量名 | 值设置规则 | 作用 |
| --- | --- | --- |
| OS_NAMESERVER | 可以为一个或多个 IP 地址、或域名，多个地址时使用“;”分号分隔。最多可以支持配置5个自定义 name server | 配置自定义 name server |

可通过打印输出 `/etc/resolv.conf` 文件检查配置生效情况。
```
with open("/etc/resolv.conf") as f:
    print(f.readlines())
```



