## 3 群组管理
### 3.1	进群

本节主要介绍sdk 进群applyJoinBigGroup api。

函数名：

```
webim.applyJoinBigGroup
```

定义：

```
webim.applyJoinBigGroup(options,cbOk, cbErr)
```

参数列表：

| 名称 | 说明 | 类型 |
|---------|---------|---------|
|options|	进群信息对象|	Object|
|cbOk	|调用接口成功回调函数	|Function|
|cbErr	|调用接口失败回调函数	|Function|

其中options对象属性定义如下：

| 名称 | 说明 | 类型 |
|---------|---------|---------|
|GroupId	|要加入的群id	|String|

示例：

```
//加入直播大群
function applyJoinBigGroup(groupId) {
    var options = {
        'GroupId': groupId//群id
    };
    webim.applyJoinBigGroup(
            options,
            function (resp) {
                //JoinedSuccess:加入成功; WaitAdminApproval:等待管理员审批
                if (resp.JoinedStatus && resp.JoinedStatus == 'JoinedSuccess') {
                    webim.Log.info('加入房间成功');
                } else {
                    alert('加入房间失败');
                }
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
}
```

### 3.2	退群

本节主要介绍sdk 退群quitBigGroup api。

函数名：

```
webim.quitBigGroup
```

定义：

```
webim.quitBigGroup(options,cbOk, cbErr)
```

参数列表：

| 名称 | 说明 | 类型 |
|---------|---------|---------|
|options	|退群信息对象	|Object|
|cbOk	|调用接口成功回调函数	|Function|
|cbErr	|调用接口失败回调函数	|Function|

其中options对象属性定义如下：

| 名称 | 说明 | 类型 |
|---------|---------|---------|
|GroupId|要退出的群id	|String|

示例：

```
//退出大群
function quitBigGroup() {
    var options = {
        'GroupId': avChatRoomId//群id
    };
    webim.quitBigGroup(
            options,
            function (resp) {
                
                webim.Log.info('退群成功');
                $("#video_sms_list").find("li").remove(); 
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
}
```