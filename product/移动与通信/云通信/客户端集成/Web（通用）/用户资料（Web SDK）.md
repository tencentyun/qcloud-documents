## 1 设置个人资料 

```
/* function setProfilePortrait
 *   设置个人资料
 * params:
 *   options	-Object, 请求参数
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err为错误对象
 * return:
 *   (无)
 */
setProfilePortrait: function(options, cbOk, cbErr) {},
```

### 1.1 options参数示例


```
{
    "ProfileItem":
    [
        {
            "Tag":"Tag_Profile_IM_Nick", 
            "Value":"MyNickName"
        },
		{
            "Tag":"Tag_Profile_IM_Gender", 
            "Value":"Gender_Type_Male"
        },
		{
            "Tag":"Tag_Profile_IM_AllowType", 
            "Value":"AllowType_Type_NeedConfirm"
        },
		{
            "Tag":"Tag_Profile_IM_Image", 
            "Value":"http://image.demo.com/head.jpg"
        }
    ]
}
```

### 1.2 options参数字段说明 

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| ProfileItem | Array | 必填 | 待设置的用户的资料对象数组，数组中每一个对象都包含了Tag和Value。 |
| Tag | String | 必填 | 指定要设置的资料字段的名称，支持标配资料字段和自定义资料字段的设置，标配资料字段的相关信息参见：[标配资料字段](http://www.qcloud.com/doc/product/269/%E8%B5%84%E6%96%99%E7%B3%BB%E7%BB%9F#3-.E6.A0.87.E9.85.8D.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)；自定义资料字段的相关信息参见：[自定义资料字段](http://www.qcloud.com/doc/product/269/%E8%B5%84%E6%96%99%E7%B3%BB%E7%BB%9F#4-.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)。 |
| Value | uint64_t/string/bytes | 必填 | 待设置的资料字段的值，详情可参见[资料字段](http://www.qcloud.com/doc/product/269/%E8%B5%84%E6%96%99%E7%B3%BB%E7%BB%9F#2-.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)。  |

### 1.3 应答包体示例

```
{
    "ActionStatus":"FAIL",
    "ErrorCode":40001,
    "ErrorInfo":"Err_Profile_Comm_Decode_Fail",
    "ErrorDisplay":""
}
```

### 1.4 应答包字段说明 

| 字段 | 类型 | 说明 |
|---------|---------|---------|
| ActionStatus | String | 请求处理的结果，“OK”表示处理成功，“FAIL”表示失败。 |
| ErrorCode | Integer | 错误码。  |
| ErrorInfo | String  | 详细错误信息。 |
| ErrorDisplay | String  | 详细的客户端展示信息。 |


### 1.5 代码示例 

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
    var gender=$('input[name="spp_gender_radio"]:checked').val();
    if(!gender){
        alert('请选择性别');
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
        'ProfileItem': profile_item
    };

    webim.setProfilePortrait(
            options,
            function (resp) {
                $('#set_profile_portrait_dialog').modal('hide');
                loginInfo.identifierNick=$("#spp_nick").val();//更新昵称
                document.getElementById("t_my_name").innerHTML = loginInfo.identifierNick;
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
 *   options	-Object, 请求参数
 *   cbOk	- function()类型, 成功时回调函数
 *   cbErr	- function(err)类型, 失败时回调函数, err为错误对象
 * return:
 *   (无)
 */
getProfilePortrait: function(options, cbOk, cbErr) {},
```

### 2.1 options参数示例


#### 2.1.1 读一个用户的一个资料字段

```
{
    "To_Account":["id1"], 
    "TagList":
    [
        "Tag_Profile_IM_Nick"
    ]
}
```

#### 2.1.2 读一个用户的多个资料字段

```
{
    "To_Account":["id1"], 
    "TagList":
    [
        "Tag_Profile_IM_Nick",
        "Tag_Profile_IM_AllowType",
        "Tag_Profile_IM_SelfSignature",
        "Tag_Profile_Custom_888888_Test"
    ]
}
```

#### 2.1.3 读多个用户的一个资料字段

```
{
    "To_Account":["id1","id2","id3"], 
    "TagList":
    [
        "Tag_Profile_IM_Nick"
    ]
}
```

#### 2.1.4 读多个用户的多个资料字段

```
{
    "To_Account":["id1","id2","id3"], 
    "TagList":
    [
        "Tag_Profile_IM_Nick",
        "Tag_Profile_IM_AllowType",
        "Tag_Profile_IM_SelfSignature",
        "Tag_Profile_Custom_888888_Test"
    ]
}
```

### 2.2 options字段说明 

| 字段 | 类型 | 属性 | 说明 |
|---------|---------|---------|---------|
| To_Account | Array | 必填 |需要拉取这些Identifier的资料  |
| TagList | Array | 必填 |指定要拉取的资料对象的名称，支持标配资料和自定义资料的拉取，标配资料的相关信息参见：[标配资料字段](http://www.qcloud.com/doc/product/269/%E8%B5%84%E6%96%99%E7%B3%BB%E7%BB%9F#3-.E6.A0.87.E9.85.8D.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)；自定义资料的相关信息参见：[自定义资料字段](http://www.qcloud.com/doc/product/269/%E8%B5%84%E6%96%99%E7%B3%BB%E7%BB%9F#4-.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)。  |


### 2.3 应答包体示例

#### 2.3.1 读一个用户的一个资料字段

```
{
    "UserProfileItem":
    [
        {
            "To_Account":"id1",
            "ProfileItem":
            [
                {
                    "Tag":"Tag_Profile_IM_Nick",
                    "Value":"NickNameTest1"
                }
            ],
            "ResultCode":0,
            "ResultInfo":""
        }
    ],
    "Fail_Account":[],
    "Invalid_Account":[],
    "ActionStatus":"OK",
    "ErrorCode":0,
    "ErrorInfo":"",
    "ErrorDisplay":""
}
```

#### 2.3.2 读一个用户的多个资料字段

```
{
    "UserProfileItem":
    [
        {
            "To_Account":"id1",
            "ProfileItem":
            [
                {
                    "Tag":"Tag_Profile_IM_Nick",
                    "Value":"NickNameTest1"
                },
                {
                    "Tag":"Tag_Profile_IM_AllowType",
                    "Value":"AllowType_Type_NeedConfirm"
                },
                {
                    "Tag":"Tag_Profile_IM_SelfSignature",
                    "Value":"I'm Test1"
                },
                {
                    "Tag":"Tag_Profile_Custom_888888_Test",
                    "Value":"Custom Data1"
                }
            ],
            "ResultCode":0,
            "ResultInfo":""
        }
    ],
    "Fail_Account":[],
    "Invalid_Account":[],
    "ActionStatus":"OK",
    "ErrorCode":0,
    "ErrorInfo":"",
    "ErrorDisplay":""
}
```

#### 2.3.3 读多个用户的一个资料字段

```
{
    "UserProfileItem":
    [
        {
            "To_Account":"id1",
            "ProfileItem":
            [
                {
                    "Tag":"Tag_Profile_IM_Nick",
                    "Value":"NickNameTest1"
                }
            ],
            "ResultCode":0,
            "ResultInfo":""
        },
        {
            "To_Account":"id2",
            "ProfileItem":
            [
                {
                    "Tag":"Tag_Profile_IM_Nick",
                    "Value":"NickNameTest2"
                }
            ],
            "ResultCode":0,
            "ResultInfo":""
        },
        {
            "To_Account":"id3",
            "ProfileItem":
            [
                {
                    "Tag":"Tag_Profile_IM_Nick",
                    "Value":"NickNameTest3"
                }
            ],
            "ResultCode":0,
            "ResultInfo":""
        }
    ],
    "Fail_Account":[],
    "Invalid_Account":[],
    "ActionStatus":"OK",
    "ErrorCode":0,
    "ErrorInfo":"",
    "ErrorDisplay":""
}
```

#### 2.3.4 读多个用户的多个资料字段

```
{
    "UserProfileItem":
    [
        {
            "To_Account":"id1",
            "ProfileItem":
            [
                {
                    "Tag":"Tag_Profile_IM_Nick",
                    "Value":"NickNameTest1"
                },
                {
                    "Tag":"Tag_Profile_IM_AllowType",
                    "Value":"AllowType_Type_NeedConfirm"
                },
                {
                    "Tag":"Tag_Profile_IM_SelfSignature",
                    "Value":"I'm Test1"
                },
                {
                    "Tag":"Tag_Profile_Custom_888888_Test",
                    "Value":"Custom Data1"
                }
            ],
            "ResultCode":0,
            "ResultInfo":""
        },
        {
            "To_Account":"id2",
            "ProfileItem":
            [
                {
                    "Tag":"Tag_Profile_IM_Nick",
                    "Value":"NickNameTest2"
                },
                {
                    "Tag":"Tag_Profile_IM_AllowType",
                    "Value":"AllowType_Type_DenyAny"
                },
                {
                    "Tag":"Tag_Profile_IM_SelfSignature",
                    "Value":"I'm Test2"
                },
                {
                    "Tag":"Tag_Profile_Custom_888888_Test",
                    "Value":"Custom Data2"
                }
            ],
            "ResultCode":0,
            "ResultInfo":""
        },
        {
            "To_Account":"id3",
            "ProfileItem":
            [
                {
                    "Tag":"Tag_Profile_IM_Nick",
                    "Value":"NickNameTest3"
                },
                {
                    "Tag":"Tag_Profile_IM_AllowType",
                    "Value":"AllowType_Type_AllowAny"
                },
                {
                    "Tag":"Tag_Profile_IM_SelfSignature",
                    "Value":"I'm Test3"
                },
                {
                    "Tag":"Tag_Profile_Custom_888888_Test",
                    "Value":"Custom Data3"
                }
            ],
            "ResultCode":0,
            "ResultInfo":""
        }
    ],
    "Fail_Account":[],
    "Invalid_Account":[],
    "ActionStatus":"OK",
    "ErrorCode":0,
    "ErrorInfo":"",
    "ErrorDisplay":""
}
```

### 2.4 应答包字段说明 

| 字段 | 类型 | 说明 |
|---------|---------|---------|
| UserProfileItem | Array | 返回的用户资料结构化信息。 |
| To_Account | String |返回的用户的Identifier。  |
| ProfileItem | Array | 返回的用户的资料对象数组，数组中每一个对象都包含了Tag和Value。 |
| Tag | String | 返回的资料对象的名称，标配资料的相关信息参见：[标配资料字段](http://www.qcloud.com/doc/product/269/%E8%B5%84%E6%96%99%E7%B3%BB%E7%BB%9F#3-.E6.A0.87.E9.85.8D.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)；自定义资料的相关信息参见：[自定义资料字段](http://www.qcloud.com/doc/product/269/%E8%B5%84%E6%96%99%E7%B3%BB%E7%BB%9F#4-.E8.87.AA.E5.AE.9A.E4.B9.89.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)。 |
| Value | uint64_t/string/bytes | 拉取的资料对象的值，详情可参见[资料字段](http://www.qcloud.com/doc/product/269/%E8%B5%84%E6%96%99%E7%B3%BB%E7%BB%9F#2-.E8.B5.84.E6.96.99.E5.AD.97.E6.AE.B5)。  |
| ResultCode | Integer | 返回的单个用户的结果，0表示正确，非0表示错误。  |
| ResultInfo | String | 返回的单个用户的结果详细信息。  |
| Fail_Account | Array | 返回处理失败的用户列表。  |
| Invalid_Account | Array | 返回请求包中的非法用户列表。  |
| ActionStatus | String | 请求处理的结果，“OK”表示处理成功，“FAIL”表示失败。 |
| ErrorCode | Integer | 错误码。  |
	| ErrorInfo | String  | 详细错误信息。 |
| ErrorDisplay | String  | 详细的客户端展示信息。 |


### 2.5 代码示例 

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
        "Tag_Profile_IM_Nick",//昵称
        "Tag_Profile_IM_Gender",//性别
        "Tag_Profile_IM_AllowType",//加好友方式
        "Tag_Profile_IM_Image"//头像
    ];
    var options = {
        'To_Account': [$("#sp_to_account").val()],
        'TagList': tag_list
    };

    webim.getProfilePortrait(
            options,
            function (resp) {
                var data = [];
                if (resp.UserProfileItem && resp.UserProfileItem.length > 0) {
                    for (var i in resp.UserProfileItem) {
                        var to_account = resp.UserProfileItem[i].To_Account;
                        var nick = null, gender = null, allowType = null,imageUrl=null;
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
                                case 'Tag_Profile_IM_Image':
                                    imageUrl = resp.UserProfileItem[i].ProfileItem[j].Value;
                                    break;
                            }
                        }
                        data.push({
                            'To_Account': to_account,
                            'Nick': webim.Tool.formatText2Html(nick),
                            'Gender': gender,
                            'AllowType': allowType,
                            'Image': imageUrl
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