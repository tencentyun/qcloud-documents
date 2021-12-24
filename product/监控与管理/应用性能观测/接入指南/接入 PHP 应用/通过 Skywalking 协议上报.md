本文将为您介绍如何使用 Skywalking  协议上报 PHP 应用数据。

>? 查看 Skywalking 开源的 [PHP SDK](https://github.com/SkyAPM/SkyAPM-php-sdk)。

## 操作前提

- gcc/g++ 编译器：大于 4.9 版本。
- PHP：大于 7.0 版本。 
- Cmake 编译器：安装大于 3.20.0 版本的 cmake ，操作如下：
<dx-codeblock>
:::  sh
wget https://cmake.org/files/v3.20/cmake-3.20.0.tar.gz
tar -zxvf cmake-3.20.0.tar.gz
cd cmake-3.20.0

./bootstrap
make
make install
:::
</dx-codeblock>
<dx-alert infotype="explain" title="">
yum 安装的版本也较低，因此采用从源码安装方式。
</dx-alert>



## 操作步骤 

### 步骤1：获取接入点和 Token
进入 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**页面，单击**接入应用**，在接入应用时选择 PHP 语言与 SkyWalking 的数据采集方式。在选择接入方式步骤获取您的接入点和 Token，如下图所示：
![img](https://main.qcloudimg.com/raw/d7d94913947d31edf70e85c6462c6bac.png)

### 步骤2：安装 GRPC
<dx-codeblock>
:::  sh
wget https://apm-php-depend-src-1258344699.cos.ap-guangzhou.myqcloud.com/grpc.submodule.tar.gz
mkdir -p cmake/build
cd cmake/build
cmake ../..
make -j$(nproc)
ldconfig
# protobuf
cd third_party/protobuf/
./autogen.sh
./configure
make -j$(nproc)
make install
ldconfig
:::
</dx-codeblock>

### 步骤3：编译 skywalking.so 扩展

1.编译 skywalking.so 扩展需要提前安装依赖库。(已安装可以忽略）
<dx-codeblock>
:::  Linux
# yum install boost-devel
# yum install autoconf
  :::
</dx-codeblock>

2. 配置境变量：
` export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/lib:/usr/local/lib64`
`export LD_RUN_PATH=$LD_RUN_PATH:/usr/local/lib:/usr/local/lib64`

3. 编译 skywalking.so 扩展：
<dx-codeblock>
:::  sh
wget https://apm-php-depend-src-1258344699.cos.ap-guangzhou.myqcloud.com/SkyAPM-php-sdk.tar.gz
cd SkyAPM-php-sdk/
/usr/local/services/php7/bin/phpize
./configure --with-grpc-src="/本机路径/grpc" --with-php-config="/本机路径/php7/bin/php-config"
make
make install
:::
</dx-codeblock>

>?编译完成后，可在 PHP 的扩展目录看到多了一个 [skywalking.so](http://skywalking.so/) 文件。

### 步骤4：修改 php.ini 配置文件

修改 php.ini 如下配置项：
<dx-codeblock>
:::  ini
[skywalking]
; 添加扩展
extension=skywalking.so
; 设置应用名称
skywalking.app_code = php_misterli_test
; 开启收集器
skywalking.enable = 1
; 设置skyWalking服务版本
skywalking.version = 8
; 设置skyWalking服务地址
skywalking.grpc = ap-guangzhou.apm.tencentcs.com:11800
; 设置鉴权的token
skywalking.authentication = jnNURCx*******biKzgu
skywalking.error_handler_enable = 0
:::
</dx-codeblock>


>?更多配置信息可参见 [SkyAPM-php-sdk/php.ini](https://github.com/SkyAPM/SkyAPM-php-sdk/blob/master/php.ini)。


### 步骤5：重启 php-fpm

**方法一：** 将修改 **php-fpm.conf** 的配置项中启动方式为 **daemonize = no** 。
**方法二：**使用 nohup 命令重启 php-fpm：
<dx-codeblock>
:::  nohup
nohup /usr/local/services/php7/sbin/php-fpm > /usr/local/services/php7/log/php-fpm-output.log 2>&1 &
:::
</dx-codeblock>


### 步骤6：请求后端服务验证是否接入成功

1. 请求您的服务，下列以用 Laravel 框架部署了一个简单的 HTTP 服务为例：
<dx-codeblock>
:::  sh
# curl "http://test.skywalking.com/getHelloWorld"
hello, skywalking
:::
</dx-codeblock>
2. 使用 tcpdump 命令查看 11800 端口是否有数据包发送：
<dx-codeblock>
:::  sh
# tcpdump -i any -A -s0 -n -nn -l port 11800
dropped privs to tcpdump
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode 262144 bytes
:::
</dx-codeblock>
3. 在 [应用性能观测控制台](https://console.cloud.tencent.com/apm) **应用监控** > **应用列表**和**应用详情**查看是否有上报数据。
