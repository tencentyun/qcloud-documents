## 功能简介
千帆玉符 IDaaS 是千帆应用连接器的重要组成部分，聚焦于企业各系统应用间统一用户、统一身份认证、单点登录等功能，实现一个账号登录所有应用。本文适用于客户用户数据已经同步至玉符 IDaaS 的场景，通过下文配置将玉符 IDaaS 作为千帆 aPaaS 用户数据源。



## 千帆玉符人员组织同步
1. 登录 [千帆 aPaaS 运行态首页](https://apaas.cloud.tencent.com/)，进入管理后台，单击【用户管理】。当租户企业管理员未进行人员组织初始化时，进入下图页面。对于用户管理的基本介绍可参考 [用户管理](https://cloud.tencent.com/document/product/1365/57571)。
 ![img](https://main.qcloudimg.com/raw/7b770a45bb124318933d60dc93235153.png)        
2. 单击【千帆玉符】进行信息填写。
 ![img](https://main.qcloudimg.com/raw/f392e51c4229d10a2d6c0f5ee9f23510.png)        
3. 当填写完信息后单击【下一步】后等待片刻即可完成通讯的同步。上图中需填写的信息获取方式请见下文。



## **获取玉符 Domain 和 Service Account**
1. 登录千帆玉符管理后台。
>?线下开通后，每位租户会有一个独立的登录链接，由工作人员进行提供。
 ![img](https://main.qcloudimg.com/raw/b0f87e203eae9c066382b5b991eb6f2c.png)        
2. 从地址栏获取 Domain 信息，并将其填入配置页面对应字段。例如：`https://apaas-test-admin.cig.tencentcs.com/#/，-admin` 前面的 apaas-test 即为 Domain。
 ![img](https://main.qcloudimg.com/raw/3967e9a1a5eda7074e60e3789ab87141.png)        
3. 联系玉符客服人员，根据所在租户的 Service Account 信息，并将其填入配置页面对应字段。



## 创建玉符 OIDC 类型应用
1. 登录千帆玉符管理后台，定位到“应用管理”。
>?线下开通后，每位租户会有一个独立的登录链接，由工作人员进行提供。
 ![img](https://main.qcloudimg.com/raw/8c45332448720d66ff5f0b27e8c2f873.png)        
2. 单击【添加应用】，选择“创建自定义应用”进入创建应用页面。
  ![img](https://main.qcloudimg.com/raw/30aab6ad45ca7d22845c9c4051d4e7f3.png)        
3. 选择 OpenID Connect 类型。
 ![img](https://main.qcloudimg.com/raw/7f386e64d5510d93e8ee0bbb649a3f37.png)        
 ![img](https://main.qcloudimg.com/raw/180cfc2d4c1c65fb87fce8473aae5bae.png)        
4. 填写应用基本信息，完成创建。
![img](https://main.qcloudimg.com/raw/ece0269b197caf580828f0c90a3bb54f.png)        



## 获取应用 Well-known 接口及 SecretId 和 SecretKey
1. 登录千帆玉符管理后台，单击“单点登录”中的【常规配置】。
  ![img](https://main.qcloudimg.com/raw/9588683fe4df33e40143dc89600d3d3a.png)        
2. 获取应用 Well-known 接口地址，并将其填入配置页面对应字段。
  ![img](https://main.qcloudimg.com/raw/9295231ae223238991f42272ebb2e54a.png)        
3. 获取应用 Client ID，并将其填入配置页面对应字段。
![img](https://main.qcloudimg.com/raw/35a71e1dda3d336200f30d282152ef4c.png)        
4. 获取应用 Client Secret，并将其填入配置页面对应字段。
  ![img](https://main.qcloudimg.com/raw/552cfb50c7c931f4bfa377f6bd792923.png)        
