## 前提条件
企业购买了 SIP 会议室连接器许可，才可以创建和管理 SIP 注册账号，了解更多，请访问：[会议室连接器](https://cloud.tencent.com/document/product/1095/50022)。
本文将介绍创建 SIP 注册账号的操作步骤以及管理 SIP 注册账号的操作。

## 创建 SIP 注册账号
1. 登录腾讯会议企业管理平台
使用企业账号登录 [腾讯会议企业管理平台](https://meeting.tencent.com)，然后访问**企业管理** > **会议室连接器** > **H.323/SIP 账号管理** > **SIP 页面**。
![](https://qcloudimg.tencent-cloud.cn/raw/ca7fe38615431398a0c79f7451b5ae11.png)
2. 注册服务地址和企业账号后缀
SIP 终端注册到腾讯会议的会议室连接器服务地址是：sip.qqmra.com。
系统会为企业创建默认的企业账号后缀，在创建SIP注册账号之前，也可以根据需要对账号后缀进行修改（可选）。
![](https://qcloudimg.tencent-cloud.cn/raw/febc9e62f9b6ec85b6218bece068d345.png)
3. 创建和修改账号
可以点击添加进行单个账号添加，或者点击导入进行批量账号导入。
 - 单个添加
单击添加进入单个账号添加操作页面，添加时需要填写登录地址、用户名、密码、显示名称和备注信息：
      - 登录地址：为 SIP 终端注册后的企业内设备唯一标识，系统已根据企业账号自动设定企业账号后缀，格式为1-50位的数字、字母或下划线。
      - 用户名：SIP 终端注册的用户名，为注册身份验证使用。
      - 密码：SIP 终端注册的密码，为注册身份验证使用。
      - 显示名称：呼叫时显示的终端或者会议室名称，非必填。
      - 备注：用于标注终端设备的备注信息，非必填。

    ![](https://qcloudimg.tencent-cloud.cn/raw/a6a2ee5b8a4d2a63cf277ffb48396836.png)
 - 批量导入
当需要同时创建多个账号时，可以通过 .xls 和 .xlsx 格式的模板文件，批量导入 SIP 终端帐号。
     1. 单击**导入**进入批量导入操作页面。
     2. 下载 Excel 模板文件，按格式填写注册账号信息。
     3. 选择文件进行上传完成批量导入。

    ![](https://qcloudimg.tencent-cloud.cn/raw/93d5c7c5b465cd6f6d09f2e57f5e95e8.png)

## 修改账号
创建账号成功后，单击账号的**编辑**查看或者修改注册账号的登录地址、用户名和密码等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/b1d1f810fe139c6cce28400f3aa2c0d9.png)

## 管理 SIP 注册账号
1. 账号禁用和启用
对已创建的账号，可以进行禁用和启用操作，单击登录地址对应账号的**更多**，选择：
 - 禁用：选择禁用后，该账号将处于**禁用**状态。
![](https://qcloudimg.tencent-cloud.cn/raw/2a8d06b78bf909e87e4860b9e54e2468.png)
 - 启用：对处于**禁用**状态的账号，选择启用操作后，该账号将可以正常使用。
![](https://qcloudimg.tencent-cloud.cn/raw/530fa1bb76210064c228f6f7aa30f5a4.png)
2. 账号删除
对已创建的账号，可以选择进行删除操作。
 - 单个删除：单击账号对应**更多** > **删除**将删除该账号。
![](https://qcloudimg.tencent-cloud.cn/raw/477e04075e0f579d7f04fe883a2ea486.png)
 - 批量删除：选择多个账号后，单击**删除**将删除选中的账号。
![](https://qcloudimg.tencent-cloud.cn/raw/9a11f23c5cfd6942344c4876f8cd9583.png)
