## 操作场景
在腾讯云的实际使用中，通过 ABAC 的授权策略，我们可以使用标签来定义权限。将标签绑定到 CAM 子用户、角色以及具体的云资源，之后可以定义权限策略，这些策略使用标签条件键来根据请求身份的标签向其授予权限。当您使用标签控制对腾讯云资源的访问时，可通过对授权策略进行较少更改来实现团队和资源的变更，操作更加灵活。

本章节将详细说明如何为员工在 CAM 中创建一个带有标签的 CAM 角色 ，以及支持通过带入角色的属性拥有访问与其标签匹配的资源的权限策略。当员工通过该角色向腾讯云发出请求时，将根据带入的角色标签和资源标签是否匹配来授予权限，实现仅允许员工查看或操作其工作需要的资源。

### 使用示例
假设在游戏公司 A 中，有两个项目 webpage 和 app，其中员工 m 为 webpage 的开发员工，员工 n 为 app 的开发员工，在创建授权策略时，需要保证不同团队内的员工能够访问其工作所需的资源，同时随着公司发展要考虑后续的扩展性。

可以通过使用资源标签和 CAM 角色标签来为支持 ABAC 策略的产品创建授权策略。当您的员工希望通过联合身份访问到腾讯云中时，其属性将应用到腾讯云中的角色标签中。然后，您可以使用 ABAC 来允许或拒绝基于这些属性的访问。
>?
>- 通过 [支持标签的产品](https://cloud.tencent.com/document/product/651/30727)，了解哪些产品支持基于标签的授权。
>- 通过 [生效条件概述](https://cloud.tencent.com/document/product/598/73088)，了解授权策略中支持哪些标记条件键。

我们根据上述项目和团队，做以下标签定义：
- game-project = web（对应 web 项目）
- game-project = app（对应 app 项目）
- web = dev（对应 web 项目开发人员）
- app = dev（对应 app 的开发人员）


### 实现原理
1. 员工使用 IAM 用户凭证进行登录，然后扮演其团队和项目的 CAM 角色。
2. 将向相同岗位的角色附加同一策略，根据标签来实现允许或拒绝操作。


### 验证场景
假设有两台云服务器 ins-78qewdr8（标签 game-project:app）和 ins-7txjj4a6（标签 game-project:web），分别属于 app 和 webpage 项目。
- 验证点1：不同项目的员工使用不同的 CAM 子用户登录后，如何实现不同员工只能访问到其所属项目下的云服务器。
- 验证点2：假设员工岗位变更，员工 n 也需要项目 webpage 的权限，如何快速调整权限。
- 验证点3：假设公司新增加一个 H5 类的项目，如何快速为员工授予新项目的权限。


## 操作步骤
### 步骤1：创建测试 CAM 子用户
1. 创建名为 access-assume-role 的自定义策略，策略内容为“当带入身份的标签与角色标签匹配时，允许带入 ABAC 角色”。
>?创建 CAM 策略的详细操作，请参考 [创建角色](https://cloud.tencent.com/document/product/598/19381)。
>
```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "sts:AssumeRole"
            ],
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "game&${qcs:principal_tag_value}"
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": [
                "cam:ListUserTags",
                "cam:ListLoginRoles"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

2. 创建 CAM 子用户 m-developer 和 n-sysmanager，并为子用户绑定 access-assume-role 的授权策略，并为子用户绑定下述标签。
>?创建 CAM 子用户的详细操作，请参考 [新建子用户](https://cloud.tencent.com/document/product/598/13674)。
>
<table>
<thead>
<tr>
<th>子用户名称</th>
<th>关联标签</th>
</tr>
</thead>
<tbody><tr>
<td>m-developer</td>
<td>web=dev</td>
</tr>
<tr>
<td>n-developer</td>
<td>app=dev</td>
</tr>
</tbody></table>


### 步骤2：创建 ABAC 策略
1. 创建名为 access-resource-project（以cvm产品为例子）的自定义策略,策略内容如下：
```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": "cvm:*",
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:request_tag": [
                       "game-project&${qcs:principal_tag_key}"
                    ]
                }
            }
        },
        {
            "effect": "allow",
            "action": "cvm:*",
            "resource": "*",
            "condition": {
                "for_any_value:string_equal": {
                    "qcs:resource_tag": [
                        "game-project&${qcs:principal_tag_key}"
                    ]
                }
            }
        },
         {
            "effect": "allow",
            "action": [
                "vpc:DescribeVpcEx",
                "vpc:DescribeSubnetEx",
                "vpc:DescribeNetworkInterfaces",
                "cvm:DescribeDiskSecurityConfigurations",
                "cvm:DescribeCbsStorages",
                "tag:DescribeTagKeys",
                "tag:DescribeTagValues"
            ],
            "resource": [
                "*"
            ]
        }
        
    ]
}
```
2. 创建角色 access-developer-role，关联上述策略，并绑定如下标签。
>?创建 CAM 策略的详细操作，请参考 [创建角色](https://cloud.tencent.com/document/product/598/19381)。
>
<table>
<thead>
<tr>
<th>CAM 角色名称</th>
<th>关联标签</th>
</tr>
</thead>
<tbody><tr>
<td>access-developer-role</td>
<td>game=dev</td>
</tr>
</tbody></table>


### 步骤3：场景验证

#### 验证点1：使用不同的子用户登录后，只能访问到对应项目下的云服务器
1. 使用子用户 m-developer 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，在控制台右上角，单击账号下的**切换角色**。
![](https://qcloudimg.tencent-cloud.cn/raw/0087ae2927998b74ec3590cb98c6a4f9.png) 
2. 在切换角色页面，应用选择 web（子用户 m-developer 的标签 value），角色选择 access-developer-role，单击**切换角色**。   
![](https://qcloudimg.tencent-cloud.cn/raw/b80b6ab6e4001fd2356819e68223524e.png)
3. 以角色身份登录腾讯云控制台，进入 CVM [**实例**](https://console.cloud.tencent.com/cvm/instance/index?rid=1) 页面。
在 CVM 产品控制台，若仅可以查看到 ins-7txjj4a6（标签 game-project:web），则符合预期。
![](https://qcloudimg.tencent-cloud.cn/raw/832430ec3fc305e0dee6bfce6f799653.png)    
4. 切换身份，使用子用户 n-developer 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，登录后切换角色，应用选择 app，角色选择 access-developer-role，显示名称为 n-developer-app，单击**切换角色**。
![](https://qcloudimg.tencent-cloud.cn/raw/7a2477bc80b952490221cd387efd353f.png)         
5. 以角色身份进入腾讯云控制台，进入 CVM [**实例**](https://console.cloud.tencent.com/cvm/instance/index?rid=1) 页面。
在 CVM 产品控制台，若仅能查看云服务器 ins-78qewdr8（标签 game-project:app），则符合预期。
![](https://qcloudimg.tencent-cloud.cn/raw/c322e4bfcfb67b7b357c4fba000e10d1.png)        



#### 验证点2：假设岗位变更，员工 n 也需要项目 webpage 的权限，该如何设置

当前场景下，我们仅需要在 [访问管理控制台](https://console.cloud.tencent.com/cam) 的用户详情中，为员工 n 对应的 CAM 子用户 n-developer 增加标签 app:web 即可。
![](https://qcloudimg.tencent-cloud.cn/raw/0060ff47d34cfaf1533735eaec45777f.png)       


1. 使用子用户 n-developer 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，在控制台右上角，单击账号下的**切换角色**。
2. 在切换角色页面，应用选择 web，角色选择access-developer-role，别名为 n-developer-web，单击**切换角色**。
![](https://qcloudimg.tencent-cloud.cn/raw/76f16e8a33dbb9374de2caa4f59fcc3c.png)    
3. 以角色身份登录腾讯云控制台，进入 CVM [**实例**](https://console.cloud.tencent.com/cvm/instance/index?rid=1) 页面。
在 CVM 产品控制台，若仅能查看云服务器 ins-7txjj4a6（标签 game-project:web），则符合预期。
![](https://qcloudimg.tencent-cloud.cn/raw/4132850abcee80d2b030c21042c82b5b.png)      





#### 验证点3：假设公司新增加一个 H5 类的项目，该如何调整权限策略适配

公司新增 H5 项目后，如果我们需要增加 H5 项目的开发权限，则无需对策略本身进行变更，仅需要：
1. 为 H5 项目的开发同事创建新的子用户。
2. 为子用户绑定 H5 项目对应的标签，关联 access-assume-role 策略即可。
