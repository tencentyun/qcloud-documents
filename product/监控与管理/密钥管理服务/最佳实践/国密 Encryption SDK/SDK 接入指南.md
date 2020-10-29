国密 Encryption SDK 目前支持 **Linux** 系统的 C 语言和 Go 语言。其中 Go 语言 SDK，底层使用 C 来实现，上层通过 cgo 封装后，提供接口供 Go 语言调用。本文档以 C 语言作为代码示例，介绍如何接入使用国密 Encryption SDK，其他语言可以参考 SDK 包中具体的示例代码。

## 环境依赖
- 开发环境的 glibc 版本需要在版本 2.12 及其以上。
- Linux 系统支持情况，已经在下述平台验证


| 系统版本                           | 位数 | 支持情况 |
| ---------------------------------- | ---- | -------- |
| Tencent Linux release 2.4（Final） | 64   | 支持     |
| CentOS 8.0                         | 64   | 支持     |
| CentOS 7.8                         | 64   | 支持     |
| CentOS 7.5                         | 64   | 支持     |
| CentOS 7.4                         | 64   | 支持     |
| CentOS 7.3                         | 64   | 支持     |
| CentOS 7.2                         | 64   | 支持     |
| CentOS 6.9                         | 64   | 支持     |
| CentOS 6.9                         | 32   | 不支持   |
| CentOS 6.8                         | 64   | 支持     |
| CentOS 6.5                         | 64   | 支持     |
| CoreOS 1745.5.0                    | 64   | 支持     |
| Debian 9.0                         | 64   | 支持     |
| Debian 8.2                         | 64   | 支持     |
| Debian 8.2                         | 32   | 不支持   |
| Debian 10.2                        | 64   | 支持     |
| FreeBSD 11.1                       | 64   | 不支持   |
| openSUSE 42.3                      | 64   | 支持     |
| Ubuntu Server 18.04.1 LTS          | 64   | 支持     |
| Ubuntu Server 16.04.1 LTS          | 64   | 支持     |
| Ubuntu Server 16.04.1 LTS          | 32   | 不支持   |
| Ubuntu Server 14.04.1 LTS          | 32   | 不支持   |

### 接入指引

#### 步骤一：开通KMS旗舰版

国密 Encryption SDK 仅适用于密钥管理系统旗舰版，请参考密钥管理系统[购买方式](https://cloud.tencent.com/document/product/573/18809)先开通 KMS 旗舰版。

#### 步骤二：创建用户主密钥

登录[密钥管理系统控制台](https://console.cloud.tencent.com/kms2)，创建用户主密钥，并保证其状态为已启用。操作详情请参见密钥管理系统[创建密钥](https://cloud.tencent.com/document/product/573/8875)。

说明：为了容灾互备，建议设置至少2个可用区的用户主密钥 CMK，国密 Encryption SDK 最多支持设置5个用户主密钥 CMK 。（调用原生接口可忽略）

#### 步骤三：下载 SDK

进入[Encryption SDK 页面]( https://console.cloud.tencent.com/kms2/sdk )，单击操作栏【下载】按钮，在弹窗中选择 SDK 语言版本，单击【确定】后成功下载。

#### 步骤四：在代码中引用加密SDK

1. 加密SDK依赖curl，如果没有，请提前安装，安装例子如下:

  - **ubuntu**
    sudo apt-get install libcurl4-openssl-dev
  - **centos**
    yum install libcurl-devel

2. 把下载的tar包解压到本地，进入src目录
3. 配置环境变量，参考setenv.sh，对应的操作指令如下：

* export LD_LIBRARY_PATH=../lib:../lib/proto

  - export OPENSSL_ENGINES=../lib/engines-1.1

4. 修改Demo文件demo_kms_pro.c和demo_original.c（Go语言版本 demo_original.go和demo_kms_pro.go）：

   * demo_kms_pro是基于KMS的密钥保护方式的Demo，demo_original是基于原生的加密方式的Demo，两种模式的差异请查看接口文档，用户根据需要修改其中一个即可。

   - 参数内容替换：
     - 在腾讯云平台中，需要查询到您的secretId和secretKey，然后替换文件中对应的"replace-with-real-secretId"、"replace-with-real-secretKey"字符串；
     - 将步骤二创建的主密钥ID替换文件中的"replace-with-realkeyid"字符串。

5. 编译Demo文件

   - C语言版本Demo直接执行make。
   - Go语言版本Demo可以运行go_make.sh进行编译，也可选择直接使用如下命令编译：
     - go build demo_original.go kms_enc_sdk.go
     - go build demo_kms_pro.go kms_enc_sdk.go
   - 编译完成后，生成可执行文件demo_kms_pro和demo_original。

6. 运行可执行文件

> 注意：使用正确的secretId、secretKey和主密钥ID的用例，Demo才可以正常运行。

### 代码示例 

#### 加解密 C 语言 SDK 的 KMS 加解密示例，其中示例代码所涉及的函数内容如下：

- **InitSdk** 是初始化函数，是用于检验用户是否开通KMS旗舰版服务。
- **InitKeyManager** 是用户主密钥的初始化函数。
- **NewMasterKey** 是设定主要的用户主密钥函数，即调用加解密操作时首要的密钥。
- **AddMasterKey** 函数是为了设定备用的用户主密钥，与NewMasterKey中设定的密钥形成CMK密钥列表，目的是为了灾备，以防首要主密钥无法使用时，可以使用密钥列表中的其他密钥。
- **Encrypt** 是加密函数
- **Decrypt** 是解密函数
  以上函数详细的参数内容请查阅 [**SDK接口文档**](新增的"旗舰版C接口文档") ，里面都有详细的对应说明。

> 注：
>
> 1. 示例代码中，CBCEnAndDeTest 函数包含了加密、解密的调用，其中采用的算法是 **SM4_CBC_128**
> 2. 原生加密方法包含 SM2、SM3 及 SM4，详细的函数及参数描述请查阅头文件 kms_enc_sdk.h

#### C 代码 KMS 的加解密示例

```
#include<stdio.h>
#include "kms_enc_sdk.h"

int CBCEnAndDeTest(struct KeyManager *p,unsigned char plaintext[],char masterKeys[])
{
        int i_ret = 0;
        unsigned char ch_orig[128];
        unsigned char ch_enheader[128];
        unsigned char ch_cipher[1024];
        size_t i_cipherlen = 0;

        unsigned char ch_dedata[1024];
        size_t i_dedatalen = 0;
        size_t sourceLength = 0;
				
        struct KeyManager keymanager;
        struct MsgHead enheader,deheader;

        char masterKeys[1024];
        memset(masterKeys,0,sizeof(masterKeys));

        memset(&enheader,0,sizeof(enheader));
        memset(&deheader,0,sizeof(deheader));

        memset(ch_orig,0,sizeof(ch_orig));
        strcpy(ch_orig,plaintext);
        sourceLength = strlen(ch_orig);

        memset(ch_dedata,0,sizeof(ch_dedata));
        memset(ch_cipher,0,sizeof(ch_cipher));
        memset(ch_dedata,0,sizeof(ch_dedata));

        unsigned char encryptionContext[2048];
        memset(encryptionContext,0,sizeof(encryptionContext));
        i_cipherlen = 0;
        i_dedatalen = 0;

        /*分片大小*/
        size_t blockSize = 0;
		/*选择加解密算法*/
        enum Algorithm al_en = SM4_CBC_128;

        strcpy(encryptionContext,"{\"name\":\"test\",\"date\":\"20200228\"}");

        NewMasterKey(masterKeys,"ap-guangzhou","replace-with-realkeyid");
        AddMasterKey(masterKeys,"ap-beijing","replace-with-realkeyid");

        /*初始化        可加密的消息数量设置为0即缓存不过期*/
        i_ret = InitKeyManager(&keymanager,masterKeys,0,0,0,p->secretId,p->secretKey);

        if ( 0 != i_ret )
        {
                printf("InitKeyManager error\n");
                return ( 0 );
        }
		
		/*ch_cipher 是加密后的密文内容 */
        i_ret = Encrypt(ch_orig,sourceLength,&keymanager,masterKeys,al_en,encryptionContext,blockSize,&enheader,ch_cipher,&i_cipherlen);
        if (i_ret == 0)
        {
                i_ret = Decrypt(ch_cipher,i_cipherlen,&keymanager,&deheader,ch_dedata,&i_dedatalen);
                if ( 0 == i_ret )
                {
                        printf("ch_dedata[%s] i_dedatalen[%d]\n",ch_dedata,i_dedatalen);
                }
                else
                {
                        printf("Decrypt is err!!!!!!!![%d]\n\n",i_ret);
                }
        }
        else
        {
                printf("Encrypt is err!!!!!!!![%d]\n\n",i_ret);
        }
        return ( 0 );
}

int main()
{
        int i_ret = 0;
        unsigned char plaintext[128];
        char region[128];
        char masterKeys[1024];

        memset(plaintext,0,sizeof(plaintext));
        memset(region,0,sizeof(region));
        memset(masterKeys,0,sizeof(masterKeys));
        
        struct KeyManager keymanager;

        strcpy(region,"ap-guangzhou");
        strcpy(keymanager.secretId,"replace-with-real-secretId");
        strcpy(keymanager.secretKey,"replace-with-real-secretKey");
        strcpy(plaintext,"abcdefg123456789abcdefg123456789abcdefg");

        i_ret = InitSdk(region,keymanager.secretId,keymanager.secretKey);
        if ( 0 != i_ret )
        {
                printf("InitSdk error\n");
                return ( -1 );
        }

        NewMasterKey(masterKeys,"ap-guangzhou","replace-with-real-secretKey");
        AddMasterKey(masterKeys,"ap-beijing","replace-with-real-secretKey");
       
        CBCEnAndDeTest(&keymanager,plaintext,masterKeys);

        return ( 0 );
}
```
