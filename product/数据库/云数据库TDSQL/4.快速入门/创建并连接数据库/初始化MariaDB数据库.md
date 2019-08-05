
1. 登录 [云数据库 MariaDB 控制台](https://console.cloud.tencent.com/tdsql)。
2. 在实例列表找到状态为【未初始化】的实例，在操作列选择【更多】>【初始化】。
![](https://main.qcloudimg.com/raw/f79e8eb644d318a5d0d84bdcd3551170.png)
3. 在弹出的对话框，配置初始化参数，单击【确认】开始初始化。
 - 支持的字符集：选择 MariaDB 数据库支持的字符集。
 - 表名大小写敏感：表名是否大小写敏感，默认为是。
 - 开启强同步：开启强同步可以保证在主机故障时备机数据的一致性。默认为不开启，即同步方式为异步同步。
![](https://main.qcloudimg.com/raw/14c32214404c1842fdf3b2d11b81c711.png)
4. 返回实例列表，实例状态变为【运行中】，说明初始化成功。
![](https://main.qcloudimg.com/raw/6abac4ea4ecdbdc47f652da8690d9e48.png)

