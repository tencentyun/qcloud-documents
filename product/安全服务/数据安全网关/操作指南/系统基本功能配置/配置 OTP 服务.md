## 操作场景
堡垒机支持运维用户使用动态口令（OTP）认证进行登录，使用 OTP 认证之前需先配置 OTP 服务，下面将为您详细介绍如何在堡垒机配置 OTP 服务。




## 操作步骤

堡垒机支持 [本地 OTP 服务](#.E6.9C.AC.E5.9C.B0-otp-.E6.9C.8D.E5.8A.A1) 和 [第三方 OTP 服务](#.E7.AC.AC.E4.B8.89.E6.96.B9-otp-.E6.9C.8D.E5.8A.A1)。本地 OTP 服务为堡垒机系统内建 OTP 服务，并提供微信小程序“数盾OTP”用于获取登录口令。第三方 OTP 服务需要额外的 OTP 服务器。




#### 本地 OTP 服务

1. 登录腾讯云 [堡垒机控制台](https://console.cloud.tencent.com/cds/dasb)，并使用管理员账号登录堡垒机。
2. 单击【系统参数】>【认证配置】>【OTP 服务配置】，进入 OTP 服务配置页面。
3. 勾选 OTP 服务开关，单击【本地 OTP 服务】，如下图所示。
![](https://main.qcloudimg.com/raw/3f663acb77e687c677eee37e30c524ea.png)
4. 单击【保存】，即可完成本地 OTP 服务配置。
5. 用户认证配置及如何使用“数盾OTP”小程序，请参见 [OTP 认证](https://cloud.tencent.com/document/product/1025/35133#.E8.AE.BE.E7.BD.AE.E7.94.A8.E6.88.B7.E8.AE.A4.E8.AF.81.E6.96.B9.E5.BC.8F)。



#### 第三方 OTP 服务

1. 登录腾讯云 [堡垒机控制台](https://console.cloud.tencent.com/cds/dasb)，并使用管理员账号登录堡垒机。
2. 单击【系统参数】>【认证配置】>【OTP 服务配置】，进入 OTP 服务配置页面。
3. 勾选 OTP 服务开关，单击【第三方 OTP 服务】，并配置以下信息。
 - **OTP 服务器主机地址**：填写真实的 OTP 服务器主机地址。
 - **OTP 服务器备机地址**：OTP 备机地址，可不填。
 - **OTP 认证端口**：默认的 OTP 端口为1812，请根据实际环境填写。
 - **OTP 认证方法**：请根据实际环境填写。例如 PAP。
 - **通信密钥**：OTP 认证密码。请根据实际环境填写。
![](https://main.qcloudimg.com/raw/0d587d9986c7f37cd085d43b463dbf88.png)
4. 单击【保存】，即可完成 OTP 服务配置。



## 相关操作

#### 初始化配置

在管理页面，单击【初始化】，系统将清除已配置的信息，并恢复至默认值。
