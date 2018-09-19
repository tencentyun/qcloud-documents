## 白板 SDK 简介

白板 SDK 已经集成在 TICKSDK 中，可以通过 getBoardInstance() 获取白板实例。


## 集成 SDK

在页面中加载以下 SDK。

```
<!-- COS SDK -->
<script src="https://sqimg.qq.com/expert_qq/cos/5.0.0/cos.mini.js"></script>
<!-- 白板SDK -->
<script src="https://sqimg.qq.com/expert_qq/edu/2.2.0/board_sdk.mini.js"></script>
```

**建议直接使用腾讯云 CDN 加速的 SDK**。

| 类                  | 说明                                       |
| ------------------ | ---------------------------------------- |
| BoardSDK     |  白板 SDK 对外唯一类，提供初始化以及白板操作功能 |

### 白板 SDK 主要接口

| 接口          | 说明      |
| ------------------ | ---------------------------------------- |
| getBoardData | 获取白板数据 |
| addBoard | 新增一页白板 |
| deleteBoard | 删除一页白板 |
| prevBoard | 向前翻页 |
| nextBoard | 向后翻页 |
| getBoardList | 获取白板列表 |
| getCurrentBoard | 获取当前白板 ID |
| switchBoard | 白板翻页（切换白板） |
| setGlobalBackgroundColor | 设置全局颜色 |
| setBackgroundColor | 设置当前页颜色 |
| setColor | 设置画笔颜色 |
| setThin | 设置线条的粗细 |
| setType | 设置涂鸦类型 |
| undo | 当前白板页撤销 |
| canUndo | 判断当前白板页是否还能撤销 |
| redo | 当前白板页恢复 |
| canRedo | 判断当前白板页是否还能恢复 |
| clear | 清空当前页涂鸦 + 背景色/图片 |
| clearDraws | 清空当前页涂鸦(保留背景色/图片) |
| setBackgroundPic | 设置当前页的背景图 |
| clearGlobalBgColor | 清除全局背景色 |
| deleteFile | 删除文件 |
| switchFile | 切换文件 |
| getFile | 获取白板中所有的文件 |
| getBoardByFile | 根据文件获取该文件的所有白板 |
| setCanDraw | 设置白板能不能涂鸦 |
| addBackgroundPic | 增加一白板，并设置该白板的背景图 |
| clearFileDraws | 清空文件涂鸦 |
| getCosInstance | 获取 COS 对象实例 |
| addFile | 上传文件，支持 doc、docx、Excel、PPT、PDF |
| addImgFile | 上传图片 |

### 白板 SDK 使用


#### 实例化白板

```
this.boardSdk = new BoardSDK(options);
```

##### 白板初始化参数 options

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
id | String | 是 | 白板渲染的在 dom 节点 ID，并保证该节点有 position: relative 样式，否则可能会引起白板定位异常的问题。
conf_id | integer | 是 | 课堂 ID
user | String | 否 | 白板用户昵称
canDraw | boolean | 否，默认 true | 白板是否可以涂鸦
color | String | 否，默认红色 |画笔颜色，只接受  Hex 色值，如 #ff00ff，大小写不敏感
globalBackgroundColor | String | 否，默认白色 | 全局的白板背景色，只接受 Hex 色值，如 #ff00ff，大小写不敏感
tlsData | Object | 是 | 白板用户鉴权信息

##### tlsData参数

参数	| 类型	| 是否必填 | 描述
--------- | --------- | ----- | --------- |
sdkAppId | Integer | 是 | 腾讯云应用的唯一标识，可以登录 [实时音视频控制台](https://console.cloud.tencent.com/rav)查看
identifier | String | 是 | 用户名
userSig | String | 是 | 登录鉴权信息

该方法传入参数，identifier 和 userSig，identifier 为用户 ID，userSig 为腾讯云后台用来鉴权的用户签名，相当于登录 TICSDK 的用户密码，需要开发者服务器遵守腾讯云生成 userSig 的规则来生成，并下发给 Web 端。

**在开发调试阶段，用户可以在自己的腾讯云应用控制台使用开发辅助工具，来生成临时的uid和userSig用于开发测试**。详情请参考 [生成签名](https://cloud.tencent.com/document/product/647/17275)。


### 白板 SDK 接口

#### 1. 设置白板是否能够涂鸦

```
board.setCanDraw(draw)
```

参数：

| 参数 |  类型     | 说明 |
| ----------- | ----------- | ------------------ |
| draw |   Boolean   | true 白板可以涂鸦  false 白板不能涂鸦  默认是 true |

#### 2. 获取白板涂鸦数据

```
board.getBoardData()
```

返回值:

|   类型     | 说明 |
| ----------- | ------------------ |
|   Array   | 返回白板数据 |

#### 3. 新增一页白板

```
board.addBoard()
```

#### 4. 删除一页白板

```
board.deleteBoard(boarId)
```

参数：

| 参数 |  类型     | 说明 |
| ----------- | ----------- | ------------------ |
| boarId |   String   | 需要删除的白板 ID，为空表示删除当前页 |


#### 5. 向前翻页

```
board.prevBoard()
```

#### 6. 向后翻页

```
board.nextBoard()
```

#### 7. 获取白板列表

```
board.getBoardList()
```

返回值:

|   类型     | 说明 |
| ----------- | ------------------ |
|   Array   | 返回白板列表 |

#### 8. 获取当前白板 ID

```
board.getCurrentBoard()
```

返回值:

|   类型     | 说明 |
| ----------- | ------------------ |
|   String   | 获取当前白板 ID |


#### 9. 白板翻页（切换白板）

```
board.switchBoard(boardid)
```

参数:

| 参数 |  类型     | 说明 |
| --- | -------- | ------------------ |
| boardid |  String   |  要切换的白板 ID |


#### 10. 设置全局颜色

```
board.setGlobalBackgroundColor(color)
```

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| color |  String   |   Hex 色值，如 #ff00ff |

#### 11. 设置当前页颜色

```
board.setBackgroundColor(color)
```

参数:

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| color |  String   |  Hex 色值，如 #ff00ff |

#### 12. 设置画笔颜色

```
board.setColor(color)
```

参数:

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| color |  String   |  Hex 色值，如 #ff00ff |

#### 13. 设置画笔的粗细

```
board.setThin(thin)
```

参数:

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| thin |  number   |  默认 100 |

#### 14. 设置涂鸦类型

```
board.setType(type)
```

参数:

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| type |  String   |  默认 line，支持的类型可以参考 BoardSDK.DRAW_TYPE |


#### 15. 当前白板页撤销

```
board.undo()
```

#### 16. 判断当前白板页是否还能撤销

```
board.canUndo()
```

#### 17. 当前白板页恢复

```
board.redo()
```

#### 18. 判断当前白板页是否还能恢复

```
board.canRedo()
```


#### 19. 清空当前页涂鸦 + 背景色/图片

```
board.clear()
```

#### 20. 清空当前页涂鸦(保留背景色/图片)

```
board.clearDraws()
```

#### 21. 设置当前页的背景图

```
board.setBackgroundPic(url)
```

参数:

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| url |  String   | 图片的 URL 地址 |


#### 22. 清除全局背景色

```
board.clearGlobalBgColor()
```

#### 23. 删除文件

```
board.deleteFile()
```

#### 24. 获取白板中上传的所有的文件

```
board.getFile()
```

返回值:

|   类型     | 说明 |
| ----------- | ------------------ |
|   Array   | 返回白板中所有的文件 |


#### 25. 根据文件获取该文件的所有白板

```
board.getBoardByFile(fid)
```

参数:

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| fid |  String   | 文件 ID, 为空时，表示默认的分组 |

返回值:

|   类型     | 说明 |
| ----------- | ------------------ |
|   Array   | 返回白板中所有的文件 |


#### 26. 增加一白板，并设置该白板的背景图

```
board.addBackgroundPic(url, switchNewBoard)
```

参数:

| 参数 |   类型     | 是否必填 |说明 |
| --- |----------- | ---- |------------------ |
| url |  String    | 是 | 图片的url |
| switchNewBoard   |  Booelan | 否，默认 true | 是否需要切换至当前的这一页 |


返回值:

|   类型     | 说明 |
| ----------- | ------------------ |
|   String   | 返回新增白板 ID |


#### 27. 清空文件涂鸦

```
board.clearFileDraws(fids)
```

参数:

| 参数 |   类型     | 是否必填 |说明 |
| --- |----------- | ---- |------------------ |
| fids |  Array    | 是 | 要清空涂鸦的文件id |


#### 28. 获取 COS 对象实例

```
board.getCosInstance()
```


返回值:

|   类型     | 说明 |
| ----------- | ------------------ |
|   COS   | 返回 COS 对象 |



#### 29. 上传文件，支持 doc、docx、Excel、PPT、PDF

```
board.addFile(file, succ, fail)
```

参数:

| 参数 |   类型     | 是否必填 |说明 |
| --- |----------- | ---- |------------------ |
| file |  File    | 是 | 文件对象，通常这样获取 document.getElementById('file_input').files[0] |
| succ |  Function    | 否 | 上传成功的回调 |
| fail |  Function    | 否 | 上传失败的回调 |

#### 30. 上传图片

```
board.addImgFile(imgFile, succ, fail)
```

参数:

| 参数 |   类型     | 是否必填 |说明 |
| --- |----------- | ---- |------------------ |
| file |  File    | 是 | 文件对象，通常这样获取document.getElementById('file_input').files[0] |
| succ |  Function    | 否 | 上传成功的回调 |
| fail |  Function    | 否 | 上传失败的回调 |


-----


### 白板事件


#### 监听事件

当初始化完成后，则需要进行事件监听，监听关键的事件来实现相关的业务。

事件监听的方法：

```
boardSdk.on('事件名'，回调函数);
```

比如：
```
var boardSdk = new TICSDK();
boardSdk.on(BoardSDK.CONSTANT.EVENT.HISTROY_DATA_COMPLETE, res => {
  // 业务侧逻辑
});
```

| 事件名 | 描述 | 
|--------- | ---------|
| BoardSDK.CONSTANT.EVENT.BOARD.HISTROY_DATA_COMPLETE | 历史数据同步完成 |
| BoardSDK.CONSTANT.EVENT.BOARD.REAL_TIME_DATA | 接收到其他端的同步数据 |
| BoardSDK.CONSTANT.EVENT.BOARD.ADD_BOARD | 新增白板 |
| BoardSDK.CONSTANT.EVENT.BOARD.DELETE_BOARD | 删除白板 |
| BoardSDK.CONSTANT.EVENT.BOARD.SWITCH_BOARD | 切换白板 |
| BoardSDK.CONSTANT.EVENT.BOARD.ADD_GROUP | 增加组/文件 |
| BoardSDK.CONSTANT.EVENT.BOARD.DELETE_GROUP | 删除组/文件 |
| BoardSDK.CONSTANT.EVENT.BOARD.SWITCH_GROUP | 切换组/文件 |
| BoardSDK.CONSTANT.EVENT.BOARD.ADD_DATA_ERROR | 接收到其他端的同步数据解析错误 |
| BoardSDK.CONSTANT.EVENT.BOARD.IMG_START_LOAD | 背景图片开始加载 |
| BoardSDK.CONSTANT.EVENT.BOARD.IMG_LOAD | 背景图片加载完成 |
| BoardSDK.CONSTANT.EVENT.BOARD.IMG_ERROR | 背景图片加载错误 |
| BoardSDK.CONSTANT.EVENT.BOARD.IMG_ABORT | 背景图片加载中断 |
| BoardSDK.CONSTANT.EVENT.BOARD.VERIFY_SDK_SUCC | 白板服务鉴权通过 |
| BoardSDK.CONSTANT.EVENT.BOARD.VERIFY_SDK_ERROR | 白板服务鉴权失败,请先购买服务 |
| BoardSDK.CONSTANT.EVENT.BOARD.CANVAS_MOUSEDOWN | 白板鼠标点击事件 |
| BoardSDK.CONSTANT.EVENT.BOARD.CANVAS_MOUSEMOVE | 白板鼠标移动事件 |
| BoardSDK.CONSTANT.EVENT.BOARD.CANVAS_MOUSEUP | 白板鼠标弹起事件 |
| BoardSDK.CONSTANT.EVENT.BOARD.CANVAS_MOUSELEAVE | 白板鼠标移出白板范围事件 |


#### 注销事件监听

```
boardSdk.off('事件名');
```

比如：
```
var boardSdk = new TICSDK();
boardSdk.off(BoardSDK.CONSTANT.EVENT.HISTROY_DATA_COMPLETE);
```


### 涂鸦类型

BoardSDK.DRAW_TYPE：

| 涂鸦类型 | 类型 | 值 | 描述 |
| --- | --- | --- | --- |
| LINE | String | line | 普通画笔，默认 |
| ERASER | String | eraser | 橡皮擦 |
| RASER | String | raser | 激光笔 |
| POINTSELECT | String | pointselect | 点选 |
| SELECT | String | select | 框选 |
| GRAPH_LINE | String | graph-line | 直线 |
| GRAPH_CIRCLE | String | graph-circle | 空心圆 |
| GRAPH_RECT | String | graph-rect | 空心矩形 |
| GRAPH_OVAL | String | graph-oval | 空心椭圆 |
| GRAPH_CIRCLE_SOLID | String | graph-circle-solid | 实心圆 |
| GRAPH_RECT_SOLID | String | graph-rect-solid | 实心矩形 |
| GRAPH_OVAL_SOLID | String | graph-oval-solid | 实心椭圆 |
