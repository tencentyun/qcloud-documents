## 简介

Java SDK 支持客户端加密，将文件加密后再进行上传，并在下载时进行解密，适用于存储敏感数据的客户。

客户端加密支持以下两种方式：
- KMS 服务托管密钥：用户只需提供 KMS 服务的用户主密钥 ID（即 CMK ID）给 SDK。使用这种方式需要用户开通 KMS 服务，更多 KMS 服务信息参见 [腾讯云密钥管理系统](https://cloud.tencent.com/document/product/573)。
- 用户自主保管密钥：用户提供和保管加密密钥，支持对称 AES 和非对称 RSA 加密。
>? 这里的对称和非对称只用于加密每次生成的随机密钥，对文件数据的加密始终使用 AES256 对称加密。
>

## 注意事项

- 用户数据在加密前不会上传到腾讯云对象存储（Cloud Object Storage，COS）。
- 客户端加密会消耗部分上传速度。
- 针对 SDK 内部的分块上传，将使用串行的方式进行上传。

## 准备事项

客户端加密内部使用 AES256 来对数据进行加密，默认 JDK6 - JDK8 早期的版本不支持256位加密。如果运行时会报出以下异常`java.security.InvalidKeyException: Illegal key size or default parameters`，那么我们需要补充 Oracle 的 JCE 无政策限制权限文件，将其部署在 JRE 的环境中。 请根据目前使用的 JDK 版本，分别下载对应的文件，将其解压后保存在 JAVA_HOME 下的`jre/lib/security`目录下。

- [JDK6 JCE 补充包](https://www.oracle.com/technetwork/java/javase/downloads/jce-6-download-429243.html)
- [JDK7 JCE 补充包](https://www.oracle.com/technetwork/java/javase/downloads/jce-7-download-432124.html)
- [JDK8 JCE 补充包](https://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html)

## 上传加密流程

1. 每次上传一个文件对象前，将随机生成一个对称加密密钥。随机生成的密钥通过 KMS 服务（或者用户的提供的密钥）进行加密，将加密后的结果 base64 编码存储在对象的元数据中。
2. 进行文件对象的上传，上传时在内存使用 AES256 算法加密。

## 下载解密流程

1. 获取文件元数据中加密必要的信息，Base64 解码后使用 KMS 服务（或者用户提供的密钥）进行解密，得到当时加密数据的密钥。
2. 使用密钥对下载输入流进行使用 AES256 解密，得到解密后的文件输入流。

## 请求示例

#### 示例1
使用腾讯云 KMS 服务加密，创建加密客户端示例，完整的示例代码请参见 [KMS 加密客户端加密完整示例](https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/demo/KMSEncryptionClientDemo.java)。

[//]: # (.cssg-snippet-put-object-cse-c-kms)

```java
// 初始化用户身份信息(secretId, secretKey)
// SECRETID和SECRETKEY请登录访问管理控制台进行查看和管理
String secretId = "SECRETID";
String secretKey = "SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
// 设置存储桶地域，COS 地域的简称请参照 https://www..com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("COS_REGION"));
// 为防止请求头部被篡改导致的数据无法解密，强烈建议只使用 https 协议发起请求。
clientConfig.setHttpProtocol(HttpProtocol.https);

// 用户 KMS 服务的主密钥
String cmk = "XXXXXXX";
//// 如果 KMS 服务的地域 与 COS 的存储桶地域不一致则需要单独设置。
//String kmsRegion = "XXXXX";

// 初始化 KMS 加密材料
KMSEncryptionMaterials encryptionMaterials = new KMSEncryptionMaterials(cmk);
// 使用AES/GCM模式，并将加密信息存储在文件元信息中.
CryptoConfiguration cryptoConf = new CryptoConfiguration(CryptoMode.AuthenticatedEncryption)
        .withStorageMode(CryptoStorageMode.ObjectMetadata);

//// 如果 KMS 服务的地域 与 COS 的地域不一致，则在加密配置里指定 KMS 服务的地域
//cryptoConf.setKmsRegion(kmsRegion);

//// 如果需要可以为 KMS 服务的 cmk 设置对应的描述信息。
// encryptionMaterials.addDescription("yourDescKey", "yourDescValue");

// 生成加密客户端 EncryptionClient, COSEncryptionClient 是 COSClient 的子类, 所有 COSClient 支持的接口他都支持。
// EncryptionClient 覆盖了 COSClient 上传下载逻辑，操作内部会执行加密操作，其他操作执行逻辑和 COSClient 一致
COSEncryptionClient cosEncryptionClient =
        new COSEncryptionClient(new COSStaticCredentialsProvider(cred),
                new KMSEncryptionMaterialsProvider(encryptionMaterials), clientConfig,
                cryptoConf);

// 上传文件
// 这里给出 putObject 的示例, 对于高级 API 上传，只用在生成 TransferManager 时传入 COSEncryptionClient 对象即可
String bucketName = "examplebucket-1250000000";
String key = "exampleobject";
File localFile = new File("localFilePath");
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
cosEncryptionClient.putObject(putObjectRequest);
cosEncryptionClient.shutdown();
```

#### 示例2
使用对称 AES256 加密每次生成的随机密钥示例，完整的示例代码请参见 [客户端对称密钥加密完整示例](https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/demo/SymmetricKeyEncryptionClientDemo.java)。

[//]: # (.cssg-snippet-put-object-cse-c-aes)

```java
// 初始化用户身份信息(secretId, secretKey)
// SECRETID和SECRETKEY请登录访问管理控制台进行查看和管理
String secretId = "SECRETID";
String secretKey = "SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
// 设置存储桶地域，COS 地域的简称请参照 https://www..com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("COS_REGION"));

// 生成对称密钥，您可以将其保存在文件中
KeyGenerator symKeyGenerator = KeyGenerator.getInstance("AES");
symKeyGenerator.init(256);
SecretKey symKey = symKeyGenerator.generateKey();

EncryptionMaterials encryptionMaterials = new EncryptionMaterials(symKey);
// 使用 AES/GCM 模式，并将加密信息存储在文件元数据中
CryptoConfiguration cryptoConf = new CryptoConfiguration(CryptoMode.AuthenticatedEncryption)
        .withStorageMode(CryptoStorageMode.ObjectMetadata);

// 生成加密客户端 EncryptionClient，COSEncryptionClient 是 COSClient 的子类, 所有 COSClient 支持的接口他都支持。
// EncryptionClient 覆盖了 COSClient 上传下载逻辑，操作内部会执行加密操作，其他操作执行逻辑和 COSClient 一致
COSEncryptionClient cosEncryptionClient =
        new COSEncryptionClient(new COSStaticCredentialsProvider(cred),
                new StaticEncryptionMaterialsProvider(encryptionMaterials), clientConfig,
                cryptoConf);

// 上传文件
// 这里给出 putObject 的示例, 对于高级 API 上传，只用在生成 TransferManager 时传入 COSEncryptionClient 对象即可
String bucketName = "examplebucket-1250000000";
String key = "exampleobject";
File localFile = new File(localFilePath);
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
cosEncryptionClient.putObject(putObjectRequest);
cosEncryptionClient.shutdown();
```

#### 示例3
使用非对称 RSA 加密每次生成的随机密钥示例，完整的示例代码请参见 [客户端非对称密钥加密完整示例](https://github.com/tencentyun/cos-java-sdk-v5/blob/master/src/main/java/com/qcloud/cos/demo/AsymmetricKeyEncryptionClientDemo.java)。

[//]: # (.cssg-snippet-put-object-cse-c-rsa)
```java
// 初始化用户身份信息(secretId, secretKey)
// SECRETID和SECRETKEY请登录访问管理控制台进行查看和管理
String secretId = "SECRETID";
String secretKey = "SECRETKEY";
COSCredentials cred = new BasicCOSCredentials(secretId, secretKey);
// 设置存储桶地域，COS 地域的简称请参照 https://cloud.tencent.com/document/product/436/6224
ClientConfig clientConfig = new ClientConfig(new Region("COS_REGION"));

// 生成非对称密钥
KeyPairGenerator keyGenerator = KeyPairGenerator.getInstance("RSA");
SecureRandom srand = new SecureRandom();
keyGenerator.initialize(1024, srand);
KeyPair asymKeyPair = keyGenerator.generateKeyPair();

EncryptionMaterials encryptionMaterials = new EncryptionMaterials(asymKeyPair);
// 使用 AES/GCM 模式，并将加密信息存储在文件元数据中
CryptoConfiguration cryptoConf = new CryptoConfiguration(CryptoMode.AuthenticatedEncryption)
        .withStorageMode(CryptoStorageMode.ObjectMetadata);

// 生成加密客户端 EncryptionClient, COSEncryptionClient 是 COSClient 的子类, 所有COSClient 支持的接口他都支持。
// EncryptionClient 覆盖了 COSClient 上传下载逻辑，操作内部会执行加密操作，其他操作执行逻辑和 COSClient 一致
COSEncryptionClient cosEncryptionClient =
        new COSEncryptionClient(new COSStaticCredentialsProvider(cred),
                new StaticEncryptionMaterialsProvider(encryptionMaterials), clientConfig,
                cryptoConf);

// 上传文件
// 这里给出 putObject 的示例，对于高级 API 上传，只用在生成 TransferManager 时传入 COSEncryptionClient 对象即可
String bucketName = "examplebucket-1250000000";
String key = "exampleobject";
File localFile = new File(localFilePath);
PutObjectRequest putObjectRequest = new PutObjectRequest(bucketName, key, localFile);
cosEncryptionClient.putObject(putObjectRequest);
cosEncryptionClient.shutdown();
```
