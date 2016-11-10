## 1 账号管理 

| 功能说明  | 接口 | 
|---------|---------|
| 独立模式帐号导入  | [v4/im_open_login_svc/account_import](/doc/product/269/独立模式账号导入接口) | 
| 独立模式帐号批量导入  | [v4/im_open_login_svc/multiaccount_import](/doc/product/269/独立模式帐号批量导入接口) | 
| 托管模式帐号导入  | [v4/registration_service/register_account_v1](/doc/product/269/托管模式存量账号导入) | 
| 失效帐号登录态  | [v4/im_open_login_svc/kick](/doc/product/269/帐号登录态失效接口) | 

## 2 单聊消息

| 功能说明  | 接口 | 
|---------|---------|
| 单发单聊消息 | [v4/openim/sendmsg](/doc/product/269/单发单聊消息) | 
| 批量发单聊消息 | [v4/openim/batchsendmsg](/doc/product/269/批量发单聊消息) | 
| 导入单聊消息 | [v4/openim/importmsg](/doc/product/269/导入单聊消息) | 

## 3 消息推送
| 功能说明  | 接口 | 
|---------|---------|
| 推送 | [v4/openim/im_push](/doc/product/269/推送) | 
| 获取推送报告 | [v4/openim/im_get_push_report](/doc/product/269/获取推送报告) | 
| 设置应用属性名称 | [v4/openim/im_set_attr_name](/doc/product/269/设置应用属性名称) | 
| 获取应用属性名称 | [v4/openim/im_get_attr_name](/doc/product/269/获取应用属性名称) | 
| 设置用户属性 | [v4/openim/im_set_attr](/doc/product/269/设置用户属性) | 
| 删除用户属性 | [v4/openim/im_remove_attr](/doc/product/269/删除用户属性) | 
| 获取用户属性 | [v4/openim/im_get_attr](/doc/product/269/获取用户属性) | 
| 添加用户标签 | [v4/openim/im_add_tag](/doc/product/269/添加用户标签) | 
| 删除用户标签 | [v4/openim/im_remove_tag](/doc/product/269/删除用户标签) | 
| 删除用户所有标签 | [v4/openim/im_remove_all_tags](/doc/product/269/删除用户所有标签) | 


## 4 群组管理

| 功能说明  | 接口 | 
|---------|---------|
| 获取APP中的所有群组 | [v4/group_open_http_svc/get_appid_group_list](/doc/product/269/获取APP中的所有群组) | 
| 创建群组 | [v4/group_open_http_svc/create_group](/doc/product/269/创建群组) | 
| 获取群组详细资料 | [v4/group_open_http_svc/get_group_info](/doc/product/269/获取群组详细资料) | 
| 获取群成员详细资料 | [v4/group_open_http_svc/get_group_member_info](/doc/product/269/获取群组成员详细资料) | 
| 修改群组基础资料 | [v4/group_open_http_svc/modify_group_base_info](/doc/product/269/修改群组基础资料) | 
| 增加群组成员  | [v4/group_open_http_svc/add_group_member](/doc/product/269/增加群组成员) | 
| 删除群组成员  | [v4/group_open_http_svc/delete_group_member](/doc/product/269/删除群组成员) | 
| 修改群组成员资料  | [v4/group_open_http_svc/modify_group_member_info](/doc/product/269/修改群成员资料) | 
| 解散群组  | [v4/group_open_http_svc/destroy_group ](/doc/product/269/解散群组)| 
| 获取用户所加入的群组  | [v4/group_open_http_svc/get_joined_group_list](/doc/product/269/获取用户所加入的群组) | 
| 查询用户在群组中的身份  |[v4/group_open_http_svc/get_role_in_group](/doc/product/269/查询用户在群组中的身份) | 
| 批量禁言和取消禁言  |[v4/group_open_http_svc/forbid_send_msg](/doc/product/269/批量禁言和取消禁言) | 
| 获取群组被禁言用户列表  |[v4/group_open_http_svc/get_group_shutted_uin](/doc/product/269/获取群组被禁言用户列表) | 
| 在群组中发送普通消息  |[v4/group_open_http_svc/send_group_msg](/doc/product/269/在群组中发送普通消息) | 
| 在群组中发送系统通知  |[v4/group_open_http_svc/send_group_system_notification](/doc/product/269/在群组中发送系统通知) | 
| 转让群组  |[v4/group_open_http_svc/change_group_owner](/doc/product/269/转让群组) | 
| 导入群基础资料  |[v4/group_open_http_svc/import_group](/doc/product/269/导入群基础资料) | 
| 导入群消息  |[v4/group_open_http_svc/import_group_msg ](/doc/product/269/导入群消息) | 
| 导入群成员  |[v4/group_open_http_svc/import_group_member](/doc/product/269/导入群成员) | 
| 设置成员未读消息计数  |[v4/group_open_http_svc/set_unread_msg_num](/doc/product/269/设置成员未读消息计数) | 
| 删除指定用户发送的消息  |[v4/group_open_http_svc/delete_group_msg_by_sender](/doc/product/269/删除指定用户发送的消息) | 
| 搜索群组  |[v4/group_open_http_svc/search_group](/doc/product/269/模糊搜索群组) | 
| 拉取群漫游消息  |[v4/group_open_http_svc/group_msg_get_simple](/doc/product/269/拉取群漫游消息) | 


## 5 资料管理 

| 功能说明 | 接口 | 
|---------|---------|
| 拉取资料 | [v4/profile/portrait_get ](/doc/product/269/拉取资料)| 
| 设置资料  | [v4/profile/portrait_set](/doc/product/269/设置资料) | 

## 6 关系链管理 

| 功能说明 | 接口 | 
|---------|---------|
| 添加好友  | [v4/sns/friend_import](/doc/product/269/添加好友)|
| 删除好友   | [v4/sns/friend_delete](/doc/product/269/删除好友) |
| 删除所有好友  | [v4/sns/friend_delete_all](/doc/product/269/删除所有好友) |
| 校验好友  | [v4/sns/friend_check](/doc/product/269/校验好友) |
| 拉取好友   | [v4/sns/friend_get_all](/doc/product/269/拉取好友) |

## 7 脏字管理

| 功能说明 | 接口 | 
|---------|---------|
| 添加脏字  | [v4/openim_dirty_words/get](/doc/product/269/查询APP自定义脏字)|
| 删除脏字   | [v4/openim_dirty_words/add](/doc/product/269/添加APP自定义脏字) |
| 删除所有脏字  | [v4/openim_dirty_words/delete](/doc/product/269/删除APP自定义脏字) |
## 8 数据下载

| 功能说明 |接口 | 
|---------|---------|
| 消息记录下载  |[v4/open_msg_svc/get_history](/doc/product/269/消息记录下载) | 

## 9 在线状态
| 功能说明 |接口 | 
|---------|---------|
| 获取用户在线状态 |[ v4/openim/querystate](/doc/product/269/获取用户在线状态) | 
## 10 全局禁言管理
| 功能说明 |接口 | 
|---------|---------|
| 设置全局禁言 |[ v4/openconfigsvr/setnospeaking](/doc/product/269/4230) | 
| 查询全局禁言 |[ v4/openconfigsvr/getnospeaking](/doc/product/269/4229) | 