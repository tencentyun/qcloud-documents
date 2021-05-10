

认证流程如下：
 ![](https://main.qcloudimg.com/raw/31fb5ea513ee05956b514ff2e68ad424.png)

## 创建导入账户
### 在 LDAP（AD）创建账户
![](https://main.qcloudimg.com/raw/851aa39fce7874d07a95e0b9d6bb7a2b.png)

### 导入 LDAP（AD）账户到数字身份管控平台（员工版）
1. 登录 [数字身份管控平台（员工版）控制台](https://console.cloud.tencent.com/eiam)，在左侧导航栏，选择【用户管理】>【组织机构管理】。
2. 在组织机构管理页面，单击【配置LDAP/AD】，配置完成后，将 LDAP（AD）中的账户数据导入到数字身份管控平台（员工版）平台中。
![](https://main.qcloudimg.com/raw/fbdf9f005ddd9785bee8a1a70a7c3328.png)

## 添加 LDAP（AD）认证源
1. 登录 [数字身份管控平台（员工版）控制台](https://console.cloud.tencent.com/eiam)，在左侧导航栏，单击【认证源管理】，在认证源管理页面，单击【新建认证源】。
![](https://main.qcloudimg.com/raw/24111c2168ea678db4f3698865fb0bb0.png)
2. 在选择认证源模板页面，选择 LDAP 或 AD 认证源，单击【下一步】。
3. 在编辑认证源信息页面，设置相关信息，单击【确定】。
![](https://main.qcloudimg.com/raw/a7074f12a9d2077dfd2ec6c0fd0710e4.png)

## 登录数字身份管控平台（员工版）门户
 LDAP（AD）种的账户需要同步数字身份管控平台后，才能使用 LDAP 认证源进行登录认证。
 用户输入 LDAP（AD）中的账户和密码时，会先检验登录的这个账户是否在平台中存在，如果存在，再传递账户到 LDAP 中去认证，如果不存在，不会进行下面的操作。
 ![](https://main.qcloudimg.com/raw/dc0152e93af2357b8a6c1d41d9ec666f.png)
 
