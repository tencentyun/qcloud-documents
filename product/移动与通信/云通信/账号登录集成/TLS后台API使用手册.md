## 1 概述

开发者可以使用TLS后台API及相关工具，生成公私钥、生成UserSig和校验UserSig。TLS后台API我们提供了6个包供开发者[下载](http://share.weiyun.com/2b3abe0e3f185c440cf455647455f661)，内容分别是windows下64位预编译文件包、windows下32位预编译文件包、linux下64位预编译文件包、linux下32位预编译文件包、zip格式的源代码文件和tar.gz格式的源代码文件。

## 2 linux平台

### 2.1 工具使用

>注：这里讲解的是工具的使用说明，实际应用中需要开发者后台调用tls的后台api接口生成sig。

**linux下生成sig和校验sig**

首先不带参数执行 tls_licence_tools，即执行下面的命令：

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

下面是演示截图：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126140600_45285.png)

输出实际上是参数模板和示例。

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

下面是生成sig演示截图：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126140852_93229.png)

上面是生成sig，下面是校验sig：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126140903_32964.png)

下面解释下参数模板中参数的意义：

```
gen和verify分别表示生成sig和校验sig的命令
pri_key_file：私钥文件的路径
pub_key_file：公钥文件的路径
sig_file：sig 文件的路径，如果是生成 sig，那么会将 sig 写入这个文件，如果是校验 sig，那么会从这个文件读取 sig 的内容
sdkappid：创建应用时页面上分配的 sdkappid
identifier：用户标识，即用户id
```

>注意：生成的sig有效期为180天，开发者需要在sig过期前，重新生成sig。

### 2.2 C++接口

首先包含include/tls_sig_api目录下的tls_signature.h。头文件中包含的接口，tls_gen_signature_ex2和tls_check_signature_ex2，前者是生成sig的接口，后者是校验sig的接口，详细的参数和返回值说明请参考头文件tls_signature.h。
然后是链接静态库，在lib目录下有下列目录：

├── jni
├── jsoncpp
├── openssl
└── tls_sig_api

需要链接的静态库是libjsoncpp.a、openssl目录下的libcrypto.a和libtlsignature.a。另外还需要链接系统的-ldl和-lz，详细可以查看example/cpp/Makefile，由于libtlsignature.a引用了openssl和json的开发库，所以链接时libtlsignature.a出现命令的最前面。

下面的截图是我们开发时编译tls_licence_tools的命令行，由于是我们这边的开发环境，链接库的路径可以按照开发者自己的实际情况给出。

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126141059_97182.png)

【特别注意】
如果程序有多线程调用TLS后台API的用法，请在程序初始化时和结束时分别调用下面的接口：

```
int multi_thread_setup(void);
void multi_thread_cleanup(void);
```

### 2.3 Java接口

目前java接口使用jni的方式实现。Java目录下tls_sigcheck.class，是由tls_sigcheck.java编译得到，如果有jdk兼容性问题，开发者可自行重新编译此文件，编译命令为：

```
javac -encoding utf-8 tls_sigcheck.java
```

请注意接口的包路径为com.tls.sigcheck，典型的使用方法是example目录下java版本demo的组织方式：

├── com
│   └── tls
│       └── sigcheck
│           └── tls_sigcheck.class
├── Demo.class
├── Demo.java
├── ec_key.pem
├── public.pem
└── README

之前提到java接口目前使用的jni的方式，所以Demo.java调用了载入so的语句，开发者根据自己的存放jnisigcheck.so实际路径进行修改，在二进制包中预编译的jnisigcheck.so存放在lib/jni目录下。demo的使用方式请参考example/java/README。
下面是演示截图：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126141635_23603.png)

【**多线程**】如果在 java 代码中使用了多线程的方式生成 usersig，请看[这里](http://bbs.qcloud.com/thread-22323-1-1.html)。

### 2.4 Java原生接口

Java原生接口依赖于5个jar包中。在tls_sig_api/java_native/lib目录下：

├── bcpkix-jdk15on-152.jar
├── bcprov-jdk15on-152.jar
├── commons-codec-1.10.jar
├── gson-2.3.1.jar
├── json.jar
└── tls_signature.jar

【特别注意】

从控制台界面[下载](/doc/product/269/下载公私钥)的公私钥，将公钥内容赋值给接口中的publicBase64Key参数，私钥内容赋值给接口中的privateBase64Key参数。

### 2.5 PHP接口

php实现的方式较为简单，就是调用命令行工具生成sig，工具是bin/signature.exe，php的调用方式如下：

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
开发者请注意命令执行的路径和可执行权限，如果出现问题请尝试打印出 command 变量的内容进行定位。

### 2.6 PHP原生接口
在源码包和二进制包中都带有php/TLSSig.php文件，生成sig接口genSig和校验sig接口verifySig均在其中，注意PHP环境需要带openssl扩展，否则接口使用会报错，另外只支持PHP 5.3及以上的版本。

如果上述实现PHP环境无法满足要求，比如使用了红帽系（fedora、centos 和 rel 等）的操作系统，可以参考[此处](http://bbs.qcloud.com/thread-22519-1-1.html)另一种与openssl和系统无关的实现。

## 3 windows平台

### 3.1 工具使用

>注：这里讲解的是工具的使用说明，实际应用中需要开发者后台调用tls的后台api接口生成sig。

**windows下生成sig和校验sig**

首先不带参数执行tls_licence_tools.exe，即执行下面的命令：

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

下面是演示截图：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126142633_17041.png)

输出实际上是参数模板和示例。

执行类似于下面的命令可以生成 sig：

```
tls_licence_tools.exe gen ec_key.pem sig 1400001052 xiaojun
```

对应的参数解释是：

```
tls_licence_tools gen 私钥文件路径 sig将要存放的路径 sdkappid 用户id
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

sig文件的内容如下图：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124221_16540.png)

校验sig演示截图：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126142759_94666.png)

下面解释下参数模板中参数的意义：

```
gen和verify分别表示生成sig和校验sig的命令
pri_key_file：私钥文件的路径
pub_key_file：公钥文件的路径
sig_file：sig 文件的路径，如果是生成 sig，那么会将 sig 写入这个文件，如果是校验 sig，那么会从这个文件读取 sig 的内容
sdkappid：创建应用时页面上分配的 sdkappid
identifier：用户标识，即用户 id
```

>注意：生成的sig有效期为180天，开发者需要在sig过期前，重新生成sig。

### 3.2 C++接口

windows下C++接口的使用方式我们采用vs2012来举例。

首先包含include\tls_sig_api目录下的tls_signature.h。头文件中包含的接口，tls_gen_signature_ex2和tls_check_signature_ex2，前者是生成sig的接口，后者是校验sig的接口，详细的参数和返回值说明请参考头文件tls_signature.h。

然后是链接静态库，在lib目录下有下列目录：

├── jni
├── jsoncpp
├── libsigcheck
├── openssl
├── tls_sig_api
└── zlib

需要链接的静态库是jsoncpp.lib、openssl目录下的libeay.lib、libtlsignature.lib和zlib目录下的zlibstat.lib，典型的编译配置如下：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124457_90952.png)

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124511_24769.png)

【特别注意】

如果程序是多线程调用TLS后台API，请在程序初始化时和结束时分别调用下面的接口：

```
int multi_thread_setup(void);
void multi_thread_cleanup(void);
```

### 3.3 Java接口

目前java接口使用jni的方式实现。Java目录下tls_sigcheck.class，是由tls_sigcheck.java编译得到，如果有jdk兼容性问题，开发者可自行重新编译此文件，编译命令为：

```
javac -encoding utf-8 tls_sigcheck.java
```

请注意接口的包路径为com.tls.sigcheck，典型的使用方法是example目录下java版本demo的组织方式：

├── com
│   └── tls
│       └── sigcheck
│           └── tls_sigcheck.class
├── Demo.class
├── Demo.java
├── ec_key.pem
├── public.pem
└── README

之前提到java接口使用的jni的方式，所以Demo.java调用了载入dll的语句，开发者根据自己的存放jnisigcheck.dll实际路径进行修改，预编译的jnisigcheck.dll存放在lib\jni目录下。demo的使用方式请参考example\java\README。下面是演示截图：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124617_41874.png)

下面是运行结果，

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126142954_16596.png)

【**多线程**】如果在 java 代码中使用了多线程的方式生成 usersig，请看[这里](http://bbs.qcloud.com/thread-22323-1-1.html)。

### 3.4 Java原生接口

Java原生接口依赖于5个jar包。在tls_sig_api/java_native/lib目录下：

├── bcpkix-jdk15on-152.jar
├── bcprov-jdk15on-152.jar
├── commons-codec-1.10.jar
├── gson-2.3.1.jar
├── json.jar
└── tls_signature.jar

【特别注意】

从控制台界面[下载](/doc/product/269/下载公私钥)的公私钥，将公钥内容赋值给接口中的publicBase64Key参数，私钥内容赋值给接口中的privateBase64Key参数。

### 3.5 C#接口

以非托管的方式调用dll实现，调用的dll为lib\libsigcheck\sigcheck.dll，C样式接口的参数与返回值说明参见include\sigcheck.h头文件，接口的转换方式如下：

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

其中dllpath.DllPath指明了dll的路径，详细请参见example\cs\csdemo.cs。
关于demo的使用方法参见example\cs\README。下面是演示截图：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013132403_75795.png)

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013132415_34994.png)

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013132427_96968.png)

下面是运行结果：

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126143241_19273.png)

>注意：如果选择Any CPU平台，请默认加载32位dll。


### 3.6 PHP接口

php实现的方式较为简单，就是调用命令行工具生成sig，工具是bin\signature.exe，php的调用方式如下：


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
开发者请注意命令执行的路径，如果出现问题请尝试打印出 command 变量的内容进行定位。

### 3.7 PHP原生接口
在源码包和二进制包中都带有php/TLSSig.php文件，生成sig接口genSig和校验sig接口verifySig均在其中，注意PHP环境需要带openssl扩展，否则接口使用会报错，另外只支持PHP 5.3及以上的版本。

如果上述实现PHP环境无法满足要求，比如使用了红帽系（fedora、centos 和 rel 等）的操作系统，可以参考[此处](http://bbs.qcloud.com/thread-22519-1-1.html)另一种与openssl和系统无关的实现。

## 4 其他平台接口
- javascript http://bbs.qcloud.com/thread-17311-1-1.html
- python http://bbs.qcloud.com/thread-14366-1-1.html
- golang http://bbs.qcloud.com/thread-21826-1-1.html

## 5 TLS 后台 API 下载
点击[这里](http://share.weiyun.com/2b3abe0e3f185c440cf455647455f661)下载。

## 6 联系我们

[这里](http://bbs.qcloud.com/thread-8287-1-1.html)的一些信息可能对您有帮助，如需支持，请@TLS帐号支持，QQ 3268519604，电子邮箱 tls_assistant@tencent.com。


