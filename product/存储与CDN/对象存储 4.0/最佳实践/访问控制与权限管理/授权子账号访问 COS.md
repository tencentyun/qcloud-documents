## 概述

对于腾讯云对象存储资源，不同企业之间或同企业多团队之间，需要对不同的团队或人员配置不同的访问权限。您可通过 CAM（访问管理，以下简称 CAM）对存储桶或对象设置不同的操作权限，使得不同团队或人员能够相互协作。

首先，我们需要先了解几个关键概念：主账号、子账号（用户）和用户。CAM 的相关术语、配置详细描述请参见访问管理的 [词汇表](https://cloud.tencent.com/document/product/598/18564)。

#### 主账号
主账号又被称为开发商。用户申请腾讯云账号时，系统会创建一个用于登录腾讯云服务的主账号身份。主账号是腾讯云资源使用计量计费的基本主体。
主账号默认拥有其名下所拥有的资源的完全访问权限，包括访问账单信息，修改用户密码，创建用户和用户组以及访问其他云服务资源等。默认情况下，资源只能被主账号所访问，任何其他用户访问都需要获得主账号的授权。

#### 子账号（用户）和用户组
- 子账号是由主账号创建的实体，有确定的身份 ID 和身份凭证，拥有登录腾讯云控制台的权限。
- 子账号默认不拥有资源，必须由所属主账号进行授权。
 - 一个主账号可以创建多个子账号（用户）。
 - 一个子账号可以归属于多个主账号，分别协助多个主账号管理各自的云资源，但同一时刻，一个子账号只能登录到一个主账号下，管理该主账号的云资源。
- 子账号可以通过控制台切换开发商（主账号），从一个主账号切换到另外一个主账号。
 - 子账号登录控制台时，会自动切换到默认主账号上，并拥有默认主账号所授予的访问权限。
 - 切换开发商之后，子账号会拥有切换到的主账号授权的访问权限，而切换前的主账号授予的访问权限会立即失效。
- 用户组是多个相同职能的用户（子账号）的集合。您可以根据业务需求创建不同的用户组，为用户组关联适当的策略，以分配不同权限。
 
## 操作步骤
授权子账号访问 COS 分为三个步骤：创建子账号、对子账号授予权限、子账号访问 COS 资源。

### 步骤1：创建子账号
在 CAM 控制台可创建子账号，并配置授予子账号的访问权限。具体操作如下所示：
1. 登录 [CAM 控制台](https://console.cloud.tencent.com/cam)。
2. 选择【用户】>【用户列表】>【新建用户】，进入新建用户页面。
3. 单击【自定义创建】， 按照要求填写用户相关信息。
 - **用户名**：支持输入大小写英文字母、数字[即a-z,A-Z,0-9]，支持`@、._[]-:`。
 - **邮箱**：您需要为子用户添加邮箱来获取由腾讯云发出的绑定微信的邮件。
 - **访问方式**：选择编程访问和腾讯云控制台访问。
![](https://main.qcloudimg.com/raw/9f2b61fc4b9e682edbf9d0f0df33fb5b.jpg)
4. 根据系统提供的策略选择，可配置简单的策略，如 COS 的存储桶列表的访问权限，只读权限等。如需配置更复杂的策略，可进行 [对子账号授予权限](#.E6.AD.A5.E9.AA.A4.E4.BA.8C.EF.BC.9A.E5.AF.B9.E5.AD.90.E8.B4.A6.E5.8F.B7.E6.8E.88.E4.BA.88.E6.9D.83.E9.99.90) 步骤。
![](https://main.qcloudimg.com/raw/ca9aa51a9517ebe241881964095f16e7.jpg)
5. 确认输入的信息无误后，单击【完成】即可创建子账号。


<span id="对子账号授予权限"></span>
### 步骤2：对子账号授予权限
对子账号授予权限可通过 CAM，对子账号（用户）或用户组进行策略配置。
1. 登录 [CAM 控制台](https://console.cloud.tencent.com/cam)。
2. 选择【策略】>【新建自定义策略】>【按策略语法创建】，进入策略创建页面。
3. 可供选择的模版有**空白模板**和与 COS 相关联的**预设策略模板**，选择您需要授予子账号的策略模板，单击【下一步】。
![](https://main.qcloudimg.com/raw/9c60306242955be93fa0bfbd5cea2bda.jpg)
4. 输入便于您记忆的策略名称，若您选择**空白模板**，则需要输入您的策略语法，详情请参见 [策略示例](#策略示例)。您可将策略内容复制粘贴到【编辑策略内容】输入框内，单击【创建策略】。
![](https://main.qcloudimg.com/raw/880f49ec0df3199c2e301fd86b108580.png)
5. 创建完成后，将刚才已创建的策略关联到子账号。
![](https://main.qcloudimg.com/raw/481057a2b826bf038bffa4f49817b380.png)
6. 勾选子账号确定授权后，子账号即可根据权限范围访问 COS 资源。
![](https://main.qcloudimg.com/raw/2a4783ba4976aa7acb89347e75d1236b.png)

### 步骤3：子账号访问 COS 资源
COS 访问（API 或 SDK）需要如下资源：APPID、SecretId、SecretKey。
当使用子账号访问 COS 资源时，需要使用主账号的 APPID，子账号的 SecretId 和 SecretKey，您可以在访问管理控制台生成子账号的 SecretId 和 SecretKey。

1. 子账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi)  。
2. 在控制台右上方，将鼠标移至账号处，在下拉列表中，单击【切换用户身份】，切换对应的主账号（开发商账号）。
3. 登录后，选择【访问密钥】>【API 密钥管理】，按照提示进入 API 密钥管理页面。
4. 单击【新建密钥】，创建子账号的 SecretID 和 SecretKey，APPID 需由主账号提供。


>!
- 子账号需通过 XML API 或基于 XML API 的 SDK 访问 COS 资源。
- 子账号访问 COS 资源时，需要使用主账号的 APPID，子账号的 SecretId 和 SecretKey。

#### 基于 XML 的 Java SDK 访问示例
以基于 XML 的 Java SDK 命令行为例，需填入参数如下：
```
// 1 初始化身份信息
COSCredentials cred = new BasicCOSCredentials("<主账号APPID>", "<子账号SecretId>", "<子账号SecretKey>");
```

实例如下：
```
// 1 初始化身份信息
COSCredentials cred = new BasicCOSCredentials("1250000000", "AKIDasdfmRxHPa9oLhJp", "e8Sdeasdfas2238Vi");
```

#### COSCMD 命令行工具访问示例
以 COSCMD `config`命令行为例，需填入参数如下：
```sh
coscmd config -u <主账号 APPID> -a <子账号 SecretId> -s <子账号SecretKey>  -b <主账号 bucketname> -r <主账号  bucket 所属地域>
```
实例如下：
```sh
coscmd config -u 1250000000 -a AKIDasdfmRxHPa9oLhJp -s e8Sdeasdfas2238Vi -b examplebucket -r ap-beijing
```


<span id="策略示例"></span>
## 策略示例
以下提供几种典型场景的策略示例，在配置自定义策略时，您可将以下参考策略复制粘贴至输入框【编辑策略内容】，根据实际配置修改即可。更多 COS 常见场景的策略语法请参见 [CAM 产品文档](https://cloud.tencent.com/document/product/598/11083) 的**商用案例**部分。

### 为子账户配置读写权限
为子账户仅配置读写权限，具体策略如下所示：
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cos:*"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": "monitor:*",
            "resource": "*"
        }
    ]
}
```
### 为子帐户配置只读权限
为子账户仅配置只读权限，具体策略如下所示：
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
                "name/cos:List*",
                "name/cos:Get*",
                "name/cos:Head*",
                "name/cos:OptionsObject"
            ],
            "resource": "*",
            "effect": "allow"
        },
        {
            "effect": "allow",
            "action": "monitor:*",
            "resource": "*"
        }
    ]
}
```

### 为子账户配置某 IP 段的读写权限
本示例中限制仅 IP 网段为`192.168.1.0/24`和`192.168.2.0/24`的地址具有读写权限，如下所示。
更丰富的生效条件填写，请参见 [生效条件](https://cloud.tencent.com/document/product/598/10608)。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
    "cos:*"
            ],
            "resource": "*",
            "effect": "allow",
            "condition": {
                "ip_equal": {
                    "qcs:ip": ["192.168.1.0/24", "192.168.2.0/24"]
                }
            }
        }
    ]
}
```
