开发者可以使用 TLS 后台 API 及相关工具，生成公私钥、生成 `UserSig` 和校验 `UserSig`。TLS 后台 API 我们提供了 6 个包供开发者 [下载](http://share.weiyun.com/2b3abe0e3f185c440cf455647455f661)，内容分别是 Windows 下 64 位预编译文件包、Windows 下32位预编译文件包、Linux 下64位预编译文件包、Linux 下32位预编译文件包、zip 格式的源代码文件和 tar.gz 格式的源代码文件。

>**注意：**
>在控制台上下载的公私钥文件名分别为 `private_key` 和 `public_key`，分别对应下面的 `ec_key.pem` 和 `public.pem`。请在使用公私钥时注意区分。

## Linux 平台
### 工具使用
>注：这里讲解的是工具的使用说明，实际应用中需要开发者后台调用 TLS 的后台 API 接口生成 sig。

**Linux 下生成 sig 和校验 sig**
首先不带参数执行 `tls_licence_tools`，即执行下面的命令：
```
$ ./tls_licence_tools
```

输出：
 ```
current version: 201511190000
Usage:
    get sig: ./tls_licence_tools gen pri_key_file sig_file sdkappid identifier
    get sig e.g.:./tls_licence_tools gen ec_key.pem sig 1400001052 xiaojun
    verify sig:./tls_licence_tools verify pub_key_file sig_file sdkappid identifier
    verify sig e.g.: ./tls_licence_tools verify public.pem sig 1400001052 xiaojun
```

输出实际上是参数模板和示例。下面是演示截图：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151126140600_45285.png)
执行类似于下面的命令可以生成 sig：
```
./tls_licence_tools gen ec_key.pem sig 1400001052 xiaojun
```

对应的参数解释是：
```
./tls_licence_tools gen 私钥文件路径 sig将要存放的路径 sdkappid 用户id
```
执行类似于下面的命令可以校验 sig：
```
./tls_licence_tools verify public.pem sig 1400001052 xiaojun
```
对应参数的解释是：
```
./tls_licence_tools verify 公钥文件路径 sig的存放路径 sdkappid 用户id
```
以下为生成 sig 演示：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151126140852_93229.png)
以下为校验 sig演示：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151126140903_32964.png)
以下为参数模板中各个参数的意义：
```
gen 和 verify 分别表示生成 sig 和校验 sig 的命令
pri_key_file：私钥文件的路径
pub_key_file：公钥文件的路径
sig_file：sig 文件的路径，如果是生成 sig，那么会将 sig 写入这个文件，如果是校验 sig，那么会从这个文件读取 sig 的内容
sdkappid：创建应用时页面上分配的 sdkappid
identifier：用户标识，即用户 id
```

> **注意：**
> 生成的 sig 有效期为 180 天，开发者需要在 sig 过期前，重新生成 sig。

### C++ 接口

首先包含 `include/tls_sig_api` 目录下的 `tls_signature.h`。头文件中包含的接口，`tls_gen_signature_ex2` 和 `tls_check_signature_ex2`，前者是生成 sig 的接口，后者是校验 sig 的接口，详细的参数和返回值说明请参考头文件 `tls_signature.h`。

然后是链接静态库，在 lib 目录下有下列目录：
```
├── jni
├── jsoncpp
├── openssl
└── tls_sig_api
```

需要链接的静态库是 `libjsoncpp.a`、`openssl` 目录下的 `libcrypto.a` 和 `libtlsignature.a`。另外还需要链接系统的 `-ldl` 和 `-lz` ，详细可以查看 `example/cpp/Makefile`，由于 `libtlsignature.a` 引用了 `openssl` 和 `json` 的开发库，所以链接时 `libtlsignature.a` 出现命令的最前面。

下面的截图是我们开发时编译 `tls_licence_tools` 的命令行，由于是我们这边的开发环境，链接库的路径可以按照开发者自己的实际情况给出。
![](//avc.qcloud.com/wiki2.0/im/imgs/20151126141059_97182.png)

>**注意：**
>如果程序有多线程调用 TLS 后台 API 的用法，请在程序初始化时和结束时分别调用下面的接口：
```
int multi_thread_setup(void);
void multi_thread_cleanup(void);
```

### Java 接口
目前 Java 接口使用 JNI 的方式实现。Java 目录下 `tls_sigcheck.class`，是由 `tls_sigcheck.java` 编译得到，如果有 jdk 兼容性问题，开发者可自行重新编译此文件，编译命令为：
```
javac -encoding utf-8 tls_sigcheck.java
```
请注意接口的包路径为 `com.tls.sigcheck`，典型的使用方法是 `example` 目录下 Java 版本 Demo 的组织方式。
```
├── com
│   └── tls
│       └── sigcheck
│           └── tls_sigcheck.class
├── Demo.class
├── Demo.java
├── ec_key.pem
├── public.pem
└── README
```
之前提到 Java 接口目前使用的 JNI 的方式，所以 `Demo.java` 调用了载入 so 的语句，开发者根据自己的存放 `jnisigcheck.so` 实际路径进行修改，在二进制包中预编译的 `jnisigcheck.so` 存放在 `lib/jni` 目录下。Demo 的使用方式请参考 `example/java/README`。下面是演示截图：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151126141635_23603.png)

>注：如果在 Java 代码中使用了**多线程**的方式生成 `usersig`，可以参阅 [腾讯云论坛](http://bbs.qcloud.com/thread-22323-1-1.html) 相关介绍。

### Java 原生接口
Java 原生接口依赖于 5 个jar包中。在 `tls_sig_api/java_native/lib` 目录下：
```
├── bcpkix-jdk15on-152.jar
├── bcprov-jdk15on-152.jar
├── commons-codec-1.10.jar
├── gson-2.3.1.jar
├── json.jar
└── tls_signature.jar
```

>**注意**
>从控制台界面 [下载](/doc/product/269/下载公私钥) 的公私钥，将公钥内容赋值给接口中的 `publicBase64Key` 参数，私钥内容赋值给接口中的 `privateBase64Key` 参数。

### PHP 接口
PHP 实现的方式较为简单，就是调用命令行工具生成 sig，工具是 `bin/signature`，PHP 的调用方式如下：
> 注：开发者请注意命令执行的路径和可执行权限，如果出现问题请尝试打印出 `command` 变量的内容进行定位。

```
function signature($identifier, $sdkappid, $private_key_path)
{
    # 这里需要写绝对路径，开发者根据自己的路径进行调整
    $command = '/home/signature'
    . ' ' . escapeshellarg($private_key_path)
    . ' ' . escapeshellarg($sdkappid)
    . ' ' . escapeshellarg($identifier);
    $ret = exec($command, $out, $status);
    if ($status == -1)
    {
        return null;
    }
    return $out;
}
```

### PHP原生接口
在源码包和二进制包中都带有 `php/TLSSig.php` 文件，生成 sig 接口 genSig 和校验 sig 接口 verifySig 均在其中，注意 PHP 环境需要带 openssl 扩展，否则接口使用会报错，另外只支持 PHP 5.3 及以上的版本。

> 注：如果上述实现 PHP 环境无法满足要求，比如使用了红帽系（fedora、centos 和 rel 等）的操作系统，可以参考[腾讯论坛](http://bbs.qcloud.com/thread-22519-1-1.html) 中另一种与 openssl 和系统无关的实现。

## Windows 平台
### 工具使用
>注：这里讲解的是工具的使用说明，实际应用中需要开发者后台调用 TLS 的后台 API 接口生成 sig。

**Windows 下生成 sig 和校验 sig**
首先不带参数执行 `tls_licence_tools.exe`，即执行下面的命令：
```
tls_licence_tools.exe
```
输出：
```
current version: 201511190000
Usage:
    get sig: tls_licence_tools.exe gen pri_key_file sig_file sdkappid identifier
    get sig e.g.: tls_licence_tools.exe gen ec_key.pem sig 1400001052 xiaojun
    verify sig: tls_licence_tools.exe verify pub_key_file sig_file sdkappid identifier
    verify sig e.g.: tls_licence_tools.exe verify public.pem sig 1400001052 xiaojun
```

输出实际上是参数模板和示例。下面是演示截图：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151126142633_17041.png)
执行类似于下面的命令可以生成 sig：
```
tls_licence_tools.exe gen ec_key.pem sig 1400001052 xiaojun
```
对应的参数解释是：
```
tls_licence_tools gen 私钥文件路径 sig 将要存放的路径 sdkappid 用户id
```
执行类似于下面的命令可以校验 sig：
```
tls_licence_tools.exe verify public.pem sig 1400001052 xiaojun
```
对应参数的解释是：
```
tls_licence_tools verify 公钥文件路径 sig的存放路径 sdkappid 用户id
```
下面演示截图：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151126142725_41827.png)
sig 文件的内容如下图：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124221_16540.png)
校验 sig 演示截图：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151126142759_94666.png)
下面解释下参数模板中参数的意义：
>**注意：**
>生成的 sig 有效期为 180 天，开发者需要在 sig 过期前，重新生成 sig。

```
gen 和 verify:分别表示生成 sig 和校验 sig 的命令
pri_key_file：私钥文件的路径
pub_key_file：公钥文件的路径
sig_file：sig 文件的路径，如果是生成 sig，那么会将 sig 写入这个文件，如果是校验 sig，那么会从这个文件读取 sig 的内容
sdkappid：创建应用时页面上分配的 sdkappid
identifier：用户标识，即用户 id
```

### C++ 接口
Windows 下 C++ 接口的使用方式我们采用 vs2012 来举例。首先包含 `include\tls_sig_api` 目录下的 `tls_signature.h`。头文件中包含的接口，`tls_gen_signature_ex2` 和 `tls_check_signature_ex2`，前者是生成 sig 的接口，后者是校验 sig 的接口，详细的参数和返回值说明请参考头文件 `tls_signature.h`。
然后是链接静态库，在 `lib` 目录下有下列目录：
```
├── jni
├── jsoncpp
├── libsigcheck
├── openssl
├── tls_sig_api
└── zlib
```
需要链接的静态库是 `jsoncpp.lib`、`openssl` 目录下的 `libeay.lib`、`libtlsignature.lib` 和 `zlib` 目录下的 `zlibstat.lib`，典型的编译配置如下：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124457_90952.png)
![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124511_24769.png)

>**注意：**
>如果程序是多线程调用 TLS 后台 API，请在程序初始化时和结束时分别调用下面的接口：

```
int multi_thread_setup(void);
void multi_thread_cleanup(void);
```

### Java 接口
目前 Java 接口使用 JNI 的方式实现。Java 目录下 `tls_sigcheck.class`，是由 `tls_sigcheck.java` 编译得到，如果有 JDK 兼容性问题，开发者可自行重新编译此文件，编译命令为：
```
javac -encoding utf-8 tls_sigcheck.java
```
请注意接口的包路径为 `com.tls.sigcheck`，典型的使用方法是 `example` 目录下 Java 版本 Demo 的组织方式：
```
├── com
│   └── tls
│       └── sigcheck
│           └── tls_sigcheck.class
├── Demo.class
├── Demo.java
├── ec_key.pem
├── public.pem
└── README
```
之前提到 Java 接口使用的 JNI 的方式，所以 `Demo.java` 调用了载入 dll 的语句，开发者根据自己的存放 `jnisigcheck.dll` 实际路径进行修改，预编译的 `jnisigcheck.dll` 存放在 `lib\jni` 目录下。Demo 的使用方式请参考 `example\java\README`。下面是演示截图：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124617_41874.png)
下面是运行结果：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151126142954_16596.png)

>**注意：**
>如果在 Java 代码中使用了多线程的方式生成 `usersig`，可以参考[腾讯云论坛](http://bbs.qcloud.com/thread-22323-1-1.html) 中的相关介绍。

### Java 原生接口
Java 原生接口依赖于 5 个 jar 包。在 `tls_sig_api/java_native/lib` 目录下：

```
├── bcpkix-jdk15on-152.jar
├── bcprov-jdk15on-152.jar
├── commons-codec-1.10.jar
├── gson-2.3.1.jar
├── json.jar
└── tls_signature.jar
```

>**注意：**
>从控制台界面 [下载](/doc/product/269/下载公私钥) 的公私钥，将公钥内容赋值给接口中的 `publicBase64Key` 参数，私钥内容赋值给接口中的 `privateBase64Key` 参数。

### C# 接口
以非托管的方式调用 dll 实现，调用的 dll 为 `lib\libsigcheck\sigcheck.dll`，C 样式接口的参数与返回值说明参见 `include\sigcheck.h` 头文件，接口的转换方式如下：

```
class sigcheck
{
    [DllImport(dllpath.DllPath, EntryPoint = "tls_gen_sig_ex", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.Cdecl)]
    public extern static int tls_gen_sig_ex(
        UInt32 sdkappid,
        string identifier,
        StringBuilder sig,
        UInt32 sig_buff_len,
        string pri_key,
        UInt32 pri_key_len,
        StringBuilder err_msg,
        UInt32 err_msg_buff_len
    );

    [DllImport(dllpath.DllPath, EntryPoint = "tls_vri_sig_ex", CharSet = CharSet.Ansi, CallingConvention = CallingConvention.Cdecl)]
    public extern static int tls_vri_sig_ex(
        string sig,
        string pub_key,
        UInt32 pub_key_len,
        UInt32 sdkappid,
        string identifier,
        ref UInt32 expire_time,
        ref UInt32 init_time,
        StringBuilder err_msg,
        UInt32 err_msg_buff_len
    );
}
```

其中 `dllpath.DllPath` 指明了 dll 的路径，详细请参见 `example\cs\csdemo.cs`。关于 Demo 的使用方法参见 `example\cs\README`。下面是演示截图：
>**注意：**
>如果选择 Any CPU 平台，请默认加载 32 位 dll。

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013132403_75795.png)
![](//avc.qcloud.com/wiki2.0/im/imgs/20151013132415_34994.png)
![](//avc.qcloud.com/wiki2.0/im/imgs/20151013132427_96968.png)

下面是运行结果：
![](//avc.qcloud.com/wiki2.0/im/imgs/20151126143241_19273.png)

### PHP 接口

PHP 实现的方式较为简单，就是调用命令行工具生成 sig，工具是 `bin\signature.exe`，PHP 的调用方式如下：
> 注：开发者请注意命令执行的路径，如果出现问题请尝试打印出 `command` 变量的内容进行定位。

```
function signature($identifier, $sdkappid, $private_key_path)
{
    # 这里需要写绝对路径，开发者根据自己的路径进行调整
    $command = 'D:\\signature.exe'
    . ' ' . escapeshellarg($private_key_path)
    . ' ' . escapeshellarg($sdkappid)
    . ' ' . escapeshellarg($identifier);
    $ret = exec($command, $out, $status);
    if ($status == -1)
    {
        return null;
    }
    return $out;
}
```

### PHP 原生接口
在源码包和二进制包中都带有 `php/TLSSig.php` 文件，生成 sig 接口 `genSig` 和校验 sig 接口 `verifySig` 均在其中，注意 PHP 环境需要带 openssl 扩展，否则接口使用会报错，另外只支持 PHP 5.3 及以上的版本。

>注：若上述实现 PHP 环境无法满足要求，比如使用了红帽系（fedora、centos 和 rel 等）的操作系统，可以参考 [腾讯云论坛](http://bbs.qcloud.com/thread-22519-1-1.html) 另一种与 openssl 和系统无关的实现。

## 其他平台接口

- [JavaScript](https://www.npmjs.com/package/tls-sig-api)
- [Python]( https://pypi.org/project/tls-sig-api/)
- [Go](http://bbs.qcloud.com/thread-21826-1-1.html)
- [Java](https://mvnrepository.com/artifact/com.github.tencentyun/tls-sig-api)
- [PHP](https://packagist.org/packages/tencent/tls-sig-api)

## TLS 后台 API 下载
下载 [TLS 后台 API ](http://share.weiyun.com/2b3abe0e3f185c440cf455647455f661)。
## 联系我们

[腾讯云论坛](http://bbs.qcloud.com/thread-8287-1-1.html) 的一些信息可能对您有帮助，如需更多帮助，请[提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=29&level2_id=40&source=0&data_title=云通信%20%20IM&step=1)。
