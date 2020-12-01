云 HDFS（Cloud HDFS，CHDFS）是腾讯云一种提供标准 HDFS 访问协议、卓越性能、分层命名空间的分布式文件系统。CHDFS 主要解决大数据场景下海量数据存储和数据分析，能够为大数据用户在无需更改现有代码的基础上，将本地自建的 HDFS 文件系统无缝迁移至具备高可用性、高扩展性、低成本、可靠和安全的 CHDFS 上。

下表为云审计支持的云 HDFS 操作列表：

| 操作名称       | 资源类型  | 事件名称                 |
|------------|-------|----------------------|
| 创建权限组      | chdfs | CreateAccessGroup    |
| 批量创建权限规则   | chdfs | CreateAccessRules    |
| 创建文件系统     | chdfs | CreateFileSystem     |
| 创建挂载点      | chdfs | CreateMountPoint     |
| 删除权限组      | chdfs | DeleteAccessGroup    |
| 批量删除权限规则   | chdfs | DeleteAccessRules    |
| 删除文件系统     | chdfs | DeleteFileSystem     |
| 删除挂载点      | chdfs | DeleteMountPoint     |
| 查看权限组列表    | chdfs | DescribeAccessGroups |
| 查看权限规则列表   | chdfs | DescribeAccessRules  |
| 查看文件系统详细信息 | chdfs | DescribeFileSystem   |
| 查看文件系统列表   | chdfs | DescribeFileSystems  |
| 查看挂载点列表    | chdfs | DescribeMountPoints  |
| 修改权限组属性    | chdfs | ModifyAccessGroup    |
| 批量修改权限规则属性 | chdfs | ModifyAccessRules    |
| 修改文件系统属性   | chdfs | ModifyFileSystem     |
| 修改挂载点属性    | chdfs | ModifyMountPoint     |
