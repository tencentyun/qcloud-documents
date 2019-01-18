## 1. Overview

Developers can use TLS backend APIs and related tools to generate public/private keys and UserSig, and verify UserSig. TLS backend APIs provide six packages for developers to [download](http://share.weiyun.com/2b3abe0e3f185c440cf455647455f661), including precompiled package on Windows 64-bit, precompiled package on Windows 32-bit, precompiled package on Linux 64-bit, precompiled package on Linux 32-bit, source code files of zip format and source code files of tar.gz format.

## 2. Linux Platform

### 2.1 How to use the tools

> Note: The following shows how to use the tools. In practice, developers need to call TLS backend APIs at backend to generate sig.

**Generate and verify sig on Linux**

First, execute tls_licence_tools without parameters, as shown below:

```
$ ./tls_licence_tools
```


Output:
 ```
current version: 201511190000
Usage:
    get sig: ./tls_licence_tools gen pri_key_file sig_file sdkappid identifier
    get sig e.g.:./tls_licence_tools gen ec_key.pem sig 1400001052 xiaojun
    verify sig:./tls_licence_tools verify pub_key_file sig_file sdkappid identifier
    verify sig e.g.: ./tls_licence_tools verify public.pem sig 1400001052 xiaojun
```

This can be illustrated by the following screenshot:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126140600_45285.png)

The output is actually parameter template and example.

Execute a command similar to the following to generate sig:

```
./tls_licence_tools gen ec_key.pem sig 1400001052 xiaojun
```

Descriptions of the parameters:


```
./tls_licence_tools gen <path to private key file> <path for storing the sig> <sdkappid> <user ID>
```


Execute a command similar to the following to verify sig:

```
./tls_licence_tools verify public.pem sig 1400001052 xiaojun
```

Descriptions of the parameters:

```
./tls_licence_tools verify <path to public key file> <path for storing the sig> <sdkappid> <user ID>
```

The following screenshot shows the generation of sig:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126140852_93229.png)

The above shows the generation of sig, and the below shows the verification of sig:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126140903_32964.png)

The descriptions of parameters in parameter template are as follows: 

```
gen and verify represent the commands for generating sig and verifying sig, respectively.
pri_key_file: The path to private key file
pub_key_file: The path to public key file
sig_file: The path to sig file. For generation of sig, the sig is written to this file; for verification of sig, the sig is read from this file.
sdkappid: The sdkappid assigned on the page when creating App.
identifier: User ID.
```

> Note: The generated sig is valid for 180 days, and developers need to generate a new sig before the sig expires.

### 2.2 C++ APIs

First, include tls_signature.h under directory include/tls_sig_api. Header file contains two APIs: tls_gen_signature_ex2, which is used to generate sig, and tls_check_signature_ex2, which is used to verify sig. For more information about parameters and returned values, please see header file tls_signature.h.
Then link the static libraries. The directories under lib directory are as follows:

├── jni
├── jsoncpp
├── openssl
└── tls_sig_api

The static libraries to be linked are libcrypto.a and libtlsignature.a under directories libjsoncpp.a and openssl. In addition, -ldl and -lz of the system also need to be linked. For more information, please check example/cpp/Makefile. Because libtlsignature.a references development libraries of openssl and json, libtlsignature.a precedes the command for linking.

The following screenshot shows the command line for compiling tls_licence_tools in our development environment. The paths for linking the libraries depend on the developer's actual situation.

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126141059_97182.png)

**Note**
If your program uses multiple threads to call the TLS backend APIs, call the following APIs respectively when initializing and ending the program:

```
int multi_thread_setup(void);
void multi_thread_cleanup(void);
```

### 2.3 Java APIs

Currently, Java APIs are implemented with jni. The file tls_sigcheck.class under Java directory is compiled from tls_sigcheck.java. In case of any jdk compatibility issue, developer can re-compile the file by using the following command:

```
javac -encoding utf-8 tls_sigcheck.java
```

Please note that the API package path is com.tls.sigcheck. Typically, it is organized in the same way as the demo of Java version under example directory:

├── com
│   └── tls
│       └── sigcheck
│           └── tls_sigcheck.class
├── Demo.class
├── Demo.java
├── ec_key.pem
├── public.pem
└── README

It was mentioned earlier that Java API is implemented with jni, therefore Demo.java calls the statement that references "so", which can be modified by developer based on the actual path for storing jnisigcheck.so. jnisigcheck.so pre-complied in the binary package is placed under directory lib/jni. For more information on how to use demo, please refer to example/java/README.
This can be illustrated by the following screenshot:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126141635_23603.png)

**Multi-thread** If usersig is generated on a multi-thread basis in Java code, please see [here](http://bbs.qcloud.com/thread-22323-1-1.html).

### 2.4 Java native APIs

Java native APIs are dependent on five jar packages. Under the directory tls_sig_api/java_native/lib:

├── bcpkix-jdk15on-152.jar
├── bcprov-jdk15on-152.jar
├── commons-codec-1.10.jar
├── gson-2.3.1.jar
├── json.jar
└── tls_signature.jar

[Note]

For the public and private keys [downloaded](/doc/product/269/下载公私钥) from console, the public key content is assigned to the parameter publicBase64Key in the API, and the private key content to the parameter privateBase64Key.

### 2.5 PHP APIs

PHP can be implemented by simply calling the command line tool bin/signature.exe to generate sig, as show below:

```
function signature($identifier, $sdkappid, $private_key_path)
{
    # An absolute path is required. This can vary with developers.
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
Developers should pay attention to the path for executing the command and execution permission. In case of any error, try to print out the content of "command" variable to locate the error.

### 2.6 PHP native APIs
Both source code package and binary package come with the file php/TLSSig.php, which contains the APIs for generating sig (genSig) and for verifying sig (verifySig). Please note that PHP environment needs openssl extension, otherwise an error will occur while using the APIs. In addition, only PHP 5.3 and above are supported. 

If the above PHP implementation does not meet the requirement, for example, in a case where Red Hat operating system (fedora, centos and rel, etc.) is used, you can refer to [here](http://bbs.qcloud.com/thread-22519-1-1.html) for another implementation independent of openssl and system.

## 3. Windows Platform

### 3.1 How to use the tools

> Note: The following shows how to use the tools. In practice, developers need to call TLS backend APIs at backend to generate sig.

**Generate and verify sig on Windows**

First, execute tls_licence_tools.exe without parameters, as shown below:

```
tls_licence_tools.exe
```

Output:

```
current version: 201511190000
Usage:
    get sig: tls_licence_tools.exe gen pri_key_file sig_file sdkappid identifier
    get sig e.g.: tls_licence_tools.exe gen ec_key.pem sig 1400001052 xiaojun
    verify sig: tls_licence_tools.exe verify pub_key_file sig_file sdkappid identifier
    verify sig e.g.: tls_licence_tools.exe verify public.pem sig 1400001052 xiaojun
```

This can be illustrated by the following screenshot:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126142633_17041.png)

The output is actually parameter template and example.

Execute a command similar to the following to generate sig:

```
tls_licence_tools.exe gen ec_key.pem sig 1400001052 xiaojun
```

Descriptions of the parameters:

```
tls_licence_tools gen <path to private key file> <path for storing the sig> <sdkappid> <user ID>
```

Execute a command similar to the following to verify sig:

```
tls_licence_tools.exe verify public.pem sig 1400001052 xiaojun
```

Descriptions of the parameters:

```
tls_licence_tools verify <path to public key file> <path for storing the sig> <sdkappid> <user ID>
```

This can be illustrated by the following screenshot:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126142725_41827.png)

Content of the sig file is as follows:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124221_16540.png)

The following screenshot shows the verification of sig:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126142759_94666.png)

The descriptions of parameters in parameter template are as follows:

```
gen and verify represent the commands for generating sig and verifying sig, respectively.
pri_key_file: The path to private key file
pub_key_file: The path to public key file
sig_file: The path to sig file. For generation of sig, the sig is written to this file; for verification of sig, the sig is read from this file.
sdkappid: The sdkappid assigned on the page when creating App.
identifier: User ID.
```

> Note: The generated sig is valid for 180 days, and developers need to generate a new sig before the sig expires.

### 3.2 C++ APIs

In the following example, we use VS2012 to show how to use C++ APIs on Windows.

First, include tls_signature.h under directory include\tls_sig_api. Header file contains two APIs: tls_gen_signature_ex2, which is used to generate sig, and tls_check_signature_ex2, which is used to verify sig. For more information about parameters and returned values, please see header file tls_signature.h.

Then link the static libraries. The directories under lib directory are as follows:

├── jni
├── jsoncpp
├── libsigcheck
├── openssl
├── tls_sig_api
└── zlib

The static libraries to be linked are libeay.lib and libtlsignature.lib under directories jsoncpp.lib and openssl, as well as zlibstat.lib under directory zlib. Typical compilation configuration is as follows:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124457_90952.png)

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124511_24769.png)

**Note**

If your program uses multiple threads to call the TLS backend APIs, call the following APIs respectively when initializing and ending the program:

```
int multi_thread_setup(void);
void multi_thread_cleanup(void);
```

### 3.3 Java APIs

Currently, Java APIs are implemented with jni. The file tls_sigcheck.class under Java directory is compiled from tls_sigcheck.java. In case of any jdk compatibility issue, developer can re-compile the file by using the following command:

```
javac -encoding utf-8 tls_sigcheck.java
```

Please note that the API package path is com.tls.sigcheck. Typically, it is organized in the same way as the demo of Java version under example directory:

├── com
│   └── tls
│       └── sigcheck
│           └── tls_sigcheck.class
├── Demo.class
├── Demo.java
├── ec_key.pem
├── public.pem
└── README

It was mentioned earlier that Java APIs are implemented with jni, therefore Demo.java calls the statement that references "dll", which can be modified by developer based on the actual path for storing jnisigcheck.dll. jnisigcheck.dll pre-complied in the binary package is placed under directory lib/jni. For more information on how to use demo, please refer to example/java/README. This can be illustrated by the following screenshot:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013124617_41874.png)

The execution results is as follows:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126142954_16596.png)

**Multi-thread** If usersig is generated on a multi-thread basis in Java code, please see [here](http://bbs.qcloud.com/thread-22323-1-1.html).

### 3.4 Java native APIs

Java native APIs are dependent on five jar packages. Under the directory tls_sig_api/java_native/lib:

├── bcpkix-jdk15on-152.jar
├── bcprov-jdk15on-152.jar
├── commons-codec-1.10.jar
├── gson-2.3.1.jar
├── json.jar
└── tls_signature.jar

**Note**

For the public and private keys [downloaded](/doc/product/269/下载公私钥) from console, the public key content is assigned to the parameter publicBase64Key in the API, and the private key content to the parameter `privateBase64Key`.

### 3.5 C# APIs

The APIs are implemented by calling dll (lib\libsigcheck\sigcheck.dll) in an unhosted mode. For more information on the parameters and returned values for C-style APIs, please see header file include\sigcheck.h. The APIs are converted as follows:

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

dllpath.DllPath is the path to dll. For more information, please see example\cs\csdemo.cs.
For more information on how to use demo, please see example\cs\README. This can be illustrated by the following screenshot:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013132403_75795.png)

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013132415_34994.png)

![](//avc.qcloud.com/wiki2.0/im/imgs/20151013132427_96968.png)

The execution result is as follows:

![](//avc.qcloud.com/wiki2.0/im/imgs/20151126143241_19273.png)

> Note: If Any CPU platform is selected, 32-bit dll needs to be loaded by default.


### 3.6 PHP APIs

PHP can be implemented by simply calling the command line tool bin/signature.exe to generate sig, as show below:


```
function signature($identifier, $sdkappid, $private_key_path)
{
    # An absolute path is required. This can vary with developers.
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
Developers should pay attention to the path for executing the command. In case of any error, try to print out the content of "command" variable to locate the error.

### 3.7 PHP native APIs
Both source code package and binary package come with the file php/TLSSig.php, which contains the APIs for generating sig (genSig) and for verifying sig (verifySig). Please note that PHP environment needs openssl extension, otherwise an error will occur while using the APIs. In addition, only PHP 5.3 and above are supported.

If the above PHP implementation does not meet the requirement, for example, in a case where Red Hat operating system (fedora, centos and rel, etc.) is used, you can refer to [here](http://bbs.qcloud.com/thread-22519-1-1.html) for another implementation independent of openssl and system.

## 4. APIs of Other Platforms
- javascript http://bbs.qcloud.com/thread-17311-1-1.html
- python http://bbs.qcloud.com/thread-14366-1-1.html
- golang http://bbs.qcloud.com/thread-21826-1-1.html

## 5. Download TLS Backend APIs
Click [here](http://share.weiyun.com/2b3abe0e3f185c440cf455647455f661) to download.

## 6 Contact Us

For more information, please [click here](http://bbs.qcloud.com/thread-8287-1-1.html) . You can also contact TLS Account Support via QQ (3268519604) or email (tls_assistant@tencent.com) to seek more support.



