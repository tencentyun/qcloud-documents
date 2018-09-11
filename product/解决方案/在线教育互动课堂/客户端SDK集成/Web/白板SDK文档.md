## 白板SDK简介

> 白板SDK已经集成在TICKSDK中，可以通过getBoardInstance()获取白板实例。

| 类                  | 说明                                       |
| ------------------ | ---------------------------------------- |
| BoardSDK     |  白板SDK对外唯一类，提供初始化以及白板操作功能 |

### 白板SDK主要接口

| 接口          | 说明      |
| ------------------ | ---------------------------------------- |
| getBoardData | 获取白板数据 |
| addBoard | 新增一页白板 |
| deleteBoard | 删除一页白板 |
| prevBoard | 向前翻页 |
| nextBoard | 向后翻页 |
| getBoardList | 获取白板列表 |
| getCurrentBoard | 获取当前白板ID |
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

### 白板SDK使用

#### 1. 设置白板是否能够涂鸦

```
board.setCanDraw(draw)
```

参数：

| 参数 |  类型     | 说明 |
| ----------- | ----------- | ------------------ |
| draw |   Boolean   | true 白板可以涂鸦  false 白板不能涂鸦  默认是true |

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
| boarId |   String   | 需要删除的白板ID，为空表示删除当前页 |


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

#### 8. 获取当前白板ID

```
board.getCurrentBoard()
```

返回值:

|   类型     | 说明 |
| ----------- | ------------------ |
|   String   | 获取当前白板ID |


#### 9. 白板翻页（切换白板）

```
board.switchBoard(boardid)
```

参数:

| 参数 |  类型     | 说明 |
| --- | -------- | ------------------ |
| boardid |  String   |  要切换的白板ID |


#### 10. 设置全局颜色

```
board.setGlobalBackgroundColor(color)
```

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| color |  String   |  hex色值，如 #ff00ff |

#### 11. 设置当前页颜色

```
board.setBackgroundColor(color)
```

参数:

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| color |  String   |  hex色值，如 #ff00ff |

#### 12. 设置画笔颜色

```
board.setColor(color)
```

参数:

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| color |  String   |  hex色值，如 #ff00ff |

#### 13. 设置画笔的粗细

```
board.setThin(thin)
```

参数:

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| thin |  number   |  默认100 |

#### 14. 设置涂鸦类型

```
board.setType(type)
```

参数:

| 参数 |   类型     | 说明 |
| --- |----------- | ------------------ |
| type |  String   |  默认line, 支持的类型可以参考BoardSDK.DRAW_TYPE |


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
| url |  String   | 图片的URL地址 |


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
| fid |  String   | 文件ID, 为空时，表示默认的分组 |

返回值:

|   类型     | 说明 |
| ----------- | ------------------ |
|   Array   | 返回白板中所有的文件 |

-----

### 涂鸦类型

> BoardSDK.DRAW_TYPE

| 涂鸦类型 | 类型 | 值 | 描述 |
| --- | --- | --- | --- |
| LINE | <code>String</code> | <code>line</code> | 普通画笔，默认 |
| ERASER | <code>String</code> | <code>eraser</code> | 橡皮擦 |
| RASER | <code>String</code> | <code>raser</code> | 激光笔 |
| POINTSELECT | <code>String</code> | <code>pointselect</code> | 点选 |
| SELECT | <code>String</code> | <code>select</code> | 框选 |
| GRAPH_LINE | <code>String</code> | <code>graph-line</code> | 直线 |
| GRAPH_CIRCLE | <code>String</code> | <code>graph-circle</code> | 空心圆 |
| GRAPH_RECT | <code>String</code> | <code>graph-rect</code> | 空心矩形 |
| GRAPH_OVAL | <code>String</code> | <code>graph-oval</code> | 空心椭圆 |
| GRAPH_CIRCLE_SOLID | <code>String</code> | <code>graph-circle-solid</code> | 实心圆 |
| GRAPH_RECT_SOLID | <code>String</code> | <code>graph-rect-solid</code> | 实心矩形 |
| GRAPH_OVAL_SOLID | <code>String</code> | <code>graph-oval-solid</code> | 实心椭圆 |


### 白板数据实时收发

不同端白板间的数据传输是建立在腾讯`IMSDK`建立的即时信道上的，该功能已经封装在TICSDK内部，开发者无需自行实行。

---

### 白板数据上报备份和拉取填充

课堂中，老师对白板的操作，涂鸦、图片、PPT、撤销、清空等操作需要上报到后台，并进行存储，这样后面中途加入课堂的成员就能拉取之前的白板数据进行展示。

该过程主要分为两步，数据上报和数据拉取：

**白板数据上报：**
在每次对白板操作后，SDK会将操作的数据上报到白板后台，目前SDK内部已经实现了该功能，白板后台服务也是由我们维护，开发者无需自行实现。

**白板数据拉取（同步）：**
每次进入课堂时，TICSDK 会拉取该课堂的所有历史白板消息，展示在白板上，该功能也已经在TICSDK内部实现，开发者无需自行实行。