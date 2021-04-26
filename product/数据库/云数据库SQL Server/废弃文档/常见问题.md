
**1.创建SQL Server数据库后，还没有写入数据或写入极少量数据，为什么存储空间监控显示是已经占用500M数据？**
腾讯云为每个SQL Server数据库创建时，会自动分配500M的初始化空间；数据写入时，会优先写入到初始化空间中；因此您没有写入数据或写入极少量数据，存储监控也会显示500M。

**2.我把我写入的数据删掉之后，存储空间监控会仍然显示我占用了相当数量的存储空间，空间不会释放吗？**
SQL Server删除数据后，已经扩展的数据文件不会收缩，文件内部空闲的空间可以支撑后续操作，如插入，更新。例如：您申请50G的实例，某一个数据库写入50G数据后再全部删除，这时候存储空间监控您已经使用了50G。但您仍然可以继续写入大量文件。

**3.通过Microsoft SQL Server Management管理数据库，系统提示“Login failed. The login is from an untrusted domain and cannot be used with Windows authentication”**
请将身份认证方式改为“**SQL Server 身份验证**”。