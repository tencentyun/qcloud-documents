## 操作场景
数据安全网关支持通过 OTP 认证方式登录。开启 OTP 服务后，将通过用户名和动态口令登录数据安全网关。OTP 认证方式支持两种，本地 OTP 和第三方 OTP。本文为您详细介绍如何配置 OTP 认证。

## 操作步骤
### 本地 OTP 认证配置
#### 开启本地 OTP 服务
1. 登录腾讯云 [数据安全网关控制台](https://console.cloud.tencent.com/cds/dasb)，并使用管理员账号登录数据安全网关。
2. 选择【系统参数】>【服务】>【认证配置】>【OTP 服务配置】，进入 OTP 服务配置界面。
3. 勾选 OTP 服务开关和本地 OTP 服务。
![](https://main.qcloudimg.com/raw/c66258e82bceb07c93d5064c0fdd1751.png)
4. 单击【保存】，开启本地 OTP 服务。
 
#### 设置用户认证方式
1. 选择【安全设置】>【设置认证方式】>【选择用户】>【设置用户认证方式】，进入用户登录认证方式配置页面。
![](https://main.qcloudimg.com/raw/d267666269ad6e1a4e9a07570ba8b6d9.png)
2. 勾选 OTP 认证（一次性口令），单击【保存】。


#### 下载客户端绑定用户
1. 手机端下载谷歌身份验证器，或在微信小程序里搜索谷歌动态口令验证字段。
2. 使用验证器扫描用户二维码（若无法扫描可手动输入标识码）。
3. 选择【用户管理】>【选择用户】>【维一身份标识】。
![](https://main.qcloudimg.com/raw/e77ef46edcc2195ae68207eec30196c6.png)
4. 绑定用户后将生成随机动态验证码。
![](https://main.qcloudimg.com/raw/95e16f85fae35c6bdc879a4ec635e71c.png)

#### 登录验证
1. 打开数据安全网关登录页面。
2. 输入用户名及动态口令登录。
![](https://main.qcloudimg.com/raw/151a527a86cec9abb55713640e1a8f97.png)

### 第三方 OTP 认证配置
#### 开启第三方 OTP 服务
1. 登录腾讯云 [数据安全网关控制台](https://console.cloud.tencent.com/cds/dasb)，并使用管理员账号登录数据安全网关。
2. 选择【系统参数】>【服务】>【认证配置】>【OTP 服务配置】，进入 OTP 服务配置界面。
3. 勾选服务开启和第三方 OTP 服务，并输入服务器信息。
 - OTP 服务器主机地址：填写真实的 OTP 服务器主机地址。
 - OTP 服务器备机地址：OTP 备机地址，可不填。
 - OTP 认证端口：默认的 OTP 端口为1812，请根据实际环境填写。
 - OTP 认证方法：请根据实际环境填写。例如 PAP。
 - 通信密钥：OTP 认证密码。请根据实际环境填写。
 ![](https://main.qcloudimg.com/raw/8a427abb0c7de1e7ae31a3d9bbad77bd.png)
 
#### 设置用户认证方式
1. 选择【安全设置】>【设置认证方式】>【选择用户】>【设置用户认证方式】，进入用户登录认证方式配置页面。
![](https://main.qcloudimg.com/raw/d267666269ad6e1a4e9a07570ba8b6d9.png)
2. 勾选 OTP 认证（一次性口令），单击【保存】。
 
#### 登录验证
1. 打开数据安全网关登录页面。
2. 输入用户名及第三方动态口令登录。
![](https://main.qcloudimg.com/raw/151a527a86cec9abb55713640e1a8f97.png)
 
