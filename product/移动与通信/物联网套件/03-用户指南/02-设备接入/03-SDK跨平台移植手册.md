##  硬件及操作系统平台抽象层（HAL 层）
SDK 抽象定义了硬件及操作系统平台抽象层（HAL 层），将所依赖的内存、定时器、网络传输交互等功能，
都封装在 HAL 层（对应库libtc_iot_hal）中，进行跨平台移植时，首先都需要根据对应平台的硬件及操作系统情况，
对应适配或实现相关的功能。

平台移植相关的头文件及源文件代码结构如下：
```shell
include/platform/
|-- linux                   # 不同的平台或系统，单独建立独立的目录
|   |-- tc_iot_platform.h   # 引入对应平台相关的定义或系统头文件
|-- tc_iot_hal_network.h    # 网络相关定义
|-- tc_iot_hal_os.h         # 操作系统内存、时间戳等相关定义
|-- tc_iot_hal_timer.h      # 定时器相关定义
src/platform/
|-- CMakeLists.txt
|-- linux
    |-- CMakeLists.txt
    |-- tc_iot_hal_net.c    # TCP 非加密直连方式网络接口实现
    |-- tc_iot_hal_os.c     # 内存及时间戳实现
    |-- tc_iot_hal_timer.c  # 定时器相关实现
    |-- tc_iot_hal_tls.c    # TLS 加密网络接口实现
```

C-SDK 中提供的 HAL 层是基于 Linux 等 POSIX 体系系统的参考实现，但并不强耦合要求实现按照 POSIX 接口方式，移植时可根据目标系统的情况，灵活调整。

所有 HAL 层函数都在 include/platform/tc_iot_hal*.h 中进行声明，函数都以 tc_iot_hal为前缀。

以下是需要实现的 HAL 层接口，详细信息可以参考注释。

###  基础功能
| 功能分类 | 函数名                               | 说明                                 | 是否可选 |
| ---- | --------------------------------- | ---------------------------------- | ---- |
| 内存   | tc_iot_hal_malloc                 | 分配所需的内存空间，并返回一个指向它的指针。             | 基础必选 |
| 内存   | tc_iot_hal_free                   | 释放之前调用 tc_iot_hal_malloc 所分配的内存空间。 | 基础必选 |
| 输入输出 | tc_iot_hal_printf                 | 发送格式化输出到标准输出 stdout。               | 基础必选 |
| 输入输出 | tc_iot_hal_snprintf               | 发送格式化输出到字符串。                       | 基础必选 |
| 时间日期 | tc_iot_hal_timestamp              | 系统时间戳，格林威治时间 1970-1-1 00点起总秒数      | 基础必选 |
| 定时器  | tc_iot_hal_sleep_ms               | 睡眠挂起一定时长，单位：ms                     | 基础必选 |
| 定时器  | tc_iot_hal_timer_init             | 初始化或重置定时器                          | 基础必选 |
| 定时器  | tc_iot_hal_timer_is_expired       | 判断定时器是否已经过期                        | 基础必选 |
| 定时器  | tc_iot_hal_timer_countdown_ms     | 设定定时器时延，单位：ms                      | 基础必选 |
| 定时器  | tc_iot_hal_timer_countdown_second | 设定定时器时延，单位：s                       | 基础必选 |
| 定时器  | tc_iot_hal_timer_left_ms          | 检查定时器剩余时长，单位：ms                    | 基础必选 |
| 随机数  | tc_iot_hal_srandom                | 设置随机数种子值                           | 基础必选 |
| 随机数  | tc_iot_hal_random                 | 获取随机数                              | 基础必选 |

###  网络功能（二选一或全选）
根据实际连接方式选择，如是否走MQTT over TLS加密，是否通过HTTPS接口获取Token等，选择性实现 TCP 或 TLS 相关接口。

####  TCP

| 功能分类   | 函数名                         | 说明              | 是否可选        |
| ------ | --------------------------- | --------------- | ----------- |
| TCP 连接 | tc_iot_hal_net_init         | 初始化网络连接数据       | 可选，非加密直连时实现 |
| TCP 连接 | tc_iot_hal_net_connect      | 连接服务端           | 可选，非加密直连时实现 |
| TCP 连接 | tc_iot_hal_net_is_connected | 判断当前是否已成功建立网络连接 | 可选，非加密直连时实现 |
| TCP 连接 | tc_iot_hal_net_write        | 发送数据到网络对端       | 可选，非加密直连时实现 |
| TCP 连接 | tc_iot_hal_net_read         | 接收网络对端发送的数据     | 可选，非加密直连时实现 |
| TCP 连接 | tc_iot_hal_net_disconnect   | 断开网络连接          | 可选，非加密直连时实现 |
| TCP 连接 | tc_iot_hal_net_destroy      | 释放网络相关资源        | 可选，非加密直连时实现 |

####  TLS

| 功能分类   | 函数名                         | 说明                   | 是否可选            |
| ------ | --------------------------- | -------------------- | --------------- |
| TLS 连接 | tc_iot_hal_tls_init         | 初始化 TLS 连接数据         | 可选，基于TLS加密通讯时实现 |
| TLS 连接 | tc_iot_hal_tls_connect      | 连接 TLS 服务端并进行相关握手及认证 | 可选，基于TLS加密通讯时实现 |
| TLS 连接 | tc_iot_hal_tls_is_connected | 判断当前是否已成功建立 TLS 连接   | 可选，基于TLS加密通讯时实现 |
| TLS 连接 | tc_iot_hal_tls_write        | 发送数据到 TLS 对端         | 可选，基于TLS加密通讯时实现 |
| TLS 连接 | tc_iot_hal_tls_read         | 接收 TLS 对端发送的数据       | 可选，基于TLS加密通讯时实现 |
| TLS 连接 | tc_iot_hal_tls_disconnect   | 断开 TLS 连接            | 可选，基于TLS加密通讯时实现 |
| TLS 连接 | tc_iot_hal_tls_destroy      | 释放 TLS 相关资源          | 可选，基于TLS加密通讯时实现 |