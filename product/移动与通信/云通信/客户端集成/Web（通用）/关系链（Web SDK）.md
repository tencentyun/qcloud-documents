## 申请增加好友 

```
/* function applyAddFriend 
 *   申请添加好友
 * params:
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err 为错误对象
 * return:
 *   (无)
 */
applyAddFriend: function(options, cbOk, cbErr) {},
```

**示例： **

```
//申请加好友
var applyAddFriend = function () {
    var len = webim.Tool.getStrBytes($("#af_add_wording").val());
    if (len > 120) {
        alert('您输入的附言超过字数限制(最长 40 个汉字)');
        return;
    }
    var add_friend_item = [
        {
            'To_Account': $("#af_to_account").val(),
            "AddSource": "AddSource_Type_Unknow",
            "AddWording": $("#af_add_wording").val() //加好友附言，可为空
        }
    ];
    var options = {
        'From_Account': loginInfo.identifier,
        'AddFriendItem': add_friend_item
    };
    webim.applyAddFriend(
            options,
            function (resp) {
                if (resp.Fail_Account && resp.Fail_Account.length > 0) {
                    for (var i in resp.ResultItem) {
                        alert(resp.ResultItem[i].ResultInfo);
                        break;
                    }
                } else {
                    if ($('#af_allow_type').val() == '允许任何人') {
                        //重新加载好友列表
                        getAllFriend(getAllFriendsCallbackOK);
                        alert('添加好友成功');
                    } else {
                        $('#add_friend_dialog').modal('hide');
                        alert('申请添加好友成功');
                    }
                }
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
};
```

## 拉取好友申请 

```
/* function getPendency 
 *   拉取好友申请
 * params:
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err 为错误对象
 * return:
 *   (无)
 */
getPendency: function(options, cbOk, cbErr) {},
```

**示例：** 

```
//读取好友申请列表
var getPendency = function () {
    initGetPendencyTable([]);
    var options = {
        'From_Account': loginInfo.identifier,
        'PendencyType': 'Pendency_Type_ComeIn',
        'StartTime': 0,
        'MaxLimited': totalCount,
        'LastSequence': 0
    };
    webim.getPendency(
            options,
            function (resp) {
                var data = [];
                if (resp.UnreadPendencyCount > 0) {
                    for (var i in resp.PendencyItem) {
                        var apply_time = webim.Tool.formatTimeStamp(
                        resp.PendencyItem[i].AddTime);
                        var nick = webim.Tool.formatText2Html(resp.PendencyItem[i].Nick);
                        if (nick == '') {
                            nick = resp.PendencyItem[i].To_Account;
                        }
                        var addWording = webim.Tool.formatText2Html(
                        resp.PendencyItem[i].AddWording);
                        data.push({
                            To_Account: resp.PendencyItem[i].To_Account,
                            Nick: nick,
                            AddWording: addWording,
                            AddSource: resp.PendencyItem[i].AddSource,
                            AddTime: apply_time
                        });
                    }
                }
                $('#get_pendency_table').bootstrapTable('load', data);
                $('#get_pendency_dialog').modal('show');
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
};
```

## 响应好友申请 

```
/* function responseFriend 
 *   响应好友申请
 * params:
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err 为错误对象
 * return:
 *   (无)
 */
responseFriend: function(options, cbOk, cbErr) {},
```

**示例：** 

```
//处理好友申请
var responseFriend = function () {
    var response_friend_item = [
        {
            'To_Account': $("#rf_to_account").val(),
            "ResponseAction": $('input[name="rf_action_radio"]:checked').val()
            //类型：Response_Action_Agree 或者 Response_Action_AgreeAndAdd
        }
    ];
    var options = {
        'From_Account': loginInfo.identifier,
        'ResponseFriendItem': response_friend_item
    };
    webim.responseFriend(
            options,
            function (resp) {
                //在表格中删除对应的行
                $('#get_pendency_table').bootstrapTable('remove', {
                    field: 'To_Account',
                    values: [$("#rf_to_account").val()]
                });
                $('#response_friend_dialog').modal('hide');
                if (response_friend_item[0].ResponseAction 
                    == 'Response_Action_AgreeAndAdd') {
                    getAllFriend(getAllFriendsCallbackOK);
                }
                alert('处理好友申请成功');
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
};
```

## 删除好友申请 

```
/* function deletePendency 
 *   删除好友申请
 * params:
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err 为错误对象
 * return:
 *   (无)
 */
deletePendency: function(options, cbOk, cbErr) {},
```

**示例：** 

```
//删除申请列表
var deletePendency = function (del_account) {
    var options = {
        'From_Account': loginInfo.identifier,
        'PendencyType': 'Pendency_Type_ComeIn',
        'To_Account': [del_account]
    };
    webim.deletePendency(
            options,
            function (resp) {
                //在表格中删除对应的行
                $('#get_pendency_table').bootstrapTable('remove', {
                    field: 'To_Account',
                    values: [del_account]
                });
                alert('删除好友申请成功');
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
};
```

## 我的好友列表 

```
/* function getAllFriend
 *   拉取我的好友
 * params:
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err 为错误对象
 * return:
 *   (无)
 */
getAllFriend: function(options, cbOk, cbErr) {},
```

**示例：** 

```
//初始化聊天界面左侧好友列表框
var getAllFriend = function (cbOK, cbErr) {
    var options = {
        'From_Account': loginInfo.identifier,
        'TimeStamp': 0,
        'StartIndex': 0,
        'GetCount': totalCount,
        'LastStandardSequence': 0,
        "TagList":
                [
                    "Tag_Profile_IM_Nick",
                    "Tag_SNS_IM_Remark"
                ]
    };
    webim.getAllFriend(
            options,
            function (resp) {
                //清空聊天对象列表
                var sessList = document.getElementsByClassName("sesslist")[0];
                sessList.innerHTML = "";
                if (resp.FriendNum > 0) {
                    var friends = resp.InfoItem;
                    if (!friends || friends.length == 0) {
                        return;
                    }
                    var count = friends.length;
                    for (var i = 0; i < count; i++) {
                        var friend_name = friends[i].Info_Account;
                        if (friends[i].SnsProfileItem && friends[i].SnsProfileItem[0] 
                            && friends[i].SnsProfileItem[0].Tag) {
                            friend_name = friends[i].SnsProfileItem[0].Value;
                        }
                        if (friend_name.length > 7) {//帐号或昵称过长，截取一部分
                            friend_name = friend_name.substr(0, 7) + "...";
                        }
                        //增加一个好友div
                        addSess(friends[i].Info_Account, webim.Tool.formatText2Html(
                        friend_name), 
                        friendHeadUrl, 0, 'sesslist');
                    }
                    if (selType == SessionType.C2C) {
                        //清空聊天界面
                        document.getElementsByClassName("msgflow")[0].innerHTML = "";
                        //默认选中当前聊天对象
                        selToID = friends[0].Info_Account;
                        //设置当前选中用户的样式为选中样式
                        var selSessDiv = $("#sessDiv_" + selToID)[0];
                        selSessDiv.className = "sessinfo-sel";
                        var selBadgeDiv = $("#badgeDiv_" + selToID)[0];
                        selBadgeDiv.style.display = "none";
                    }
                    if (cbOK)
                        cbOK();
                }
            },
            function (err) {
                //alert(err.ErrorInfo);
            }
    );
};
```

## 删除好友 

```
/* function deleteFriend
 *   删除好友
 * params:
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err 为错误对象
 * return:
 *   (无)
 */
deleteFriend: function(options, cbOk, cbErr) {},
```

**示例：** 

```
//删除好友
var deleteFriend = function () {
    if (!confirm("确定删除该好友吗？")) {
        return;
    }
    var to_account = [];
    to_account = [
        $("#df_to_account").val()
    ];
    if (to_account.length <= 0) {
        return;
    }
    var options = {
        'From_Account': loginInfo.identifier,
        'To_Account': to_account,
        //Delete_Type_Both'//单向删除："Delete_Type_Single", 双向删除："Delete_Type_Both".
        'DeleteType': $('input[name="df_type_radio"]:checked').val()
    };
    webim.deleteFriend(
            options,
            function (resp) {
                //在表格中删除对应的行
                $('#get_my_friend_table').bootstrapTable('remove', {
                    field: 'Info_Account',
                    values: [$("#df_to_account").val()]
                });
                //重新加载好友列表
                getAllFriend(getAllFriendsCallbackOK);
                $('#delete_friend_dialog').modal('hide');
                alert('删除好友成功');
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
};
```

## 增加黑名单 

```
/* function addBlackList 
 *   增加黑名单
 * params:
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err 为错误对象
 * return:
 *   (无)
 */
addBlackList: function(options, cbOk, cbErr) {},
```

**示例：** 

```
//添加黑名单
var addBlackList = function (add_account) {
    var to_account = [];
    if (add_account) {
        to_account = [add_account];
    }
    if (0 == to_account.length) {
        alert('需要拉黑的帐号为空');
        return;
    }
    var options = {
        'From_Account': loginInfo.identifier,
        'To_Account': to_account
    };
    webim.addBlackList(
            options,
            function (resp) {
                //在表格中删除对应的行
                $('#get_my_friend_table').bootstrapTable('remove', {
                    field: 'Info_Account',
                    values: [add_account]
                });
                //重新加载好友列表
                getAllFriend(getAllFriendsCallbackOK);
                alert('添加黑名单成功');
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
};
```

## 我的黑名单 

```
/* function getBlackList  
 *   删除黑名单
 * params:
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err 为错误对象
 * return:
 *   (无)
 */
getBlackList: function(options, cbOk, cbErr) {},
```

**示例：**

```
//我的黑名单
var getBlackList = function (cbOK, cbErr) {
    initGetBlackListTable([]);
    var options = {
        'From_Account': loginInfo.identifier,
        'StartIndex': 0,
        'MaxLimited': totalCount,
        'LastSequence': 0
    };
    webim.getBlackList(
            options,
            function (resp) {
                var data = [];
                if (resp.BlackListItem && resp.BlackListItem.length > 0) {
                    for (var i in resp.BlackListItem) {
                        var add_time = webim.Tool.formatTimeStamp(
                        resp.BlackListItem[i].AddBlackTimeStamp);
                        data.push({
                            To_Account: resp.BlackListItem[i].To_Account,
                            AddBlackTimeStamp: add_time
                        });
                    }
                }
                $('#get_black_list_table').bootstrapTable('load', data);
                $('#get_black_list_dialog').modal('show');
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
};
```

## 删除黑名单 

```
/* function deleteBlackList  
 *   我的黑名单
 * params:
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err 为错误对象
 * return:
 *   (无)
 */
deleteBlackList: function(options, cbOk, cbErr) {},
```

**示例：**

```
//删除黑名单
var deleteBlackList = function (del_account) {
    var to_account = [
        del_account
    ];
    var options = {
        'From_Account': loginInfo.identifier,
        'To_Account': to_account
    };
    webim.deleteBlackList(
            options,
            function (resp) {
                //在表格中删除对应的行
                $('#get_black_list_table').bootstrapTable('remove', {
                    field: 'To_Account',
                    values: to_account
                });
                alert('删除黑名单成功');
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
};
```