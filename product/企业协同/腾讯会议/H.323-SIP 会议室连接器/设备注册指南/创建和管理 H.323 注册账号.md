## 前提条件
企业购买了 H.323 会议室连接器许可，才可以创建和管理 H.323 注册账号，更多请参见 [会议室连接器](https://cloud.tencent.com/document/product/1095/50022)。
本文将介绍创建 H.323 注册账号的操作步骤以及管理 H.323 注册账号的操作。

## 创建 H.323 注册账号
1. 登录腾讯会议企业管理平台
使用企业账号登录 [腾讯会议企业管理平台](https://meeting.tencent.com)，然后单击**企业管理** > **会议室连接器** > **H.323/SIP 账号管理** > **H.323 页面**。
![](https://qcloudimg.tencent-cloud.cn/raw/19095503abb3ab7cfe6ef83179d3482f.png)
2. 注册服务地址和企业短号前缀、
H.323 终端注册到腾讯会议 [会议室连接器服务](gk.qqmra.com)。
系统会为企业创建默认的企业短号前缀，在创建 H.323 注册账号之前，也可以根据需要对短号进行修改（可选）。
![](https://qcloudimg.tencent-cloud.cn/raw/f30e00d3174de72a71a58c22983397c2.png)
3. 创建和修改账号
可以单击**添加**进行单个账号添加，或者单击**导入**进行批量账号导入。
 - 单个添加
 添加时需要填写短号码（E.164地址）、用户名、密码、显示名称和备注信息：
<table>
   <tr>
      <th width="0%" >名称</td>
      <th width="0%" >描述</td>
   </tr>
   <tr>
      <td>短号码（E.164地址）</td>
      <td>为 H.323 终端注册后的唯一号码标识，系统已根据企业账号自动设定企业短号前缀，需填写后四位数字，企业内唯一。</td>
   </tr>
   <tr>
      <td>用户名</td>
      <td>H.323 终端注册的用户名，为注册身份验证使用。</td>
   </tr>
   <tr>
      <td>密码</td>
      <td>H.323 终端注册的密码，为注册身份验证使用。</td>
   </tr>
   <tr>
      <td>显示名称</td>
      <td>呼叫时显示的终端或者会议室名称，非必填。</td>
   </tr>
   <tr>
      <td>备注</td>
      <td>用于标注终端设备的备注信息，非必填。</td>
   </tr>
</table> 
<img style="width:978px; max-width: inherit;" src="https://qcloudimg.tencent-cloud.cn/raw/66d39944a482c63ac4d36f681a1a8409.png" />
 - 批量导入
当需要同时创建多个账号时，可以通过 .xls 和 .xlsx 格式的模板文件，批量导入 H.323 终端帐号。
    1. 单击**导入**进入批量导入操作页面。
     2. 下载 Excel 模板文件，按格式填写注册账号信息。
     3. 选择文件进行上传完成批量导入。

    ![](https://qcloudimg.tencent-cloud.cn/raw/b0909532fc6b4317e5f729e427e0c548.png)

## 修改账号
创建成功后可以单击对应短号的**编辑**查看或者修改注册账号的短号码、用户名和密码等信息。
![](https://qcloudimg.tencent-cloud.cn/raw/2e6740764ad3a9e05af211bc5471dffc.png)

## 管理 H.323 注册账号
### 账号禁用和启用
对已创建的账号，可以进行禁用和启用操作。
单击登录地址对应账号的**更多**，选择**禁用**或者**启用**。
- **禁用：**选择禁用后，该账号将处于**禁用**状态。
![](https://qcloudimg.tencent-cloud.cn/raw/c2a489e6d79de08630cff6b51652668d.png)
- **启用：**对处于**禁用**状态的账号，选择启用操作后，该账号将可以正常使用。
![](https://qcloudimg.tencent-cloud.cn/raw/fc19537f91d501f2ed2a0d0bce0ce6c0.png)

### 账号删除
对已创建的账号，可以选择进行删除操作。
- **单个删除：**单击账号对应选择的**更多** > **删除**将删除该账号。
![](https://qcloudimg.tencent-cloud.cn/raw/9256d955f1c96fdf07e85cef36f9343d.png)
- **批量删除：**选择多个账号后，单击**删除**将删除选中的账号。
![](https://qcloudimg.tencent-cloud.cn/raw/5c9f702d81038c6b3e54bf75b48b6100.png)
