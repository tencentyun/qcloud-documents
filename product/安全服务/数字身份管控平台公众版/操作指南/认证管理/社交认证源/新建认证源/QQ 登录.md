## 操作场景
支持用户通过 QQ 认证的方式，使用 QQ 身份快速登录应用。

## 新建认证源
1. 登录 [数字身份管控平台（公众版）控制台](https://console.cloud.tencent.com/ciam)，在左侧导航栏，选择**认证管理** > **社交认证源**，进入社交认证源页面。
2. 在社交认证源页面，单击**新建认证源**，进入新建认证源页面。
 ![](https://main.qcloudimg.com/raw/24ecbeb720a568efe8101f756e072af6.png)
3. 在新建认证源页面，选择 **QQ 登录**，单击**下一步**。
4. 在新建认证源页面，设置相关参数后，单击**确定**，即可创建认证源。
![](https://main.qcloudimg.com/raw/5471e335d1051342d220be2d0e45637c.png)
参数说明：
 - 认证源图标：用于在列表和门户中展示，用户可单击**重新上传**，代替默认图标。
 - 认证源名称：用户标识认证源，必填项。
 - 认证源描述：认证源的简单描述，非必填。
 - APP ID：访问 [QQ 开放平台](https://connect.qq.com/index.html) > **应用管理** > **创建应用**，可获得 APP ID(即clientID)。
 - APP Key：访问 [QQ 开放平台](https://connect.qq.com/index.html) > **应用管理** > **创建应用**，可获得 APP Key(即client secret)。
 - 属性映射：用于将 QQ 认证过程中返回的属性映射到平台定义的属性，默认包含 openid 和 unionid 两条不可编辑的属性映射；可单击**新增**添加新的映射关系，认证源属性名称为 QQ 认证源属性，平台属性为属性自定义中的属性。

## 创建应用
在 [QQ 开放平台](https://connect.qq.com/index.html) 创建应用详细操作请参见 [创建应用文档](https://wiki.connect.qq.com/__trashed-2)。如果使用 CIAM 提供的域名，资料填写时需要按以下要求填写：
![](https://qcloudimg.tencent-cloud.cn/raw/b0c0ab4e1b37097236c2caabd2e9a1c1.png)
**参数说明**

| 参数名称     | 填写详情                                                     |
| ------------ | ------------------------------------------------------------ |
| 网站域名     | https://{域名前缀}.prod.tencentciam.com                      |
| 网站回调地址 | https://{域名前缀}.prod.tencentciam.com/login/oauth2/code/{认证源id} |
| 提供方       | 深圳市腾讯计算机系统有限公司                                 |
| 网站备案号   | 粤B2-20090059                                                |

>?其中{} 为占位符，需要替换为实际内容。
>
