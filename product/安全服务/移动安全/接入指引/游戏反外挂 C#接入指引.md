### 1. 准备工作
接入安全SDK，开发者需要完成以下步骤： 
```
1. 根据游戏运行平台和支持的CPU架构将SDK动态库拷贝到指定工程目录
2. 根据游戏id和用户登录信息调用SDK接口函数
3. 验证SDK接入是否正确
```
安全SDK在开发语言为C/C++的Android系统下接入需要的相关文件有以下:
```
tp2.cs
tp2.jar (Android)
libtersafe2.so (Android)
```
需要申请的权限:
```
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.GET_TASKS" />
<uses-permission android:name="android.permission.INTERNET" />
```
SDK接口函数：
```
初始化接口 Tp2SdkInitEx
用户登录接口 Tp2UserLogin
前后台切换接口 Tp2SetGamestatus
```

### 2. 添加SDK文件到工程
#### 2.1 添加文件
（1）将sdk\android\c#目录下的tp2.cs放在工程的Assets目录下
（2）将sdk\android\c#目录下的tp2.jar放在工程的Assets\Plugins\Android目录下
（3）多CPU：
以Unity5.0为例，如果游戏支持Android多cpu架构(目前只支持arm-v7a和x86)，将sdk\android\c#\lib目录下的armeabi和x86文件夹下的libtersafe2.so分别拷贝到以下目录:
```
Assets/Plugins/Android/libs/armeabi-v7a/
Assets/Plugins/Android/libs/x86/
```
（4）单CPU架构：
如果游戏只支持arm-v7，以Unity4.5为例，将SDK提供的tp2.jar和armeabi-v7a目录下的 libtersafe2.so两个文件放在/Assets/Plugins/Android/目录下即可

#### 2.2 工程属性设置
多cpu架构支持时选择[File] -> [Build settings] -> [Player Settings] -> [Other Settings] -> [Device Filter] -> [FAT(ARMv7+x86)]
![](https://mc.qcloudimg.com/static/img/c94b432701454a02efdc3a2110902fa6/image.png)

### 3. SDK接口调用
#### 3.1 初始化函数
**函数原型**
```
void Tp2SdkInitEx (int gameId, string appKey );
```
**参数说明**

| 参数 | 是否必须 | 说明 |
|---------|---------|---------|
| gameId | 是 | 由腾讯云官网分配的game_id  |
| appKey | 是 | 由腾讯云官网分配game_key，与game_id对应  |
gameId和appKey在腾讯云官网（xxxxxxxxxxxx）注册完新游戏后自动生成
**返回值**：0表示调用成功

#### 3.2 设置用户信息
**函数原型**
```
void Tp2UserLogin (int accountType, int worldId, String openId, String roleId);
```

**参数说明**

| 参数 | 标题2 |
|---------|---------|
| account_type | 与运营平台相关的帐号类型，参考下文的TssSdkEntryId填写 | 
| world_id | 用户游戏角色的大区信息 | 
| open_id | 用户唯一身份标识，可自定义字符串。（和处罚相关必须填写） | 
| role_id | 区分用户创建的不同角色的标识 | 
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

#### 3.3 设置游戏状态
**函数原型**
```
void Tp2SetGamestatus (Tp2Status status);
```
**参数说明**

| 参数 | 说明 |
|---------|---------|
| status | 前台 Tp2Status. FRONTEND<br>后台 Tp2Status. BACKEND | 

**枚举类型**
```
public enum Tp2Status
{
FRONTEND = 1, // 前台
BACKEND = 2 // 后台
}
```
**返回值**：0表示调用成功

#### 3.4 调用时机
（1）Tp2SdkInitEx在游戏启动的第一时间调用，参数为游戏id和appKey信息。更早时机调用安全接口函数可以更安全的保护游戏进程。
（2）Tp2UserLogin在游戏获取到用户授权的登录信息后调用，如果游戏有设置大区id和角色id，则在获取大区id和角色id之后再调用Tp2UserLogin函数。在游戏过程中，如果出现断线重连，用户注销重新登录等需要重新获取用户登录信息的情况，也需要再次调用该函数。传递的参数为用户的帐号信息，可自定义。
（3）Tp2SetGamestatus在游戏切换前后台调用。当游戏从后台切换到前台运行时调用Tp2SetGamestatus接口，设置参数为Tp2Status. FRONTEND。当游戏切从前台切换到后台时传递参数为Tp2Status. BACKEND。SDK部分功能在切换到后台时停止运行，因此该接口将影响SDK功能是否正常。

#### 3.5 示例代码
```
void Awake () 
{ 
Tp2Sdk.Tp2SdkInitEx(8888, "d5ab8dc7ef67ca92e41d730982c5c602"); 
} 
// 用户登录后调用 
void Start () 
{ 
int accountType = (int)Tp2Entry.ENTRY_ID_QZONE ; /*帐号类型*/ 
int worldId = 100; /*大区id*/ 
string openId = "B73B36366565F9E02C752"; /*用户id*/ 
string roleId = "paladin"; /*角色id*/ 
Tp2Sdk.Tp2UerLogin(accountType， worldId， openId， roleId); 
} 
// 游戏切换前后台调用 
void OnApplicationPause (bool pause)
 { 
if (pause)
 { 
Tp2Sdk.Tp2SetGamestatus(Tp2Status. BACKEND); // 切换到后台 
} 
else 
{ 
Tp2Sdk.Tp2SetGamestatus(Tp2Status. FRONTEND); // 切换回前台 
} 
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
如果没有生成日志，请检查/sdcard/sdk和enable.log是否有读写权限。少部分机型无法读写这个目录，可更换机型测试或将/sdcard/sdk改为/data/data/log(需要root)。
注：enable.log只用于测试使用。
5.打开tp2.log文件，检查日志中是否包含三个接口（native）信息**tp2_sdk_init_ex，tp2_setuserinfo，setgamestatus**以及jar包版本号**jar_ver**。以上条件必须都满足才能正确运行安全SDK。setgamestatus:1表示当前进程运行在前台，setgamestatus:2表示当前进程运行在后台。 
请测试app切换前后台，查看接口调用是否正确。除了接口调用，还要检查用户信息(userinfo)是否填写正确。 
![](https://mc.qcloudimg.com/static/img/75eef4a35cf89e8e1d02be304403377b/image.png)
6.打开tlog.log可查看安全SDK发送的数据，如图
![](https://mc.qcloudimg.com/static/img/50526870e79bb4d21d5b5bb0c333f86f/image.png)
安全SDK除了在初始化时会上报一些进程基本信息，还会根据定期的安全扫描结果来发送数据，例如扫描到app证书签名不正确，内存被修改，外挂进程正在运行等信息。tlog.log记录SDK发送的数据（只在测试时生成），一般1小时的数据是20K左右，可以查看tlog.log的大小来统计安全SDK发送的数据量。