访问管理（Cloud Access Management，CAM）是腾讯云提供的一套 Web 服务，用于帮助客户安全地管理腾讯云账户的访问权限，资源管理和使用权限。通过 CAM，您可以创建、管理和销毁用户（组），并通过身份管理和策略管理控制哪些人可以使用哪些腾讯云资源。

下表为云审计支持的访问管理操作列表：

| 操作名称                    | 资源类型 | 事件名称                              |
|-------------------------|------|-----------------------------------|
| 添加控制台子用户                | cam  | AddConsoleUser                    |
| 新增用户                    | cam  | AddSubAccount                     |
| 创建子用户                   | cam  | AddSubAccountCheckingMFA          |
| 用户加入到用户组                | cam  | AddSubAccountsToGroup             |
| 添加子用户                   | cam  | AddUser                           |
| 用户加入用户组                 | cam  | AddUserToGroup                    |
| 绑定多个策略到用户组              | cam  | AttachGroupPolicies               |
| 绑定策略到用户组                | cam  | AttachGroupPolicy                 |
| 绑定策略到多个用户组              | cam  | AttachGroupsPolicy                |
| 绑定多个策略到角色               | cam  | AttachRolePolicies                |
| 绑定策略到角色                 | cam  | AttachRolePolicy                  |
| 绑定策略到多个角色               | cam  | AttachRolesPolicy                 |
| 绑定多个策略到用户               | cam  | AttachUserPolicies                |
| 绑定策略到用户                 | cam  | AttachUserPolicy                  |
| 绑定策略到多个用户               | cam  | AttachUsersPolicy                 |
| 批量绑定                    | cam  | BatchOperateCamStrategy           |
| 绑定 Token 卡                | cam  | BindToken                         |
| 检查子用户名称                 | cam  | CheckSubAccountName               |
| 查询用户是否关联策略              | cam  | CheckUserPolicyAttachment         |
| 验证自定义多因子 Token           | cam  | ConsumeCustomMFAToken             |
| 创建访问密钥                  | cam  | CreateAccessKey                   |
| 创建 API 密钥                 | cam  | CreateApiKey                      |
| 创建子账户密钥                 | cam  | CreateCollApiKey                  |
| 创建用户组                   | cam  | CreateGroup                       |
| 新增策略                    | cam  | CreatePolicy                      |
| CreatePolicyVersion     | cam  | CreatePolicyVersion               |
| 创建项目密钥                  | cam  | CreateProjectKey                  |
| 创建角色                    | cam  | CreateRole                        |
| 控制台创建角色                 | cam  | CreateRoleByConsole               |
| 创建 SAML 身份提供商             | cam  | CreateSAMLProvider                |
| 创建子账号绑定限制               | cam  | CreateSubAccountBindPolicy        |
| 创建子账号登录 IP 策略             | cam  | CreateSubAccountLoginIpPolicy     |
| 新增用户                    | cam  | CreateSubAccounts                 |
| 创建子账号邀请二维码              | cam  | CreateSubUserInviteQRCode         |
| 删除访问密钥                  | cam  | DeleteAccessKey                   |
| 删除 API 密钥                 | cam  | DeleteApiKey                      |
| 删除子帐号密钥                 | cam  | DeleteCollApiKey                  |
| 删除实体权限边界                | cam  | DeleteEntitiesPermissionsBoundary |
| 删除用户组                   | cam  | DeleteGroup                       |
| 删除策略                    | cam  | DeletePolicy                      |
| DeletePolicyVersion     | cam  | DeletePolicyVersion               |
| 删除项目密钥                  | cam  | DeleteProjectKey                  |
| 删除角色                    | cam  | DeleteRole                        |
| 删除角色权限边界                | cam  | DeleteRolePermissionsBoundary     |
| 删除 SAML 身份提供商             | cam  | DeleteSAMLProvider                |
| 删除用户                    | cam  | DeleteSubAccount                  |
| 删除子用户                   | cam  | DeleteUser                        |
| 查询协助审批人                 | cam  | DescribeAssistApprover            |
| 获取策略详情                  | cam  | DescribeCamStrategyDetail         |
| 获取角色列表                  | cam  | DescribeRoleList                  |
| 查看子账号绑定限制               | cam  | DescribeSubAccountBindPolicy      |
| 查看子账号登录IP策略             | cam  | DescribeSubAccountLoginIpPolicy   |
| 解绑多个策略到用户组              | cam  | DetachGroupPolicies               |
| 解绑策略到用户组                | cam  | DetachGroupPolicy                 |
| 解绑策略到多个用户组              | cam  | DetachGroupsPolicy                |
| 解绑多个策略到角色               | cam  | DetachRolePolicies                |
| 解绑策略到角色                 | cam  | DetachRolePolicy                  |
| 解绑策略到多个角色               | cam  | DetachRolesPolicy                 |
| 解绑多个策略到用户               | cam  | DetachUserPolicies                |
| 解绑策略到用户                 | cam  | DetachUserPolicy                  |
| 解绑策略到多个用户               | cam  | DetachUsersPolicy                 |
| 禁用 API 密钥                 | cam  | DisableApiKey                     |
| 删除子帐号密钥                 | cam  | DisableCollApiKey                 |
| 禁用项目密钥                  | cam  | DisableProjectKey                 |
| 启用 API 密钥                 | cam  | EnableApiKey                      |
| 启用子帐号密钥                 | cam  | EnableCollApiKey                  |
| 启用项目密钥                  | cam  | EnableProjectKey                  |
| 获取账户摘要                  | cam  | GetAccountSummary                 |
| 获取所有用户信息                | cam  | GetAllSubUser                     |
| 拉取 API 密钥                 | cam  | GetApiKey                         |
| 获取自定义多因子 Token 关联信息       | cam  | GetCustomMFATokenInfo             |
| 查询用户组                   | cam  | GetGroup                          |
| 获取 CAM 密码设置规则             | cam  | GetPasswordRules                  |
| 查看策略详情                  | cam  | GetPolicy                         |
| GetPolicyVersion        | cam  | GetPolicyVersion                  |
| 拉取项目密钥                  | cam  | GetProjectKey                     |
| 获取角色详情                  | cam  | GetRole                           |
| 获取安全设置概览信息              | cam  | GetSafeAuthInfo                   |
| 查询 SAML 身份提供商信息           | cam  | GetSAMLProvider                   |
| 拉取子用户绑定信息               | cam  | GetSubAccountBindInfo             |
| 拉取子用户信息                 | cam  | GetUser                           |
| 拉取用户基础信息                | cam  | GetUserBasicInfo                  |
| 列出访问密钥                  | cam  | ListAccessKeys                    |
| 查询所有用户组关联的策略            | cam  | ListAllGroupsPolicies             |
| 查看用户组关联的策略列表            | cam  | ListAttachedGroupPolicies         |
| 查看角色关联的策略列表             | cam  | ListAttachedRolePolicies          |
| 列出用户关联的策略（包括随组关联）       | cam  | ListAttachedUserAllPolicies       |
| 查看用户关联的策略列表             | cam  | ListAttachedUserPolicies          |
| 查看策略关联的实体列表             | cam  | ListEntitiesForPolicy             |
| 获取用户组列表                 | cam  | ListGroups                        |
| 查询用户关联的用户组列表            | cam  | ListGroupsForUser                 |
| 批量查询用户组关联的策略            | cam  | ListGroupsPolicies                |
| 查询身份提供商列表               | cam  | ListIdentityProvider              |
| 只读访问所有策略                | cam  | ListPolicies                      |
| ListPolicyVersions      | cam  | ListPolicyVersions                |
| 获取消息接收人列表               | cam  | ListReceiver                      |
| 查询 SAML 身份提供商列表           | cam  | ListSAMLProviders                 |
| 获取用户列表                  | cam  | ListSubAccounts                   |
| 拉取子用户列表                 | cam  | ListUsers                         |
| 查询用户组关联的用户列表            | cam  | ListUsersForGroup                 |
| 列出策略关联的用户列表（包括随组关联）     | cam  | ListUsersForPolicy                |
| 踢出角色登录态                 | cam  | LogoutRoleSessions                |
| 拉取上次登录信息                | cam  | LookupRecentlyLogin               |
| 传递角色                    | cam  | PassRole                          |
| 设置实体权限边界                | cam  | PutEntitiesPermissionsBoundary    |
| 设置角色权限边界                | cam  | PutRolePermissionsBoundary        |
| 拉取 API 密钥列表               | cam  | QueryApiKey                       |
| 子帐号密钥列表查询               | cam  | QueryCollApiKey                   |
| 拉取项目密钥列表                | cam  | QueryProjectKeyList               |
| 从用户组删除用户                | cam  | RemoveUserFromGroup               |
| 发送子帐号信息                 | cam  | SendSubAccountInfo                |
| SetDefaultPolicyVersion | cam  | SetDefaultPolicyVersion           |
| 设置安全保护                  | cam  | SetSafeAuthFlag                   |
| 解绑软 Token 卡               | cam  | UnbindStoken                      |
| 解绑子用户登录方式               | cam  | UnbindSubAccount                  |
| 更新访问密钥                  | cam  | UpdateAccessKey                   |
| 更新角色信任策略                | cam  | UpdateAssumeRolePolicy            |
| 更新策略                    | cam  | UpdateCamStrategy                 |
| 更新用户组                   | cam  | UpdateGroup                       |
| 更新 CAM 密码设置规则             | cam  | UpdatePasswordRules               |
| 修改策略                    | cam  | UpdatePolicy                      |
| 修改角色是否可登录               | cam  | UpdateRoleConsoleLogin            |
| 更新角色备注                  | cam  | UpdateRoleDescription             |
| 更新 SAML 身份提供商信息           | cam  | UpdateSAMLProvider                |
| 更新用户                    | cam  | UpdateSubAccount                  |
| 更新子账号属性                 | cam  | UpdateSubAccountAttr              |
| 更新子用户                   | cam  | UpdateUser                        |
