## 简介

COS 控制台提供了按存储桶标签筛选存储桶列表的功能，该功能依赖于腾讯云标签服务。
假设企业帐号 CompanyExample（OwnerUin 为100000000001，Owner_appid 为1250000000）下有一个子账号 Developer，企业帐号 CompanyExample 需要授予该子账号拥有拉取标签列表操作权限。
下面将为您详细介绍如何进行授权操作。



## 相关说明
如您需要授予子账户在控制台上拉取标签列表的权限，需要授予子账户`GetResourceTags`和`GetResourceByTags`操作权限，同样需要通过新建自定义策略实现。这里可以根据业务需要，通过策略生产器或者策略语法创建。


## 操作步骤

1. 使用企业账号 CompanyExample 登录到 [访问管理控制台](https://console.cloud.tencent.com/cam/policy)，进入到策略配置页面。
2. 授予子账号 Developer 拥有拉取标签列表的权限，有以下两种方式：


#### 通过策略生成器创建

1. 进入 [访问管理](https://console.cloud.tencent.com/cam/policy) 策略配置页面。
2. 单击【新建自定义策略】>【按策略生成器创建】。
3. 您可以根据业务需要勾选相应的操作授予子账户`GetResourceTags`和`GetResourceByTags`的操作权限，并将该策略关联至相应的子账号下。如下图所示。
![](https://main.qcloudimg.com/raw/36bde76ee88688e37d6effe1501dffd1.png)

#### 通过策略语法创建

1. 进入 [访问管理](https://console.cloud.tencent.com/cam/policy) 策略配置页面。
2. 单击【新建自定义策略】>【按照策略语法创建】。
3. 您可以选择空白模板或者已有的标签模板创建。
![](https://main.qcloudimg.com/raw/a217975ec777820eb21480db22b19fca.png)
4. 单击【下一步】，输入策略名称，并对模板中的策略语法进行修改，将`action`修改为指定的标签`action`名称。策略语法如下所示。
```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "name/tag:GetResourceTags",
                "name/tag:GetResourcesByTags"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```
