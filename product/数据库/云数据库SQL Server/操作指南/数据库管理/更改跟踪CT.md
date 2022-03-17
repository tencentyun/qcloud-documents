
更改跟踪（CT）可以应用跟踪到一个数据库中的具体表甚至是具体列，在用户对启用了更改跟踪的表进行了增加、修改和删除操作时，系统自动将该操作生成一个版本号，记录下操作的时间戳、操作的类型、受影响数据的主键等信息。

启用更改跟踪，它只记录表中的行是否有过更改，而不记录更改的历史数据，故对数据操作的性能影响不是很大。这些信息将记录到 SQL Server 系统表中，系统自动负责清理和维护。

## 单库启用/禁用更改跟踪 CT
1. 登录 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver)，在实例列表，单击实例 ID 或**操作**列的**管理**，进入实例管理页面。
2. 在实例管理页面，选择**数据库管理**页，选择目标数据库所在行，在**操作**列选择**其它** > **启用/禁用更改跟踪**。
![](https://main.qcloudimg.com/raw/09c0c14d1d9d65ac5119a91d4dbe6c4c.png)
3. 在弹出的对话框，展示了数据库名称及当前 CT 状态，对 CT 进行启用或者禁用后，单击**确定**，其中启用 CT 支持设置数据保留时长。
<img src="https://main.qcloudimg.com/raw/e6d0c7dc3e678d0745df6aa2d5e2b90e.png" style="zoom:40%;" /><br>
您可以通过**数据库管理**页右上角的**当前任务**，查看启用或禁用跟踪 CT 的任务进度。<br>
<img src="https://main.qcloudimg.com/raw/081c4bc90c7f4f6a399361e047d6e197.png" style="zoom:50%;" />

## 批量启用/禁用更改跟踪 CT
1. 登录 [SQL Server 控制台](https://console.cloud.tencent.com/sqlserver)，在实例列表，单击实例 ID，进入实例管理页面。
2. 在实例管理页面，选择**数据库管理**页，勾选目标数据库，在列表上方选择**批量管理** > **批量启用/禁用更改跟踪**。
![](https://main.qcloudimg.com/raw/9f9813b8d5d6639aadcda64259bdf73a.png)
3. 在弹出的对话框，展示了数据库名称及当前 CT 状态，对 CT 进行启用或者禁用后，单击**确定**，其中启用 CT 支持设置数据保留时长。
<img src="https://main.qcloudimg.com/raw/62f2591286e77c0b404ea5b93b668d89.png" style="zoom:40%;" /><br>
您可以通过**数据库管理**页右上角的**当前任务**，查看启用或禁用跟踪 CT 的任务进度。<br>
<img src="https://main.qcloudimg.com/raw/081c4bc90c7f4f6a399361e047d6e197.png" style="zoom:50%;" />
