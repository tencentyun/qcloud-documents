腾讯云 XP2P 直播解决方案，可帮助用户直接使用经过大规模验证的直播流媒体分发服务。用户可通过 SDK 中简洁的接口快速同自有应用集成，实现 Windows 客户端的 P2P 直播功能。

## 支持的流媒体格式 

- RTMP
- HTTP-FLV

## 准备工作

- 在 [提交 X-P2P 开通申请](https://cloud.tencent.com/apply/p/npwwbfakdis) 后，再联系我们的研发工程师，确保 CDN 分发域名及 domain 白名单已完成配置。
- 确保您已在开发者中心上注册帐号并创建应用，创建应用时要写对包名。应用创建成功后获得一对有效的 `Access ID`、`Key`、`Secret`。
> ? 如果我们已向您提供，可忽略该步骤。

## 集成工作

1. 初始化日志（可选）：
``` C++
CVbyteP2P::EnableFileLog("./log", 10 * 1024 * 1024, 3);// 开启本地日志
```
或者开启 console 日志：
``` C++
CVbyteP2P::EnableDebug();
//CVbyteP2P::DisableDebug();
```
2. 首先加载 SDK 并指定一磁盘路径用于保存用户信息（需要校验返回值）。
``` C++
CVbyteP2P:: LoadAndInit ("D://");
```
3. 设置一些 SDK 的属性，如 package、version、appId 等：
``` C++
CVbyteP2P::SetPackage(package);
//CVbyteP2P::SetVersion(version);  // Deprecated，由p2p sdk指定
CVbyteP2P::SetAppId(appId);
CVbyteP2P::SetAppKey(appKey);
CVbyteP2P::SetSecretKey(secretKey);
```
4. 创建实例，注册两个事件回调函数，用来处理 SDK 抛出的事件和异常，`ErrorCallback` 和 `EventCallback` 是自定义的处理函数。
``` C++
int id = CVbyteP2P::CreateInstance(EventCallback, ErrorCallback, "No.1 player");
```

>? 至此，整个 SDK 加载初始工作已经完成。

使用 SDK 进行直播加速时，通过将直播流 URL 传给 SDK，SDK 会下载该直播流数据，并通过一个本地代理 URL（通常会 port 动态生成地址：`http://127.0.0.1:port/media.flv`）将数据提供给播放器播放，由事件处理函数获取对应 URL（ `CVbyteP2P::STARTED` 信号）。
``` C++
CVbyteP2P::PlayURL(id, url);
```
退出单个实例：
``` C++
CVbyteP2P::Unplay(id)
```
退出 P2P 服务，调用 unload 接口：
``` C++
CVbyteP2P::Unload();
```

>? 为避免 X-P2P 服务故障影响用户播放，在 SDK 播放失败后，播放器可直接播放 CDN URL 实现播放回退，即在 STARTED 事件中：
- 如果回调得到的 URL 是本地代理 URL，则说明 SDK 启动成功。
- 若回调得到的 URL 是原来传入的原始 URL，则说明 SDK 播放失败。
>
>无论是两者中哪种情况，将 URL 传递给播放器播放即可.

## 完整的调用代码

``` C++
#include <stdio.h>
#include <WinSock2.h>
#include "vbyte_p2p.h"
#include <windows.h>

#pragma comment(lib, "ws2_32.lib")
#pragma comment(lib, "qvbclient.lib")

int ErrorCallback(int error_id, const char *error_message, int id)
{
    printf("[ErrorCallback] id:%d, handle error_id: %d, message: %s\n", id, error_id, error_message);
    return 0;
}

int EventCallback(int event_id, const char *event_message, int id)
{
    printf("[EventCallback] id: %d, handle event_id: %d, message: %s\n", id, event_id, event_message);
    return 0;
}

int main()
{   
    WSADATA wsa;    
    if (WSAStartup(MAKEWORD(2, 0), &wsa) != 0) {
        printf("WSAStartup failed\n");
        return -1;
    }
    CVbyteP2P::EnableFileLog("./log", 10 * 1024 * 1024, 3);
    //CVbyteP2P::EnableDebug();
    //CVbyteP2P::DisableDebug();

    if (!CVbyteP2P::LoadAndInit("D://p2p")) {
        printf("load p2p failed\n");
        return -1;
    }

    char * package = "you_package";
    char * appId = "you_appId";
    char * appKey = "you_appKey";
    char * secretKey = "you_secretKey";

    CVbyteP2P::SetPackage(package);
    //CVbyteP2P::SetVersion("v1.0.0"); // Deprecated，由p2p sdk指定
    CVbyteP2P::SetAppId(appId);
    CVbyteP2P::SetAppKey(appKey);
    CVbyteP2P::SetSecretKey(secretKey);

    Sleep(500);

    int id = CVbyteP2P::CreateInstance(EventCallback, ErrorCallback, "No.1 player");
    if (id <= 0) {
        printf("create instance error\n");
        return -1;
    }
    const char *url = "http://tc-tct.douyucdn.cn/dyliveflv1/85894rmovieChow.flv?token=tencent_video ";
    if (!CVbyteP2P::PlayURL(id, url)) {
        printf("play url error\n");
        return -1;
    }
    getchar();
    CVbyteP2P::Unplay(id);        

    CVbyteP2P::Unload();
    WSACleanup();
    return 0;
}
事件码和错误码如下：

	/*========================*
    * 事件信息
    *========================*/
    typedef enum EventCode_ {
        START = 10010000,       // 仅仅属于直播的，启动一个频道
        STARTED,
        STOP,                   // 仅仅属于直播的，停止一个频道
        STOPPED,
        LOAD_READY,
        STUCK_TO_ORIGIN = 10010005, //多次卡播，回退播源
        STATISTICS_DATA = 10010006
    } EventCode;

    /*========================*
    * 错误信息
    *========================*/
    typedef enum ErrorCode_ {
        CONF_UNAVAILABLE = 10001000,    // 公共的，配置服务的
        AUTH_FAILED,                    // 公共的，配置服务的
        CONF_INVALID,                   // 公共的，配置服务的
        LIBEVENT_ERROR = 10001012,      // 公共的,libevent初始化异常,

        CHANNEL_EMPTY = 10011000,       // 仅仅是直播的
        NO_SUCH_CHANNEL,                // 仅仅直播的
        RESOLUTION_INVALID,             // 仅仅直播的，点播应有自己的一套
        FORMAT_INVALID,                 // 仅仅直播的，setMediaFormat与conf的不一致
        SOURCE_DATA_ERROR               // 仅仅是直播的.源或者切片出问题了
    } ErrorCode;
```
