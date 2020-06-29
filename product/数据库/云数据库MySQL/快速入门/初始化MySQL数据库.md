本文为您提供初始化 MySQL 数据库的全程指导，助您轻松启用云数据库 MySQL。

## 前提条件
1. 已注册腾讯云账号并完成实名认证。
如需注册腾讯云账号：
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.3128.btn1">点此注册腾讯云账号</a></div>
如需完成实名认证：
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/developer" target="_blank"  style="color: white; font-size:16px;"  hotrep="document.guide.3128.btn2">点此完成实名认证</a></div>
2. 已购买云数据库 MySQL。
如需购买云数据库 MySQL：
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://buy.cloud.tencent.com/cdb" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.3128.btn3">点此进入购买页面</a></div>

## 操作步骤
1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)，在左侧导航选择【实例列表】页签。
2. 选择状态为【未初始化】的 MySQL 实例，在操作列单击【初始化】。
![](https://main.qcloudimg.com/raw/5161cf5c35bf952ba6b1f0ba77cc6f07.png)
3. 在弹出的初始化对话框中，配置初始化相关参数，单击【确定】开始初始化。
 - **支持字符集**：支持 LATIN1 、GBK、UTF8 、UTF8MB4 字符集，默认字符集编码格式是 LATIN1，即 ISO-8859-1 编码格式。初始化实例后，亦可在控制台实例详情页修改字符集。
 - **表名大小写敏感**：表名是否大小写敏感，默认为是。
 - **自定义端口**：数据库的访问端口，默认为3306。
 - **设置root帐号密码**：新创建的 MySQL 数据库的用户名默认为 root，此处用来设置该 root 帐号的密码。
 - **确认密码**：再次输入密码。
4. 返回实例列表，目标 MySQL 实例的状态变为【运行中】，说明已初始化成功。


## 后续步骤
- 通过 Windows 云服务器或 Linux 云服务器，以内外网两种不同的方式访问云数据库 MySQL，请参见 [访问 MySQL 数据库](https://cloud.tencent.com/document/product/236/3130)。
- 在控制台的实例列表页和实例管理页，查看实例相关信息、实例监控及管理数据库等，请参见 [管理 MySQL 数据库](https://cloud.tencent.com/document/product/236/3131)。
