本文提供从注册腾讯云账号、购买到最终完成初始化云数据库 MySQL 的全程指导，助您轻松启用云数据库 MySQL。

## 步骤1：注册腾讯云账号
如果已完成，可忽略此步骤。
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://cloud.tencent.com/register?s_url=https%3A%2F%2Fcloud.tencent.com%2F" target="_blank"  style="color: white; font-size:16px;">点此注册腾讯云账号</a></div>

## 步骤2：完成实名认证
如果已完成，可忽略此步骤。
详细认证流程请参见 [实名认证介绍](https://cloud.tencent.com/document/product/378/3629)。
<div style="background-color:#00A4FF; width: 170px; height: 35px; line-height:35px; text-align:center;"><a href="https://console.cloud.tencent.com/developer" target="_blank"  style="color: white; font-size:16px;">点此完成实名认证</a></div>

## 步骤3：购买云数据库 MySQL
<div style="background-color:#00A4FF; width: 190px; height: 35px; line-height:35px; text-align:center;"><a href="https://buy.cloud.tencent.com/cdb" target="_blank"  style="color: white; font-size:16px;">点此进入快速购买页面</a></div>
</br>

![](https://main.qcloudimg.com/raw/4548e6acba4c064763c16096d25510c9.png)
如下信息确认无误后，单击【立即购买】。
- **计费模式**：支持包年包月和按量计费。
 - 若业务量有较稳定的长期需求，建议选择包年包月。
 - 若业务量有瞬间大幅波动场景，建议选择按量计费。
- **地域**：选择您业务需要部署 MySQL 的地域。不同地域的云产品内网不通，购买后不能更换。
- **主可用区和备可用区**：建议选择主备机处于同一可用区，避免网络延迟问题。
- **网络**：云数据库 MySQL 所属网络，缺省设置为“Default-VPC（默认）”。
- **安全组**：安全组创建与管理请参见 [云数据库安全组](https://cloud.tencent.com/document/product/236/9537)。
- **架构**：提供基础版和高可用版。
- **指定项目**：选择数据库实例所属的项目，缺省设置为默认项目。
- **购买数量**：每个用户在每个可用区可购买按量计费实例的总数量为10个。


## 步骤4：初始化云数据库 MySQL
1. 登录 [云数据库 MySQL 控制台](https://console.cloud.tencent.com/cdb)，在左侧导航选择【实例列表】页签。
3. 选择状态为【未初始化】的 MySQL 实例，在操作列单击【初始化】。
![](https://main.qcloudimg.com/raw/5161cf5c35bf952ba6b1f0ba77cc6f07.png)
4. 在弹出的初始化对话框中，配置初始化相关参数，单击【确定】开始初始化。
 - **支持字符集**：选择字符集。
 - **表名大小写敏感**：表名是否大小写敏感，默认为是。
 - **自定义端口**：数据库的访问端口，默认为3306。
 - **设置root帐号密码**：新创建的 MySQL 数据库的用户名默认为 root，此处用来设置该 root 帐号的密码。
 - **确认密码**：再次输入密码。
5. 返回实例列表，目标 MySQL 实例的状态变为【运行中】，说明已初始化成功。
