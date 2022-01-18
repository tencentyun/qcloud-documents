## 简介

[访问管理（Cloud Access Management，CAM）](https://cloud.tencent.com/document/product/598)是腾讯云提供的 Web 服务，主要用于帮助用户安全管理腾讯云账户下资源的访问权限。用户可以通过 CAM 创建、管理和销毁用户（组），并使用身份管理和策略管理控制其他用户使用腾讯云资源的权限，CAM 策略的详细信息及使用请参见 [CAM 策略](https://cloud.tencent.com/document/product/598/10601)  文档。

主账号可以授权子账号或协作者访问管理权限，访问指定的日志服务资源。

## 预设权限策略

日志服务预设两条权限策略，可满足最基本的权限管理需求。
- 全读写访问权限（QcloudCLSFullAccess）：具备日志服务所有功能及所有资源的权限，例如创建日志主题、修改索引配置、删除日志主题、检索日志、上传日志等。
- 只读访问权限（QcloudCLSReadOnlyAccess）：仅具备数据查看权限，不能执行新建、编辑或删除类型的操作。

配置方式参见 [授权管理](https://cloud.tencent.com/document/product/598/10602) 文档。

## 自定义权限策略

通过自定义权限策略可实现细粒度的权限划分，例如仅允许某个用户查看特定日志主题的数据。

自定义权限策略主要由两部分组成：
- 操作（Action）：用户可进行的操作，例如检索日志、修改索引配置、上传日志、创建告警策略等。
- 资源（Resource）：可操作的资源范围，例如特定的日志主题、仪表盘、数据加工任务等。

日志服务支持的所有操作及资源定义方式参见 CAM 的 [日志服务](https://cloud.tencent.com/document/product/598/66554) 文档，配置方式参见 [创建自定义策略](https://cloud.tencent.com/document/product/598/37739)。

自定义权限策略配置存在一定的复杂度，实际使用过程中可参见 [自定义权限策略示例](https://cloud.tencent.com/document/product/614/68374)，这些示例能够满足大多数的权限管理需求，也可以基于这些策略示例再进行个性化调整。详细操作方式如下：
1. 主账号（或具备 CAM 管理权限的用户）在 [策略](https://console.cloud.tencent.com/cam/policy) 页面，单击**新建自定义策略**。
2. 在弹出的窗口中，单击**按策略语法创建**。
3. 在选择策略模板页面，选择**空白模版**，单击**下一步**。
4. 在编辑策略页面，设置策略名称，输入策略内容，策略内容可从 [自定义权限策略示例](https://cloud.tencent.com/document/product/614/68374) 中进行复制。
5. 单击**完成**，保存该策略。
创建完成自定义策略后，可通过 [授权管理](https://cloud.tencent.com/document/product/598/10602) 将策略关联至用户/用户组，使用户/用户组获得对应的操作权限。
