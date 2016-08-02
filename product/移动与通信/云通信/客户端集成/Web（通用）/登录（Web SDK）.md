## 1 TLS登录（托管模式）
 
Demo集成了托管模式下的腾讯登录服务（Tencent Login Service，TLS），当帐号为独立模式时，请跳过这一小节，关于TLS账号集成（托管模式和独立模式）更多详细介绍，请参考链接：[云通信帐号登录集成](http://www.qcloud.com/doc/product/269/%E8%B4%A6%E5%8F%B7%E7%99%BB%E5%BD%95%E9%9B%86%E6%88%90%E8%AF%B4%E6%98%8E)，这里只介绍在demo中如何集成托管模式下的web 版TLS SDK。

在index.html引入web 版TLS sdk，如： 

```
<script type="text/javascript" src="https://tls.qcloud.com/libs/api.min.js"></script>
```

然后在页面中调用`TLSHelper.getQuery('tmpsig')`，判断是否获取到了临时身份凭证，没有，则调用`TLSHelper.goLogin({sdkappid: loginInfo.sdkAppID,acctype: loginInfo.accountType,url: callBackUrl})`，跳转到tls登录页面，登录成功会跳转到回调地址callBackUrl。

**示例： **

```
//判断是否已经拿到临时身份凭证
if (TLSHelper.getQuery('tmpsig')) {
    if (loginInfo.identifier == null) {
        console.info('start fetchUserSig');
        //获取正式身份凭证，成功后会回调tlsGetUserSig(res)函数
        TLSHelper.fetchUserSig();
    }
} else {//未登录
    if (loginInfo.identifier == null) {
        //弹出选择应用类型对话框
        $('#select_app_dialog').modal('show');
        $("body").css("background-color", 'white');
    }
}
//tls登录
function tlsLogin() {
    //跳转到TLS登录页面
    TLSHelper.goLogin({
        sdkappid: loginInfo.sdkAppID,
        acctype: loginInfo.accountType,
        url: callBackUrl
    });
}
```

如果已经拿到了临时凭证，则继续调用`TLSHelper.fetchUserSig()`获取正式身份凭证，成功之后会回调`tlsGetUserSig(res)`函数。 

**示例： **

```
//第三方应用需要实现这个函数，并在这里拿到UserSig
function tlsGetUserSig(res) {
    //成功拿到凭证
    if (res.ErrorCode == TlsErrorCode.OK) {
        //从当前URL中获取参数为identifier的值
        loginInfo.identifier = TLSHelper.getQuery("identifier");
        //拿到正式身份凭证
        loginInfo.userSig = res.UserSig;
        //从当前URL中获取参数为sdkappid的值
        loginInfo.sdkAppID = loginInfo.appIDAt3rd = Number(TLSHelper.getQuery("sdkappid"));
        //从cookie获取accountType
        var accountType = webim.Tool.getCookie('accountType');
        if (accountType) {
            loginInfo.accountType = accountType;
            initDemoApp();
        } else {
            alert('accountType非法');
        }
    } else {
        //签名过期，需要重新登录
        if (res.ErrorCode == TlsErrorCode.SIGNATURE_EXPIRATION) {
            tlsLogin();
        } else {
            alert("[" + res.ErrorCode + "]" + res.ErrorInfo);
        }
    }
}
```


## 2 Sdk登录

本节主要介绍sdk 登录login api。

函数名：

```
webim.login
```

定义：

```
webim.login(loginInfo, listeners, options,cbOk,cbErr)
```

示例：

```
//sdk登录
function webimLogin() {
    webim.login(
            loginInfo, listeners, options,
            function (resp) {
                loginInfo.identifierNick = resp.identifierNick;//设置当前用户昵称
                initDemoApp();
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
}
```

下面介绍每个参数的定义。

### 2.1 用户信息对象loginInfo


属性名：

| 名称 | 说明 | 类型 |
|---------|---------|---------|
|sdkAppID	|用户标识接入SDK的应用ID，必填|	String|
|appIDAt3rd	|App用户使用OAuth授权体系分配的Appid，和sdkAppID一样，必填	|String|
|accountType|	账号类型，必填|	Integer|
|identifier	|用户帐号，选填	|String|
|identifierNick|	用户昵称，选填	|String|
|userSig	|鉴权Token，identifier不为空时，userSig必填	|String|



### 2.2	事件回调对象listeners


属性名：

| 名称 | 说明 | 类型 |
|---------|---------|---------|
|onConnNotify	|用于监听用户连接状态变化的函数，选填	|Function|
|jsonpCallback	|用于IE9(含)以下浏览器中jsonp回调函数,移动端可不填，pc端必填|	Function|
|onMsgNotify	|监听新消息函数，必填	|Function|
|onGroupSystemNotifys	|监听（多终端同步）群系统消息事件，必填|	Object|
|onGroupInfoChangeNotify|	监听群资料变化事件，选填	|Function|


示例：

```
//监听事件
var listeners = {
    "onConnNotify": onConnNotify,
    "jsonpCallback": jsonpCallback, //IE9(含)以下浏览器用到的jsonp回调函数
    "onMsgNotify": onMsgNotify, //监听新消息(私聊，群聊，群提示消息)事件
    "onGroupInfoChangeNotify": onGroupInfoChangeNotify, //监听群资料变化事件
    "groupSystemNotifys": groupSystemNotifys//监听（多终端同步）群系统消息事件
};
```



### 2.3	事件回调对象listeners.onConnNotify


示例：

```
//监听连接状态回调变化事件
var onConnNotify = function (resp) {
    switch (resp.ErrorCode) {
        case webim.CONNECTION_STATUS.ON:
            //webim.Log.warn('连接状态正常...');
            break;
        case webim.CONNECTION_STATUS.OFF:
            webim.Log.warn('连接已断开，无法收到新消息，请检查下你的网络是否正常');
            break;
        default:
            webim.Log.error('未知连接状态,status=' + resp.ErrorCode);
            break;
    }
};
```

其中回调返回的参数resp对象属性定义如下：

| 名称 | 说明 | 类型 |
|---------|---------|---------|
|ActionStatus	|连接状态标识，OK-标识连接成功FAIL-标识连接失败|	String|
|ErrorCode	|连接状态码，具体请参考webim. CONNECTION_STATUS常量对象|Integer|
|ErrorInfo	|错误提示信息	|String|


### 2.4	事件回调对象listeners.jsonpCallback

为了兼容低版本的ie浏览器，sdk使用了jsonp技术调用后台接口。

示例：

```
//位于js/demo_base.js中
//IE9(含)以下浏览器用到的jsonp回调函数
function jsonpCallback(rspData) {
//设置jsonp返回的
    webim.setJsonpLastRspData(rspData);
}
```


属性名：

| 名称 | 说明 | 类型 |
|---------|---------|---------|
|rspData	|接口返回的数据	|String|



### 2.5	事件回调对象listeners.onMsgNotify


示例：

```
//监听新消息事件
//newMsgList 为新消息数组，结构为[Msg]
function onMsgNotify(newMsgList) {
    //console.warn(newMsgList);
    var sess, newMsg;
    //获取所有聊天会话
    var sessMap = webim.MsgStore.sessMap();

    for (var j in newMsgList) {//遍历新消息
        newMsg = newMsgList[j];

        if (newMsg.getSession().id() == selToID) {//为当前聊天对象的消息
            selSess = newMsg.getSession();
            //在聊天窗体中新增一条消息
            //console.warn(newMsg);
            addMsg(newMsg);
        }
    }
    //消息已读上报，以及设置会话自动已读标记
    webim.setAutoRead(selSess, true, true);

    for (var i in sessMap) {
        sess = sessMap[i];
        if (selToID != sess.id()) {//更新其他聊天对象的未读消息数
            updateSessDiv(sess.type(), sess.id(), sess.unread());
        }
    }
}
```

其中参数newMsgList 为webim.Msg数组，即[webim.Msg]


### 2.6	事件回调对象listeners.onGroupSystemNotifys

示例：

```
//监听（多终端同步）群系统消息方法，方法都定义在receive_group_system_msg.js文件中
//注意每个数字代表的含义，比如，
//1表示监听申请加群消息，2表示监听申请加群被同意消息，3表示监听申请加群被拒绝消息
var groupSystemNotifys = {
    "1": onApplyJoinGroupRequestNotify, //申请加群请求（只有管理员会收到）
    "2": onApplyJoinGroupAcceptNotify, //申请加群被同意（只有申请人能够收到）
    "3": onApplyJoinGroupRefuseNotify, //申请加群被拒绝（只有申请人能够收到）
    "4": onKickedGroupNotify, //被管理员踢出群(只有被踢者接收到)
    "5": onDestoryGroupNotify, //群被解散(全员接收)
    "6": onCreateGroupNotify, //创建群(创建者接收)
    "7": onInvitedJoinGroupNotify, //邀请加群(被邀请者接收)
    "8": onQuitGroupNotify, //主动退群(主动退出者接收)
    "9": onSetedGroupAdminNotify, //设置管理员(被设置者接收)
    "10": onCanceledGroupAdminNotify, //取消管理员(被取消者接收)
    "11": onRevokeGroupNotify, //群已被回收(全员接收)
    "255": onCustomGroupNotify//用户自定义通知(默认全员接收)
};
```


更详细介绍，请参考第10节。


### 2.7	事件回调对象listeners.onGroupInfoChangeNotify

示例：

```
//监听 群资料变化 群提示消息
function onGroupInfoChangeNotify(groupInfo) {
    webim.Log.warn("执行 群资料变化 回调： " + JSON.stringify(groupInfo));
    var groupId = groupInfo.GroupId;
    var newFaceUrl = groupInfo.GroupFaceUrl;//新群组图标, 为空，则表示没有变化
    var newName = groupInfo.GroupName;//新群名称, 为空，则表示没有变化
    var newOwner = groupInfo.OwnerAccount;//新的群主id, 为空，则表示没有变化
    var newNotification = groupInfo.GroupNotification;//新的群公告, 为空，则表示没有变化
    var newIntroduction = groupInfo.GroupIntroduction;//新的群简介, 为空，则表示没有变化

    if (newName) {
        //更新群组列表的群名称
        //To do
        webim.Log.warn("群id=" + groupId + "的新名称为：" + newName);
    }
}
```


其中返回的参数groupInfo对象属性如下：

属性名：

| 名称 | 说明 | 类型 |
|---------|---------|---------|
|GroupId	|群id	|String|
|GroupFaceUrl |	新群组图标, 为空，则表示没有变化|String|
|GroupName	|新群名称, 为空，则表示没有变化	|String|
|OwnerAccount	|新的群主id, 为空，则表示没有变化|	String|
|GroupNotification	|新的群公告, 为空，则表示没有变化	|String|
|GroupIntroduction	|新的群简介, 为空，则表示没有变化|	String|


### 2.8	其他对象options

属性名：

| 名称 | 说明 | 类型 |
|---------|---------|---------|
|isAccessFormalEnv	|是否访问正式环境下的后台接口，True-访问正式，False-访问测试环境默认访问正式环境接口，选填	|Boolean|
|isLogOn	|是否开启控制台打印日志,True-开启;False-关闭，默认开启，选填|	Boolean|


### 2.9	回调函数cbOk & cbErr

Sdk登录时，可以定义成功回调函数和失败回调函数。

示例：

```
//sdk登录
function webimLogin() {
    webim.login(
            loginInfo, listeners, options,
            function (resp) {
                loginInfo.identifierNick = resp.identifierNick;//设置当前用户昵称
                initDemoApp();
            },
            function (err) {
                alert(err.ErrorInfo);
            }
    );
}
```