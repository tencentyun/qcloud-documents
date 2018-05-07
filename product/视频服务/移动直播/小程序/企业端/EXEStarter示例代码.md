如下视频代码展示了如何使用 EXEStarter.js 启动 TXCloudRoom.exe

```html
<HTML>
<HEAD>
    <meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
    <TITLE>web+exe解决方案test</TITLE>
    <script type="text/javascript" src="./js/jquery.min.js" charset="utf-8"></script>
    <script type="text/javascript" src="./js/EXEStarter.js" charset="utf-8"></script>
</HEAD>
<BODY>
    <input type=submit value="开课" onClick="opencourse()">
    <input type=submit value="下载EXE"  id="download" style="display:none" onClick="downloadExe()">
    <div id="text_div"></div>
    <script>
        function downloadExe() {
            window.open(EXEStarter.EXEUrl);
        }
        function opencourse()
		{
            var userID = 'user_1212312', roomID = 'room_123123'; //您业务中的userid和roomid
            var roomserverInfo;
            var roomServerDomain = "https://room.qcloud.com/";
            //第一步：通过您的账号userid，获取roomserver的 usersig
            getSDKLoginInfo({
                data: {  userID: userID, roomServerDomain:
                       roomServerDomain,method : "GET",time: 24 * 60 * 60 * 7
                },
                success: function (res) {
                    if (res.status && res.status === 200) {
                        roomserverInfo = res.data;

                        //第二步：设置事件监听
                        EXEStarter.setListener({
                            onRoomClose: function (ret) { 
                                //监控返回的事件，具体参考SDK接口。
                                alert("【errMsg:" + ret.data.msg + "】");
                            }
                        });

                        document.getElementById('text_div').innerHTML = '正在打开EXE，请稍后.....';
                        //第三步：通过usersig和您的房间信息，拉起本地应用程序。
                        EXEStarter.createExeAsRoom({
                            userdata: {
                                userID: roomserverInfo.userID,
                                userName: "雷锋",
                                sdkAppID: roomserverInfo.sdkAppID,
                                accType: roomserverInfo.accountType,
                                userSig: roomserverInfo.userSig,
                            },
                            roomdata: {
                                serverDomain: roomServerDomain,
                                roomAction: EXEStarter.RoomAction.CreateRoom,
                                roomID: roomID,
                                roomName: "雷锋的房间",
                                roomTitle: "LiveRoom视频直播间",
                                roomLogo: "",
                                type: EXEStarter.StyleType.LiveRoom,
                                template: EXEStarter.Template.Template1V3,
                            },
                            success: function (ret) { },
                            fail: function (ret) {
                                //ret.errCode == -1，本地未检测有安装EXE，需要处理下载逻辑
                                alert("createExeAsRoom error: ret.code:" + ret.errCode + ", ret.msg:" + ret.errMsg);
                                if (ret.errCode == -1) {
                                    //下载exe，此处需要UI交互，用js触发的下载会被chrome拦截。
                                    //window.open(EXEStarter.EXEUrl);
                                    document.getElementById('download').style.display = 'block';
                                }
                            },
                        })
                    }
                },
            });
           
        }
    </script>
</BODY>
</HTML>
```

