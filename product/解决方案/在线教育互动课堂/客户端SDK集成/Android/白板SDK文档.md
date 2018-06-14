## 主要类简介

| 类                  | 说明                                       |
| ------------------ | ---------------------------------------- |
| WhiteboardSDK     |  白板 SDK 初始化类，App 启动时调用 init 方法进行初始化。 |
| WhiteboardView     | 继承 SurfaceView，独立主线程渲染。白板数据采集和展示网络白板数据控件。 |
| WhiteboardManager  | 白板主要业务逻辑管理类，提供了包括绘制参数设置、撤销、重做、擦除和选择等所有白板功能接口。 |
| WhiteboardEventListener | 白板事件回调接口，业务须实现所有接口。                               |
| WhiteboardConfig   | 白板绘制参数配置。                                |
| PaintType          | 绘制类型。详见代码注释说明。                           |
| FillMode           | 背景图的显示模式。详见代码注释说明。                       |
| BaseAction             | 白板绘制操作封装类抽象类。所有白板操作均继承该类。                     |
| WhiteboardEvent         | 白板对外的数据结构，由一系列的 Action 组成。                 |

**教育SDK里重要类**

| 类                | 说明                                     |
| ---------------- | ---------------------------------------- |
| ILVConfMgr       | 教育业务管理类。                              | 
| JsonProto        | 转换成协议数据格式，并通过数据链路外发。   |

## 白板使用方法
### WhiteboardView 使用方法
跟普通的自定义控制使用方法相同，在布局文件中可以直接使用、按需继承。
```
<com.tencent.boardsdk.board.WhiteboardView
	 android:id="@+id/cbv_board"
	 android:layout_width="match_parent"
	 android:layout_height="match_parent" />

```
> **注意：**
> 为了保证各端体验一致，白板视图的宽高比固定为 16：9。WhiteboardView 控件内部已做处理，开发者直接使用即可。

**主要方法说明**

| 接口                  | 说明          |
| ------------------- | ----------- |
| setWhiteboardEnable | 关启白板绘制。      |
| setDragEnable       | 关启白板缩放和拖拽功能。 |

### WhiteboardManager 使用方法

#### 初始化
从 WhiteboardManager 获取 WhiteboardConfig 实例（也可自己构建），设置相关参数后，通过 WhiteboardManager 的`init`方法进行初始化。

```
	WhiteboardConfig config = WhiteboardManager.getInstance().getConfig();
	config.setPaintSize(6).setPaintColor(Color.BLUE);
	WhiteboardManager.getInstance().init(getActivity().getBaseContext(), config);
```
#### 主要方法说明

| 接口                                 | 说明                                       |
| ---------------------------------- | ---------------------------------------- |
| init                               | 初始化白板绘制参数。                               |
| setBackgroundColor                 | 设置背景色。|
| setGlobalBackgroundColor				| 设置全部白板背景色，已设置背景色或者新创建背景色均生效。 |
| setPaintColor                      | 设置画笔颜色。                                   |
| setPaintType                       | 设置绘制类型。                                   |
| setPaintSize                       | 设置画笔笔画大小（默认是6）。                           |
| setCornerRadius                    | 设置矩形的圆角半径。                               |
| setFillStyle                       | 设置封闭形状如矩形，圆形的填充样式。仅支持 Paint.Style.FILL 和 Paint.Style.STROKE 两种，FILL为实心，STROKE 为空心。 |
| setDottedEnable                    | 开启虚线，默认实线。      |                         |
| setFillMode                        | 设置背景图显示模式。                               |
| getConfig                          | 获取白板绘制参数配置。                               |
| createSubBoard                     | 创建子白板。返回创建的白板 ID 标识。                       |
| switchBoardById                    | 切换白板。结果返回，0，表示切换成功（ID 如不存在，则新建）；-1，表示白板 ID 非法（空ID）。 |
| deleteBoardById                    | 删除白板，并切换至默认白板。结果返回，0，表示删除成功；-1，表示白板 id 非法（原因如：1.默认白板删除‘#DEFAULT’不允许删除；2.该白板不存在）。 |
| getCurrentWhiteboardId             | 获取当前白板 ID。默认的 ID 为 #DEFAULT。                 |
| getBoardList                       | 获取所有白板的 ID，返回白板列表。                         |
| revoke                             | 撤销绘制操作。                                   |
| redo                               | 重做。                                       |
| clear                              | 清空白板内容。                                   |
| setTimePeriod                      | 设置白板数据外发时间间隔（默认是 200ms）。             |
| registerBoardListChangedListener   | 注册白板列表变化监听，注意去注册操作，避免内存泄露。               |
| unregisterBoardListChangedListener | 去注册监听白板列表。                               |


设置背景色接口：

```java
    /**
     * 设置白板背景颜色(默认为白色)，当前白板生效
     *
     * @param backgroundColor 背景颜色，格式ARGB
     * @return
     */
    public void setBackgroundColor(int backgroundColor);

    /**
     * 设置全部白板背景色，已设置背景色或者新创建背景色均生效
     * @param backgroundColor 背景颜色，格式ARGB
     */
    public void setGlobalBackgroundColor(int backgroundColor);
```

设置背景图接口：

```java
	> WhiteboardManager.java
   /**
     * 设置白板背景，默认当前所在白板
     *
     * @param filePath  文件所在路径
     * @param bAutoFill 填充样式
     * @param callBack  结果回调
     */
    public void setBoardBackGround(final String filePath, final boolean bAutoFill, final IWbCallBack<String> callBack);

    /**
     * 设置指定白板的背景
     *
     * @param filePath  文件所在路径，文件为空时，清空白板背景
     * @param bAutoFill 填充样式
     * @param boardId   白板标识
     * @param callBack  结果回调, onSuccess回调中返回图片上传到服务后台存放的的url
     */
    public void setBoardBackGround(final String filePath, final boolean bAutoFill, final String boardId, final IWbCallBack<String> callBack);

```
#### 多终端交互
| 接口        | 说明                           |
| --------- | ---------------------------- |
| onReceive | 各端白板操作数据由此接口填入，白板内部会处理并展示出来。 |


##  白板数据实时收发

不同端白板间的数据传输是建立在腾讯`IMSDK`建立的即时信道上的，该功能已经封装在 TICSDK 内部，开发者无需自行实现。

##  白板数据上报备份和拉取填充

课堂中，老师对白板的操作，涂鸦、图片、PPT、撤销、清空等操作需要上报到后台，并进行存储，这样后面中途加入课堂的成员就能拉取之前的白板数据进行展示。

该过程主要分为两步，数据上报和数据拉取：

1. 白板数据上报：
在每次对白板操作后，SDK 会将操作的数据上报到白板后台，目前 SDK 内部已经实现了该功能，白板后台服务也是由我们维护，开发者无需自行实现。

2. 白板数据拉取（同步）：
每次进入课堂时，TICSDK 会拉取该课堂的所有历史白板消息，展示在白板上，该功能也已经在 TICSDK 内部实现，开发者无需自行实行。

