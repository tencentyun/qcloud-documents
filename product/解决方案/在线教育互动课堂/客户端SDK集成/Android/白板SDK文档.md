## 主要类简介

| 类                  | 说明                                       |
| ------------------ | ---------------------------------------- |
| BoardSDK     |  白板 SDK 初始化类，App 启动时调用 init 方法进行初始化 |
| WhiteboardView     | 继承 SurfaceView，独立主线程渲染，白板数据采集和展示网络白板数据控件 |
| WhiteboardManager  | 白板主要业务逻辑管理类，提供了包括绘制参数设置、撤销、重做、擦除和选择等所有白板功能接口 |
| WhiteboardEventListener | 白板事件回调接口，业务须实现所有接口                               |
| WhiteboardConfig   | 白板绘制参数配置                             |
| WhiteboardEvent         | 白板事件的数据结构                 |


## 白板使用方法
### WhiteboardView 使用方法
跟普通的自定义控制使用方法相同，在布局文件中可以直接使用、按需继承。
```
<com.tencent.boardsdk.board.WhiteboardView
 android:id="@+id/cbv_board"
 android:layout_width="match_parent"
 android:layout_height="match_parent" />

```
>!为保证各端体验一致，白板视图的宽高比默认为16:9，WhiteboardView 控件内部已做处理，开发者直接使用即可。

**主要方法说明**

| 接口                  | 说明          |
| ------------------- | ----------- |
| setWhiteboardEnable | 关启白板绘制      |
| setDragEnable       | 关启白板缩放和拖拽功能 |
| setAspectRatio       | 设置控件宽高比例（高度/宽度，内置默认是9.0f/16.0f），控件初始化后调用 |

### WhiteboardManager 使用方法

#### 初始化
从 WhiteboardManager 获取 WhiteboardConfig 实例（也可自己构建），设置相关参数后，通过 WhiteboardManager 的`init`方法进行初始化。

```
WhiteboardConfig config = WhiteboardManager.getInstance().getConfig();
config.setPaintSize(6).setPaintColor(Color.BLUE);
WhiteboardManager.getInstance().init(getActivity().getBaseContext(), config);
```
#### 主要方法说明

**初始化和释放：**

| 接口                                 | 说明                                       |
| ---------------------------------- | ---------------------------------------- |
| init                               | 初始化白板绘制参数                              |
| release                               | 释放白板相关资源，在退出课堂时调用                              |

**白板事件监听：**

| 接口                                 | 说明                                       |
| ---------------------------------- | ---------------------------------------- |
| setEventListener                    |设置白板绘制回调，**如果通过 TIC SDK 使用白板，不要单独设置次监听，否则会导致白板功能异常**                              |

**白板管理接口：**

| 接口                                 | 说明                                       |
| ---------------------------------- | ---------------------------------------- |
| createSubBoard                   | 创建子白板  					|
| switchBoardById                   |切换白板  					|
| deleteBoardById                   | 删除白板及其内容，并切换至默认白板 					|
| whiteboardPageCtrlById             | 删除白板及其内容，并切换至指定白板，如未指定目标白板，则切换至目标白板 	|
| getCurrentWhiteboardId                   | 获取当前白板 ID  					|
| getBoardList                   | 获取白板 ID 列表  					|
| getFidList                   | 获取文件 ID 列表信息，包括普通白板  					|

**白板数据接口：**

| 接口                                 | 说明                                       |
| ---------------------------------- | ---------------------------------------- |
| getBoardData                   | 同步课堂白板历史数据，仅在进入课堂后调用有效  	|
| setTimePeriod                   | 设置白板数据上抛间隔（默认为200ms）		|

**白板操作接口：**

| 接口                                 | 说明                                       |
| ---------------------------------- | ---------------------------------------- |
| revoke                   | 撤回本人最新的一次绘制操作  	|
| redo                   | 取消撤回操作  					|
| clear                   | 清除当前白板内容，并同步到各端  					|
| clearDraws                   | 清空当前白板所绘制的涂鸦涂鸦，并同步到各端。 					|
| clearFileDraws                   | 清空指定文件涂鸦  					|
| setPaintColor                   | 设置画笔颜色（默认为蓝色）  					|
| setPaintType                   | 设置绘制类型  					|
| setPaintSize                   | 设置画笔宽度（默认为5） 					|
| setCornerRadius                   | 设置矩形的圆角半径  					|
| setFillStyle                   | 设置封闭图形，如矩形或者圆形的填充样式，白板目前支持 Style.FILL 和 Style.STROKE 两种模式  					|

**背景接口：**

| 接口                                 | 说明                                       |
| ---------------------------------- | ---------------------------------------- |
| setBoardBackGround                   | 设置白板背景图  	|
| updateCurrentFillMode                   | 更新当前背景图对齐模式  	|
| setBackgroundColor                   | 设置白板背景颜色（默认为白色），当前白板生效  	|
| setGlobalBackgroundColor                   | 设置全部白板背景色，已设置背景色或者新创建背景色均生效  	|


**文档接口：**

| 接口                                 | 说明                                       |
| ---------------------------------- | ---------------------------------------- |
| addFile                   | 添加文件，如 ppt、pdf 等格式文档  	|
| deleteFile                   | 设删除文档  	|
| switchFile                   |  切换文档  	|
| nextPage                   | 下一页 	|
| prePage                   | 上一页  	|
| getAllFileInfo                   | 获取所有文档信息（包括普通白板） 	|


#### 多终端交互
| 接口        | 说明                           |
| --------- | ---------------------------- |
| onReceive | 各端白板操作数据由此接口填入，白板内部会处理并展示出来 |


##  白板数据实时收发

不同端白板间的数据传输是建立在腾讯`IMSDK`建立的即时信道上的，该功能已经封装在 TICSDK 内部，开发者无需自行实现。

##  白板数据上报备份和拉取填充

课堂中，老师对白板的操作，涂鸦、图片、PPT、撤销、清空等操作需要上报到后台，并进行存储，这样后面中途加入课堂的成员就能拉取之前的白板数据进行展示。

该过程主要分为两步，数据上报和数据拉取：

1. 白板数据上报：
在每次对白板操作后，SDK 会将操作的数据上报到白板后台，目前 SDK 内部已经实现了该功能，白板后台服务也是由腾讯云维护，开发者无需自行实现。

2. 白板数据拉取（同步）：
每次进入课堂时，TICSDK 会拉取该课堂的所有历史白板消息，展示在白板上，该功能也已经在 TICSDK 内部实现，开发者无需自行实现。
