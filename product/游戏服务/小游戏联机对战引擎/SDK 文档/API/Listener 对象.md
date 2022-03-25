>!由于产品逻辑已无法满足当前游戏技术发展，游戏联机对战引擎 MGOBE 将于2022年7月1日下线，请您在2022年6月30日前完成服务迁移。


Listener 对象为 MGOBE 的子属性，该对象方法全为静态方法，不需要实例化。该对象主要用于给 Room 对象的实例绑定广播事件监听。

### init

#### 接口描述
初始化监听器。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|gameInfo|[MGOBE.types.GameInfoPara](https://cloud.tencent.com/document/product/1038/35534#gameinfopara)|游戏信息|
|config|[MGOBE.types.ConfigPara](https://cloud.tencent.com/document/product/1038/35534#configpara)|游戏配置|
|callback|[MGOBE.types.ReqCallback](https://cloud.tencent.com/document/product/1038/33331#.E5.93.8D.E5.BA.94.E5.9B.9E.E8.B0.83.E5.87.BD.E6.95.B0-mgobe.types.reqcallback)&lt;null&gt;|初始化回调函数|

<dx-alert infotype="explain" title="">
- 该方法为静态方法。初始化 Listener 时需要传入 gameInfo 和 config 两个参数。
- 初始化结果在 callback 中异步返回，错误码为0表示初始化成功。
</dx-alert>



#### 返回值说明

无

#### 使用示例
```
    const gameInfo = {
        gameId: "xxxxx",
        openId: 'xxxxxx',
        secretKey: 'xxxxxx',
    };

    const config = {
        url: 'xxxxxxx.com',
        reconnectMaxTimes: 5,
        reconnectInterval: 1000,
        resendInterval: 1000,
        resendTimeout: 10000,
    };

    const room = new MGOBE.Room();

    Listener.init(gameInfo, config, event => {
        if (event.code === MGOBE.ErrCode.EC_OK) {
            console.log("初始化成功");
            // 初始化后才能添加监听
            Listener.add(room);
        } else {
            console.log("初始化失败");
        }
    });
```

### add

#### 接口描述
为 Room/Group 实例添加广播监听。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|entity|Room 或 Group|需要监听的房间/队组对象|

<dx-alert infotype="explain" title="">
- 该方法为静态方法。实例化 Room/Group 对象之后，需要通过该方法给 Room/Group 注册广播事件监听。
- Listener 完成初始化之后才能添加监听。
</dx-alert>


#### 返回值说明

无


#### 使用示例
```
    const room = new MGOBE.Room();
    // 初始化后才能添加监听
    Listener.add(room);
```

### remove

#### 接口描述
为 Room/Group 实例移除广播监听。

#### 参数描述

|参数名|类型/值|描述|
|:---|---|---|
|entity|Room 或 Group|需要移除监听的房间/队组对象|



<dx-alert infotype="explain" title="">
该方法为静态方法。如果不再需要监听某个 Room/Group 对象的广播事件，可以通过该方法进行移除。
</dx-alert>



#### 返回值说明

无


#### 使用示例
```
    const room = new MGOBE.Room();
    // 监听
    Listener.add(room);
    // 移除监听
    Listener.remove(room);
```

### clear

#### 接口描述
移除全部 Room/Group 对象的广播监听。

#### 参数描述

无



<dx-alert infotype="explain" title="">
该方法为静态方法。
</dx-alert>




#### 返回值说明

无


#### 使用示例
```
    Listener.clear();
```

