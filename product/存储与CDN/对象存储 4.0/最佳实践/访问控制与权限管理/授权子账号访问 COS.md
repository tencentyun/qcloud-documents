对于腾讯云对象存储资源，不同企业之间或同企业多团队之间，需要对不同的团队或人员配置不同的访问权限。您可通过 CAM（访问管理，以下简称 CAM）进行配置，实现对不同团队或人员，以存储桶/对象粒度进行不同操作的权限设置。
总的来说，配置分为三步：创建子账号，对子账号授予权限，子账号访问。

首先，我们需要先了解几个关键概念。
## 名词解释
CAM 相关术语、配置详细描述请查看 [CAM 概述](/doc/product/598/10583)。
### 根账号
根账号又被称为开发商。用户申请腾讯云账号时，系统会创建一个用于登录腾讯云服务的根账号身份。根账号是腾讯云资源使用计量计费的基本主体。
根账号默认拥有其名下所拥有的资源的完全访问权限，包括访问账单信息，修改用户密码，创建用户和用户组以及访问其他云服务资源等。默认情况下，资源只能被根账号所访问，任何其他用户访问都需要获得根账号的授权。

### 子账号（用户）和用户组
- 子账号是由根账号创建的实体，有确定的身份 ID 和身份凭证，拥有登录腾讯云控制台的权限。
- 子账号默认不拥有资源，必须由所属根账号进行授权。
 - 一个根账号可以创建多个子账号（用户）。
 - 一个子账号可以归属于多个根账号，分别协助多个根账号管理各自的云资源，但同一时刻，一个子账号只能登录到一个根账号下，管理该根账号的云资源。
- 子账号可以通过控制台切换开发商（根账号），从一个根账号切换到另外一个根账号。
 - 子账号登录控制台时，会自动切换到默认根账号上，并拥有默认根账号所授予的访问权限。
 - 切换开发商之后，子账号会拥有切换到的根账号授权的访问权限，而切换前的根账号授予的访问权限会立即失效。
- 用户组是多个相同职能的用户（子账号）的集合。您可以根据业务需求创建不同的用户组，为用户组关联适当的策略，以分配不同权限。

## 子账号权限配置
### 步骤一：创建子账号
在 CAM 控制台可创建子账号，并配置授予子账号的访问权限。具体操作如下所示：
1. 登录 [CAM控制台](https://console.cloud.tencent.com/cam)，单击左侧菜单栏【用户管理】，单击页面按钮【新建用户】：
 ![子账户1](//mc.qcloudimg.com/static/img/5d9194888617f10bfde81afa01c69e0b/image.png)
 
2. 按照要求填写用户相关信息。
 ![子账户2](//mc.qcloudimg.com/static/img/97dbdb848557f0195f90e1a78561eb37/image.png)
> **注意：**
> “登录帐号”为可登录腾讯云的账号，可添加三种类型账号为子账号，添加方式如下：
 - 邮箱：请输入已注册腾讯云的邮箱或对应账号 ID；
 - 微信公众号：请输入其在腾讯云的账号 ID；
 - QQ号：请输入QQ号或其账号 ID。

3. 根据系统提供的策略选择，可配置简单的策略，如 COS 的读写权限，只读权限等。如需配置更复杂的策略，可参考 [步骤二：对子账号授予权限](#对子账号授予权限)。
![子账户3](//mc.qcloudimg.com/static/img/8c3be83e576d892c99b90190d5f5c0b2/image.png)

<span id="对子账号授予权限"></span>
### 步骤二：对子账号授予权限
对子账号授予权限可通过 CAM，对子账号（用户）或用户组进行策略配置。
1. 登录 [CAM 控制台](https://console.cloud.tencent.com/cam)，单击左侧菜单栏【策略管理】，单击标签页【自定义策略】，单击按钮【新建自定义策略】：
![4](//mc.qcloudimg.com/static/img/c1edfdc87bc078d8bc8f0fb052313d28/image.png)
2. 选择【按策略语法创建】，进入创建页面。
![5](//mc.qcloudimg.com/static/img/94801671fcdff7b80dc973d9ee0e1165/image.png)
3. 可供选择的模版有空白模板和已有的 COS 模板，您可以根据实际情况进行选择。
![6](//mc.qcloudimg.com/static/img/8ee0f66634765849bb90a1a2d60806a5/image.png)
4. 编辑策略，COS 常见场景的策略请参见 [CAM 产品文档](/doc/product/598) 的商用案例部分。您可将策略内容复制粘贴到【编辑策略内容】输入框内。
![7](//mc.qcloudimg.com/static/img/2a5ce2ce4863f1a537dc74d45284ee5d/image.png)
5. 创建完成后，可将策略关联到子账户。
![8](//mc.qcloudimg.com/static/img/3517b05ee79c818883d1ecf96dbbad89/image.png)
完成子账户授权，子账号即可根据权限范围访问 COS 资源。
![9](//mc.qcloudimg.com/static/img/606cdbcdccb90cf65dbc8826bc7d92da/image.png)
 

本文还通过以下策略示例说明几种典型场景，详情参见 [策略示例](#策略示例)：
- 使用 COS 对象存储时，如何给子账户配置读写权限？
- 使用 COS 对象存储时，如何给子账户配置只读权限？
- 使用 COS 对象存储时，如何仅对某 IP 段设置读写权限？

### 步骤三：子账号访问根账号 COS 资源
COS 访问（API/SDK）需要如下资源：APPID、SecretId、SecretKey。
当使用子账号访问 COS 资源时，需要使用根账号的 APPID，子账号的 SecretId 和 SecretKey，您可以在访问管理控制台创建子账号的 SecretId 和 SecretKey。
1. 子账号登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi)  时，需选择对应的根账号（开发商账号）。
![10](//mc.qcloudimg.com/static/img/7f109890f04a9f57f3b8c924b3788e2d/image.png)
2. 登录后，单击按钮【新建密钥】，即可创建子账号的 SecretID 和 SecretKey，APPID 需由根账号提供。
![11](//mc.qcloudimg.com/static/img/294e294ef54662dedf57af975b7bea75/image.png)


> **注意：**
- 子账号需通过 XML API 或基于 XML API 的 SDK 访问 COS 资源。
- 子账号访问 COS 资源时，需要使用根账号的 APPID，子账号的 SecretId 和 SecretKey。

#### 基于 XML 的 JAVA SDK 访问示例
以基于 XML 的 JAVA SDK 命令行为例，需填入参数如下：
```
// 1 初始化身份信息
COSCredentials cred = new BasicCOSCredentials("<主账号APPID>", "<子账号SecretId>", "<子账号SecretKey>");
```

实例如下：
```
// 1 初始化身份信息
COSCredentials cred = new BasicCOSCredentials("1250000011", "AKIDasdfmRxHPa9oLhJp9wqwraCdtzvfPasdfaqW", "e8Sdeasdfas2238ViAXjpkU6XloeN2Wpxue");
```

#### COSCMD 命令行工具访问示例
以 COSCMD `config`命令行为例，需填入参数如下：
```
coscmd config -u <主账号APPID> -a <子账号SecretId> -s <子账号SecretKey>  -b <主账号bucketname> -r <主账号bucketname地域>
```
实例如下：
```
coscmd config -u 1250000011 -a AKIDasdfmRxHPa9oLhJp9wqwraCdtzvfPasdfaqW -s e8Sdeasdfas2238ViAXjpkU6XloeN2Wpxue -b bucket1 -r ap-beijing
```
<span id="策略示例"></span>
## 策略示例
在配置自定义策略时，您可将以下参考策略复制粘贴至输入框【编辑策略内容】，根据实际配置修改即可。

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
更丰富的生效条件填写，可查看 [生效条件](/doc/product/598/10608)。
```
{
    "version": "2.0",
    "statement": [
        {
            "action": [
	cos:*
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
