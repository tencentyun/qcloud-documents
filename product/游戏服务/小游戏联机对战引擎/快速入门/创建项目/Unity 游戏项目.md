
本文档以 Unity Editor 2019.3 版本为例，指导开发者在 Unity 项目中快速接入游戏联机对战引擎 MGOBE 。

## 版本支持
Unity Editor 版本： 2019.1.9+。

## 前提条件

- 已在游戏联机对战引擎控制台创建游戏实例，并开通联机对战服务。
- 已获取游戏 gameID 和 secretKey。


## 操作步骤
### 创建游戏项目
1. 打开 Unity Hub，创建一个游戏项目。如下图所示：
![](https://tva1.sinaimg.cn/large/007S8ZIlgy1get4lqc9haj31bl0u047r.jpg)
2. 单击【创建】，进入项目开发界面：
![](https://tva1.sinaimg.cn/large/007S8ZIlgy1get4ni1sl2j31c00u0tfs.jpg)


### 导入 Mgobe Package
1. 将 com.unity.Mgobe.unitypackage 拖入 editor 中的 Project 栏，单击【import】进行 package 导入。 单击进入 [Package 下载](https://cloud.tencent.com/document/product/1038/33406) 页面。
![](https://tva1.sinaimg.cn/large/007S8ZIlgy1get5f4ycq5j31bu0n87ba.jpg)
![](https://tva1.sinaimg.cn/large/007S8ZIlgy1get5ug7wg4j30yj0u0tip.jpg)
2. 在 Assets 目录下创建 “Scripts” 文件夹，并新建 Scripts/main.cs 文件。
3. 在 Hierachy 视图下，右击 SampleScene，选中 GameObject > CreateEmpty，新建一个空的游戏对象。
![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf4jabgegvj30k00eojs7.jpg)
4. 选中新建的 GameObject，拖动 main.cs，添加为该 GameObject 的 Component。
![](https://tva1.sinaimg.cn/large/007S8ZIlgy1gf4jcjjhomj31c00u010v.jpg)
5. 参考以下示例代码，将 mgobe package 导入 main.cs。
```c#
using Packages.com.unity.mgobe.Runtime.src;
using Packages.com.unity.mgobe.Runtime.src.SDK;
using Lagame;
```



### 调用 API 
1. 在 main.cs 中输入以下代码，完成 SDK 初始化，获得 room 实例。
```c#
GameInfoPara gameInfo = new GameInfoPara {
    // 替换 为控制台上的“游戏ID”
    GameId = "XXXXXXXXXXXXXX",
    // 玩家 openId
    OpenId = "openid_123_test",
    //替换 为控制台上的“游戏Key”
    SecretKey = "XXXXXXXXXXXXXX"
};

ConfigPara config = new ConfigPara {
    // 替换 为控制台上的“域名”
    Url = "XXXXXXX.wxlagame.com",
    ReconnectMaxTimes = 5,
    ReconnectInterval = 1000,
    ResendInterval = 1000,
    ResendTimeout = 10000
};

// 初始化监听器 Listener
  Listener.Init (gameInfo, config, (ResponseEvent eve) => {
      if (eve.Code == 0) {
          Debug.Log ("初始化成功");
    // 初始化成功之后才能调用其他 API
    var room = new Room(null);
    // ...
  }
  // 初始化广播回调事件

});
```
2. 修改初始化回调函数，调用 room 对象的查询房间接口（getRoomDetail），即可验证是否成功接入对战平台。示例代码如下所示：
```c#
 // 初始化监听器 Listener
Listener.Init (gameInfo, config, (ResponseEvent eve) => {
    if (eve.Code == 0) {
        Debug.Log ("初始化成功");
        // 初始化成功之后才能调用其他 API
        //查询玩家自己的房间
        var room = new Room (null);
        room.GetRoomDetail ((ResponseEvent e) => {
            if (e.Code != 0 && e.Code != 20011) {
                Debug.Log ("初始化失败");
            }
            // Type type = e.data.GetType();
            // Debug.LogFormat ("查询成功: {0}", type);
            Debug.Log ("查询成功");
            if (e.Code == 20011) {
                Debug.Log ("玩家不在房间内");
            } else {
                // 玩家已在房间内
                var res = (GetRoomByRoomIdRsp) e.Data;
                Debug.LogFormat ("房间名 {0}", res.RoomInfo.Name);
            }
        });
    } else {
        Debug.LogFormat ("初始化失败: {0}", eve.Code);
    }
    // 初始化广播回调事件
});
```
3. 编译并运行项目，控制台中输出“查询成功”信息即表示接入成功。
