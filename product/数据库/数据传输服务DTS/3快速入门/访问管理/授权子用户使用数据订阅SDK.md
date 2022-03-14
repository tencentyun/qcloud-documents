## 操作场景 
用户可以使用子用户进行订阅任务的创建和管理，也可以在 SDK Demo 中使用子用户的 AccessKey 和 AccessKeySecret 进行数据订阅。 

当用户使用 CAM  （Cloud Access Management，访问管理） 的时候，可以将策略与一个用户或一组用户关联起来，策略能够授权或者拒绝用户使用指定资源完成指定任务。有关 CAM 策略的更多信息，请参见 [策略语法](https://cloud.tencent.com/document/product/598/10603)。 

## 给子用户授权
1. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam)。
2. 在**用户** > **用户列表**页面搜索需要授权的子用户，单击右侧操作列下的**授权**，如下图：
    ![](https://main.qcloudimg.com/raw/0e282f57a0b3a4e21a7265cef73ea093.png)
3. 在弹出的窗口中搜索“DTS”，选择需要授权的权限。
    - QcloudDTSFullAccess：表示授权读和写访问权限。
    - QcloudDTSReadOnlyAccess：表示仅授权读访问权限。
![](https://main.qcloudimg.com/raw/d5ef07626438321d7b2f99c9e00e377e.png)
4. 单击**确定**，完成授权。

## 策略语法
DTS 的 CAM 策略描述如下：
```
 {     
        "version":"2.0", 
        "statement": 
        [ 
           { 
              "effect":"effect", 
              "action":["action"], 
              "resource":["resource"]
           } 
       ] 
} 
```

- **版本 version**：必填项，目前仅允许值为"2.0"。
- **语句 statement**：用来描述一条或多条权限的详细信息。该元素包括 effect、action、resource 等多个其他元素的权限或权限集合。一条策略有且仅有一个 statement 元素。
>?由于 DTS 需要操作用户的数据库，因此用户还须单独对 DTS 任务所涉及的数据库资源将子账号进行授权（需要读操作，即“Describe\*”）。此授权操作不包含在本文中。
- **影响 effect**：必填项，描述声明产生的结果是“允许”还是“显式拒绝”。包括 allow（允许）和 deny（显式拒绝）两种情况。
```
"effect": "allow"
```
- **操作 action**：必填项，用来描述允许或拒绝的操作。操作可以是 API（以 name 前缀描述）或者功能集（一组特定的 API ，以 permid 前缀描述）。
- **资源 resource**：必填项，描述授权的具体数据。

## DTS 的操作
在 CAM 策略语句中，您可以从支持 CAM 的任何服务中指定任意的 API 操作。对于 DTS，请使用以 name/dts: 为前缀的 API 。如果您要在单个语句中指定多个操作，请使用逗号将它们隔开，如下所示：
```
"action":["name/dts:action1","name/dts:action2"]
```

您也可以使用通配符指定多项操作。例如，您可以指定名字以单词"Describe"开头的所有操作，如下所示：
```
"action":["name/dts:Describe*"]
```

如果您要指定 DTS 中所有操作，请使用 * 通配符，如下所示：
```
"action"：["name/dts:*"]
```

## DTS 的资源路径
资源路径的一般形式如下：
```
 qcs::service_type::account:resource
```
- service_type：产品简称，此处为 dts。
- account：资源拥有者的主帐号信息，如 uin/32xxx546。
- resource：产品的具体资源详情，每个 DTS 任务（task）就是一个资源。

示例如下：
```
 "resource": ["qcs::dts::uin/32xxx546:task/dts-kf291vh3"]
```
其中，dts-kf291vh3 是 DTS 任务的 ID，在这里是 CAM 策略语句中的资源 resource。

## 示例
>?以下示例仅为展示 CAM 用法，一个 DTS 任务的完整流程及对应 API 请参见 [API 文档]( https://cloud.tencent.com/document/product/571/18135)。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "name/dts:DescribeAccessKeys"
            ],
            "resource": [
                "*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "name/dts:CreateAccess*"
            ],
            "resource": [
                "*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "name/dts:DescribeMigrateJobs"
            ],
            "resource": [
                "qcs::dts::uin/32xxx546:task/dts-kf291vh3"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "name/dts:CreateMigrateCheckJob"
            ],
            "resource": [
                "qcs::dts::uin/32xxx546:task/dts-kf291vh3"
            ]
        }
    ]
}
```

