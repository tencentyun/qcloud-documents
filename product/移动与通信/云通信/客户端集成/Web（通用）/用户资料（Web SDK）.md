## 1 设置个人资料 

```
/* function setProfilePortrait
 *   设置个人资料
 * params:
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err为错误对象
 * return:
 *   (无)
 */
setProfilePortrait: function(options, cbOk, cbErr) {},
```

请求和应答参数请参考[设置资料协议说明](http://www.qcloud.com/doc/product/269/%E8%AE%BE%E7%BD%AE%E8%B5%84%E6%96%99)

**示例： **

```
//设置个人资料
var setProfilePortrait = function () {
    if ($("#spp_nick").val().length == 0) {
        alert('请输入昵称');
        return;
    }
    if (webim.Tool.trimStr($("#spp_nick").val()).length == 0) {
        alert('您输入的昵称全是空格,请重新输入');
        return;
    }
    var profile_item = [
        {
            "Tag": "Tag_Profile_IM_Nick",
            "Value": $("#spp_nick").val()
        },
        {
            "Tag": "Tag_Profile_IM_Gender",
            "Value": $('input[name="spp_gender_radio"]:checked').val()
        },
        {
            "Tag": "Tag_Profile_IM_AllowType",
            "Value": $('input[name="spp_allow_type_radio"]:checked').val()
        }
    ];
    var options = {
        'From_Account': loginInfo.identifier,
        'ProfileItem': profile_item
    };
    webim.setProfilePortrait(
            options,
            function (resp) {
                $('#set_profile_portrait_dialog').modal('hide');
                alert('设置个人资料成功');
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
};
```

## 2 获取个人资料 

```
/* function getProfilePortrait
 *   拉取资料（搜索用户）
 * params:
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err为错误对象
 * return:
 *   (无)
 */
getProfilePortrait: function(options, cbOk, cbErr) {},
```

请求和应答参数请参考[拉取资料协议说明](http://www.qcloud.com/doc/product/269/%E6%8B%89%E5%8F%96%E8%B5%84%E6%96%99)

**示例：** 

```
//搜索用户
var searchProfileByUserId = function () {
    if ($("#sp_to_account").val().length == 0) {
        alert('请输入用户ID');
        return;
    }
    if (webim.Tool.trimStr($("#sp_to_account").val()).length == 0) {
        alert('您输入的用户ID全是空格,请重新输入');
        return;
    }
    var tag_list = [
        "Tag_Profile_IM_Nick",
        "Tag_Profile_IM_Gender",
        "Tag_Profile_IM_AllowType"
    ];
    var options = {
        'From_Account': loginInfo.identifier,
        'To_Account': [$("#sp_to_account").val()],
        'LastStandardSequence': 0,
        'TagList': tag_list
    };
    webim.getProfilePortrait(
            options,
            function (resp) {
                var data = [];
                if (resp.UserProfileItem && resp.UserProfileItem.length > 0) {
                    for (var i in resp.UserProfileItem) {
                        var to_account = resp.UserProfileItem[i].To_Account;
                        var nick = null, gender = null, allowType = null;
                        for (var j in resp.UserProfileItem[i].ProfileItem) {
                            switch (resp.UserProfileItem[i].ProfileItem[j].Tag) {
                                case 'Tag_Profile_IM_Nick':
                                    nick = resp.UserProfileItem[i].ProfileItem[j].Value;
                                    break;
                                case 'Tag_Profile_IM_Gender':
                                    switch (resp.UserProfileItem[i].ProfileItem[j].Value) {
                                        case 'Gender_Type_Male':
                                            gender = '男';
                                            break;
                                        case 'Gender_Type_Female':
                                            gender = '女';
                                            break;
                                        case 'Gender_Type_Unknown':
                                            gender = '未知';
                                            break;
                                    }
                                    break;
                                case 'Tag_Profile_IM_AllowType':
                                    switch (resp.UserProfileItem[i].ProfileItem[j].Value) {
                                        case 'AllowType_Type_AllowAny':
                                            allowType = '允许任何人';
                                            break;
                                        case 'AllowType_Type_NeedConfirm':
                                            allowType = '需要确认';
                                            break;
                                        case 'AllowType_Type_DenyAny':
                                            allowType = '拒绝任何人';
                                            break;
                                        default:
                                            allowType = '需要确认';
                                            break;
                                    }
                                    break;
                            }
                        }
                        data.push({
                            'To_Account': to_account,
                            'Nick': webim.Tool.formatText2Html(nick),
                            'Gender': gender,
                            'AllowType': allowType
                        });
                    }
                }
                $('#search_profile_table').bootstrapTable('load', data);
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
};
```