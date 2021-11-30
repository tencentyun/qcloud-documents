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


## 初始化 SDK 接口 

### InitSdk

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
    <td rowspan="4">入参</td>
    <td>region</td>
	  <td>是</td>
    <td>char *</td>	
      <td>CMK 地域信息字符串，详见产品支持的 <a href="https://cloud.tencent.com/document/product/573/34406#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8">地域列表</a></td>
  </tr>
  <tr>
    <td>secretId</td>
	  <td>是</td>
    <td>char *</td>		
		<td>云账户 API 密钥 ID</td>
  </tr>
  <tr>
    <td>secretKey</td>
	  <td>是</td>
    <td>char *</td>			
		<td>云账户 API 密钥 Key</td>
  </tr>
  <tr>
    <td>domainName</td>
	  <td>是</td>
    <td>char *</td>			
		<td>域名信息字符串</td>
  </tr>
 </table>


- 返回值：初始化成功返回0，否则返回相应的 [错误码](#test2)。

>!
> - 需注意 SecretId 和 SecretKey 的保密存储：腾讯云接口认证主要依靠 SecretID 和 SecretKey，SecretID 和 SecretKey 是用户的唯一认证凭证。业务系统需要该凭证调用腾讯云接口。
> - 需注意 SecretId 和 SecretKey 的权限控制：建议使用子账号，根据业务需要进行接口授权的方式管控风险。
> - 需注意 domainName 的设置：如果domainName入参为""，则从环境变量TENCENT_SDK_DOMAIN中读取值，反之，则以入参为准。

## KMS 密钥保护方式接口说明
KMS 密钥保护方式基于 KMS 密钥管理平台实现，由 KMS 提供密钥的全生命周期管理，其中接口包括主密钥信息列表的新建添加、KeyManager 的初始化、加解密接口等。

### NewMasterKey

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
    <td rowspan="1">出参</td>
    <td>masterKeys</td>
	  <td>是</td>
    <td>char *</td>	
		<td>主密钥信息列表，长度根据用户加入的密钥数量来确定，每个CMK 占用的空间为 region 和 KeyId 长度。</td>
  </tr>
  <tr>
	   <td rowspan="2">入参</td>
    <td>cmkRegion</td>
	  <td>是</td>
    <td>char *</td>		
		<td>主密钥 CMK 地域信息</td>
  </tr>
  <tr>
    <td>cmkKeyId</td>
	  <td>是</td>
    <td>char *</td>			
		<td>主密钥 CMK 的 ID，从 KMS 控制台中查询</td>
  </tr>
 </table>
- 返回值：加入主密钥调用成功返回0，否则返回相应的 [错误码](#test2)。

>!用于加密的首个主密钥，在 KMS 平台中是处于**生效**的状态。

### AddMasterKey

- 功能描述：加入备用的用户主密钥，目的是为了灾备，当首个主密钥无法使用时，将会使用的备用密钥，最多支持加入4个。
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
    <td rowspan="1">出参</td>
    <td>masterKeys</td>
	  <td>是</td>
    <td>char *</td>	
		<td>主密钥信息列表，长度根据用户加入的密钥数量来确定，每个 CMK 占用的空间为 region 和 KeyId 长度。</td>
  </tr>
  <tr>
    <td rowspan="2">入参</td>	
    <td>cmkRegion</td>
	  <td>是</td>
    <td>char *</td>		
		<td>主密钥 CMK 地域信息</td>
  </tr>
  <tr>
    <td>cmkKeyId</td>
	  <td>是</td>
    <td>char *</td>			
		<td>主密钥 CMK 的 ID，从 KMS 控制台中查询</td>
  </tr>
 </table>
- 返回值：加入主密钥调用成功返回0，否则返回相应的 [错误码](#test2)。

>!请保证 masterKeys 至少保留有512字节的空间，否则可能会产生内存错误。

<span id="test"></span>
### InitKeyManager
- 功能描述：初始化 KeyManager 的结构体，KeyManager 用来保存密钥管理相关参数，包含主密钥信息、密钥加密次数、密钥生效时间等。
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
    <td rowspan="1">出参</td>
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
		<td>主密钥 CMK 信息列表</td>
  </tr>
  <tr>
    <td>msgCount</td>
	  <td>是</td>
    <td>int</td>			
		<td>每个缓存 DataKey 可加密的消息数量，加密的数量达到后，会重新向 KMS 后台请求，生成新的 DataKey，设置为0表示没有限制使用次数</td>
  </tr>
  <tr>
    <td>enExpiretime</td>
	  <td>是</td>
    <td>int</td>			
		<td>加密使用的 DataKey 在缓存中的有效期，单位为秒。和消息数量一起生效，消息数量超过或者超时时间达到，都会触发 DataKey 的替换，0表示不过期</td>
  </tr>
  <tr>
    <td>deExpiretime</td>
	  <td>是</td>
    <td>int</td>			
		<td>解密使用的 DataKey 缓存的有效期，单位为秒，0表示不过期</td>
  </tr>
  <tr>
    <td>secretId</td>
	  <td>是</td>
    <td>char *</td>	
		<td>云账户 API 密钥 ID</td>
  </tr>
  <tr>
    <td>secretKey</td>
	  <td>是</td>
    <td>char *</td>		
		<td>云账户 API 密钥 Key</td>
  </tr>
</table>
- 返回值：初始化成功返回0，否则返回相应的 [错误码](#test2)。

### Encrypt

- 功能描述：使用 KMS 平台创建的 DataKey，进行本地数据加密。
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
		<td>已经初始化的 KeyManager 结构体指针</td>
  </tr>
  <tr>
    <td>masterKeys</td>
	  <td>是</td>
    <td>char *</td>			
		<td>主密钥 CMK 信息列表</td>
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
		<td>用于标识 DataKey 的辅助字段，key/value 对的 JSON 字符串格式，最大支持1024字节。例如{"name":"test","date":"20200228"}</td>
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
    <td>头部数据结构体，用于返回本次加密的一些基本信息，具体请查看后续描述</td>
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
- 返回值：加密成功返回0，否则返回相应的 [错误码](#test2)。

>!加密后的数据，会加入DataKey相关信息，只能使用KMS密钥保护方式的接口进行解密。
>
<span id="test1"></span>
### 支持的加密算法列表

| 枚举值                     | 数值 | 说明                            |
| -------------------------- | ---- | ------------------------------- |
| SM4_CBC_128_WITH_SIGNATURE | 1    | 使用 SM3 HAC 签名的 SM4 CBC 模式     |
| SM4_CBC_128                | 2    | 不使用签名的 SM4 CBC 模式加密     |
| SM4_GCM_128_WITH_SIGNATURE | 3    | 使用 SM3 HAC 签名的 SM4 GCM 模式     |
| SM4_GCM_128                | 4    | 不使用签名的 SM4 GCM 模式加密算法 |
| SM4_CTR_128_WITH_SIGNATURE | 5    | 使用 SM3 HAC 签名的 SM4 CTR 模式     |
| SM4_CTR_128                | 6    | 不使用签名的 SM4 CTR 模式         |
| SM4_ECB_128_WITH_SIGNATURE | 7    | 使用 SM3 HAC 签名的 SM4 ECB 模式     |
| SM4_ECB_128                | 8    | 不使用签名的 SM4 ECB 模式         |

<span id="test3"></span>
### EncryptedDataKey 结构体说明

| 参数名称  | 类型   | 说明                                 |
| --------- | ------ | ------------------------------------ |
| cmkRegion | char * | 主密钥 CMK 地域信息                |
| cmkKeyId  | char * | 主密钥 CMK 的 ID，从 KMS 控制台中查询 |
| dataKey   | char * | 存储的 DataKey 对应的密文              |

### MsgHead结构体说明

| 参数名称          | 类型                      | 说明                                                         |
| ----------------- | ------------------------- | ------------------------------------------------------------ |
| algorithm         | enum                      | 算法枚举值，请参见 [加密算法列表](#test1)                           |
| encryptionContext | char *                    | 用于标识 DataKey 的辅助字段，key/value 对的 JSON 字符串格式，最大支持1024字节。例如{"name":"test","date":"20200228"} |
| dataKeyNum        | int                       | 使用的加密后 DataKey 数量和有效的主密钥 CMK 数量相关，由各个地域的主密钥加密产生 |
| dataKey           | Array of EncryptedDataKey | DataKey 的信息列表，详情请参见 [EncryptedDataKey 结构体说明](#test3) |
| blockType         | enum                      | 密文加密分块的枚举值，用于标识该密文是否被分块，详情请参见 [BlockType 结构体说明](#test4) |
| blockLength       | int                       | 分块的长度                                                   |

<span id="test4"></span>
### BlockType 结构体说明

| 枚举值        | 数值 | 说明             |
| ------------- | ---- | ---------------- |
| WITHOUT_BLOCK | 1    | 密文加密未做分块 |
| WITH_BLOCK    | 2    | 密文加密开设分块 |

### Decrypt

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
		<td>已经初始化的 KeyManager 结构体指针</td>
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
- 返回值：解密成功则返回0，否则返回相应的 [错误码](#test2)。

### KMS 加密方式接口调用示例
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

        NewMasterKey(masterKeys,"ap-guangzhou","replace-with-realkeyid");
        AddMasterKey(masterKeys,"ap-beijing","replace-with-realkeyid");
       
        CBCEnAndDeTest(&keymanager,plaintext,masterKeys);

        return ( 0 );
}

```

## 原生加密方式的接口说明

原生加密方式对应的服务也需要升级为 KMS 旗舰版，与 KMS 密钥保护方式相比，原生加密方式需要用户本身生成加密密钥进行加解密，由用户保证密钥的安全性。出于安全与合规的考虑，建议用户使用 KMS 密钥保护方式。
>?其中 CTR 模式加密没有填充，其他的模式加密采用 PKCS#7 标准进行填充。

### Sm2GetKey

- 功能描述：使用SM2算法生成密钥对。
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
    <td rowspan="2">出参</td>	
    <td>pubKey</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>公钥内容，长度为64字节</td>
   </tr>
   <tr>
    <td>priKey</td>
	  <td>是</td>
    <td>unsigned char *</td>		
		<td>私钥内容，长度为32字节</td>
   </tr>	 
 </table>


- 返回值：密钥对生成成功返回0，否则返回相应的错误码。

### Sm2Sign

- 功能描述：使用 SM2 算法进行签名。
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
- 返回值：数据签名成功返回0，否则返回相应的 [错误码](#test2)。

>!公钥和私钥的长度为固定长度，用户如果输入长度不一致的数据，可能导致内存访问异常。

### Sm2Verify

- 功能描述：使用 SM2 算法进行验签。
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
- 返回值：验签成功返回0，否则返回相应的 [错误码](#test2)。

>!公钥长度为固定长度64字节，用户如果输入长度不一致的数据，可能导致内存访问异常。

### Sm2PemChangeToPubkey

- 功能描述：对pem格式的公钥内容进行转换。
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
    <td rowspan="1">入参</td>
    <td>pemPubKeyInfo</td>
	  <td>是</td>
    <td>unsigned char *</td>		
		<td>pem格式的公钥信息</td>
  </tr>
	<tr>
    <td rowspan="1">出参</td>
    <td>pubKey</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>转换后的公钥信息</td>
  </tr>
</table>

- 返回值：转换成功返回0，否则返回相应的错误码。

### HashForSM3WithSM2

- 功能描述：使用 **Sm2GetKey** 接口生成的公钥，并基于SM3算法生成信息摘要。
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
    <td rowspan="5">入参</td>
		<td>msg</td>
	  <td>是</td>
    <td>unsigned char *</td>	
		<td>原文数据</td>
  </tr>
  <tr>
    <td>msgLen</td>
	  <td>是</td>
    <td>int</td>		
		<td>原文数据的长度</td>
  </tr>
	<tr>
    <td>pubKey</td>
	  <td>是</td>
    <td>unsigned char *</td>		
		<td>公钥内容，数据长度固定为64字节</td>
  </tr> 
  <tr>
    <td>id</td>
	  <td>是</td>
    <td>unsigned char *</td>		
		<td>id值</td>
  </tr>  
	<tr>
    <td>idLen</td>
	  <td>是</td>
    <td>int</td>		
		<td>id值的长度</td>
  </tr>
	<tr>
    <td rowspan="2">出参</td>
    <td>digest</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>生成的摘要</td>
  </tr>
  <tr>
    <td>digestLen</td>
	  <td>是</td>
    <td>int *</td>
    <td>摘要数据的长度</td>
  </tr>
</table>


- 返回值：生成摘要成功返回0，否则返回相应的错误码。

> 注意：公钥的长度为固定长度，用户如果输入长度不一致的数据，可能导致内存访问异常。

### Sm2SignWithDigest

- 功能描述：使用本地生成的消息摘要生成签名
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
		<td>公钥内容，数据长度固定为64字节</td>
  </tr>
	<tr>
    <td>priKey</td>
	  <td>是</td>
    <td>unsigned char *</td>		
		<td>私钥内容，数据长度固定为32字节</td>
  </tr> 
	<tr>
    <td>digest</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>摘要数据</td>
  </tr>
  <tr>
    <td>digestLen</td>
	  <td>是</td>
    <td>int </td>
    <td>摘要数据的长度</td>
  </tr>
	<tr>
    <td rowspan="2">出参</td>
    <td>sig</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>生成的签名值</td>
  </tr>
  <tr>
    <td>sigLen</td>
	  <td>是</td>
    <td>int *</td>
    <td>签名数据的长度</td>
  </tr>
</table>


- 返回值：生成签名成功返回0，否则返回相应的错误码。

> 注意：公钥和私钥的长度为固定长度，用户如果输入长度不一致的数据，可能导致内存访问异常。

### Sm2VerifyWithDigest

- 功能描述：通过生成的摘要内容进行验签。
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
    <td rowspan="5">入参</td> 
    <td>pubKey</td>
    <td>是</td>
    <td>unsigned char *</td>  
    <td>公钥内容，数据长度为64字节</td>
   </tr>
   <tr>
    <td>sig</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>签名内容</td>
  </tr>
  <tr>
    <td>sigLen</td>
	  <td>是</td>
    <td>int </td>
    <td>签名数据的长度</td>
  </tr> 
  <tr>
    <td>digest</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>摘要数据</td>
  </tr>
  <tr>
    <td>digestLen</td>
	  <td>是</td>
    <td>int </td>
    <td>摘要数据的长度</td>
  </tr>
 </table>


- 返回值：验签成功返回0，否则返回相应的错误码。

### Sm2Encrypt

- 功能描述：使用 SM2 算法进行加密。
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
		<td>SM2 加密的源数据</td>
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
- 返回值：加密成功返回0，否则返回相应的 [错误码](#test2)。

>!SM2 加密适用于小数据的场景，不建议加密超过256k的数据。

### Sm2Decrypt

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
- 返回值：解密成功返回0，否则返回相应的 [错误码](#test2)。

### Sm3Hmac

- 功能描述：使用 SM3 哈希运算 Hmac 计算。
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
		<td>计算 Hmac 的密钥内容</td>
  </tr>
  <tr>
    <td>keyLen</td>
	  <td>是</td>
    <td>int</td>		
		<td>计算 Hmac 的密钥长度，单位 byte</td>
  </tr>
  <tr>
    <td rowspan="2">出参</td>
    <td>hmac</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>生成的 Hmac 值</td>
  </tr>
  <tr>
    <td>hmacLen</td>
	  <td>是</td>
    <td>int *</td>
    <td>Hmac 长度，单位 byte</td>
  </tr>
</table>
- 返回值：接口调用成功返回0，否则返回相应的 [错误码](#test2)。

### Sm3Digest

- 功能描述：使用SM3生成摘要。
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
    <td rowspan="2">入参</td>
    <td>data</td>
	  <td>是</td>
    <td>unsigned char *</td>		
		<td>原文数据</td>
  </tr>
  <tr>
    <td>dataLen</td>
	  <td>是</td>
    <td>int </td>		
    <td>原文数据的长度</td>
  </tr>
	<tr>
    <td rowspan="2">出参</td>
    <td>digest</td>
	  <td>是</td>
    <td>unsigned char *</td>		
    <td>生成的摘要</td>
  </tr>
  <tr>
    <td>digestLen</td>
	  <td>是</td>
    <td>int </td>		
    <td>生成的摘要的长度</td>
  </tr>
</table>

### Sm4CbcEncrypt/Sm4CtrEncrypt

- 功能描述：使用 SM4 加密算法 CBC、CTR 模式的加密。
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
- 返回值：加密成功返回0，否则返回相应的 [错误码](#test2)。

### Sm4CbcDecrypt/Sm4CtrDecrypt

- 功能描述：用于 SM4 加密算法 CBC、CTR 模式下的解密。
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
- 返回值：解密成功返回0，否则返回相应的 [错误码](#test)。

### Sm4EcbEncrypt
- 功能描述：方法是用于 SM4 加密算法 ECB 模式下的加密。
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
- 返回值：加密成功返回0，否则返回相应的 [错误码](#test2)。

### Sm4EcbDecrypt

- 功能描述：使用 SM4 加密算法 ECB 模式下的解密。
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
- 返回值：解密成功返回0，否则返回相应的 [错误码](#test2)。

### Sm4GcmEncrypt

- 功能描述：用于 SM4 加密算法 GCM 模式下的加密。
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
- 返回值：加密成功返回0，否则返回相应的 [错误码](#test2)。

### Sm4GcmDecrypt

- 功能描述：使用 SM4 加密算法 GCM 模式下的解密。
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
- 返回值：解密成功返回0，否则返回相应的 [错误码](#test2)。

### 原生加密方式的接口调用示例
原生加密方式的接口调用示例代码如下：
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
        memset(domainName,0,sizeof(domainName));
        
        strcpy(region,"ap-guangzhou");
        strcpy(domainName,"kms.tencentcloudapi.com");
        strcpy(secretId,"replace-with-real-secretId");
        strcpy(secretKey,"replace-with-real-secretKey");
        
        i_ret = InitSdk(region,secretId,secretKey,domainName);
        if ( i_ret != 0 )
        {
                printf("InitSdk error\n");
                return ( -1 );
        }

        Sm4CbcTest();

        return ( 0 );	
}

```

<span id="test2"></span>
## 错误码

| 返回值 | 枚举值                   | 说明                       |
| ------ | ------------------------ | -------------------------- |
| 0      | ES_OK                    | 正常返回                   |
| -1     | ES_ERROR                 | 一般错误                   |
| -2     | ES_ENCRYPT_SOURCE_EMPTY  | 加密的原文为空             |
| -3     | ES_NO_CMKEY              | 未设置主密钥               |
| -4     | ES_ALGRITHM_ERR          | 算法不支持                 |
| -5     | ES_GENERATE_DATAKEY_ERR  | 产生 DataKey 错误            |
| -6     | ES_ENCRYPT_DATA_ERR      | 加密 DataKey 错误            |
| -7     | ES_MARSHAL_PROTOBUF_ERR  | 序列化 ProtoBuf 出错         |
| -8     | ES_CIPHER_TEXT_TOO_SHORT | 密文数据太短               |
| -9     | ES_GET_PROTO_ERR         | 获取 ProtoBuf 报文出错       |
| -10    | ES_PARSE_PROTO_ERR       | 解析 ProtoBuf 报文出错       |
| -11    | ES_DECRYPT_DATAKEY_ERR   | 解密 DataKey 错误            |
| -12    | ES_SET_DATAKEY_ERR       | 设置 DataKey 错误            |
| -13    | ES_DIGEST_INVALIDATE     | 签名不合法，导致校验不通过 |
| -14    | ES_MEMORY_ERR            | 内存错误                   |
| -15    | ES_KMSSERVICE_ERR        | KMS 服务未开通              |
| -16    | ES_USEREDITION_ERR       | 未升级为 KMS 旗舰版          |
