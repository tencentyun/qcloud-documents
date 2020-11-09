文件存储（Cloud File Storage，CFS）提供了可扩展的共享文件存储服务，可与腾讯云的 CVM 等服务搭配使用。CFS 提供了标准的 NFS 文件系统访问协议，为多个 CVM 实例提供共享的数据源，支持弹性容量和性能的扩展，现有应用无需修改即可挂载使用，是一种高可用、高可靠的分布式文件系统，适合于大数据分析、媒体处理和内容管理等场景。

下表为云审计支持的文件存储操作列表：

| 操作名称        | 资源类型 | 事件名称                         |
|-------------|------|------------------------------|
| 添加文件系统      | cfs  | CreateCfsFileSystem          |
| 创建权限组       | cfs  | CreateCfsPGroup              |
| 创建权限组规则     | cfs  | CreateCfsRule                |
| 删除文件系统      | cfs  | DeleteCfsFileSystem          |
| 删除权限组       | cfs  | DeleteCfsPGroup              |
| 删除权限组规则     | cfs  | DeleteCfsRule                |
| 删除挂载点       | cfs  | DeleteMountTarget            |
| 查询文件系统      | cfs  | DescribeCfsFileSystems       |
| 查询权限组列表     | cfs  | DescribeCfsPGroups           |
| 查询权限组规则列表   | cfs  | DescribeCfsRules             |
| 查询 KMS 密钥     | cfs  | DescribeKmsKeys              |
| 查询文件系统挂载点   | cfs  | DescribeMountTargets         |
| 开通 CFS 服务     | cfs  | SignUpCfsService             |
| 更新文件系统名     | cfs  | UpdateCfsFileSystemName      |
| 更新文件系统所属权限组 | cfs  | UpdateCfsFileSystemPGroup    |
| 更新文件系统空间限制  | cfs  | UpdateCfsFileSystemSizeLimit |
| 更新权限组信息     | cfs  | UpdateCfsPGroup              |
| 更新权限组规则     | cfs  | UpdateCfsRule                |
