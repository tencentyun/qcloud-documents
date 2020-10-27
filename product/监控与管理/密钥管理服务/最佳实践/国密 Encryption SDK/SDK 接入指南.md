本文档以 Linux 系统和 C 语言为例，介绍如何在 KMS 中接入国密 Encryption SDK，其他语言类似。

## 环境依赖

- 编译器
  -  支持 GCC 4.8 或以上版本。
  -  目前仅支持 Linux 环境，不支持 Windows 环境。
- 头文件引用 `CipherSuite_Sdk.h`，库文件引用 `libCipherSuite_Sdk.so`。

## 操作步骤

### 步骤一：开通KMS旗舰版

国密 Encryption SDK 仅适用于密钥管理系统旗舰版，开通 KMS 旗舰版，详情请参见 [购买方式](https://cloud.tencent.com/document/product/573/18809)。

### 步骤二：创建用户主密钥

登录 [密钥管理系统控制台](https://console.cloud.tencent.com/kms2)，创建用户主密钥，并保证其状态为已启用。操作详情请参见 [创建密钥](https://cloud.tencent.com/document/product/573/8875)。
>?为了容灾互备，建议设置至少2个可用区的用户主密钥 CMK ，国密 Encryption SDK 最多支持设置5个用户主密钥 CMK （调用原生接口可忽略） 。

### 步骤三：下载 SDK

进入 [Encryption SDK 页面]()，单击操作栏【下载】按钮，在弹窗中选择 SDK 语言版本，本示例选用的是 C 语言版本，单击【确定】后成功下载。

### 步骤四：数据加解密

C SDK KMS 加解密示例代码所涉及的函数内容如下：
- **InitSdk**：初始化函数，用于检验用户是否已开通 KMS 旗舰版服务。
- **InitKeyManager** ：用户主密钥的初始化函数。
- **NewMasterKey** ：设定主要用户的主密钥函数，即调用加解密操作时首要的密钥。
- **AddMasterKey** ：设定备用的用户主密钥，与 NewMasterKey 中设定的密钥形成 CMK 密钥列表，目的是做容灾互备，以防首要主密钥无法使用时，可以使用密钥列表中的其他密钥。
- **Encrypt** ：加密函数。
- **Decrypt** ：解密函数。

以上函数详细的参数说明，请参见 [**SDK 接口文档**](http://cloud.tencent.com) 。

>?
> 1. 示例代码中，CBCEnAndDeTest 函数包含加密、解密的调用，其中采用的算法是 **SM4_CBC_128**。
> 2. 原生加密方法包含 SM2、SM3 和 SM4，详细的函数及参数描述，请参见头文件 CipherSuite_Sdk.h。？？？链接

C 代码 KMS 的加解密示例如下：
```
#include<stdio.h>
#include "CipherSuite_Sdk.h"

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

        NewMasterKey(masterKeys,"ap-guangzhou","replace-with-****keyid");
        AddMasterKey(masterKeys,"ap-beijing","replace-with-****keyid");

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
        strcpy(keymanager.secretId,"replace-with-real-****etId");
        strcpy(keymanager.secretKey,"replace-with-real-****etKey");
        strcpy(plaintext,"abcdef****456789abcdefg123456789****efg");

        i_ret = InitSdk(region,keymanager.secretId,keymanager.secretKey);
        if ( 0 != i_ret )
        {
                printf("InitSdk error\n");
                return ( -1 );
        }

        NewMasterKey(masterKeys,"ap-guangzhou","replace-with-real-****etKey");
        AddMasterKey(masterKeys,"ap-beijing","replace-with-real-****etKey");
       
        CBCEnAndDeTest(&keymanager,plaintext,masterKeys);

        return ( 0 );
}
```


