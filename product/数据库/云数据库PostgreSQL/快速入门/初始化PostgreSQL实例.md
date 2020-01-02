本文为您提供初始化 PostgreSQL 数据库的全程指导，助您轻松启用云数据库 PostgreSQL。

## 前提条件
1. 已注册腾讯云账号并完成实名认证。
如需注册腾讯云账号：
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.3128.btn1">点此注册腾讯云账号</a></div>
如需完成实名认证：
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/developer" target="_blank"  style="color: white; font-size:16px;"  hotrep="document.guide.3128.btn2">点此完成实名认证</a></div>
2. 已购买云数据库 PostgreSQL。
如需购买云数据库 PostgreSQL：
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://buy.cloud.tencent.com/pgsql" target="_blank"  style="color: white; font-size:16px;" hotrep="document.guide.3128.btn3">点此进入购买页面</a></div>

## 操作步骤
1. 登录 [云数据库 PostgreSQL 控制台](https://console.cloud.tencent.com/pgsql)，在左侧导航选择【实例列表】页签。
2. 选择状态为【待初始化】的 PostgreSQL 实例，在操作列单击【初始化】。
![](https://main.qcloudimg.com/raw/e5dc7ca9c83294340bfd82a75ff06b93.png)
3. 在弹出的初始化对话框中，配置初始化相关参数，单击【确定】开始初始化。
 - **管理员用户名**：帐号名需要1-16个字符，由字母、数字或特殊字符组成；以字母开头，字母或数字结尾；特殊字符为\_；不区分大小写；不能为: postgres，不能以 pg\_ 开头。
 - **密码**：密码需要8-32个字符，至少包含英文、数字和符号_+-&=!@#$%^*()中的2种。
 - **确认密码**：再次输入密码。
 - **支持字符集**：支持 LATIN1 、UTF8 字符集，默认字符集编码格式是 UTF8。
4. 返回实例列表，待 PostgreSQL 实例的状态变为【运行中】，说明已初始化成功。
