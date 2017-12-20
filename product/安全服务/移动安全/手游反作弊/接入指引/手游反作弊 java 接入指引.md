### 1. 准备工作
接入安全SDK，开发者需要完成以下步骤： 
```
1. 根据游戏运行平台和支持的CPU架构将SDK动态库拷贝到指定工程目录
2. 根据游戏id和用户登录信息调用SDK接口函数
3. 验证SDK接入是否正确
```
安全SDK在开发语言为C/C++的Android系统下接入需要的相关文件有以下:
```
tp2.jar
libtersafe2.so
```
需要申请的权限
```
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.GET_TASKS" />
<uses-permission android:name="android.permission.INTERNET" />
```
SDK接口函数：
```
初始化接口 initEx
用户登录接口 onUserLogin
前台切换到后台接口 onAppPause
后台切换到前台接口 onAppResume
```

### 2. 添加SDK文件到工程
#### 2.1 添加文件
（1）将sdk/android/c目录下的tp2.jar文件拷贝到android工程目录的libs目录下;
（2）将sdk/android/java/lib目录下以CPU架构命名的文件夹(包含libtersafe2.so文件)拷贝到android工程目录的libs目录下,对不支持的CPU架构体系不需要拷贝.
![](https://mc.qcloudimg.com/static/img/eab83b3ae6d2a13b8f6a8479137a5e07/image.png)

#### 2.2 工程属性设置
在Eclipse中左边的项目导航栏[Project Explorer]中选择游戏项目，点击鼠标右键，在弹出的菜单中选择[Properties]，选中Properties窗口左边导航栏中的[Java Build Path]选项，然后在[Library]中点击[add JARs]添加tp2.jar
![](https://mc.qcloudimg.com/static/img/2b038746f019e439ef5bbdb473ab16b2/image.png)
 选择已拷贝到工程目录的tp2.jar
 ![](https://mc.qcloudimg.com/static/img/b48aeb6b30b9c689ca5e56357a0c72b3/image.png)
 添加tp2.jar后在[Order and Export]中选中tp2.jar
 ![](https://mc.qcloudimg.com/static/img/e19cbe55f0997e7bdb68eeef275a1fb4/image.png)
clean工程并重新编译

### 3. SDK接口调用
导入包
```
import com.tencent.tersafe2.TP2Sdk;
```

#### 3.1 初始化函数
**函数原型**
```
public static int initEx(int gameId, String appKey);
```

**参数说明**

| 参数 | 是否必须 | 说明 |
|---------|---------|---------|
| gameId | 是 | 由腾讯云官网分配的game_id  |
| appKey | 是 | 由腾讯云官网分配game_key，与game_id对应  |
gameId和appKey在腾讯云官网（xxxxxxxxxxxx）注册完新游戏后自动生成
**返回值**：0表示调用成功

#### 3.2 用户登录接口
**函数原型**
```
public static native int onUserLogin(int accountType, int worldId, String openId, String roleId);
```

**参数说明**

| 参数 | 标题2 |
|---------|---------|
| account_type | 与运营平台相关的帐号类型，参考下文的TssSdkEntryId填写 | 
| worldId | 用户游戏角色的大区信息 | 
| openId | 用户唯一身份标识，可自定义字符串。（和处罚相关必须填写） | 
| roleId | 区分用户创建的不同角色的标识 | 
account_type默认QQ平台填1，微信平台填2，其他平台填99。国内外主流帐号登录平台可参考以下数值填写。
```
enum TssSdkEntryId
{
ENTRY_ID_QZONE = 1, // QQ
ENTRY_ID_MM = 2, // 微信
ENTRT_ID_FACEBOOK = 3, // facebook
ENTRY_ID_TWITTER = 4, // twitter
ENTRY_ID_LINE = 5, // line
ENTRY_ID_WHATSAPP = 6, // whatsapp
ENTRY_ID_OTHERS = 99, // 其他平台
};
```
world_id由游戏自定义，如果游戏没有分区可填0。
role_id用于区分同一帐号同一分区下的不同角色，如果没有角色区分可填””。
open_id由所在运营平台分配，用于唯一区分用户。
**返回值**：0表示调用成功

#### 3.3 前台切换到后台接口
**函数原型**
```
int onAppPause ();
```
程序由前台切换到后台，表明游戏当前为非活动状态。
**返回值**：0表示调用成功

#### 3.4 后台切换到前台接口
**函数原型**
程序由后台切换到前台，表明游戏当前为活动状态。
**返回值**：0表示调用成功

#### 3.5 调用时机
（1）TP2Sdk.initEx在游戏启动的第一时间调用，参数为游戏id和appKey信息。更早时机调用安全接口函数可以更安全的保护游戏进程。
（2）TP2Sdk.onUserLogin在游戏获取到用户授权的登录信息后调用，如果游戏有设置大区id和角色id，则在获取大区id和角色id之后再调用TP2Sdk.onUserLogin函数。在游戏过程中，如果出现断线重连，用户注销重新登录等需要重新获取用户登录信息的情况，也需要再次调用该函数。传递的参数为用户的帐号信息，可自定义。
（3）TP2Sdk.onAppPause在游戏从前台切换到后台时调用。 
（4）TP2Sdk.onAppResume在游戏从后台切换到前台时调用。 

#### 3.6 示例代码
```
public void onCreate()
 { 
//游戏启动的第一时间调用 
TP2Sdk. initEx(9000, “d5ab8dc7ef67ca92e41d730982c5c602”); 
int accountType = ENTRYID.ENTRY_ID_QZONE; /*帐号类型*/ 
int worldId = 1; /*大区id*/ 
String openId = "B73B36366565F9E02C752"; /*与平台相关的用户标识*/ 
String roleId = "paladin"; /*角色id*/ 
//用户登录游戏时调用 
TP2Sdk.onUserLogin(accountType, worldId, openId, roleId); 
} 
// 游戏切换到后台 
public void onPause()
 { 
super.onResume(); 
TP2Sdk.onPause(); 
} 
// 游戏切换到前台 
public void onResume() 
{ 
super.onResume(); 
TP2Sdk.onResume(); 
}
```

### 4. 验证SDK接入是否正确
1.将安卓手机通过usb数据线连接windows电脑。连接成功后，使用windows的命令行工具，登录到android adb控制台，如图：
![](https://mc.qcloudimg.com/static/img/091f2d44b4862e843748fdd9655e9914/image.png)
2.敲入cd /sdcard回车，再敲入mkdir sdk回车，用于创建/sdcard/sdk目录。其中，如果目录已经存在，则系统会提示mkdir failed for /sdcard/sdk，File exists，继续下一步：
![](https://mc.qcloudimg.com/static/img/748c74c2ef3f5bec2a650f3d8eb0bdc6/image.png)
3.cd /sdcard/sdk进入目录，echo>enable.log创建enable.log空文件 ：
![](https://mc.qcloudimg.com/static/img/26aa6733a77a4c2625d131cddba47b89/image.png)
有的机型可能无法访问shell创建的目录下的文件，这种情况请切换为root用户更改/sdcard/sdk目录权限或更换手机
![](https://mc.qcloudimg.com/static/img/91cd8bb85e88eede943d47570a792c35/image.png)
4.运行游戏并登录用户，查看/data/data/log目录会生成日志文件tp2.log和tlog.log，如图：
![](https://mc.qcloudimg.com/static/img/3ce91cbdb15cdb72998fbfcc2bdf074e/image.png)
如果没有生成日志，请检查/sdcard/sdk和enable.log是否有读写权限。少部分机型无法读写这个目录，可更换机型测试或将/sdcard/sdk改为/data/data/log(需要root)。<br><font color=red>注：enable.log只用于测试使用。</font color=red>
5.打开tp2.log文件，检查日志中是否包含三个接口（native）信息**tp2_sdk_init_ex，tp2_setuserinfo，setgamestatus**以及jar包版本号**jar_ver**。以上条件必须都满足才能正确运行安全SDK。setgamestatus:1表示当前进程运行在前台，setgamestatus:2表示当前进程运行在后台。 
请测试app切换前后台，查看接口调用是否正确。除了接口调用，还要检查用户信息(userinfo)是否填写正确。 
![](https://mc.qcloudimg.com/static/img/75eef4a35cf89e8e1d02be304403377b/image.png)
6.打开tlog.log可查看安全SDK发送的数据，如图
![](https://mc.qcloudimg.com/static/img/50526870e79bb4d21d5b5bb0c333f86f/image.png)
安全SDK除了在初始化时会上报一些进程基本信息，还会根据定期的安全扫描结果来发送数据，例如扫描到app证书签名不正确，内存被修改，外挂进程正在运行等信息。tlog.log记录SDK发送的数据（只在测试时生成），一般1小时的数据是20K左右，可以查看tlog.log的大小来统计安全SDK发送的数据量。