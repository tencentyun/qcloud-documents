创建 MySQL 实例后，您还需要进行 MySQL 实例的初始化，以轻松启用实例。

## 操作步骤
1. 登录 [MySQL 控制台](https://console.cloud.tencent.com/cdb)，选择对应地域后，在实例列表，选择状态为“未初始化”的实例，在“操作”列单击【初始化】。
![](https://main.qcloudimg.com/raw/5161cf5c35bf952ba6b1f0ba77cc6f07.png)
2. 在弹出的初始化对话框，配置初始化相关参数，单击【确定】。
 - **支持字符集**：支持 LATIN1 、GBK、UTF8 、UTF8MB4 字符集，默认字符集编码格式是 UTF8。初始化实例后，亦可在控制台实例详情页修改字符集，更多说明请参见 [字符集说明](https://cloud.tencent.com/document/product/236/7259#.E5.AD.97.E7.AC.A6.E9.9B.86.E8.AF.B4.E6.98.8E)。
 - **表名大小写敏感**：表名是否大小写敏感，默认为是。
 - **自定义端口**：数据库的访问端口，默认为3306。
 - **设置root帐号密码**：新创建的 MySQL 数据库的用户名默认为 root，此处用来设置该 root 帐号的密码。
 - **确认密码**：再次输入密码。
3. 在弹出的初始化对话框，单击【确定】。
![](https://main.qcloudimg.com/raw/f83e0cba43b84aa8e9706d7e1cc625a9.png)
4. 返回实例列表，待实例状态变为“运行中”，即可正常使用。


## 后续操作
通过 Windows 云服务器或 Linux 云服务器，以内外网两种不同的方式连接云数据库 MySQL，请参见 [连接 MySQL 实例](https://cloud.tencent.com/document/product/236/3130)。
