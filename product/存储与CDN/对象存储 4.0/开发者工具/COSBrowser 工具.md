## 功能说明
COSBrowser 工具即 COS 客户端工具，用户可以通过可视化界面方便的进行数据的上传、下载和管理。

>!
>- COSBrowser 桌面端（Windows/macOS/Linux）会使用系统配置的代理来尝试网络连接，请确保您的代理配置正常或请停用无法连接互联网的代理配置。Windows 用户可在操作系统的“Internet 选项”中查询，macOS 用户可在“网络偏好设置”中查询，Linux 用户可在系统设置 > 网络 > 网络代理中查询。
>- 使用该工具上传同名文件，会覆盖较旧的同名文件，不支持校对是否存在同名文件的功能。

## 下载地址

|支持平台|下载地址|
|:---|:---|
|Windows 桌面端|[Windows](https://cos5.cloud.tencent.com/cosbrowser/releases/cosbrowser-setup-latest.exe)|
|macOS 桌面端|[macOS](https://cos5.cloud.tencent.com/cosbrowser/releases/cosbrowser-latest.dmg)|
|Linux 桌面端|[Linux](https://cos5.cloud.tencent.com/cosbrowser/releases/cosbrowser-latest-linux.zip)|
|Android 移动端|[Android](https://sj.qq.com/myapp/detail.htm?apkName=com.qcloud.cos.client)|
|iOS 移动端|[iOS](https://apps.apple.com/cn/app/id1469323992)|

## 桌面端

>?COSBrowser 桌面端支持 Windows/macOS/Linux 系统。

#### 软件界面

![COSBrowser PC 端](https://main.qcloudimg.com/raw/6b36f6090281ac7925544ac42bbef55c.png)

#### 登录说明

  - **云 API 密钥（SecretId/SecretKey）**：用户可使用云 API 密钥 SecretId 和 SecretKey（不支持项目密钥）进行登录，该密钥可在访问管理控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取，成功登录后密钥会保存在**历史密钥**中。
  - **历史密钥**：单击**历史密钥**，可查看并使用已在该电脑成功登录过的云 API 密钥。

## 移动端

#### 软件界面

![COSBrowser移动端](https://main.qcloudimg.com/raw/8cde524816485071348ff3d7aaca863f.png)

#### 登录说明

COSBrowser 移动端支持以下两种登录方式：
  - **微信快捷登录**：通过微信创建的腾讯云账号，可以使用微信快捷登录方式快速登录 COSBrowser 。
  - **永久密钥登录**：用户可使用云 API 密钥 SecretId 和 SecretKey（不支持项目密钥）进行登录，该密钥可在访问管理控制台的 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 页面获取，登录后将永久保持该账号的登录状态。

>?若用户的腾讯云账号为 QQ 账号所创建的，同样可使用微信快捷登录方式登录，只需在跳转的微信小程序界面选择 QQ 登录即可。

## 使用方法

下面以 Windows PC 端为例，其他 PC 端、移动端可参照类似操作。

### 管理文件/文件夹
#### 创建文件夹
1. 登录 COSBrowser 工具，在左侧存储桶模块下，单击选择存储桶。
2. 单击【新建文件夹】。
3. 填写文件夹名并确认。
>?
>- 文件夹名称长度限制在255个字符内，可用数字、英文和可见字符的组合。
>- 文件夹名称不可包含`\ / : * ? " | < >`等特殊字符。
>- 不允许以`..`作为文件夹名称。
>- 文件夹无法进行重命名操作，请谨慎命名。

#### 上传文件/文件夹
在指定的存储桶或目录内，单击【上传文件】或【上传文件夹】，选择要上传的文件或文件夹，即可完成文件或文件夹的上传。
>?COSBrowser 移动端仅支持上传图片和视频。

#### 下载文件/文件夹
1. 在指定的存储桶或目录内，选中要下载的文件或文件夹。
2. 单击【下载】，即可以默认下载方式进行下载。
3. 用户还可以选择【高级下载】，进行下载选项的配置。
![下载文件夹](https://main.qcloudimg.com/raw/e57f4a12cfce6c97ddc5c27d8f25cf4b.jpg)
>?COSBrowser 移动端没有**高级下载**模式，不支持下载文件夹。

#### 复制、粘贴文件/文件夹
1. 在指定的存储桶或目录内，选中要复制的文件或文件夹，单击【复制】。
2. 进入要粘贴文件的存储桶或目录内，单击【粘贴】。
>!
>- 公有云地域和金融云地域之间不支持相互复制、粘贴。
>- 若复制文件的源地址和目的地址一致，会默认对同名文件进行重命名，若复制文件的源地址和目的地址不一致，则会覆盖同名文件。
>- COSBrowser 移动端不支持复制、粘贴文件夹。

#### 重命名文件
1. 在指定的存储桶或目录内，选中要重命名的文件，单击【重命名】。
2. 输入新的文件名称。
>?文件夹无法进行重命名操作。

#### 删除文件/文件夹
在指定的存储桶或目录内，选中要删除的文件/文件夹，单击【删除】。
>?删除操作可选中多个文件/文件夹批量进行。

### 更多操作
#### 通用设置
选择【设置】>【通用】，进入 COSBrowser 的设置界面修改通用配置，例如语言、服务端域名、是否使用 HTTPS 等。

#### 上传/下载参数配置
- 文件并发数：设置文件上传或下载的并发任务数，超过最大并发数量的任务会进入等待队列，待前序任务完成后执行。
- 分片并发数：设置文件上传或下载的分片数量。
- 失败重试次数：设置文件上传或下载的重试失败次数。

## 更新日志

桌面端更新日志： [changelog](https://github.com/tencentyun/cosbrowser/blob/master/changelog.md)
移动端更新日志： [changelog_mobile](https://github.com/tencentyun/cosbrowser/blob/master/changelog_mobile.md)

## 反馈和建议

如您在使用 COSBrowser 工具有疑问或建议，欢迎反馈给我们：
- 桌面端：[issues](https://github.com/tencentyun/cosbrowser/issues)
- 移动端：[issues_mobile](https://support.qq.com/embed/phone/67467)
