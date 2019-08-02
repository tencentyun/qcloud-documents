## 帐号管理

| 功能说明  | 接口 |
|---------|---------|
| 导入单个帐号 | [v4/im_open_login_svc/account_import](https://cloud.tencent.com/document/product/269/1608) |
| 导入批量帐号 | [v4/im_open_login_svc/multiaccount_import](https://cloud.tencent.com/document/product/269/4919) |
| 帐号删除接口  | [v4/im_open_login_svc/account_delete](https://cloud.tencent.com/document/product/269/36443) |
| 失效帐号登录态  | [v4/im_open_login_svc/kick](https://cloud.tencent.com/document/product/269/3853) |

## 在线状态

| 功能说明         | 接口                                                       |
| ---------------- | ---------------------------------------------------------- |
| 获取用户在线状态 | [ v4/openim/querystate](https://cloud.tencent.com/document/product/269/2566) |

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
| 拉取好友 | [v4/sns/friend_get](https://cloud.tencent.com/document/product/269/1647) |
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
| 单发单聊消息 | [v4/openim/sendmsg](https://cloud.tencent.com/document/product/269/2282) |
| 批量发单聊消息 | [v4/openim/batchsendmsg](https://cloud.tencent.com/document/product/269/1612) |
| 导入单聊消息 | [v4/openim/importmsg](https://cloud.tencent.com/document/product/269/2568) |

## 群组管理

| 功能说明               | 接口                                                         |
| ---------------------- | ------------------------------------------------------------ |
| 获取APP中的所有群组    | [v4/group_open_http_svc/get_appid_group_list](https://cloud.tencent.com/document/product/269/1614) |
| 创建群组               | [v4/group_open_http_svc/create_group](https://cloud.tencent.com/document/product/269/1615) |
| 获取群组详细资料       | [v4/group_open_http_svc/get_group_info](https://cloud.tencent.com/document/product/269/1616) |
| 获取群成员详细资料     | [v4/group_open_http_svc/get_group_member_info](https://cloud.tencent.com/document/product/269/1617) |
| 修改群组基础资料       | [v4/group_open_http_svc/modify_group_base_info](https://cloud.tencent.com/document/product/269/1620) |
| 增加群组成员           | [v4/group_open_http_svc/add_group_member](https://cloud.tencent.com/document/product/269/1621) |
| 删除群组成员           | [v4/group_open_http_svc/delete_group_member](https://cloud.tencent.com/document/product/269/1622) |
| 修改群组成员资料       | [v4/group_open_http_svc/modify_group_member_info](https://cloud.tencent.com/document/product/269/1623) |
| 解散群组               | [v4/group_open_http_svc/destroy_group ](https://cloud.tencent.com/document/product/269/1624) |
| 获取用户所加入的群组   | [v4/group_open_http_svc/get_joined_group_list](https://cloud.tencent.com/document/product/269/1625) |
| 查询用户在群组中的身份 | [v4/group_open_http_svc/get_role_in_group](https://cloud.tencent.com/document/product/269/1626) |
| 批量禁言和取消禁言     | [v4/group_open_http_svc/forbid_send_msg](https://cloud.tencent.com/document/product/269/1627) |
| 获取群组被禁言用户列表 | [v4/group_open_http_svc/get_group_shutted_uin](https://cloud.tencent.com/document/product/269/2925) |
| 在群组中发送普通消息   | [v4/group_open_http_svc/send_group_msg](https://cloud.tencent.com/document/product/269/1629) |
| 在群组中发送系统通知   | [v4/group_open_http_svc/send_group_system_notification](https://cloud.tencent.com/document/product/269/1630) |
| 群组消息撤回           | [v4/group_open_http_svc/group_msg_recall](https://cloud.tencent.com/document/product/269/12341) |
| 转让群组               | [v4/group_open_http_svc/change_group_owner](https://cloud.tencent.com/document/product/269/1633) |
| 导入群基础资料         | [v4/group_open_http_svc/import_group](https://cloud.tencent.com/document/product/269/1634) |
| 导入群消息             | [v4/group_open_http_svc/import_group_msg ](https://cloud.tencent.com/document/product/269/1635) |
| 导入群成员             | [v4/group_open_http_svc/import_group_member](https://cloud.tencent.com/document/product/269/1636) |
| 设置成员未读消息计数   | [v4/group_open_http_svc/set_unread_msg_num](https://cloud.tencent.com/document/product/269/1637) |
| 删除指定用户发送的消息 | [v4/group_open_http_svc/delete_group_msg_by_sender](https://cloud.tencent.com/document/product/269/2359) |
| 拉取群漫游消息         | [v4/group_open_http_svc/group_msg_get_simple](https://cloud.tencent.com/document/product/269/2738) |


## 全局禁言管理
| 功能说明 |接口 |
|---------|---------|
| 设置全局禁言 |[ v4/openconfigsvr/setnospeaking](https://cloud.tencent.com/document/product/269/4230) |
| 查询全局禁言 |[ v4/openconfigsvr/getnospeaking](https://cloud.tencent.com/document/product/269/4229) |

## 脏字管理

| 功能说明 | 接口 |
|---------|---------|
| 查询 App 自定义脏字  | [v4/openim_dirty_words/get](https://cloud.tencent.com/document/product/269/2396)|
| 添加 App 自定义脏字   | [v4/openim_dirty_words/add](https://cloud.tencent.com/document/product/269/2397) |
| 删除 App 自定义脏字  | [v4/openim_dirty_words/delete](https://cloud.tencent.com/document/product/269/2398) |

## 运营管理

| 功能说明 |接口 |
|---------|---------|
| 下载消息记录  |[v4/open_msg_svc/get_history](https://cloud.tencent.com/document/product/269/1650) |
| 拉取运营数据  |[v4/openconfigsvr/getappinfo](https://cloud.tencent.com/document/product/269/4193) |
