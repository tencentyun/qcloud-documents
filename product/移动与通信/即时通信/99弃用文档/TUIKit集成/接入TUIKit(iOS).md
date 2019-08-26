## 简介
#### 腾讯云 TUIKit

TUIKit 是基于腾讯云 IMSDK 的一款 UI 组件库，里面提供了一些通用的 UI 组件，您可通过该组件库选取自己所需要的组件快速的搭建一个 IM 应用。
IM 软件都具备一些通用的 UI 界面，如会话列表，聊天界面等。TUIKit 提供了这一类的组件，并提供了灵活的 UI 和交互扩展接口，方便您的用户做个性化开发。

#### IMSDK 与 TUIKit 的结合
腾讯云 IMSDK 提供了 IM 通信所需的各种基础能力，如通信网络，消息收发、存储等。 TUIKit 中的组件在实现 UI 功能的同时，调用 IMSDK 相应的接口实现了 IM 相关逻辑和数据的处理，因而您在使用 TUKit 时只需关注自身业务或做一些个性化的扩展即可。
下面我们将指导您如何快速的接入和使用 TUIKit。

## 帐号相关的基本概念

这里我们先来了解帐号相关的几个概念。

- **用户标识（userId）**：
userId（用户标识）用于在一个 IM 应用中唯一标识一个用户，即我们通常所说的帐号。这个一般由您自己的服务生成，即用户信息的生成（注册）需由您开发实现。

- **用户签名（userSig）**：
userSig（用户签名）是用于对一个用户进行鉴权认证，确认用户是否真实的。即用户在您的服务里注册一个帐号后，您的服务需要给该帐号配置一个 userSig，后续用户登录 IM 的时候需要带上 userSig 让 IM 服务器进行校验。用户签名生成方法可参考 [UserSig 后台 API](https://cloud.tencent.com/document/product/269/32688) 文档。

了解了前面的概念后，您可以通过下图了解集成了 IMSDK 应用的注册/登录流程。
![](https://main.qcloudimg.com/raw/00900a1542cef0820f3dac4cd89bfe23.jpg)
首先用户的终端需要向您的服务器注册帐号(userId)，您的服务器在进行注册业务处理时，按照用户签名文档中的方法生成一个该用户的 userSig，并返回给客户端。客户端再通过该 userId 和 userSig 到 IM SDK 进行登录操作。
为方便您接入开发测试，我们在腾讯云 IM 控制台提供了快速生成 userSig 的工具（在这之前您需要先在腾讯云创建自己的 IM 应用，可参考 [云通信 IM 入门](https://cloud.tencent.com/product/im/getting-started)）。登录控制台后，在顶部导航栏选择 >【云通信】>【应用列表】（选择您当前在使用的应用）>【应用配置】>【开发辅助工具】，参考 [UserSig 后台 API](https://cloud.tencent.com/document/product/269/32688#.E6.8E.A7.E5.88.B6.E5.8F.B0.E6.89.8B.E5.B7.A5.E7.94.9F.E6.88.90-usersig) 即可生成 userSig。

## TUIKit 工程集成
1. **安装 CocoaPods**
在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）：
```
sudo gem install cocoapods
```

2. **创建 Podfile 文件**
进入项目所在路径输入以下命令行，之后项目路径下会出现一个 Podfile 文件。
```
pod init
```

3. **编辑 Podfile 文件**
编辑 Podfile 文件，按如下方式设置：
```
platform :ios, '8.0'
source 'https://github.com/CocoaPods/Specs.git'
target 'App' do
# 这里不需要再 pod 'TXIMSDK_iOS' ，TXIMSDK_TUIKit_iOS 会自动依赖最新的 TXIMSDK 库
pod 'TXIMSDK_TUIKit_iOS'
end
```

4. **更新并安装 SDK**
在终端窗口中输入如下命令安装 TUIKit ：

```
pod install
```
或使用以下命令更新本地库版本：
```
pod update
```
pod 命令执行完后，会生成集成了 SDK 的 .xcworkspace 后缀的工程文件，双击打开即可。

## TUIkit API 调用
### 目录结构
![](https://main.qcloudimg.com/raw/6f5b7c7c8bc0d228840d4dd4da457387.png)

| 文件名 |主要用途|
|---|------|
|TUIKit|TUIKit 入口类，主要用于初始化，登录等|
|TUIKitConfig|TUIKit 资源配置类，主要用于加载资源图片，表情包等|
|Chat|聊天界面，主要用于发送和接收各种自定义消息|
|Commom|公共基类，主要用于管理公用的基础模块|
|Contact|通信录界面，目前主要用于管理好友关系链逻辑|
|Conversation|消息列表界面，主要用于管理消息的列表逻辑|
|Group|群组设置界面，主要用于设置群资料，加群，退群的逻辑|

### 初始化
通常情况下 TUIKit 的初始化非常简单，只需调用下面接口初始化默认配置即可。
```
NSInteger sdkAppid = 1400173143; //填入自己 App 的 SDKAppID
NSString *accountType = @"36862"; //填入自己 App 的 accountType
TUIKitConfig *config = [TUIKitConfig defaultConfig];//默认 TUIKit 配置，这个您可以根据自己的需求在 TUIKitConfig 里面自行配置
[[TUIKit sharedInstance] initKit:sdkAppid accountType:accountType withConfig:[TUIKitConfig defaultConfig]];
```
### 登录
在获取了用户的 identifier 和 userSig 后可以调用 TUIKit 接口直接登录。
```
NSString *identifier = @"user1" //填入登录用户名
NSString *userSig = @"";        //填入签名 userSig
[[TUIKit sharedInstance] loginKit:identifier userSig:userSig succ:^{
      //登录成功
} fail:^(int code, NSString *msg) {
      //登录失败   
}];
```
### UI 主界面
当您登录成功后，可以直接创建主界面管理类 TabBarController，在 TabBarController 添加会话列表类和信息设置类，在具体方式如下：
```
//1，创建 TabBarController
TTabBarController *tbc = [[TTabBarController alloc] init];
NSMutableArray *items = [NSMutableArray array];

//2，初始化会话列表类
TTabBarItem *msgItem = [[TTabBarItem alloc] init];
msgItem.title = @"消息";
msgItem.controller = [[TNavigationController alloc] initWithRootViewController:[[ConversationController alloc] init]];
[items addObject:msgItem];

//3，初始化通信录类
TTabBarItem *contactItem = [[TTabBarItem alloc] init];
contactItem.title = @"通讯录";
contactItem.controller = [[TNavigationController alloc] initWithRootViewController:[[ContactsController alloc] init]];
[items addObject:contactItem];
 
//4，初始化个人设置类
TTabBarItem *setItem = [[TTabBarItem alloc] init];
setItem.title = @"我";
setItem.controller = [[TNavigationController alloc] initWithRootViewController:[[SettingController alloc] init]];
[items addObject:setItem];
tbc.tabBarItems = items;

//跳转
[self presentViewController:tbc animated:YES completion:nil];
```

### 会话列表
一个聊天的发起可以理解成一个会话，IM SDK 中会话分为以下两种：
- **C2C 会话**：表示单聊情况下自己与对方建立的对话，读取消息和发送消息都是通过会话完成。
-  **群会话**：表示群聊情况下，群内成员组成的会话，群会话内发送消息群成员都可接收到。
![](https://main.qcloudimg.com/raw/46aa2633fbdee137fd7a838870309615.jpg)

您可以单击会话列表右上角的添加按钮，选择 "发起群聊" 或 "添加会话"，具体步骤如下：
**第一步**：进入会话列表类 ConversationController，创建并添加 TUIKit  的列表UI类 TConversationController，并且设置代理监听。
```
- (void)viewDidLoad {
    [super viewDidLoad];
		//初始化 TUIKit 的会话列表 UI 类
    TConversationController *conv = [[TConversationController alloc] init];
    conv.delegate = self;
    [self addChildViewController:conv];
    [self.view addSubview:conv.view];
}
```

**第2步**：选择 "发起群聊" 或 "添加会话" 会触发对应的逻辑回调，您可以在回调里面根据选择的内容跳转到对应的界面类。
```
- (void)popView:(TPopView *)popView didSelectRowAtIndex:(NSInteger)index
{
    UIViewController *add = nil;
    if(index == 0){
	//初始化发起群聊界面类
        add = [[AddGroupController alloc] init];
    }
    else if(index == 1){
	//初始化添加会话界面类
        add = [[AddC2CController alloc] init];
    }
	//跳转到对应的界面类
    UINavigationController *addNavi = [[UINavigationController alloc] initWithRootViewController:add];
    [self.navigationController presentViewController:addNavi animated:YES completion:nil];
}
```
**第3步**：如果选择发起群聊，会进入发起群聊类 AddGroupController ，在 AddGroupController 创建并添加 TUIKit 的发起群聊 UI 类 TAddGroupController ，并且设置代理监听。如果选择添加会话，会进入添加会话类 AddC2CController ，在 AddC2CController 创建并添加 TUIKit 的添加会话 UI 类 TAddC2CController ，并且设置代理监听。
```
//AddGroupController
- (void)viewDidLoad {
    [super viewDidLoad];
	//初始化 TUIKit 发起群聊类
    TAddGroupController *add = [[TAddGroupController alloc] init];
    add.delegate = self;
    [self addChildViewController:add];
    [self.view addSubview:add.view];
}

//AddC2CController
- (void)viewDidLoad {
    [super viewDidLoad];
	//初始化 TUIKit 添加会话类
    TAddC2CController *add = [[TAddC2CController alloc] init];
    add.delegate = self;
    [self addChildViewController:add];
    [self.view addSubview:add.view];
}
```

**第4步**：在发起群聊成功后，会收到 addGroupController 的回调，在回调里面可以获取群组的信息。在添加会话成功后，会收到 addC2CController 的回调，在回调里面可以获取会话信息。
```
//AddGroupController
- (void)addGroupController:(TAddGroupController *)controller didCreateGroupId:(NSString *)groupId groupName:(NSString *)groupName
{
    //获取群聊信息
    TConversationCellData *data = [[TConversationCellData alloc] init];
	//群聊 ID
    data.convId = groupId;
	//群聊类型
    data.convType = TConv_Type_Group;
	//群聊名字
    data.title = groupName;
}
//AddC2CController
- (void)addC2CController:(TAddC2CController *)controller didCreateChat:(NSString *)user
{
    TConversationCellData *data = [[TConversationCellData alloc] init];
	//会话 ID
    data.convId = user;
	//会话类型
    data.convType = TConv_Type_C2C;
	//会话 title
    data.title = user;
}
```

**第5步**：单击会话列表的某一个会话时，会收到以下回调，这时候创建会话界面类 ChatViewController ，透传 TConversationCellData （包含了消息的 Id，消息类型，消息内容等信息）。
```
- (void)conversationController:(TConversationController *)conversationController didSelectConversation:(TConversationCellData *)conversation
{
   //初始化会话界面
    ChatViewController *chat = [[ChatViewController alloc] init];
    chat.conversation = conversation;
    [self.navigationController pushViewController:chat animated:YES];
}
```

### 会话界面
#### 添加会话界面
进入上一步创建跳转的会话类 ChatViewController，创建并添加 TUIKit 的会话 UI 类 TChatController，并且设置代理监听。
```
- (void)viewDidLoad {
    [super viewDidLoad];
	//初始化 TUIKit 的会话UI类
    _chat = [[TChatController alloc] init];
    _chat.conversation = _conversation;
    _chat.delegate = self;
    [self addChildViewController:_chat];
    [self.view addSubview:_chat.view];
}
```

#### 收发消息
**第1步**：在会话界面，普通文本，表情的收发都会由 TChatController 直接接管，您不需要关注太多细节。相册、视频、文件的发送需要在收到 UI 触发事件（chatController：didSelectMoreAtIndex）后去对应的系统模块获取。
```
- (void)chatController:(TChatController *)chatController didSelectMoreAtIndex:(NSInteger)index
{
    if(index == 0 || index == 1 || index == 2){
        UIImagePickerController *picker = [[UIImagePickerController alloc] init];
        if(index == 0){
			//系统相册
            picker.sourceType = UIImagePickerControllerSourceTypePhotoLibrary;
            picker.mediaTypes = [UIImagePickerController availableMediaTypesForSourceType:UIImagePickerControllerSourceTypeCamera];
        }
        else if(index == 1){
			//系统拍照
            picker.sourceType = UIImagePickerControllerSourceTypeCamera;
            picker.cameraCaptureMode =UIImagePickerControllerCameraCaptureModePhoto;
        }
        else{
			//系统拍视频
            picker.sourceType = UIImagePickerControllerSourceTypeCamera;
            picker.mediaTypes = [UIImagePickerController availableMediaTypesForSourceType:UIImagePickerControllerSourceTypeCamera];
            picker.cameraCaptureMode =UIImagePickerControllerCameraCaptureModeVideo;
            picker.videoQuality =UIImagePickerControllerQualityTypeHigh;
        }
        picker.delegate = self;
        [self presentViewController:picker animated:YES completion:nil];
    }
    else{
		//系统文件
        UIDocumentPickerViewController *picker = [[UIDocumentPickerViewController alloc] initWithDocumentTypes:@[(NSString *)kUTTypeData] inMode:UIDocumentPickerModeOpen];
        picker.delegate = self;
        [self presentViewController:picker animated:YES completion:nil];
    }
}
```

**第2步**：在系统函数回调 imagePickerController 里面获取返回的图片和视频，调用 TChatController 的接口发送。
```
- (void)imagePickerController:(UIImagePickerController *)picker didFinishPickingMediaWithInfo:(NSDictionary<NSString *,id> *)info
{
    NSString *mediaType = [info objectForKey:UIImagePickerControllerMediaType];
		//图片
    if([mediaType isEqualToString:(NSString *)kUTTypeImage]){
		   //获取图片
        UIImage *image = [info objectForKey:UIImagePickerControllerOriginalImage];
       //发送图片
        [_chat sendImageMessage:image];
    }
	//视频
    else if([mediaType isEqualToString:(NSString *)kUTTypeMovie]){
		  //获取视频
        NSURL *url = [info objectForKey:UIImagePickerControllerMediaURL];
			//发送视频
        [_chat sendVideoMessage:url];
    }
}
```

**第3步**：在系统函数 documentPicker 回调里面获取系统返回的文件，调用 TChatController 接口发送。
```
- (void)documentPicker:(UIDocumentPickerViewController *)controller didPickDocumentAtURL:(NSURL *)url
{
   //获取文件 url 并发送
    [_chat sendFileMessage:url];
    [controller dismissViewControllerAnimated:YES completion:nil];
}
```

#### 图片、视频、文件消息查看
查看消息列表的图片、视频、文件消息需要先下载对应的消息内容，具体操作步骤如下：
**第1步**：在会话类 ChatViewController 监听代理 TChatControllerDelegate，在下面的回调跳转到对应的消息查看类。
```
- (void)chatController:(TChatController *)chatController didSelectMessages:(NSMutableArray *)msgs atIndex:(NSInteger)index
{
    TMessageCellData *data = msgs[index];
    if([data isKindOfClass:[TImageMessageCellData class]]){
		  //图片查看类
        ImageViewController *image = [[ImageViewController alloc] init];
        image.data = (TImageMessageCellData *)data;
        [self presentViewController:image animated:YES completion:nil];
    }
    else if([data isKindOfClass:[TVideoMessageCellData class]]){
		 //视频查看类
        VideoViewController *video = [[VideoViewController alloc] init];
        video.data = (TVideoMessageCellData *)data;
        [self presentViewController:video animated:YES completion:nil];
    }
    else if([data isKindOfClass:[TFileMessageCellData class]]){
		  //文件查看类
        FileViewController *file = [[FileViewController alloc] init];
        file.data = (TFileMessageCellData *)data;
        UINavigationController *nav = [[UINavigationController alloc] initWithRootViewController:file];
        [self.navigationController pushViewController:file animated:YES];
    }
}
```

**第2步**：跳转到图片、视频、文件查看类后，根据上一步获取的消息 data 信息调用 TUIKit 函数下载对应的图片、视频、文件数据。
```
 __weak typeof(self) ws = self;
//下载图片
[data downloadImage:type progress:^(NSInteger curSize, NSInteger totalSize) {
} response:^(int code, NSString *desc, NSString *path) {
   if(code == 0){
	   //下载成功，获取图片
       UIImage *image = [UIImage imageWithContentsOfFile:path];
    }
 }];
				
 //下载视频
 [data downloadVideo:^(NSInteger curSize, NSInteger totalSize) {
    //视频下载进度信息
    NSString *progress = [NSString stringWithFormat:@"%ld%%", curSize * 100 / totalSize];
 } response:^(int code, NSString *desc, NSString *path) {
    if(code == 0){
        //path 下载成功，获取视频地址
     }
 }];
 
//下载文件
[data downloadFile:^(NSInteger curSize, NSInteger totalSize) {
	//文件下载进度信息
    NSString *progress = [NSString stringWithFormat:@"%ld%%", curSize * 100 / totalSize];
 } response:^(int code, NSString *desc, NSString *path) {
    if(code == 0){
        //path 下载成功，获取文件地址
     }
 }];
```




