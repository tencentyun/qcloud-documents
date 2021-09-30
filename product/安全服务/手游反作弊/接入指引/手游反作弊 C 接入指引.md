##  准备工作
- 接入安全 SDK，开发者需要完成以下步骤：
 1. 根据游戏运行平台和支持的 CPU 架构将 SDK 动态库拷贝到指定工程目录。
 2. 根据用户登录信息调用 SDK 接口函数。
 3. 验证 SDK 接入是否正确。

- 安全 SDK 在开发语言为 C/C++ 的 Android 系统下接入需要的相关文件有以下:
```
tp2.jar
tp2_sdk.h
tss_sdt.h,tss_sdt_ex.h（安全数据类型选接，接入教程见《SDK 安全数据类型接入教程 C++》）
libtersafe2.so
```

- 需要申请的权限：
```
<uses-permission android:name="android.permission.ACCESS_WIFI_STATE"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
<uses-permission android:name="android.permission.GET_TASKS" />
<uses-permission android:name="android.permission.INTERNET" />
```

- SDK 接口函数：
```
初始化接口 tp2_sdk_init_ex
用户登录接口 tp2_setuserinfo
前后台切换接口 tp2_setgamestatus
```

## 添加 SDK 文件到工程
### 添加文件
1. 将 sdk/Android/c 目录下的 tp2.jar 文件拷贝到 Android 工程目录的 libs 目录下。
2. 将 sdk/Android/c 目录下 tp2_sdk.h 文件拷贝到 Android 工程目录的 jni 目录下。
3. 将 sdt/c++ 目录下的 tss_sdt.h 和 tss_sdt_ex.h 文件拷贝到 Android 工程目录的 jni 目录下（选接，接入教程见《C++ 安全数据类型接入教程. doc》）。
4. 将 sdk/Android/c/lib 目录下以 CPU 架构命名的文件夹 (包含 libtersafe2.so 文件) 拷贝到 Android 工程目录的 jni / 对应存 so 文件的目录，如 jni/armeabi、jni/x86 等, 对不支持的 CPU 架构体系不需要拷贝。
 ![](https://mc.qcloudimg.com/static/img/5c0861221c69ff2a296717b48223b614/image.png)

### 工程属性设置
1. 在 Eclipse 中左侧的项目导航栏 [Project Explorer] 中选择游戏项目，单击鼠标右键，在弹出的菜单中选择 [Properties]，选中 Properties 窗口左边导航栏中的[Java Build Path] 选项，然后在 [Library] 中单击 [add JARs] 添加 tp2.jar。
![](https://mc.qcloudimg.com/static/img/2b038746f019e439ef5bbdb473ab16b2/image.png)
2. 选择已拷贝到工程目录的 tp2.jar。
![](https://mc.qcloudimg.com/static/img/b48aeb6b30b9c689ca5e56357a0c72b3/image.png)
3. 添加 tp2.jar 后在 [Order and Export] 中选中 tp2.jar
![](https://mc.qcloudimg.com/static/img/e19cbe55f0997e7bdb68eeef275a1fb4/image.png)
4. 再在 Android 工程加载游戏 so 的地方，添加对 libtersafe2.so 的引用。
>!libtersafe2.so 的加载顺序，需要在游戏自己的 so 之前。

### 修改 Android.mk
1. 在 jin/Android.mk 中添加如下代码, 用于加载 libtersafe2.so。
```
include $(CLEAR_VARS)
LOCAL_MODULE:=libtp2
LOCAL_SRC_FILES:=$(TARGET_ARCH_ABI)/libtersafe2.so
include $(PREBUILT_SHARED_LIBRARY)
```
2. 在 jni/Android.mk 中，游戏所在 so 节，添加如下代码，用于指示对 libtp2 的引用。
```
LOCAL_SHARED_LIBRARIES:=libtp2
```

## SDK 接口调用
```
#include “tp2_sdk.h”；//所需头文件
int tp2_sdk_init_ex(int game_id  const char* app_key);// 初始化接口 函数原型
```

### 参数说明

| 参数 | 是否必须 | 说明 |
|---------|---------|---------|
| game_id | 是 | 由腾讯云官网分配的 game_id  |
| app_key | 是 | 由腾讯云官网分配 game_key，与 game_id 对应  |

- gameId 和 AppKey 在腾讯云官网（xxxxxxxxxxxx）注册完新游戏后自动生成。
- **返回值**：0 表示调用成功

### 用户登录接口
**函数原型**
```
int tp2_setuserinfo(int account_type, int world_id, string open_id, string role_id);
```

**参数说明**

| 参数 | 说明 |
|---------|---------|
| account_type | 与运营平台相关的帐号类型，参考下文的 TssSdkEntryId 填写 |
| world_id | 用户游戏角色的大区信息 |
| open_id | 用户唯一身份标识，可自定义字符串。（和处罚相关必须填写） |
| role_id | 区分用户创建的不同角色的标识 |

account_type 默认 QQ 平台填 1，微信平台填 2，其他平台填 99。国内外主流帐号登录平台可参考以下数值填写。
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
- world_id 由游戏自定义，如果游戏没有分区可填 0。
- role_id 用于区分同一帐号同一分区下的不同角色，如果没有角色区分可填""（空）。
- open_id 由所在运营平台分配，用于唯一区分用户。
- **返回值**：0 表示调用成功。

### 前后台切换接口
**函数原型**
```
int tp2_setgamestatus (int status);
```

| 参数 | 说明 |
|---------|---------|
| status | 前台 TP2_GAME_STATUS_FRONTEND<br> 后台 TP2_GAME_STATUS_BACKEND |

**枚举类型**
```
enum TP2GameStatus
{
TP2_GAME_STATUS_FRONTEND = 1, // 前台
TP2_GAME_STATUS_BACKEND = 2 // 后台
}
```

- **返回值**：0 表示调用成功

### 调用时机
1. tp2_sdk_init_ex 在游戏启动的第一时间调用，参数为游戏 ID 和 App_key 信息。更早时机调用安全接口函数可以更安全的保护游戏进程。
2. tp2_setuserinfo 在游戏获取到用户授权的登录信息后调用，如果游戏有设置大区 ID 和角色 ID，则在获取大区 ID 和角色 ID 之后再调用 tp2_setuserinfo 函数。在游戏过程中，如果出现断线重连，用户注销重新登录等需要重新获取用户登录信息的情况，也需要再次调用该函数。传递的参数为用户的帐号信息，可自定义。
3. tp2_setgamestatus 在游戏切换前后台调用。当游戏从后台切换到前台运行时调用 Tp2SetGamestatus 接口，设置参数为 Tp2Status. FRONTEND。当游戏切从前台切换到后台时传递参数为 Tp2Status. BACKEND。SDK 部分功能在切换到后台时停止运行，因此该接口将影响 SDK 功能是否正常。

### 示例代码
```
void Start ()
{
// 游戏启动的第一时间调用
tp2_sdk_init_ex (8888, “a5ab8dc7ef67ca92e41d730982******”);
// 用户登录时调用
int account_type = ENTRY_ID_QZONE; /* 帐号类型 */
int world_id = 101; /* 大区 id*/
string open_id = "B73B36366565F9E******"; /* 与平台相关的用户标识 */
string role_id = "paladin"; /* 角色 id*/
tp2_setuserinfo(account_type, world_id, open_id, role_id);
}

// 游戏切换到前台
void onResume ()
{
tp2_setgamestatus(TP2_GAME_STATUS_FRONTEND);
}

// 游戏切换到后台
void onPause ()
{
tp2_setgamestatus(TP2_GAME_STATUS_BACKEND);
}
```

## 验证 SDK 接入是否正确
1. 将 Android 手机通过 usb 数据线连接 Windows 电脑。连接成功后，使用 Windows 的命令行工具，登录到 Android adb 控制台，如图：
 ![](https://mc.qcloudimg.com/static/img/091f2d44b4862e843748fdd9655e9914/image.png)
2. 敲入 cd /sdcard 回车，再敲入 mkdir sdk 回车，用于创建 / sdcard/sdk 目录。其中，如果目录已经存在，则系统会提示 mkdir failed for /sdcard/sdk，File exists，继续下一步。：
 ![](https://mc.qcloudimg.com/static/img/748c74c2ef3f5bec2a650f3d8eb0bdc6/image.png)
3. cd /sdcard/sdk 进入目录，echo>enable.log 创建 enable.log 空文件 ：
 ![](https://mc.qcloudimg.com/static/img/26aa6733a77a4c2625d131cddba47b89/image.png)
有的机型可能无法访问 shell 创建的目录下的文件，这种情况请切换为 root 用户更改 / sdcard/sdk 目录权限或更换手机
 ![](https://mc.qcloudimg.com/static/img/91cd8bb85e88eede943d47570a792c35/image.png)
4. 运行游戏并登录用户，查看 / data/data/log 目录会生成日志文件 tp2.log 和 tlog.log，如图：
 ![](https://mc.qcloudimg.com/static/img/3ce91cbdb15cdb72998fbfcc2bdf074e/image.png)
如果没有生成日志，请检查 / sdcard/sdk 和 enable.log 是否有读写权限。少部分机型无法读写这个目录，可更换机型测试或将 / sdcard/sdk 改为 / data/data/log（需要 root）。
>**注意：**enable.log 只用于测试使用。
5. 打开 tp2.log 文件，检查日志中是否包含三个接口（native）信息 **tp2_sdk_init_ex，tp2_setuserinfo，setgamestatus** 以及 jar 包版本号 **jar_ver**。以上条件必须都满足才能正确运行安全 SDK。setgamestatus:1 表示当前进程运行在前台，setgamestatus:2 表示当前进程运行在后台。
请测试 App 切换前后台，查看接口调用是否正确。除了接口调用，还要检查用户信息 (userinfo) 是否填写正确。
 ![](https://mc.qcloudimg.com/static/img/75eef4a35cf89e8e1d02be304403377b/image.png)
6. 打开 tlog.log 可查看安全 SDK 发送的数据，如图
 ![](https://mc.qcloudimg.com/static/img/50526870e79bb4d21d5b5bb0c333f86f/image.png)
安全 SDK 除了在初始化时会上报一些进程基本信息，还会根据定期的安全扫描结果来发送数据，例如扫描到 App 证书签名不正确，内存被修改，外挂进程正在运行等信息。tlog.log 记录 SDK 发送的数据（只在测试时生成），一般 1 小时的数据是 20K 左右，可以查看``tlog.log``的大小来统计安全 SDK 发送的数据量。
