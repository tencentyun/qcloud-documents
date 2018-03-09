在创建或编辑云函数时，您可以通过修改高级配置中的网络配置，来为云函数的运行环境增加至 VPC 网络的访问能力。

## 编辑网络配置

在创建函数的过程中，或针对创建后的函数进行编辑时，可通过点击 【显示高级设置】 按钮，展开高级设置内容。

可通过【高级设置】>【网络】配置项，选择需接入的 VPC 网络和所需要使用的子网。如果在当前地域无 VPC 网络，可通过【新建网络】 跳转至 VPC 网络控制台以创建新的 VPC 网络，也可以通过 【新建子网】 创建 VPC 网络下的新子网。

通过选择网络选项中的 `无`，可重新切换云函数的网络环境至当前所属的独立网络环境

## 查看网络配置

在配置好云函数的网络项后，可通过查看云函数的函数配置，通过 **所属网络** 和 **所在子网** 了解到具体配置。

## 使用 VPC 网络

在配置完成并开始使用 VPC 网络后，此云函数的运行网络环境，将从当前独立的网络环境中切换至用户的 VPC 中。云函数启动时，将占用用户 VPC 子网中的 IP 地址作为云函数运行环境的 IP 地址。

> **注意** 
> 请确保子网中有足够的可用空闲的 IP 地址。如果由于无空闲 IP 导致的 IP 分配失败，将使得云函数启动运行失败。



云函数启动后，可通过代码访问 VPC 内的其他各产品，例如 [弹性缓存 Redis](https://cloud.tencent.com/product/crs?idx=1)、[云数据库 CDB](https://cloud.tencent.com/product/cdb-overview)、或用户配置在 VPC 中的 CVM 等等各种访问入口位于 VPC 中的产品或服务，直接通过内网 IP 地址即可访问。如下为访问 [弹性缓存 Redis](https://cloud.tencent.com/product/crs?idx=1) 的示例代码，其中 Redis 实例在 VPC 内的 IP 地址为 `10.0.0.86`。

```
# -*- coding: utf8 -*- 
import redis

def main_handler(event,context):
    r = redis.StrictRedis(host='10.0.0.86', port=6379, db=0,password="crs-i4kg86dg:abcd1234")
    print(r.set('foo', 'bar'))
    print(r.get('foo'))
    return r.get('foo')
```

云函数切换至 VPC 网络环境后，将失去原有独立网络环境中的外网访问能力，如需继续访问外网，在 VPC 上通过 [配置公网网关](https://cloud.tencent.com/document/product/215/11119)、[配置 NAT 网关](https://cloud.tencent.com/document/product/215/4975) 等方式，打通 VPC 访问外网的能力。

## 使用场景

* 内网服务访问：访问内网的数据库、Redis、Kafka 等产品或服务，确保数据安全，连接安全。
* 访问控制：外网访问统一收敛至同一地址，通过 VPC 外网出口可控出口地址。
