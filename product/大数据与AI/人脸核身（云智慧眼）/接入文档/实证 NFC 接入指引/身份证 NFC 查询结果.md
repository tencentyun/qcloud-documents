## 合作伙伴服务端验证结果
此方式用于：合作伙伴服务端生成签名，并调用实证 NFC 服务端查询结果，鉴权完成后返回结果（服务端上送 orderNo 和 appId 查询）。
### 合作方后台生成签名
#### 准备步骤
前置条件：请合作方确保 SIGN ticket 已经正常获取，获取方式见 [获取 SIGN ticket](https://cloud.tencent.com/document/product/1007/57613)。
合作方为实证 NFC 识别服务生成签名，需要具有以下参数：

| 参数 | 说明 | 来源 |
|---------|---------|---------|
| appId| 腾讯服务分配的 Appid| 参考 [获取 WBappid](https://cloud.tencent.com/document/product/1007/49634) 指引在人脸核身控制台内申请 | 
| orderNo| 订单号，本次 NFC 识别合作伙伴上送的订单号，唯一标识，字母/数字组成的字符串| 合作方自行分配| 
| version| 默认值：1.0.0| -| 
| api ticket| 合作伙伴服务端缓存的   tikcet，注意是 SIGN 类型| 获取方式见 [获取 SIGN ticket](https://cloud.tencent.com/document/product/1007/57613)| 
| nonceStr | 32位随机字符串，字母和数字| 合作方自行生成| 

#### 基本步骤
1. 生成一个 32 位的随机字符串 nonceStr（其为字母和数字，登录时也要用到）。
2. 将 appId、orderNo、version 连同 ticket、nonceStr 共五个参数的值进行字典序排序。
3. 将排序后的所有参数字符串拼接成一个字符串。
4. 将排序后的字符串进行 SHA1 编码，编码后的 40 位字符串作为签名（sign）。

>! 签名算法可参考 [签名算法说明](https://cloud.tencent.com/document/product/1007/57640)。

## 实证 NFC 识别结果查询接口
### 请求
请求 URL：`https://miniprogram-kyc.tencentcloudapi.com/api/v2/nfcpaas/getIdcardNfcResult?orderNo=xxx`
>! 为方便查询耗时，该请求 url 后面请拼接 orderNo 订单号参数。
>
请求方法：POST。
报文格式：`Content-Type: application/json`。
请求参数：

| 参数 | 说明 | 类型 |    长度（字节） | 是否必填 |
|---------|---------|---------|---------|---------|
| appId | 腾讯服务分配的 Appid | 字符串 | 腾讯服务分配 | 是| 
| orderNo | 订单号，合作方订单的唯一标识，字母/数字组成的字符串| 字符串| 32| 是| 
| nonce| 随机数| 字符串| 32| 是| 
| version| 版本号，默认值：1.0.0| 字符串| 20| 是| 
| sign| 签名值，使用本页第一步生成的签名| 字符串| 40| 是| 
| reqId| 本次实证 NFC读取唯一标识| 字符串| 40| 是| 
|getPhoto   |是否需要获取 NFC 识别的证件图片文件，值为1则返回图片 |字符串    |1| 否|

### 响应
响应参数：

| 参数 | 类型 | 说明 |
|---------|---------|---------|
| code| String| 0：成功；非0：失败；详情请参见 [SaaS 服务错误码](https://cloud.tencent.com/document/product/1007/47912)| 
| msg| String| 请求结果描述| 
| result | NfcQueryRsp| nfc 查询加密结果集| 
| transactionTime| String| 交易时间戳| 

NfcQueryRsp 响应参数结构：

| 参数 | 类型 | 说明 |
|---------|---------|---------|
| code| String| 0：成功；非0：失败；详情请参见[ SaaS 服务错误码](https://cloud.tencent.com/document/product/1007/47912)| 
| msg| String| 请求结果描述| 
| nfcEnResult| String| 加密的 nfc 识别结果| 
| transactionTime| String| 交易时间戳| 

nfcEnResult 响应参数结构内容：

| 参数 | 类型 | 说明 |居民身份证|港澳回乡证|
|---------|---------|---------|---------|---------|
| orderNo| string| 订单编号| &#10003;| &#10003;|
| reqId| string| 本次实证 NFC 读取唯一标识| &#10003;| &#10003;|
| name| string| 姓名| &#10003;| &#10003;|
|enName|string|英文名|-|&#10003;|
| sex| string| 性别| &#10003;| &#10003;|
| nation| string| 民族| &#10003;| -|
| birth| string| 出生日期| &#10003;| &#10003;|
| address| string| 地址| &#10003;| -|
| idcard| string| 证件号| &#10003;| &#10003;|
| validDateBegin| string| 证件的有效期起始时间| &#10003;| -|
| validDateEnd| string| 证件的有效期结束时间| &#10003;| &#10003;|
| signingOrganization| string| 发证机关| &#10003;| -|
| frontPhoto| Base 64 string| 证件正面照| &#10003;|-|
| backPhoto| Base 64 string| 证件反面照| &#10003;| -|
| portraitPhoto| Base 64 string| 证件人像照| &#10003;| &#10003;|

```
{
    "code": "0"，
    "msg": "请求成功"，
    "result": {
"bizSeqNo": "1607280FD01141000000000000009003"，
"nfcEnResult":SgoeKZt5nIHQmiLluNxxsdfasdfasdfasdfa1uOswIiebhOPe0SgoeKZt5nIHQmiLluN123123MdsdfKsmiLluN123123MdfsIHQmiLluN123123MdsdfKdf1uOswIiebhOPe0SgoeKZt5nIH"
}，
    "bizSeqNo": "1607280FD01141000000000000009003"，    
    "transactionTime": "20160728075617"
}
```

>! 
>- 照片均为 base64 位编码，其中照片解码后格式一般为 JPG。
>- 返回报文加密nfcEnResult部分，解密后为响应参数。

解密示例：
第一步先 base64解码 nfcEnResult 字段，第二步通过 SM4国密算法根据下发的处理后密钥(主力方式：将十六进制密钥转为字节数组)解密第一步解码结果，第三步将第二步结果 json 解析为 nfcEnResult 解密结构内容。
解密代码示例(JAVA)：

```
import com.google.common.io.BaseEncoding;
import org.bouncycastle.jce.provider.BouncyCastleProvider;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;
import java.security.Key;
import java.security.Security;
import java.util.Random;
/**
 *     项目所依赖的类：
 *      List utils = [
 *      "commons-io:commons-io:2.7"，
 *      "com.google.guava:guava:16.0.1"，
 *      "org.bouncycastle:bcprov-jdk15to18:1.66"，
 *      ]
 *
 * @date 2022-03-04-10:27
 */
public class SM4 {
    private static final String ENCODING = "UTF-8";
    public static final String ALGORITHM_NAME = "SM4";
    // 加密算法/分组加密模式/分组填充方式
    // PKCS5Padding-以8个字节为一组进行分组加密
    // 定义分组加密模式使用：PKCS5Padding
    public static final String ALGORITHM_NAME_ECB_PADDING = "SM4/ECB/PKCS5Padding";
    /**
     * 生成 SM4 Cipher
     * @return
     * @throws Exception
     */
    protected static Cipher generateCipher(int mode，byte[] keyData) throws Exception {
        Cipher cipher = Cipher.getInstance(ALGORITHM_NAME_ECB_PADDING，BouncyCastleProvider.PROVIDER_NAME);
        Key sm4Key = new SecretKeySpec(keyData，ALGORITHM_NAME);
        cipher.init(mode，sm4Key);
        return cipher;
    }
    /**
     * 加密模式之
     * @param key  密钥
     * @param data 待加密的内容
     * @return
     * @throws Exception
     * @explain
     */
    public static byte[] encrypt(byte[] key，byte[] data) throws Exception {
        Cipher cipher = generateCipher(Cipher.ENCRYPT_MODE，key);
        return cipher.doFinal(data);
    }
    /**
     * sm4解密
     * @param
     * @param cipherText 16进制的加密字符串（忽略大小写）
     * @return 解密后的字符串
     * @throws Exception
     * @explain 解密模式：采用ECB
     */
    public static String decrypt(String key，String cipherText) throws Exception {
        // 用于接收解密后的字符串
        String decryptStr = "";
        byte[] keyData = key.getBytes();
        byte[] cipherData = cipherText.getBytes();
        // 解密
        byte[] srcData = decrypt(keyData，cipherData);
        // byte[]-->String
        decryptStr = new String(srcData，ENCODING);
        return decryptStr;
    }
    /**
     * 解密
     * @param key
     * @param cipherText
     * @return 解密后的内容  byte[]
     * @throws Exception
     * @explain
     */
    public static byte[] decrypt(byte[] key，byte[] cipherText) throws Exception {
        Cipher cipher = generateCipher(Cipher.DECRYPT_MODE，key);
        return cipher.doFinal(cipherText);
    }
    /**
     * 将byte转换为16进制字符串
     * @param src
     * @return
     */
    public static String byteToHexString(byte[] src) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < src.length; i++) {
            int v = src[i] & 0xff;
            String hv = Integer.toHexString(v);
            if (hv.length() < 2) {
                sb.append("0");
            }
            sb.append(hv);
        }
        return sb.toString();
    }
    /**
     * 将16进制字符串转换为字节数组
     * @param str 16进制字符串
     * @return byte[]
     */
    public static byte[] hexStringToBytes(String str) {
        byte[] bytes;
        bytes = new byte[str.length() / 2];
        for (int i = 0; i < bytes.length; i++) {
            bytes[i] = (byte) Integer.parseInt(str.substring(2 * i，2 * i + 2)，16);
        }
        return bytes;
    }
    /**
     * 接入方拿到key（即控制台申请的 NFC 秘钥） 先可以跑通下面的案例，并认真阅读 1，2，3，4
     * 项目所依赖的类：
     * List utils = [
     * "commons-io:commons-io:2.7"，
     * "com.google.guava:guava:16.0.1"，
     * "org.bouncycastle:bcprov-jdk15to18:1.66"，
     * ]
     * @param args
     * @throws Exception
     */
    public static void main(String[] args) throws Exception {
        // 1. 系统初始话的时候，需要注入所使用的 provider
        Security.addProvider(new BouncyCastleProvider());
        // 2.收到key后，先从hex转成byte[]，加解密就是用byte[]输入
        byte[] key = hexStringToBytes("7F26724F72D48EBA5AD3848B30B81122");
        // 3.测试的文本内容
        String src = "168，FM973 全角半角测试，你好，大家好，你好，美丽人生Ｅｆｇｋｙｍｋ";
        byte[] enSrc = encrypt(key，src.getBytes());
        String base64EnStr = BaseEncoding.base64().encode(enSrc);
        System.out.println("base64 en:" + base64EnStr);
        // 4.解密，用户只需要执行解密即可(先base64 转成byte[] 然后执行解密)
        byte[] decSrc = decrypt(key，BaseEncoding.base64().decode(base64EnStr));
        System.out.println("===== base64 dec:" + new String(decSrc，ENCODING));
    }
}
```

