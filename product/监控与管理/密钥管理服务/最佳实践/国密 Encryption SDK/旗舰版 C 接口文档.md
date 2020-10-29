国密 Encryption SDK 集成了 [**KMS**](https://cloud.tencent.com/document/product/573)，帮助用户解决密钥的生命周期管理问题，用户只需设置相关参数，调用加解密接口，便可实现本地、高效、稳定的国密加解密。

为了提供更好的服务，国密 Encryption SDK 支持基于 KMS 的密钥保护和原生加密的两种加密方式。
- 基于 KMS 的密钥保护方式：是指调用 KMS 平台生成加密密钥，由 KMS 提供密钥的全生命周期的管理，用户通过接口设置密钥的使用和替换策略，详情请参见 [InitKeyManager 接口](#test)。
- 原生的加密方式：是指用户自行创建加密密钥，传入接口进行加解密，密钥的整个生命周期由用户管理，用户需要自己保证密钥的安全。

出于安全和合规考虑，建议用户使用基于 KMS 的密钥保护方式。

## 前提条件
- 国密 Encryption SDK 仅适用于密钥管理系统旗舰版，开通 KMS 旗舰版，详情请参见 [购买方式](https://cloud.tencent.com/document/product/573/18809)。
- 用户需要确保本机支持 CPU 支持 SDK 指令集优化，执行以下命令进行验证：
```
cat /proc/cpuinfo|grep aes
cat /proc/cpuinfo|grep avx
```
若可以查询到内容，则说明机器支持指令集加速。

## SDK 特性

-  支持基于 SM4 的多种模式加解密，详情请参见 [算法列表](#test1)。
-  SDK 基于 CPU 指令集进行优化，提供高效的加解密。
-  SDK 采用信封加密方式，密文包含元数据信息，用户无需额处理密钥存储问题。关于信封加密，详情请参见  [**信封加密**](https://cloud.tencent.com/document/product/573/8791) 。
-  支持多地域容灾，对数据加密可指定多个地域主密钥，任意主密钥均可解密数据密钥，从而对数据进行解密。
-  密文数据格式可支持各语言间相互解析。
-  数据密钥具备缓存管理功能，用户通过接口参数指定数据密钥缓存的加密次数和使用时间，使用一次加密一个密钥的方式，可以提高加解密的安全性，使用缓存可以提升程序性能。
-  支持 EncryptionContext 作为辅助参数，以明文的方式存储，方便用户进行日志输出、对密文增加属性描述信息等。
-  支持基于 SM3-HMAC 的方式验证密文完整性，用户可通过加密算法设置。

## 初始化 SDK 接口 

#### InitSdk

- 功能描述：检验用户是否已开通 KMS 旗舰版服务。
- 参数说明：
<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="3">入参</td>
    <td>region</td>
	  <td>是</td>
    <td>char</td>	
      <td>CMK 地域信息字符串，详见产品支持的<a href="https://cloud.tencent.com/document/product/1038/33406">地域列表</a></td>
  </tr>
  <tr>
    <td>secretId</td>
	  <td>是</td>
    <td>char </td>		
		<td>云账户 API 密钥 ID</td>
  </tr>
  <tr>
    <td>secretKey</td>
	  <td>是</td>
    <td>char</td>			
		<td>云账户 API 密钥 Key</td>
  </tr>
 </table>
- 返回值：初始化成功返回0，否则返回相应的错误码，-15表示未开通KMS服务，-16表示需升级为KMS旗舰版。

>>!
>  - 需注意 SecretId 和 SecretKey 的保密存储：
>    腾讯云接口认证主要依靠 SecretID 和 SecretKey，SecretID 和 SecretKey 是用户的唯一认证凭证。业务系统需要该凭证调用腾讯云接口. 
>  - 需注意 SecretID 和 SecretKey 的权限控制：
>    建议使用子账号，根据业务需要进行接口授权的方式管控风险。

### KMS密钥保护方式接口说明：

#### NewMasterKey

- 功能描述：把用户首个主密钥加入主密钥信息列表。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="1">出入参</td>
    <td>masterKeys</td>
	  <td>是</td>
    <td>char *</td>	
		<td>主密钥信息列表，长度根据用户加入的密钥数量来确定，每个CMK占用的空间为Region和KeyId长度。</td>
  </tr>
  <tr>
	   <td rowspan="2">入参</td>
    <td>cmkRegion</td>
	  <td>是</td>
    <td>char *</td>		
		<td>主密钥（CMK）地域信息</td>
  </tr>
  <tr>
    <td>cmkKeyId</td>
	  <td>是</td>
    <td>char *</td>			
		<td>主密钥（CMK）的ID，从KMS控制台中查询</td>
  </tr>
 </table>


- 返回值：加入主密钥调用成功返回0，否则返回相应的错误码。

> 注意：用于加密的首个主密钥，在KMS平台中是处于**生效**的状态。

#### AddMasterKey

- 功能描述：加入备用的用户主密钥，目的是为了灾备，当首个主密钥无法使用时，会使用的备用密钥，最多支持加入4个。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="1">出入参</td>
    <td>masterKeys</td>
	  <td>是</td>
    <td>char *</td>	
		<td>主密钥信息列表，长度根据用户加入的密钥数量来确定，每个CMK占用的空间为Region和KeyId长度。</td>
  </tr>
  <tr>
    <td rowspan="2">入参</td>	
    <td>cmkRegion</td>
	  <td>是</td>
    <td>char *</td>		
		<td>主密钥（CMK）地域信息</td>
  </tr>
  <tr>
    <td>cmkKeyId</td>
	  <td>是</td>
    <td>char *</td>			
		<td>主密钥（CMK）的ID，从KMS控制台中查询</td>
  </tr>
 </table>


- 返回值：加入主密钥调用成功返回0，否则返回相应的错误码。

> 注意：请保证masterKeys留有足够的空间，否则可能产生内存错误。

<span id="test"></span>
#### InitKeyManager

- 功能描述：初始化KeyManager的结构体，KeyManager用来保存密钥管理相关参数，包含主密钥信息、密钥加密次数、密钥生效时间等，具体看后续参数。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="1">出入参</td>
    <td>keyManager</td>
	  <td>是</td>
    <td>struct of KeyManager *</td>	
		<td>KeyManager 结构体指针</td>
  </tr>
  <tr>
    <td rowspan="6">入参</td>	
    <td>masterKeys</td>
	  <td>是</td>
    <td>char *</td>		
		<td>主密钥（CMK）信息列表</td>
  </tr>
  <tr>
    <td>msgCount</td>
	  <td>是</td>
    <td>int</td>			
		<td>每个缓存DataKey可加密的消息数量，加密的数量达到后，会重新向KMS后台请求，生成新的DataKey，设置为0表示没有限制使用次数。</td>
  </tr>
  <tr>
    <td>enExpiretime</td>
	  <td>是</td>
    <td>int</td>			
		<td>加密使用的DataKey在缓存中的有效期，单位为秒。和消息数量一起生效，消息数量超过或者超时时间达到，都会触发DataKey的替换，0表示不过期。</td>
  </tr>
  <tr>
    <td>deExpiretime</td>
	  <td>是</td>
    <td>int</td>			
		<td>解密使用的DataKey缓存的有效期，单位为秒，0表示不过期。</td>
  </tr>
  <tr>
    <td>secretId</td>
	  <td>是</td>
    <td>char *</td>	
		<td>云账户API密钥ID</td>
  </tr>
  <tr>
    <td>secretKey</td>
	  <td>是</td>
    <td>char *</td>		
		<td>云账户API密钥Key</td>
  </tr>
  <tr>
</table>

- 返回值：初始化成功返回0，否则返回相应的错误码。

#### Encrypt

- 功能描述：使用kms平台创建的DataKey，进行本地数据加密。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="7">入参</td>
    <td>source</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>待加密的明文数据</td>
  </tr>
  <tr>
    <td>sourceLength</td>
	  <td>是</td>
    <td>size_t</td>		
		<td>待加密数据长度，单位 byte</td>
  </tr>
  <tr>
    <td>keyManager</td>
	  <td>是</td>
    <td>struct of KeyManager *</td>			
		<td>已经初始化的KeyManager结构体指针</td>
  </tr>
  <tr>
    <td>masterKeys</td>
	  <td>是</td>
    <td>char *</td>			
		<td>主密钥（CMK）信息列表</td>
  </tr>
  <tr>
    <td>algorithm</td>
	  <td>是</td>
    <td>enum</td>			
		<td>算法枚举值，参照后面算法列表</td>
  </tr>
  <tr>
    <td>encryptionContext</td>
	  <td>是</td>
    <td>char *</td>	
		<td>用于标识DataKey的辅助字段，key/value对的json字符串格式,最大支持2048字节。如：{"name":"test","date":"20200228"}</td>
  </tr>
  <tr>
    <td>blockSize</td>
	  <td>是</td>
    <td>size_t</td>		
		<td>0 表示加密时不分块加密，非0表示分块加密以及分块大小，单位 byte</td>
  </tr>
  <tr>
    <td rowspan="3">出参</td>
    <td>header</td>
	  <td>是</td>
    <td>struct of MsgHead *</td>		
    <td>头部数据结构体，用于返回本次加密的一些基本信息，具体请查看后续描述。</td>
  </tr>
  <tr>
    <td>cipher</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>加密后的密文内容</td>
  </tr>
  <tr>
    <td>cipherLength</td>
	  <td>是</td>
    <td>size_t</td>
    <td>密文长度，单位 byte</td>
  </tr>
</table>

- 返回值：加密成功返回0，否则返回相应的错误码。

> 注意：加密后的数据，会加入DataKey相关信息，只能使用KMS密钥保护方式的接口进行解密。
>

<span id="test1"></span>
#### 支持的加密算法列表：

| 枚举值                     | 数值 | 说明                            |
| -------------------------- | ---- | ------------------------------- |
| SM4_CBC_128_WITH_SIGNATURE | 1    | 使用SM3HAC签名的SM4 CBC模式     |
| SM4_CBC_128                | 2    | 不使用签名的SM4 CBC模式加密     |
| SM4_GCM_128_WITH_SIGNATURE | 3    | 使用SM3HAC签名的SM4 GCM模式     |
| SM4_GCM_128                | 4    | 不使用签名的SM4 GCM模式加密算法 |
| SM4_CTR_128_WITH_SIGNATURE | 5    | 使用SM3HAC签名的SM4 CTR模式     |
| SM4_CTR_128                | 6    | 不使用签名的SM4 CTR模式         |
| SM4_ECB_128_WITH_SIGNATURE | 7    | 使用SM3HAC签名的SM4 ECB模式     |
| SM4_ECB_128                | 8    | 不使用签名的SM4 ECB模式         |

#### EncryptedDataKey结构体说明：

| 参数名称  | 类型   | 说明                                 |
| --------- | ------ | ------------------------------------ |
| cmkRegion | char * | 主密钥（CMK）地域信息                |
| cmkKeyId  | char * | 主密钥（CMK）的ID，从KMS控制台中查询 |
| dataKey   | char * | 存储的datakey对应的密文              |

#### MsgHead结构体说明：

| 参数名称          | 类型                      | 说明                                                         |
| ----------------- | ------------------------- | ------------------------------------------------------------ |
| algorithm         | enum                      | 算法枚举值，参照上面的加密算法列表                           |
| encryptionContext | char *                    | 用于标识DataKey的辅助字段，key/value对的json字符串格式,最大支持2048字节。如：{"name":"test","date":"20200228"} |
| dataKeyNum        | int                       | 使用的加密后DataKey数量，和有效的主密钥(CMK)数量相关，由各个地域的主密钥加密产生 |
| dataKey           | Array of EncryptedDataKey | DataKey的信息列表，包含的字段参照上面的EncryptedDataKey结构体说明 |
| blockType         | enum                      | 密文加密分块的枚举值，用于标识该密文是否被分块，参照下面的BlockType枚举值说明 |
| blockLength       | int                       | 分块的长度                                                   |

#### BlockType结构体说明：

| 枚举值        | 数值 | 说明             |
| ------------- | ---- | ---------------- |
| WITHOUT_BLOCK | 1    | 密文加密未做分块 |
| WITH_BLOCK    | 2    | 密文加密开设分块 |

#### Decrypt

- 功能描述：方法用于解密密文，得到明文数据。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="3">入参</td>
    <td>source</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>加密后的数据</td>
  </tr>
  <tr>
    <td>sourceLength</td>
	  <td>是</td>
    <td>size_t</td>		
		<td>加密后的数据长度，单位 byte</td>
  </tr>
  <tr>
    <td>keyManager</td>
	  <td>是</td>
    <td>struct of KeyManager *</td>			
		<td>已经初始化的KeyManager结构体指针</td>
  </tr>  <tr>
    <td rowspan="3">出参</td>
    <td>header</td>
	  <td>是</td>
    <td>struct of MsgHead *</td>		
    <td>头部数据结构体，用于返回本次解密的一些基本信息，具体请看关于结构体的描述</td>
  </tr>
  <tr>
    <td>plainText</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>解密后的明文数据</td>
  </tr>
  <tr>
    <td>plainTextLength</td>
	  <td>是</td>
    <td>size_t</td>
    <td>明文长度，单位 byte</td>
  </tr>
</table>

- 返回值：解密成功则返回0，否则返回相应的错误码。

#### KMS加密方式接口调用示例：

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

### 原生加密方式的接口说明：

原生加密方式对应的服务也需要升级为旗舰版，与KMS密钥保护方式相比，原生加密方式需要用户自己生成加密密钥进行加解密，由用户保证密钥的安全性。出于安全与合规的考虑，建议用户使用KMS密钥保护方式。

其中CTR模式加密没有填充，其他的模式加密采用PKCS#7标准进行填充。


#### Sm2Sign

- 功能描述：使用SM2算法进行签名。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="4">入参</td>
    <td>pubKey</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>未编码的公钥内容，数据长度固定为64字节。</td>
  </tr>
  <tr>
    <td>priKey</td>
	  <td>是</td>
    <td>unsigned char *</td>		
		<td>未编码的私钥内容，数据长度固定为32字节。</td>
  </tr>  
		<td>msg</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>原文数据</td>
  </tr>
  <tr>
    <td>msgLen</td>
	  <td>是</td>
    <td>int</td>		
		<td>原文数据的长度，单位 byte</td>
  </tr>  
	<tr>
    <td rowspan="2">出参</td>
    <td>sig</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>生成的签名</td>
  </tr>
  <tr>
    <td>sigLen</td>
	  <td>是</td>
    <td>int *</td>
    <td>签名数据的长度，单位 byte</td>
  </tr>
</table>

- 返回值：数据签名成功返回0，否则返回相应的错误码。

> 注意：公钥和私钥的长度为固定长度，用户如果输入长度不一致的数据，可能导致内存访问异常。

#### Sm2Verify

- 功能描述：使用SM2算法进行验签。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="3">入参</td>
    <td>pubKey</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>未编码的公钥内容，数据长度固定为64字节</td>
  </tr>
  <tr>
    <td>sig</td>
	  <td>是</td>
    <td>unsigned char *</td>		
		<td>签名后的数据</td>
  </tr>
	  <tr>
    <td>sigLen</td>
	  <td>是</td>
    <td>int</td>	
		<td>签名后的数据长度，单位 byte</td>
  </tr>
  <tr>
    <td rowspan="2">出参</td>
    <td>msg</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>原文数据</td>
  </tr>
  <tr>
    <td>msgLen</td>
	  <td>是</td>
    <td>int *</td>
    <td>原文数据的长度，单位 byte</td>
  </tr>
</table>

- 返回值：验签成功返回0，否则返回相应的错误码。

> 注意：公钥长度为固定长度64字节，用户如果输入长度不一致的数据，可能导致内存访问异常。

#### Sm2Encrypt

- 功能描述：使用SM2算法进行加密。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="3">入参</td>
    <td>pubKey</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>未编码的公钥内容，数据长度为64字节</td>
  </tr>
  <tr>
    <td>source</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>SM2加密的源数据</td>
   </tr>
   <tr>
    <td>sourceLength</td>
	  <td>是</td>
    <td>int</td>		
		<td>源数据长度，单位 byte</td>
   </tr>
  <tr>
    <td rowspan="2">出参</td>	
    <td>cipherText</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>密文数据</td>
   </tr>
   <tr>
    <td>cipherLength</td>
	  <td>是</td>
    <td>int *</td>		
		<td>密文数据长度，单位 byte</td>
   </tr>	 
 </table>

- 返回值：加密成功返回0，否则返回相应的错误码。

> 注意：SM2加密适用于小数据的场景，不建议加密超过256k的数据。

#### Sm2Decrypt

- 功能描述：使用SM2算法进行解密。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="3">入参</td>
    <td>priKey</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>未编码的私钥内容，数据长度固定为32字节</td>
  </tr>
  <tr>
    <td>source</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>加密后的数据</td>
   </tr>
   <tr>
    <td>sourceLength</td>
	  <td>是</td>
    <td>int</td>		
		<td>加密后的数据长度，单位 byte</td>
   </tr>
  <tr>
	   <td rowspan="2">出参</td>
    <td>plainText</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>明文数据</td>
   </tr>
   <tr>
    <td>plainTextLength</td>
	<td>是</td>
    <td>int *</td>		
	<td>明文数据长度，单位 byte</td>
   </tr>	 
 </table>

- 返回值：解密成功返回0，否则返回相应的错误码。

#### Sm3Hmac

- 功能描述：使用SM3哈希运算Hmac计算。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="4">入参</td>
    <td>data</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>原文数据</td>
  </tr>
  <tr>
    <td>dataLen</td>
	  <td>是</td>
    <td>int</td>		
		<td>原文数据的长度，单位 byte</td>
  </tr>
	  <tr>
    <td>hmacKey</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>计算Hmac的密钥内容</td>
  </tr>
  <tr>
    <td>keyLen</td>
	  <td>是</td>
    <td>int</td>		
		<td>计算Hmac的密钥长度，单位 byte</td>
  </tr>
  <tr>
    <td rowspan="2">出参</td>
    <td>hmac</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>生成的Hmac值</td>
  </tr>
  <tr>
    <td>hmacLen</td>
	  <td>是</td>
    <td>int *</td>
    <td>Hmac长度，单位 byte</td>
  </tr>
</table>

- 返回值：接口调用成功返回0，否则返回相应的错误码。

#### Sm4CbcEncrypt/Sm4CtrEncrypt

- 功能描述：使用SM4加密算法CBC、CTR模式的加密。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="4">入参</td>
    <td>source</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>原文数据</td>
  </tr>
  <tr>
    <td>sourceLength</td>
	  <td>是</td>
    <td>int</td>		
		<td>原文数据的长度，单位 byte</td>
  </tr>
	  <tr>
    <td>key</td>
	  <td>是</td>
    <td>int char *</td>	
		<td>用户自定义的SM4密钥，长度固定为128位(16字节)</td>
  </tr>
  <tr>
    <td>iv</td>
	  <td>是</td>
    <td>unsigned char *</td>		
		<td>初始化向量，固定为128位(16字节)</td>
  </tr>
  <tr>
    <td rowspan="2">出参</td>
    <td>cipherText</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>密文数据</td>
  </tr>
  <tr>
    <td>cipherLength</td>
	  <td>是</td>
    <td>int *</td>
    <td>密文数据长度，单位 byte</td>
  </tr>
</table>


- 返回值：加密成功返回0，否则返回相应的错误码。

#### Sm4CbcDecrypt/Sm4CtrDecrypt

- 功能描述：用于SM4加密算法CBC、CTR模式下的解密。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="4">入参</td>
    <td>source</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>加密后的数据</td>
  </tr>
  <tr>
    <td>sourceLength</td>
	  <td>是</td>
    <td>int</td>		
		<td>加密后的数据长度，单位 byte</td>
  </tr>
	  <tr>
    <td>key</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>用户自定义的SM4密钥，长度固定为128位(16字节)</td>
  </tr>
  <tr>
    <td>iv</td>
	  <td>是</td>
    <td>unsigned char *</td>		
		<td>初始化向量，固定为128位(16字节)</td>
  </tr>
  <tr>
    <td rowspan="2">出参</td>
    <td>plainText</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>解密后的明文数据</td>
  </tr>
  <tr>
    <td>plainTextLength</td>
	  <td>是</td>
    <td>int *</td>
    <td>解密后的明文数据长度，单位 byte</td>
  </tr>
</table>


- 返回值：解密成功返回0，否则返回相应的错误码。

#### Sm4EcbEncrypt

- 功能描述：方法是用于SM4加密算法ECB模式下的加密。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="3">入参</td>
    <td>source</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>原文数据</td>
  </tr>
  <tr>
    <td>sourceLength</td>
	  <td>是</td>
    <td>int</td>		
		<td>原文数据的长度，单位 byte</td>
  </tr>
	  <tr>
    <td>key</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>用户自定义的SM4密钥，长度固定为128位(16字节)</td>
  </tr>
  <tr>
    <td rowspan="2">出参</td>
    <td>cipherText</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>密文数据</td>
  </tr>
  <tr>
    <td>cipherLength</td>
	  <td>是</td>
    <td>int *</td>
    <td>密文数据长度，单位 byte</td>
  </tr>
</table>

- 返回值：加密成功返回0，否则返回相应的错误码。

#### Sm4EcbDecrypt

- 功能描述：使用SM4加密算法ECB模式下的解密。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="3">入参</td>
    <td>source</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>加密后的数据</td>
  </tr>
  <tr>
    <td>sourceLength</td>
	  <td>是</td>
    <td>int</td>		
		<td>加密后的数据长度，单位 byte</td>
  </tr>
	  <tr>
    <td>key</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>用户自定义的SM4密钥，长度固定为128位(16字节)</td>
  </tr>
  <tr>
    <td rowspan="2">出参</td>
    <td>plainText</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>解密后的明文数据</td>
  </tr>
  <tr>
    <td>plainTextLength</td>
	  <td>是</td>
    <td>int *</td>
    <td>解密后的明文数据长度，单位 byte</td>
  </tr>
</table>

- 返回值：解密成功返回0，否则返回相应的错误码。

#### Sm4GcmEncrypt

- 功能描述：用于SM4加密算法GCM模式下的加密。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="9">入参</td>
    <td>source</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>原文数据</td>
  </tr>
  <tr>
    <td>sourceLength</td>
	  <td>是</td>
    <td>int</td>		
		<td>原文数据的长度，单位 byte</td>
  </tr>
	<tr>
    <td>key</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>用户自定义的SM4密钥，长度固定为128位(16字节)</td>
  </tr>
	<tr>
    <td>iv</td>
    <td>是</td>
    <td>unsigned char *</td>  
    <td>初始化向量，固定为128位(16字节)</td>
  </tr>
  <tr>
    <td>ivLen</td>
    <td>是</td>
    <td>int</td>    
    <td>向量内容的长度，单位 byte</td>
  </tr>
    <tr>
    <td>add</td>
    <td>是</td>
    <td>unsigned char *</td>  
    <td>附加校验信息</td>
  </tr>
	<tr>
    <td>addLen</td>
    <td>是</td>
    <td>int</td>  
    <td>附加校验信息长度，单位 byte</td>
  </tr>
  <tr>
    <td>tag</td>
    <td>是</td>
    <td>unsigned char *</td>    
    <td>tag值，即校验码</td>
  </tr>
    <tr>
    <td>tagLen</td>
    <td>是</td>
    <td>int</td>  
    <td>校验码的长度，单位 byte</td>
  </tr>
  <tr>
    <td rowspan="2">出参</td>
    <td>cipherText</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>密文数据</td>
  </tr>
  <tr>
    <td>cipherLength</td>
	  <td>是</td>
    <td>int *</td>
    <td>密文数据长度，单位 byte</td>
  </tr>
</table>


- 返回值：加密成功返回0，否则返回相应的错误码。

#### Sm4GcmDecrypt

- 功能描述：使用SM4加密算法GCM模式下的解密。
- 参数说明：

<table>
  <tr>
    <th>属性</th>
    <th>参数名称</th>
		<th>必选</th>
		<th>类型</th>
    <th>描述</th>
  </tr>
  <tr>
    <td rowspan="9">入参</td>
    <td>source</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>加密后的数据</td>
  </tr>
  <tr>
    <td>sourceLength</td>
	  <td>是</td>
    <td>int</td>		
		<td>加密后的数据长度，单位 byte</td>
  </tr>
	<tr>
    <td>key</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>用户自定义的SM4密钥，长度固定为128位(16字节)</td>
  </tr>
	<tr>
    <td>iv</td>
    <td>是</td>
    <td>unsigned char *</td>  
    <td>初始化向量，固定为128位(16字节)</td>
  </tr>
  <tr>
    <td>ivLen</td>
    <td>是</td>
    <td>int</td>    
    <td>初始化向量内容的长度，单位 byte</td>
  </tr>
    <tr>
    <td>add</td>
    <td>是</td>
    <td>unsigned char *</td>  
    <td>附加校验信息</td>
  </tr>
	<tr>
    <td>addLen</td>
    <td>是</td>
    <td>int</td>  
    <td>附加校验信息的长度，单位 byte</td>
  </tr>
  <tr>
    <td>tag</td>
    <td>是</td>
    <td>unsigned char *</td>    
    <td>tag值，即校验码</td>
  </tr>
    <tr>
    <td>tagLen</td>
    <td>是</td>
    <td>int</td>  
    <td>校验码的长度，单位 byte</td>
  </tr>
  <tr>
    <td rowspan="2">出参</td>
    <td>plainText</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>解密后的明文数据</td>
  </tr>
  <tr>
    <td>plainTextLength</td>
	  <td>是</td>
    <td>int *</td>
    <td>解密后的明文数据长度，单位 byte</td>
  </tr>
</table>


- 返回值：解密成功返回0，否则返回相应的错误码。

### 原生加密方式的接口调用示例：

```
#include<stdio.h>
#include "kms_enc_sdk.h"

int Sm4CbcTest()
{
        int i_ret = 0;

        unsigned char ch_orig[1024];
        int i_orig = 0;
        unsigned char ch_en[1024];
        int i_en = 0;
        unsigned char ch_de[1024];
        int i_de = 0;

        memset(ch_orig,0,sizeof(ch_orig));
        memset(ch_en,0,sizeof(ch_en));
        memset(ch_de,0,sizeof(ch_de));

        unsigned char key[16] = {
                0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
                0xfe, 0xdc, 0xba, 0x98, 0x76, 0x54, 0x32, 0x10};

        unsigned char iv[16] = {
                0x01, 0x23, 0x45, 0x67, 0x89, 0xab, 0xcd, 0xef,
                0xfe, 0xdc, 0xba, 0x98, 0x76, 0x54, 0x32, 0x10};

        strcpy(ch_orig,"this Sm4CbcTest");
        i_orig = strlen(ch_orig);

        i_ret = Sm4CbcEncrypt(ch_orig,i_orig,ch_en,&i_en,key,iv);
        if ( 0 != i_ret )
        {
                printf("Sm4CbcEncrypt error\n");
                return ( -1 );
        }

        i_ret = Sm4CbcDecrypt(ch_en,i_en,ch_de,&i_de,key,iv);
        if ( 0 != i_ret )
        {
                printf("Sm4CbcDecrypt error\n");
                return ( -1 );
        }
        printf("Sm4CbcDecrypt data is [%s]\n",ch_de);

        return ( 0 );
}

int main()
{
	int i_ret = 0;
	
	char region[128];
	char secretId[128];
	char secretKey[128];
	
	memset(region,0,sizeof(region));
	memset(secretId,0,sizeof(secretId));
	memset(secretKey,0,sizeof(secretKey));
	
	strcpy(region,"ap-guangzhou");
	strcpy(secretId,"replace-with-real-secretId");
	strcpy(secretKey,"replace-with-real-secretKey");
	
	i_ret = InitSdk(region,secretId,secretKey);
	if ( i_ret != 0 )
	{
		printf("InitSdk error\n");
		return ( -1 );
	}

   Sm4CbcTest();

return ( 0 );	
}

```

#### 错误码

| 返回值 | 枚举值                   | 说明                       |
| ------ | ------------------------ | -------------------------- |
| 0      | ES_OK                    | 正常返回                   |
| -1     | ES_ERROR                 | 一般错误                   |
| -2     | ES_ENCRYPT_SOURCE_EMPTY  | 加密的原文为空             |
| -3     | ES_NO_CMKEY              | 未设置主密钥               |
| -4     | ES_ALGRITHM_ERR          | 算法不支持                 |
| -5     | ES_GENERATE_DATAKEY_ERR  | 产生DataKey错误            |
| -6     | ES_ENCRYPT_DATA_ERR      | 加密DataKey错误            |
| -7     | ES_MARSHAL_PROTOBUF_ERR  | 序列化ProtoBuf出错         |
| -8     | ES_CIPHER_TEXT_TOO_SHORT | 密文数据太短               |
| -9     | ES_GET_PROTO_ERR         | 获取ProtoBuf报文出错       |
| -10    | ES_PARSE_PROTO_ERR       | 解析ProtoBuf报文出错       |
| -11    | ES_DECRYPT_DATAKEY_ERR   | 解密DataKey错误            |
| -12    | ES_SET_DATAKEY_ERR       | 设置DataKey错误            |
| -13    | ES_DIGEST_INVALIDATE     | 签名不合法，导致校验不通过 |
| -14    | ES_MEMORY_ERR            | 内存错误                   |
| -15    | ES_KMSSERVICE_ERR        | KMS服务未开通              |
| -16    | ES_USEREDITION_ERR       | 未升级为KMS旗舰版          |
