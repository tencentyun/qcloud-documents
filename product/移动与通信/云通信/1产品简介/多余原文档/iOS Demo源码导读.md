# TIMChat源码导读
## 目的
本文档描述了ImSDK的Demo的架构、以及核心流程，并作为其他开发者了解 ImSDK功能以及集成ImSDK指导说明。

## 架构设计及说明
App基于系统（OS System Service），自底向上再分作三层：
1.App Core Service：App核心服务层，对外提供核心功能（如IMSDK）等；
2.App Adapter：业务逻辑适配层，App根据自身的业务不同，将App Core Service提供的核心功能进行封装，以供外部使用；
3.UI层:
App UI ：各功能模块对就看整屏界面，主要负责界面内部Custom UI的布局与调度；
Custom UI : 自定义UI层，主要作用是把界面上的大模块拆分到小的自定义的小模块（Custom View）中进行实现，实际开发中隶属于AppUI，可在各App　UI模块中进行复用的部分；
Common Library：公用代码库，主要基础工具类，第三方代码等，用作代码搜集以及后期复用；
App分层通信模型如下：
各箭头含义:
Call：调用  CallBack：回调  Broadcast：广播  Support：支撑/支持
<img src="//mccdn.qcloud.com/static/img/90c3bacc07baad640bcc38958b9e1043/image.png" width=640 />

## 架构内各层通信规则说明
1. App Adapter层之间的各模块允许相互访问:
<img src="//mccdn.qcloud.com/static/img/d9542fee67988a5a3781725abcd683d8/image.png" width=640 />
2. App UI层各模块不允许直接访问，可通过Adapter层间接访问:
<img src="//mccdn.qcloud.com/static/img/54763231d03bda1dfb302841cffaf0b5/image.png" width=640 />
3. App Core Service层各模块不允许直接访问，虽通过Apdater层间接访问:
<img src="//mccdn.qcloud.com/static/img/b0e04d3ea2833092b95de66344682cb9/image.png" width=640 />

## TIMChat工程与架构图的对应关系
<img src="//mccdn.qcloud.com/static/img/9506396b4c1b2fea7116dc34d0facb53/image.png" width=640 />

## TIMChat工程目录与架构图的对应关系
<img src="//mccdn.qcloud.com/static/img/e24f0bb4ca418386b899e2dc6dec0eb8/image.jpg" />

| 目录名 | 	功能说明 | 对应架构图名称 |
|---------|---------|---------|
| SystemLibrary | 工程依赖的系统库 | 无 |
| CommonLibrary | 公用代码库 | CommonLibrary |
| TIMAdapter | IMSDK业务逻辑适配，不建议直接使用SDK，而是在SDK再封装一层，具体如何封装依赖于App具体逻辑 | AppAdapter |
| CustomUI | 界面中通用的自定义UI | CustomViews |
| AppUI | App界面 | AppUI |

## CommonLibrary介绍
CommonLibrary中主要是整理了一些常用工具类，以及常用的界面布局框架。另外考虑到有些代码与用户现有的代码冲突，用户可根据自身需要，通过控制宏来决定要导入的内容（TIMChat工程中目前只加载了其中部分，具体操作后面CommonLibrary集成说明中介绍）。
CommonLibrary中包含了一般App开发中常用的功能，较简单的界面布局框架，以及一些通用的界面基类，用户可快速地集成并通过继承来实现开发与自定义
<img src="//mccdn.qcloud.com/static/img/0657b5d778a896cf7ec79a074cd0c2ec/image.jpg" />

## TIMAdapter设计说明
TIMAdapter是腾讯云IMSDK Demo中对IMSDK的一层再封装，其覆盖基本的联系人以及聊天功能，为方便用户进行复用以及扩展各自App的业务逻辑，此处只说明设计思路，用户也可以参照此处的做法，进行自定义扩展。
实际开发过程中，用户App的逻辑与Demo逻辑可能不一致，建议用户通过继承重写某些类与自身逻辑不一致的方法，以及来增加新方法来扩展自身逻辑，这样Demo更新的时候，如果TIMAdapter有更新，再用工具对比TIMAdapter的即可。
复用TIMAdapter的好处在于：
- 可扩展：可以横向进行扩展，不影响现有功能；
- 可定制:  用户可以通过索引头文件，以及编译宏等方式来控件需要导入的代码，来实现用户自定义的需求；
- 稳定性上有保证：Demo中会持续修复其中的问题，之后的版本也会慢慢提升性能方面，一些基本用例也会有覆盖；

TIMAdapter物理目录以及对应的功能介绍（以下说明中的物理目录结构对应IMSDK 1.9.2版本之后，请阅读者注意，1.9.2之前的版本基本思路相同）
<img src="//mccdn.qcloud.com/static/img/f6a9e666d648743117b830542ecef20c/image.jpg" width=640 />


| 目录或文件 | 说明 | 注意事项 |
|---------|---------|---------|
| Framework | TIMAdapter所依赖的IMSDK，TLSSDK | 目录中有readme，里面的导入介绍 |
| TIMAdapter.h | TIMAdapter中的参数配置，以及目录索引	 | 为方便用户集成，工程内部会把TIMAdapter中的文件中pch中全部导入，这样会影响编译效率 |
| IMAAppDelegate | IMSDK通常在AppDelegate中的配置 | 使用时，用户可自已App里面的AppDelegate直接继承该类，或仿照该类实现 |
| Localizable.strings | IMSDK没玩内部错码描述	 |    |
| IMAUI | Demo中使用的登录界面逻辑 |    |
| Platform | TIMChat适配IMSDK核心逻辑层，提供登录，IMSDK回调处理，联系人，会话，关系链等的入口 | 复用时，用户可选择性的挑选必要的文件，不过这样会带来额外的编译工作量  |
| TIMModel | 对IMSDK基本数据类型(用户，会话，消息等)的封装，方便用户使用 |   |
| TIMShow | 界面上用于展示的相关的方法 | 1.9.2版本对该文件夹作拆分  |

TIMAdapter中较复杂的部分主要是：TIMModel ，TIMShow，IMAPlatform，其分别对应MVC中的M, V,C，下面重点介绍这三个模块

#### 其中TIMModel对应目录结构如下：
<img src="//mccdn.qcloud.com/static/img/3f696242d73126493ee8defb5f200571/image.jpg" />


| 目录或文件 | 说明 |
|---------|---------|
| User | 将SDK声明的用户相关的对象（TIMUserProfile，TIMGroupInfo,TIMGroupMember等）全部转换成IMAUser类型，方便UI层使用  |
| Group | 将当前用户对于群的基本操作进行封装，User的子集，此处单独提出来  |
| MSG | 将TIMMessage进行进行封装，简化UI层对于消息的使用  |
| Conversation | 封装后的TIMConversation，使用IMAMsg进行收发消息，单个会话的消息列表管理 |
<img src="//mccdn.qcloud.com/static/img/d16aa5575fb774c9647d84443664dfca/image.png" width=640 />


| 类名 | 含义 |
|---------|---------|
| IMAUser | 适配层中的用户类型基类，对应IM看人单个人，对应IMSDK TIMUserProfile  |
| IMAHost | 当前使用者，当前登录IMSDK的人  |
| IMAGroup | 群类型，对应IMSDK TIMGroupInfo  |
| IMAGroupMember | 群成员，对应IMSDK TIMGroupMember  |

这样对应的基本交互模型如下：
<img src="//mccdn.qcloud.com/static/img/36ff1c7963c3fbd2366b001cf420715f/image.png" width=640 />

#### 从上图可推出IMAPlatform主要职责如下：
- 如何通过IMAPlatform获取到会话的IMUser（即接收方），即联系人管理功能
- 如何通过IMAPlatform管理与消息接收方的会话，即会管理管理功能
- 以及当前用户的的状态维护，IMAHost的管理

TIMAdapter中的控制层IMAPlatform对应的代码如下：
<img src="//mccdn.qcloud.com/static/img/e3886e1dc1f6c861b5288b74e648c7bf/image.jpg" width=640 />
<img src="//mccdn.qcloud.com/static/img/cd6aa686b97984bbeb98a7a6832e7937/image.png" width=640 />

| 类名 | 说明 |
|---------|---------|
| IMAPlatform | 对IMSDK核心IM流程进行再封装 |
| IMAPlatform+AppConfig | 主要是AppDelegate中需要配置 
| IMAPlatform+Login | 登录相关 |
| IMAPlatform+IMSDKCallBack | IMSDK回调处理 |
| IMAPlatform+FriendShip | 搜索好友相关 |
| IMAPlatform+Friend | 好友相关 |
| IMAContactManager | 联系人管理 |
| IMAContactManager+SubGroup | 分组管理相关 |
| IMAContactManager+Group | 群管理相关 |
| IMAConversationManager | 	会话管理 |

#### 数据层与控制层都有了，那么如何显示？
再来看TIMShow，TIMShow在架构对应图中属于AppAdapte UI Interface 这一层，因为与App UI 层依赖比较紧密，具体实现时无法做到不依赖界面，所以此处不详细介绍其内容，只提供一种方案来适配不同的App的UI层，以达到复用的效果

1. 先声明界面上与IMSDK相关的显示协议
<img src="//mccdn.qcloud.com/static/img/8e84cf0ddfed7ba652e4b1b151574f63/image.jpg" width=640 />
<img src="//mccdn.qcloud.com/static/img/998914e077a24f588c02b6fc32e38574/image.jpg" width=640 />
2. 对现有的IMAModel中的类添加类别，并在类别中实现对应的协议
<img src="//mccdn.qcloud.com/static/img/31b0aa51be1a01ad8636edffebd283e2/image.jpg" width=640 />
3. 也可以将IMSDK中的数据类型能过类别的方式进行扩展
<img src="//mccdn.qcloud.com/static/img/7d4ab2c5bf1e910ec4fdce6cf8e9bae2/image.jpg" width=640 />
4. 界面中使用时，使用声明的协议或基类来访问，而不是直接使用数据类型进行操作
<img src="//mccdn.qcloud.com/static/img/c4fe5595a0013770d353a4cf76fe87ed/image.jpg" width=640 />


## 用户集成说明
用户可按照以下步骤进行集成，注意在保证每步都Build成功的情况下再进行下一步，（因1.9.2版本为方便用户集成，将TCShow进行了拆分，下面的信成是按照1.9.2版本来处理）

1. 新建空工程TIMDemo，增加PCH文件，并删除默认生成的内容，设置Enable BitCode 为NO，设置Other Linker Flags 为 -ObjC
<img src="//mccdn.qcloud.com/static/img/0394770bdb5134c37d74b39621678849/image.jpg" width=640 />
<img src="//mccdn.qcloud.com/static/img/0e1351393d95431ec008df2a1f9f6b8b/image.jpg" width=640 />
<img src="//mccdn.qcloud.com/static/img/4e468229805249acab137cd907bcc040/image.jpg" width=640 />
注:在工程配置中配置pch路径，不然编译不过
<img src="//mccdn.qcloud.com/static/img/7d959474a19e01a8954b79d6934ab2f4/image.jpg" width=640 />
2. 导入CommonLibrary
<img src="//mccdn.qcloud.com/static/img/8ce9b0ac47dbb1e95da898308d20ee80/image.jpg" width=640 />
具体添加项，还要看CommonLibrary里面的各索引文件里面都有编译开关来控制要导入的文件，使用时请注意，如果CommonLibrar中有文件与现有代码冲突，可参考其他编译开关的做法进行配置
<img src="//mccdn.qcloud.com/static/img/a22d92d8654d8fa721a294cae8488a4b/image.jpg" width=640 />
此时用户若只想用CommonLibrary进行App开发，还需要配置AppDelegate，
修改前：
<img src="//mccdn.qcloud.com/static/img/c5437b0c3ecadb4ad3f1bef07c5d272c/image.jpg" width=640 />
修改后：
<img src="//mccdn.qcloud.com/static/img/89b8c41bf56ff59345b4126ac4066922/image.jpg" width=640 />


3. 导入TIMAdapter，加入依赖库，并在PCH文件中导入TIMAdapter.h
<img src="//mccdn.qcloud.com/static/img/615986ed4f6b80da2d102e555118c34a/image.jpg" width=640 />
<img src="//mccdn.qcloud.com/static/img/e5c3ac5f71f1112b95230a57284e19f4/image.jpg" width=640 />


4. 配置AppDelegate 进入登录界面
<img src="//mccdn.qcloud.com/static/img/09f5398e2bf19bc4deb90a7b1d7c443e/image.jpg" width=640 />

配置完成后即可使用TIMAdapter的封装后的功能。











	
	
	
	








