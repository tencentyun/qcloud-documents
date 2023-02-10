## 操作场景

本文介绍利用 Kong 官方的 **decK** 工具来完成自建 Kong 网关到腾讯云云原生 Kong 网关的配置迁移。

## 前置条件

- 已购买 Kong 网关实例，[操作文档](https://cloud.tencent.com/document/product/1364/72495)，并 [配置 **admin-api**](https://cloud.tencent.com/document/product/1364/73237)。
- 有自建的 Kong 网关，并配置了 **services**、**routes**、**plugins**。
- 终端机安装了 **decK** 工具，请前往 Kong 官方下载 [decK](https://docs.konghq.com/deck/latest/installation/) 并安装到您的终端。

## 操作步骤

### 步骤1：利用 decK 工具导出自建的 Kong 网关的配置

1. 打开终端，运行如下命令导出自建 Kong 网关的配置。
<dx-codeblock>
:::  sh
# 注意将 kong-zj 替换为自建kong网关的ip地址或域名
deck --kong-addr http://kong-zj:8001/ dump
:::
</dx-codeblock>
2. 检查生成的`kong.yaml`文件。
<dx-codeblock>
:::  yaml
# 注意kong.yaml内容与实际情况会有所不同
cat kong.yaml
_format_version: "1.1"
plugins:
- config:
    per_consumer: false
  enabled: true
  name: prometheus
  protocols:
  - grpc
  - grpcs
  - http
  - https
services:
- connect_timeout: 60000
  host: 127.0.0.1
  name: admin-api
  path: /
  port: 8001
  protocol: http
  read_timeout: 60000
  retries: 5
  routes:
  - https_redirect_status_code: 426
    name: admin-api
    path_handling: v1
    paths:
    - /admin-api
    preserve_host: false
    protocols:
    - http
    - https
    regex_priority: 0
    request_buffering: true
    response_buffering: true
    strip_path: true
  write_timeout: 60000
- connect_timeout: 60000
  host: www.tencent.com
  name: tencent
  path: /
  port: 80
  protocol: http
  read_timeout: 60000
  retries: 5
  routes:
  - https_redirect_status_code: 426
    id: 040b0c62-4d31-4286-a595-1832e55bf568
    path_handling: v1
    paths:
    - /
    preserve_host: false
    protocols:
    - http
    - https
    regex_priority: 0
    request_buffering: true
    response_buffering: true
    strip_path: true
  write_timeout: 60000
:::
</dx-codeblock>


### 步骤2：利用 decK 工具导入配置到云原生 API 网关 Kong

1. 打开终端，运行如下命令查看`Kong.yaml`中的配置与云原生 **Kong** 网关的配置差异性。
<dx-codeblock>
:::  sh
# 注意将 kong-tencent 替换为腾讯云云原生 API 网关Kong的代理地址
deck --kong-addr http://kong-tencent/admin-api diff
creating service tencent
creating route 040b0c62-4d31-4286-a595-1832e55bf568
creating plugin prometheus (global)
Summary:
  Created: 3
  Updated: 0
  Deleted: 0
:::
</dx-codeblock>
2. 运行如下命令将`Kong.yaml`中的配置导入腾讯云云原生 **Kong** 网关中。
<dx-codeblock>
:::  sh
# 注意 kong-tencent 替换为腾讯云云原生 API 网关Kong的代理地址
deck --kong-addr http://kong-tencent/admin-api sync
creating service tencent
creating route 040b0c62-4d31-4286-a595-1832e55bf568
creating plugin prometheus (global)
Summary:
  Created: 3
  Updated: 0
  Deleted: 0
:::
</dx-codeblock>
3. 打开腾讯云云原生 **Kong** 网关的控制台查看配置是否导入成功。
![](https://qcloudimg.tencent-cloud.cn/raw/0e8a14051b8d7aafa35e685307c769f3.png)
![](https://qcloudimg.tencent-cloud.cn/raw/01272673e5280ede88468d050080a5d8.png)
![](https://qcloudimg.tencent-cloud.cn/raw/0cd42144d7a4bad3dfd9b079caccc5ba.png)

## 注意事项
为了操作方便 **admin-api** 并未开启安全认证插件，强烈建议配置同步完成后为 **admin-api** 开启安全认证插件。

## 参考
更多相关说明请参见 [decK 参考文档](https://docs.konghq.com/deck/)。
