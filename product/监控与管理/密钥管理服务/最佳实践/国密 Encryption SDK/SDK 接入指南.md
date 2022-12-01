国密 Encryption SDK 目前支持 **Linux** 和 **Windows** 系统的 C 语言、 Go 语言、Python2 和 Python3 语言。
其中 Go 语言 SDK，底层使用 C 语言来实现，上层通过 cgo 封装后，提供接口供 Go 语言调用；而 Python 语言 SDK，底层也是使用 C 语言来实现，上层通过 ctypes 封装后，提供接口供 Python 语言调用。

本文档以 C 语言作为代码示例，介绍如何接入使用国密 Encryption SDK，其他语言可以参考SDK包中具体的示例代码。

## 环境依赖
- Linux 系统支持情况，已经在下述平台验证：

| 系统版本                            | 位数 | 支持情况 |
| ----------------------------------- | ---- | -------- |
| Tencent Linux release 2.4（Final）  | 64   | 支持     |
| CentOS 8.2                          | 64   | 支持     |
| CentOS 8.0                          | 64   | 支持     |
| CentOS 7.8                          | 64   | 支持     |
| CentOS 7.7                          | 64   | 支持     |
| CentOS 7.6                          | 64   | 支持     |
| CentOS 7.5                          | 64   | 支持     |
| CentOS 7.4                          | 64   | 支持     |
| CentOS 7.3                          | 64   | 支持     |
| CentOS 7.2                          | 64   | 支持     |
| CentOS 6.9                          | 64   | 支持     |
| CentOS 6.8                          | 64   | 支持     |
| Debian 9.0                          | 64   | 支持     |
| Ubuntu Server 20.04.1 LTS           | 64   | 支持     |
| Ubuntu Server 18.04.1 LTS           | 64   | 支持     |
| Ubuntu Server 16.04.1 LTS           | 64   | 支持     |
| Ubuntu Server 14.04.1 LTS           | 64   | 支持     |
| CoreOS 1745.5.0                     | 64   | 支持     |
| Debian 10.2                         | 64   | 支持     |
| Debian 8.2                          | 64   | 支持     |
| openSUSE Leap 15.1                  | 64   | 支持     |
| openSUSE 42.3                       | 64   | 支持     |
| SUSE Linux Enterprise Server 12 SP3 | 64   | 支持     |

>! Linux开发环境仅支持 glibc 2.12 及其以上版本

- Windows 系统支持情况，已经在下述平台验证：

| 系统版本                                     | 位数 | 支持情况 |
| -------------------------------------------- | ---- | -------- |
| Windows Server 2019 数据中心版 64位 中文版   | 64   | 支持     |
| Windows Server 2016 数据中心版 64位中文版    | 64   | 支持     |
| Windows Server 2012 R2 数据中心版 64位中文版 | 64   | 支持     |

- SDK 基于 OpenSSL1.1.1 改造。

## 接入指引

### 步骤1：开通 KMS 旗舰版
国密 Encryption SDK 仅适用于密钥管理系统旗舰版，开通 KMS 旗舰版，详情请参见 [购买方式](https://cloud.tencent.com/document/product/573/18809)。

<span id="test2"></span>
### 步骤2：创建用户主密钥
登录 [密钥管理系统控制台](https://console.cloud.tencent.com/kms2)，创建用户主密钥，并保证其状态为已启用。具体操作详情请参见 [创建密钥](https://cloud.tencent.com/document/product/573/8875)。
>?为了容灾互备，建议设置至少2个可用区的用户主密钥 CMK，国密 Encryption SDK 最多支持设置5个用户主密钥 CMK （调用原生接口可忽略）。
>
<span id="test"></span>
### 步骤3：下载 SDK
进入 [Encryption SDK 页面]( https://console.cloud.tencent.com/kms2/sdk )，单击操作栏【下载】，在弹窗中选择 SDK 语言版本，单击【确定】后成功下载。

### 步骤4：在代码中引用加密 SDK
1. 加密 SDK 依赖 curl，如果没有，请提前安装，各不同操作系统的安装命令如下：
  - **Ubuntu**
  ```
	sudo apt-get install libcurl4-openssl-dev
  ```
  - **CentOS**
  ```
    yum install libcurl-devel
  ```
2. 将下载的 tar 包解压到本地，进入 src 目录。
3. 编辑 setenv.sh，配置环境变量。setenv.sh 包含的操作指令如下：
```
 export LD_LIBRARY_PATH=../lib:../lib/proto
 export OPENSSL_ENGINES=../lib/engines-1.1
```
4. 环境变量配置完成后保存，执行source ./setenv.sh，使配置生效。
5. 修改 `src`路径下的 `demo_kms_pro.c` 和 `demo_original.c`文件。国密 Encryption SDK 支持基于 KMS 的密钥保护（`demo_kms_pro.c`）和原生加密（`demo_original.c`）的两种加密方式，两种模式的差异请参见 [接口文档](https://cloud.tencent.com/document/product/573/49527)，用户根据需要修改其中一个即可，参数替换如下：
     - 使用主账号登录[ API 密钥管理控制台 ](https://console.cloud.tencent.com/cam/capi)获取您的 secretId 和 secretKey，并替换为文件中对应的 "replace-with-real-secretId"、"replace-with-real-secretKey" 字符串。
     - 将 [步骤2](#test2) 创建的主密钥 ID 替换文件中的 "replace-with-realkeyid" 字符串。
6. 编译 `src`路径下的 `make` 文件。
7. 运行可执行文件。
>!使用正确的 secretId、secretKey 和主密钥 ID ，Demo 才可以正常运行。

## C SDK KMS 示例 

### 加解密函数
- **InitSdk**：初始化函数，用于检验用户是否已开通 KMS 旗舰版服务。
- **InitKeyManager**：用户主密钥初始化函数。
- **NewMasterKey**：设定主 CMK，在调用加解密函数时，会优先使用主 CMK，建议设置和 SDK 运行环境相同区域的 CMK 以减少延时。当主 CMK 不可用时，会使用 AddMasterKey 函数设定的备用CMK。
- **AddMasterKey**：设定备用的 CMK，备用 CMK 建议设定在不同区域，其备用 CMK 与 NewMasterKey 中设定的密钥形成 CMK 密钥列表，目的是为了容灾互备，以防首要主密钥无法使用时，可以使用密钥列表中的其他密钥。
- **Encrypt**：加密函数。
- **Decrypt**：解密函数。

以上函数详细的参数说明请参见 [C SDK 接口文档](https://cloud.tencent.com/document/product/573/49506)。

>?
> 1. 示例代码中，CBCEnAndDeTest 函数包含加密、解密的调用，其中采用的算法是 **SM4_CBC_128**。
> 2. 原生加密方法包含 SM2、SM3 及 SM4，详细的函数及参数说明请参见 [步骤3](#test) 下载的 SDK 头文件 kms_enc_sdk.h。

### 示例代码
KMS 密钥保护方式接口调用示例如下：
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

        unsigned char encryptionContext[1024];
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
        char domainName[128];

        memset(plaintext,0,sizeof(plaintext));
        memset(region,0,sizeof(region));
        memset(masterKeys,0,sizeof(masterKeys));
        memset(domainName,0,sizeof(domainName));
        
        struct KeyManager keymanager;

        strcpy(region,"ap-guangzhou");
        strcpy(domainName,"kms.tencentcloudapi.com");
        strcpy(keymanager.secretId,"replace-with-real-secretId");
        strcpy(keymanager.secretKey,"replace-with-real-secretKey");
        strcpy(plaintext,"abcdefg123456789abcdefg123456789abcdefg");

        i_ret = InitSdk(region,keymanager.secretId,keymanager.secretKey,domainName);
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
