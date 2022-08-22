## 操作场景

JSON 目前是互联网信息传递中最通用的格式协议之一。目前数据处理也主要围绕 JSON 数据格式进行解析处理。

JSONPath 是针对 JSON 格式推出的消息查询语法规范。在数据处理中，不仅能够使用简单的 JSONPath 语法，快速获取复杂嵌套 JSON 结构体的某一成员的值；还能使用 [**JayWay**](https://github.com/json-path/JsonPath) 库的扩展函数，聚合或操作某一类型的成员字段。

## 基础功能

### 基础语法

- `$` 根结点操作符，表示当前 JSON 结构体的根结点。
- `.<childName>` 点操作符或 `['<childName>']` 方括号操作符，表示选取当前作用对象名为 `childName` 的子成员。
- `..` 递归操作符，表示 **递归** 获取当前作用对象的所有子成员。
- `[<index>]` 片选操作符，表示获取当前可迭代对象的第 `index` 个子成员。

### 获取嵌套 JSON 特定成员变量

下图为 TKE 采集的容器标准输出日志结构：
<dx-codeblock>
:::  JSON
{
  "@timestamp": 1648803500.63659,
  "@filepath": "/var/log/tke-log-agent/test7/xxxxxxxx-adfe-4617-8cf3-9997aea90ded/c_tke-es-xxxxxxxx57-n29jr_default_nginx-xxxxxxxx49626ef42d5615a636aae74d6380996043cf6f6560d8131f21a4d8ba/jgw_INFO_2022-02-10_15_4.log",
  "log": "15:00:00.000[4349811564226374227] [http-nio-8081-exec-64] INFO  com.qcloud.jgw.gateway.server.topic.TopicService",
  "kubernetes": {
    "pod_name": "tke-es-xxxxxxxxxx-n29jr",
    "namespace_name": "default",
    "pod_id": "xxxxxxxx-adfe-4617-8cf3-9997aea90ded",
    "labels": {
      "k8s-app": "tke-es",
      "pod-template-hash": "xxxx95d557",
      "qcloud-app": "tke-es"
    },
    "annotations": {
      "qcloud-redeploy-timestamp": "1648016531476",
      "tke.cloud.tencent.com/networks-status": "[{\n    \"name\": \"tke-bridge\",\n    \"interface\": \"eth0\",\n    \"ips\": [\n        \"172.16.x.xx\"\n    ],\n    \"mac\": \"xx:xx:xx:4a:c2:ba\",\n    \"default\": true,\n    \"dns\": {}\n}]"
    },
    "host": "10.0.xx.xx",
    "container_name": "nginx",
    "docker_id": "xxxxxxxx49626ef42d5615a636aae74d6380996043cf6f6560d8131f21a4d8ba",
    "container_hash": "nginx@sha256:xxxxxxxx7b29b585ed1aee166a17fad63d344bc973bc63849d74c6452d549b3e",
    "container_image": "nginx"
  }
}
:::
</dx-codeblock>


当用户需要获取当前 pod 名称，即获取 `qcloud-app` 成员字段时，可以在数据处理中使用 `$.kubernetes.labels.qcloud-app`，或 `$.['kubernetes'].['labels'].['qcloud-app']` JSONPath 语法获取。

运行结果如下所示，可以看出在测试结果中已经成功读取到 JSONPath 对应的日志：

![](https://qcloudimg.tencent-cloud.cn/raw/bf48e9a31b8be22b036d5d577d3a0b3c.png)

![](https://qcloudimg.tencent-cloud.cn/raw/414e28be90679024725c61da41ddc951.png)

> ?在使用 JSONPath 处理参数时，当 JSON 变量名称本身带有英文句号 `.` 等特殊符号时，就只能使用方括号操作符进行包装。
>
> 例如 `{"key1.key2":"value1"}` 的 JSON 结构体，要想取得对应成员字段，则需要使用 `$.['key1.key2']` 进行获取。
>
## 进阶功能

### 进阶语法
- `*` 通配操作符，表示获取当前作用对象的 **所有** 子成员。
- `*~` 内置函数，表示获取当前可迭代对象所有子对象的名称。
- `min()` 内置函数，表示获取当前可迭代对象子对象的最小值。
- `max()` 内置函数，表示获取当前可迭代对象子对象的最大值。
- `sum()` 内置函数，表示获取当前可迭代对象子对象之和。
- `concat()` 内置函数，表示连接多个对象并生成字符串。


### 聚合特定字段数据

当 JSON 结构体中存在对象列表时，通常列表为变长形式，以下图中的请求返回日志为例：
<dx-codeblock>
:::  JSON
{
  "data": {
    "Response": {
      "Result": {
        "Routers": [
          {
            "AccessType": 0,
            "RouteId": 81111,
            "VpcId": "vpc-xxxxxxxx",
            "VipType": 3,
            "VipList": [
              {
                "Vip": "10.0.0.189",
                "Vport": "9xxx"
              }
            ]
          },
          {
            "AccessType": 0,
            "RouteId": 81112,
            "VpcId": "vpc-r5sbavzp",
            "VipType": 3,
            "VipList": [
              {
                "Vip": "10.0.0.248",
                "Vport": "9xxx"
              }
            ]
          },
          {
            "AccessType": 0,
            "RouteId": 81113,
            "VpcId": "vpc-xxxxxxxx",
            "VipType": 3,
            "VipList": [
              {
                "Vip": "10.0.0.210",
                "Vport": "9xxx"
              }
            ]
          }
        ]
      },
      "RequestId": "20e74750-ca40-403d-9ea9-d3f63b5415d2"
    }
  },
  "code": 0
}
:::
</dx-codeblock>


当需要聚合变长列表的成员属性时，此时无法使用处理链形式聚合处理。此时可以使用 JSONPath 中的 `*` 语法匹配列表中所有元素。

例如当需要得到所有的 VipList 中的 Vip 时，可以使用 `$.data.Response.Result.Routers[*].VipList[0].Vip` 的 JSONPath 语法获取。

运行结果如下所示，可以看出在测试结果中已经成功获取到了所有结构体中的 Vip：

![](https://qcloudimg.tencent-cloud.cn/raw/758b8ece9966d34320e8072e4ba92542.png)

![](https://qcloudimg.tencent-cloud.cn/raw/2db88e22f45bcaa59643b85006b2ce19.png)

### 合并修改结构体成员

在某些场景下，需要在数据处理中对 JSON 结构体的多个对象进行合并整合处理，以便投递到下游进行下一步操作。考虑如下格式：
<dx-codeblock>
:::  JSON
{
  "data": {
    "Response": {
      "SubnetSet": [
        {
          "VpcId": "vpc-xxxxxxxx",
          "SubnetId": "subnet-xxxxxxxx",
          "SubnetName": "ckafka_cloud_subnet-1",
          "CidrBlock": "10.0.0.0/19",
          "Ipv6CidrBlock": "",
          "IsDefault": false,
          "IsRemoteVpcSnat": false,
          "EnableBroadcast": false,
          "Zone": "ap-changsha-ec-1",
          "RouteTableId": "rtb-xxxxxxxx",
          "NetworkAclId": "",
          "TotalIpAddressCount": 8189,
          "AvailableIpAddressCount": 8033,
          "CreatedTime": "2021-01-25 17:31:00",
          "TagSet": [],
          "CdcId": "",
          "IsCdcSubnet": 0,
          "LocalZone": false,
          "IsShare": false
        }
      ],
      "TotalCount": 1,
      "RequestId": "705c4955-0cd9-48b2-9132-79eadae2e3e6"
    }
  },
  "code": 0
}
:::
</dx-codeblock>

当下游不具有计算功能，需要在数据处理中聚合 Vpc 以及子网属性时，可以使用 JSONPath 中的 `concat()` 函数进行多个字段的聚合，并且在此基础上对字符串进行修改。

例如可以使用 `$.concat($.data.Response.SubnetSet[0].VpcId,"#",$.data.Response.SubnetSet[0].SubnetId,"#",$.data.Response.SubnetSet[0].CidrBlock))` 语法拼接 Vpc 和子网的属性，并且通过 `#` 字符加以分割。

运行结果如下所示，可以看出在测试结果中已经成功获取整合了 VPC 相关的资源信息：

![](https://qcloudimg.tencent-cloud.cn/raw/c21df71048ed813f55e95a6eaedc4392.png)

![](https://qcloudimg.tencent-cloud.cn/raw/34aa2fe60fa537b92f5625436bab1093.png)
