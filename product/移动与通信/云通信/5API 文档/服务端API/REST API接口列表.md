## 帐号管理

| 功能说明  | 接口 |
|---------|---------|
| 导入单个帐号 | [v4/im_open_login_svc/account_import](/doc/product/269/独立模式帐号导入接口) |
| 导入批量帐号 | [v4/im_open_login_svc/multiaccount_import](/doc/product/269/独立模式帐号批量导入接口) |
| 失效帐号登录态  | [v4/im_open_login_svc/kick](/doc/product/269/帐号登录态失效接口) |

## 在线状态

| 功能说明         | 接口                                                       |
| ---------------- | ---------------------------------------------------------- |
| 获取用户在线状态 | [ v4/openim/querystate](/doc/product/269/获取用户在线状态) |

## 资料管理

| 功能说明 | 接口                                                         |
| -------- | ------------------------------------------------------------ |
| 拉取资料 | [v4/profile/portrait_get](https://cloud.tencent.com/document/product/269/1639) |
| 设置资料 | [v4/profile/portrait_set](https://cloud.tencent.com/document/product/269/1640 ) |

## 关系链管理

| 功能说明 | 接口                                                         |
| -------- | ------------------------------------------------------------ |
| 添加好友 | [v4/sns/friend_add](https://cloud.tencent.com/document/product/269/1643) |
| 导入好友 | [v4/sns/friend_import](https://cloud.tencent.com/document/product/269/8301) |
| 删除好友 | [v4/sns/friend_delete](https://cloud.tencent.com/document/product/269/1644) |
| 删除所有好友 | [v4/sns/friend_delete_all](https://cloud.tencent.com/document/product/269/1645) |
| 校验好友 | [v4/sns/friend_check](https://cloud.tencent.com/document/product/269/1646) |
| 拉取好友 | [v4/sns/friend_get_all](https://cloud.tencent.com/document/product/269/1647) |
| 拉取指定好友 | [v4/sns/friend_get_list](https://cloud.tencent.com/document/product/269/8609) |
| 添加黑名单 | [v4/sns/black_list_add](https://cloud.tencent.com/document/product/269/3718) |
| 删除黑名单 | [v4/sns/black_list_delete](https://cloud.tencent.com/document/product/269/3719) |
| 拉取黑名单 | [v4/sns/black_list_get](https://cloud.tencent.com/document/product/269/3722) |
| 校验黑名单 | [v4/sns/black_list_check](https://cloud.tencent.com/document/product/269/3725) |
| 添加分组 | [v4/sns/group_add](https://cloud.tencent.com/document/product/269/10107) |
| 删除分组 | [v4/sns/group_delete](https://cloud.tencent.com/document/product/269/10108) |

## 单聊消息

| 功能说明  | 接口 |
|---------|---------|
| 单发单聊消息 | [v4/openim/sendmsg](/doc/product/269/单发单聊消息) |
| 批量发单聊消息 | [v4/openim/batchsendmsg](/doc/product/269/批量发单聊消息) |
| 导入单聊消息 | [v4/openim/importmsg](/doc/product/269/导入单聊消息) |

## 群组管理

| 功能说明               | 接口                                                         |
| ---------------------- | ------------------------------------------------------------ |
| 获取APP中的所有群组    | [v4/group_open_http_svc/get_appid_group_list](/doc/product/269/获取APP中的所有群组) |
| 创建群组               | [v4/group_open_http_svc/create_group](/doc/product/269/创建群组) |
| 获取群组详细资料       | [v4/group_open_http_svc/get_group_info](/doc/product/269/获取群组详细资料) |
| 获取群成员详细资料     | [v4/group_open_http_svc/get_group_member_info](/doc/product/269/获取群组成员详细资料) |
| 修改群组基础资料       | [v4/group_open_http_svc/modify_group_base_info](/doc/product/269/修改群组基础资料) |
| 增加群组成员           | [v4/group_open_http_svc/add_group_member](/doc/product/269/增加群组成员) |
| 删除群组成员           | [v4/group_open_http_svc/delete_group_member](/doc/product/269/删除群组成员) |
| 修改群组成员资料       | [v4/group_open_http_svc/modify_group_member_info](/doc/product/269/修改群成员资料) |
| 解散群组               | [v4/group_open_http_svc/destroy_group ](/doc/product/269/解散群组) |
| 获取用户所加入的群组   | [v4/group_open_http_svc/get_joined_group_list](/doc/product/269/获取用户所加入的群组) |
| 查询用户在群组中的身份 | [v4/group_open_http_svc/get_role_in_group](/doc/product/269/查询用户在群组中的身份) |
| 批量禁言和取消禁言     | [v4/group_open_http_svc/forbid_send_msg](/doc/product/269/批量禁言和取消禁言) |
| 获取群组被禁言用户列表 | [v4/group_open_http_svc/get_group_shutted_uin](/doc/product/269/获取群组被禁言用户列表) |
| 在群组中发送普通消息   | [v4/group_open_http_svc/send_group_msg](/doc/product/269/在群组中发送普通消息) |
| 在群组中发送系统通知   | [v4/group_open_http_svc/send_group_system_notification](/doc/product/269/在群组中发送系统通知) |
| 群组消息撤回           | [v4/group_open_http_svc/group_msg_recall](https://cloud.tencent.com/document/product/269/12341) |
| 转让群组               | [v4/group_open_http_svc/change_group_owner](/doc/product/269/转让群组) |
| 导入群基础资料         | [v4/group_open_http_svc/import_group](/doc/product/269/导入群基础资料) |
| 导入群消息             | [v4/group_open_http_svc/import_group_msg ](/doc/product/269/导入群消息) |
| 导入群成员             | [v4/group_open_http_svc/import_group_member](/doc/product/269/导入群成员) |
| 设置成员未读消息计数   | [v4/group_open_http_svc/set_unread_msg_num](/doc/product/269/设置成员未读消息计数) |
| 删除指定用户发送的消息 | [v4/group_open_http_svc/delete_group_msg_by_sender](/doc/product/269/删除指定用户发送的消息) |
| 拉取群漫游消息         | [v4/group_open_http_svc/group_msg_get_simple](/doc/product/269/拉取群漫游消息) |

## 消息推送
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

## 全局禁言管理
| 功能说明 |接口 |
|---------|---------|
| 设置全局禁言 |[ v4/openconfigsvr/setnospeaking](/doc/product/269/4230) |
| 查询全局禁言 |[ v4/openconfigsvr/getnospeaking](/doc/product/269/4229) |

## 脏字管理

| 功能说明 | 接口 |
|---------|---------|
| 查询 App 自定义脏字  | [v4/openim_dirty_words/get](/doc/product/269/查询APP自定义脏字)|
| 添加 App 自定义脏字   | [v4/openim_dirty_words/add](/doc/product/269/添加APP自定义脏字) |
| 删除 App 自定义脏字  | [v4/openim_dirty_words/delete](/doc/product/269/删除APP自定义脏字) |

## 运营管理

| 功能说明 |接口 |
|---------|---------|
| 下载消息记录  |[v4/open_msg_svc/get_history](/doc/product/269/1650) |
| 拉取运营数据  |[v4/openconfigsvr/getappinfo](/doc/product/269/4193) |
