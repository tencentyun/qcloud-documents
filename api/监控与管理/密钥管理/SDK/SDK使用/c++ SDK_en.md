# C ++ sdk
## Preparations for Development

### Related Resources
-[GitHub Address](https://github.com/tencentyun/kms-cpp-sdk.git). Welcome to share codes and report problems.

-[Download C++ SDK locally]()
### Development Environment
1. [Install the library and header files of openssl](http://www.openssl.org/source/)
2. [Install libcurl](https://curl.haxx.se/download.html)
3. [Install cmake tool](https://cmake.org/download/)
4. Obtain APP ID, SecretID, SecretKey from the console.


### Configuring SDK
Download the source code from GitHub, and integrate it into your development environment.

Execute the following command:

```
    cd ${kms-cpp-sdk}
    mkdir -p build 
    cd build
    cmake ..
    make 
```

Some common examples of APIs can be found in sample/kms_sample.cpp. The generated kms_sample can be run directly. The generated libKMS.a and libKMS.so files can be placed in their own lib folder. The directory inc is copied to the include path of your project.
### Historical Version

## Generating Client Object

``` 
    string secretId="xxxxxx";    #Replaced with user's secretId
    string secretKey = "xxxxxx"; #Replaced with user's secretKey
    string endpoint = "https://kms-region.api.tencentyun.com"; # Replaced with user's region. For example, sh refers to Shanghai, gz refers to Guangzhou, and bj refers to Beijing.
    KMSAccount account(endpoint,secretId,secretKey);
```
### Initializing Client Configuration
The client uses sha1 signature algorithm by default. The signature algorithm can be called to modify the signature.

```
    account.set_sign_method("sha256");
```

## Key Management
### Creating CMK
#### Method Prototype

```
    void create_key(KeyMetadata & meta,const string &Description="",const string & Alias = "" , const string  & KeyUsage="ENCRYPT/DECRYPT");
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| KeyMetadata | struct | | CMK attribute structure. The created CMK attribute structure is returned for this parameter | 
| Description | String | None | CMK description.
| Alias | string | Empty string | CMK alias |
| KeyUsage | string | 'ENCRYPT/DECRYPT' | CMK usage. Default is encryption/decryption |

KeyMetadata structure is returned and described as below:

| Attribute Name | Type | Description |
|---------|---------|---------|
| keyId | String | Key ID |
| CreatedTime | uinx time | Creation time |
| Description | string | Key description |
| KeyState | string | Key status |
| KeyUsage | string | Key usage |
| Alias | string | Key alias |

#### Example

```
    KeyMetadata meta ;
    string description ="test";
    string alias = "kms_test";
    string KeyUsage="ENCRYPT/DECRYPT";
    account.create_key(meta,Description,Alias,KeyUsage);
```

### Obtaining CMK Attribute
#### Method Prototype

```
    void get_key_attributes(const string & KeyId, KeyMetadata & meta);
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |
| KeyMetadata | struct | | CMK attribute structure. The created CMK attribute structure is returned for this parameter | 

KeyMetadata structure is returned and described as below:

| Attribute Name | Type | Description |
|---------|---------|---------|
| keyId | String | Key ID |
| CreatedTime | uinx time | Creation time |
| Description | string | Key description |
| KeyState | string | Key status |
| KeyUsage | string | Key usage |
| Alias | string | Key alias |

#### Example

```
    KeyMetadata meta;
    string keyId=""  # Enter your keyId
    account.get_key_attributes(meta.KeyId,meta);
```

### Configuring CMK Attribute
#### Method Prototype

```
    void set_key_attributes(const string & KeyId, const string & Alias);
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |
| Alias | string | None | CMK attribute structure. The created CMK attribute structure is returned for this parameter | 


#### Example

```
    Alias = "For test";
    account.set_key_attributes(KeyId, Alias);
```

### Obtaining CMK List
#### Method Prototype

```
    void list_key(vector<string> & keyIds, const int offset= 0 , const int limit = 10);
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyIds | vector | None | Return keyid vector |
| offset | int | 0 | Return list offset value |
| limit | int | 10 | The limited number of lists returned this time. If left empty, it is 10 by default |

#### Example

```
     vector<string> KeyIds;
     account.list_key(KeyIds);
     for(unsigned int i = 0 ; i < KeyIds.size(); ++i)
         cout<<"the "<<i<<" key id is :"<<KeyIds[i]<<endl;
```
### Generating Data Key
#### Method Prototype

```
    void generate_data_key( string &KeyId, const string & KeySpace, int NumberOfBytes,const string & EncryptionContext,string & Plaintext,string &CiphertextBlob);
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |
| KeySpec | string | None | Generate data key algorithm |
| NumberOfBytes | int | None | Specified length of data key to be generated |
| EncryptionContext | json string | None | An additional json key-value provided when data key is generated |
| Plaintext | string | None | Generated data key plaintext |
| CiphertextBlob | string | None | Generated data key ciphertext |

Returned value (in input parameters)

| Parameter Name | Type | Description |
|---------|---------|---------|
| plaintext | string | Generated data key plaintext |
| ciphertextBlob | string | Generated data key ciphertext |

#### Example

```
       string KeySpec="AES_128";
       string Plaintext,CiphertextBlob;
       account.generate_data_key(meta.KeyId,KeySpec,1024,"",Plaintext, CiphertextBlob);
```
### Enabling CMK
#### Method Prototype

```
    void enable_key(const string & KeyId);
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |

Returned value: None

#### Example

```
    string KeyId= ""  // Enter your keyId;
    account.enable_key(KeyId)
```
### Disabling CMK
#### Method Prototype

```
    void disable_key(const string & KeyId);
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |

Returned value: None
#### Example

```
    string KeyId= ""  // Enter your keyId;
    account.disable_key(KeyId)
```

## Encryption and Decryption
### Encryption
#### Method Prototype

```
    string encrypt(const string &KeyId , const string & plaintext, const string & EncryptionContext);
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |
| Plaintext | string | Empty string | Plaintext |
| EncryptionContext | string | None | JSON string in key/value pair format. If this parameter is specified, the same parameter is provided when Decrypt API is called |

Returned value  

| Parameter Name | Type | Description |
|---------|---------|---------|
| ciphertextBlob | string | Generated ciphertext |



#### Example

```
    string KeyId = "" ; // Enter your keyId;
    string Plaintest = "test message data"
    string CiphertextBlob = account.encrypt(KeyId,Plaintest,"");
```
### Decryption
#### Method Prototype

```
    string decrypt(const string & CiphertextBlob, const string & EncryptionContext);
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| CiphertextBlob | string | Empty string | Ciphertext |
| EncryptionContext | string | None | JSON string in key/value pair format. If this parameter is specified, the same parameter is provided when Decrypt API is called. |

Returned value  

| Parameter Name | Type | Description |
|---------|---------|---------|
| plaintext | string | Plaintext obtained through decryption of ciphertext |

#### Example

```
     Plaintext = account.decrypt(CiphertextBlob,"");
```




