## 策略语法
CAM 策略：
```
{     
        "version":"2.0", 
        "statement": 
        [ 
           { 
              "effect":"effect", 
              "action":["action"], 
              "resource":["resource"], 
               "condition": {"key":{"value"}} 
           } 
       ] 
}
```

- 版本 **version** 是必填项，目前仅允许值为"2.0"。
- 语句 **statement** 是用来描述一条或多条权限的详细信息。该元素包括 effect、action、resource，condition 等多个其他元素的权限或权限集合。一条策略有且仅有一个 statement 元素。
 1. **操作 action** 用来描述允许或拒绝的操作。操作可以是 API （以 name 前缀描述）或者功能集（一组特定的 API ，以 permid 前缀描述）。该元素是必填项。
 2. **资源 resource** 描述授权的具体数据。资源是用六段式描述。每款产品的资源定义详情会有所区别。有关如何指定资源的信息，请参阅您编写的资源声明所对应的产品文档。该元素是必填项。
 3. **生效条件 condition** 描述策略生效的约束条件。条件包括操作符、操作键和操作值组成。条件值可包括时间、IP 地址等信息。有些服务允许您在条件中指定其他值。该元素是非必填项。
 4. **影响 effect** 描述声明产生的结果是“允许”还是“显式拒绝”。包括 allow (允许)和 deny (显式拒绝)两种情况。该元素是必填项。

## 弹性网卡的操作[](id:caozuo)
在 CAM 策略语句中，您可以从支持 CAM 的任何服务中指定任意的 API 操作。对于 VPC，请使用以 name/vpc: 为前缀的 API 。例如： name/vpc:Modify 或者 name/vpc:CreateNetworkInterface 。
如果您要在单个语句中指定多个操作的时候，请使用逗号将它们隔开，如下所示:
```
"action":["name/vpc:action1","name/vpc:action2"]
```
您也可以使用通配符指定多项操作。例如，您可以指定名字以单词" Modify "开头的所有操作，如下所示：
```
"action":["name/vpc:Modify*"]
```
如果您要指定 VPC 中所有操作，请使用 * 通配符，如下所示：
```
"action"：["name/vpc:*"]
```

## 弹性网卡的资源路径[](id:ziyuanlujing)
每个 CAM 策略语句都有适用于自己的资源。
资源路径的一般形式如下：
```
qcs:project_id:service_type:region:account:resource
```

- **project_id**：描述项目信息，仅为了兼容 CAM 早期逻辑，无需填写。
- **service_type**：产品简称，如 VPC。
- **region**：地域信息，如 bj。
- **account**：资源拥有者的根帐号信息，如 uin/164256472。
- **resource**：各产品的具体资源详情，如 eni/eni_id1 或者 eni/*。

例如，您可以使用特定实例 (eni-abcdefgh) 在语句中指定它，如下所示：
```
"resource":[ "qcs::vpc:bj:uin/164256472:eni/eni-abcdefgh"]
```
您还可以使用 * 通配符指定属于特定账户的所有实例，如下所示： 
```
"resource":[ "qcs::vpc:bj:uin/164256472:eni/*"]
```
您要指定所有资源，或者如果特定 API 操作不支持资源级权限，请在 Resource 元素中使用 * 通配符，如下所示：
```
"resource": ["*"]
```
如果您想要在一条指令中同时指定多个资源，请使用逗号将它们隔开，如下所示为指定两个资源的例子：
```
"resource":["resource1","resource2"]
```
