
对于腾讯云COS对象存储资源，不同企业之间或同企业多团队之间，需要对不同的团队或人员配置不同的访问权限。可通过CAM（访问控制）进行配置，实现对不同团队或人员，以存储桶/对象粒度进行不同操作的权限设置。

总的来说，配置分为三步：创建子账号，配置权限，子账号访问。

首先，描述几个关键概念。

## 名词解释
CAM（访问控制）相关术语、配置详细描述请查看[CAM概述](https://cloud.tencent.com/document/product/598/10583)。
### 根账号

根账号又被称为开发商。用户申请腾讯云账号时，系统会创建一个用于登陆腾讯云服务的根账号身份。根账号是腾讯云资源使用计量计费的基本主体。

根账号默认拥有其名下所拥有的资源的完全访问权限，包括访问账单信息，修改用户密码，创建用户和用户组以及访问其他云服务资源等。默认情况下，资源只能被根账号所访问，任何其他用户访问都需要获得根账号的授权。

### 子账号（用户）和用户组

子账号是由根账号创建的实体，有确定的身份 ID 和身份凭证，拥有登录腾讯云控制台的权限。子账号默认不拥有资源，必须由所属根账号进行授权。一个根账号可以创建多个子账号(用户)。一个子账号可以归属于多个根账号，分别协助多个根账号管理各自的云资源，但同一时刻，一个子账号只能登录到一个根账号下，管理该根账号的云资源。
子账号可以通过控制台切换开发商（根账号），从一个根账号切换到另外一个根账号。子账号登陆控制台时，会自动切换到默认根账号上，并拥有默认根账号所授予的访问权限。切换开发商之后，子账号会拥有切换到的根账号授权的访问权限，而切换前的根账号授予的访问权限会立即失效。
用户组是多个相同职能的用户（子账号）的集合。您可以根据业务需求创建不同的用户组，为用户组关联适当的策略，以分配不同权限。

## 子账号权限配置

### 步骤一：创建子账号

在CAM（访问控制）控制台可创建子账号，并配置授予子账号的访问权限。具体操作如下所示：

1. 登陆CAM（云访问管理）[控制台](https://console.cloud.tencent.com/cam)，点击左侧菜单栏【用户管理】，单击页面按钮【新建用户】：
  ![image](http://mypics-1251729613.cosgz.myqcloud.com/1.png)
2. 按照要求填写用户相关信息。
  ![image]( http://mypics-1251729613.cosgz.myqcloud.com/2.png)
  注：“登陆帐号”为可登陆腾讯云的账号，可添加三种类型账号为子账号，添加方式如下：
 - 邮箱：请输入已注册腾讯云的邮箱或对应账号ID
 - 微信公众号：请输入其在腾讯云的账号ID
 - QQ号：请输入QQ号或其账号ID

3. 根据系统提供的策略选择，可配置简单的策略，如COS的读写权限，只读权限。如需配置更复杂的策略，可参考步骤二。
  ![image](http://mypics-1251729613.cosgz.myqcloud.com/3.png)

### 步骤二：对子账号授予权限


对子账号授予权限可通过CAM，对子账号（用户）或用户组进行策略配置，本文将通过实例说明几种场景：
- 使用COS对象存储时，如何给子帐户配置读写权限？
- 使用COS对象存储时，如何给子帐户配置只读权限？
- 使用COS对象存储时，如何仅对某IP段设置读写权限？

1. 登陆CAM（云访问管理）[控制台](https://console.cloud.tencent.com/cam)，点击左侧菜单栏【策略管理】，点击标签页【自定义策略】，单击按钮【新建自定义策略】：
  ![image](http://mypics-1251729613.cosgz.myqcloud.com/4.png)
2. 选择【按策略语法创建】
  ![image](http://mypics-1251729613.cosgz.myqcloud.com/5.png)
3. 可选择空白模板和已有的COS模板，进行再编辑，常见场景的策略请查看，可将其拷贝至输入框【编辑策略内容】。
  ![image](http://mypics-1251729613.cosgz.myqcloud.com/6.png)
  ![image](http://mypics-1251729613.cosgz.myqcloud.com/7.png)
4. 创建完成后，可将策略关联到子帐户。
  ![image](http://mypics-1251729613.cosgz.myqcloud.com/8.png)
  ![image](http://mypics-1251729613.cosgz.myqcloud.com/9.png)
  完成子帐户授权，子账号即可根据权限范围访问COS资源。

## 常见场景的策略

在【自定义策略】中，可将以下参考策略拷贝至输入框【编辑策略内容】，根据实际配置修改即可。

### 为子帐户配置读写权限

例：对子帐户仅配置读写权限，如下所示。

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

例：对子帐户仅配置只读权限，如下所示。

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
### 为子帐户配置某IP段的读写/只读权限

例：限制仅IP网段为“192.168.1.0/24”和“192.168.2.0/24”的地址才能访问，如下所示。
更丰富的生效条件填写，可查看[生效条件](https://cloud.tencent.com/document/product/598/10608)。
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

### 步骤三：子账号访问根账号COS资源

COS访问（API/SDK）需要如下资源：APPID、SecretID、SecretKey。
当使用子账号访问COS资源时，需要使用根账号的APPID，子账号的SecretId和SecretKey。子账号登陆腾讯云控制台时，需选择对应的根帐号（开发商账号）。
![image](http://mypics-1251729613.cosgz.myqcloud.com/10.png)

登陆后，单击按钮【新建密钥】，即可创建子账号的SecretID和SecretKey，APPID需由根帐号提供。
![image](http://mypics-1251729613.cosgz.myqcloud.com/11.png)
![image](http://mypics-1251729613.cosgz.myqcloud.com/12.png)

*注: 

1. 子账号需通过XML API或基于XML API的SDK访问。
2. 需要使用根账号的APPID，子账号的SecretId和SecretKey。

#### 基于XML的JAVA SDK访问实例
以基于XML的JAVA SDK命令行为例，需填入参数如下：

```
// 1 初始化身份信息
COSCredentials cred = new BasicCOSCredentials("<主账号APPID>", "<子账号SecretId>", "<子账号SecretKey>");
```

实例如下：

```
// 1 初始化身份信息
COSCredentials cred = new BasicCOSCredentials("1250000011", "AKIDasdfmRxHPa9oLhJp9wqwraCdtzvfPasdfaqW", "e8Sdeasdfas2238ViAXjpkU6XloeN2Wpxue");
```

#### COSCMD命令行工具访问实例

以COSCMD config命令行为例，需填入参数如下：

```
coscmd config -u <主账号APPID> -a <子账号SecretId> -s <子账号SecretKey>  -b <主账号bucketname> -r <主账号bucketname地域>
```

实例如下：

```
coscmd config -u 1250000011 -a AKIDasdfmRxHPa9oLhJp9wqwraCdtzvfPasdfaqW -s e8Sdeasdfas2238ViAXjpkU6XloeN2Wpxue -b bucket1 -r ap-beijing
```

