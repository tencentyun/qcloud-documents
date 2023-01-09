## 操作场景
本文档介绍如何在客户端集成 c++ 版本的 SDK。

## 操作步骤
### 步骤一：引入 c++ SDK
需要在项目中包含 SDK 的头文件和库，进行 SDK 的使用。头文件和库提供以下两种获取方式：
1. 获取源码自行编译，请参见 [SDK 编译使用](https://github.com/apache/inlong/tree/release-1.3.0/inlong-sdk/dataproxy-sdk-twins/dataproxy-sdk-cpp)。
2. 直接使用现有的头文件和库，[点击前往下载](https://inlong-resource-1312784730.cos-website.ap-guangzhou.myqcloud.com/download/index.html)。

### 步骤二：数据上报流程
引入 SDK 后，可以通过调用 SDK 的 `send` 相关接口进行单条（批量）数据的上报，发送 demo 可参考 [send_demo.cc](https://github.com/apache/inlong/blob/release-1.3.0/inlong-sdk/dataproxy-sdk-twins/dataproxy-sdk-cpp/release/demo/send_demo.cc)。整体流程包括以下三个步骤：
1. 初始化 SDK
SDK 支持对象实例化和配置文件初始化两种方式（二选一即可）：
	- **对象实例初始化**
首先初始化客户端配置，然后调用初始化接口：
``` 
// 初始化客户端配置
ClientConfig client;
// 设置client相关配置参数，其中proxy_URL_为必选参数（格式如下），其他参数详见client_config.h文件
client.proxy_cluster_URL_="http://{Manager url}/inlong/manager/openapi/dataproxy/getIpList";
// 初始化SDK, 返回值为零表示初始化成功，非零表示失败
int32_t result = tc_api_init(client);
```
	- **配置文件初始化**
配置文件采用 json 格式，请参见 [配置文件说明](#配置文件说明)，通过配置文件初始化 SDK：
```
// 初始化SDK，参数为配置文件的路径名；返回值为零表示初始化成功
int32_t result = tc_api_init("/home/conf/config.json");
```

2. 调用发送接口进行数据上报
SDK 支持单条（推荐）和批量发送，二者发送过程均为异步模式，数据上报接口是线程安全的。在进行数据上报前，可设置回调函数在数据发送失败时进行回调处理，回调函数签名如下：
```
int32_t callBackFunc(const char* inlong_group_id, const char* inlong_stream_id, const char* msg, int32_t msg_len, const int64_t report_time, const char* client_ip);
```
	- **单条数据数据上报接口**
```
// 返回值：零表示发送成功，非零表示失败，具体异常返回值详见tc_api.h中的SDKInvalidReuslt
int32_t tc_api_send(const char* inlong_group_id, const char* inlong_stream_id, const char* msg, int32_t msg_len, UserCallBack call_back = NULL);
```
	- **批量数据上报接口**
```
int32_t tc_api_send_batch(const char* inlong_group_id, const char* inlong_stream_id, const char** msg_list, int32_t msg_cnt, UserCallBack call_back = NULL);
```

3. 关闭 SDK
调用 close 接口关闭 SDK：
```
// 返回值为零表示关闭成功，后续无法再进行数据上报
// max_waitms：关闭SDK前的等待最大毫秒数，等待SDK内部数据发送完成
int32_t tc_api_close(int32_t max_waitms);
```

## 注意事项
1. SDK 的初始化和关闭都是进程级别的，只需初始化一次，fork 的子进程中需调用初始化接口后再进行数据上报。
2. 建议采用将 SDK 作为常驻服务来进行数据上报，避免同个进程中途频繁地初始化和关闭，重复初始化和关闭会带来更多开销。
3. SDK 发送是异步进行的，返回值为0表示数据成功存入了 SDK 内部缓冲区，等待网络发送。如果 `inlong_group_id` 本身配置有误或者网络异常，也会导致数据发送失败，所以建议用户在调用该接口时设置回调，数据多次重试发送仍失败时执行回调。

## 配置文件说明<span id="配置文件说明"></span>
配置文件格式和重要参数如下：
```
{
    "init-param": {
        "thread_num": 5, //网络收发线程的数量
        "enable_pack": true, //是否多条打包发送
        "pack_size": 409600, //数据达到pack_size大小，进行打包发送，单位字节
        "ext_pack_size": 409600, //单条数据最大长度，单位字节
        "enable_zip": true, //是否进行数据压缩
        "min_ziplen": 4096, //最小压缩长度，单位字节
        "enable_retry": true, //发送失败是否进行重试
        "retry_ms": 10000, //重试间隔时间，单位毫秒
        "retry_num": 3, //发送失败最大重试次数
        "max_active_proxy": 4, //tcp最大连接数，用于网络数据收发
        "max_buf_pool": 548576000, //单个数据缓存区大小，单位字节
		 "buffer_num_per_groupId": 3, //每个groupid的数据缓存区个数
        "log_num": 10, //最大日志文件数
        "log_size": 10, //单个日志大小限制，单位MB
        "log_level": 3, //日志级别，trace(4)>debug(3)>info(2)>warn(1)>error(0)
        "log_file_type": 2, //日志输出，2->文件, 1->控制台
        "log_path": "./", //日志路径
        "proxy_cfg_preurl": "http://127.0.0.1:8099/inlong/manager/openapi/dataproxy/getIpList", //访问manager的url
        "need_auth": false, //是否需要认证
        "auth_id": "admin", //认证id
        "auth_key": "adminKey" //认证key
    }
}
```
