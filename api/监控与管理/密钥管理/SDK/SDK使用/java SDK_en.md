# JAVA SDK
## Preparations for Development

### Related Resources
-[GitHub Address](https://github.com/tencentyun/kms-java-sdk). Welcome to share codes and report problems.

-[Download JAVA SDK locally]()
### Environment Dependency
JDK1.7

### Historical Version

## Generating Client Object

``` 
    //Cloud API key information queried from Tencent Cloud official website
    String secretId="";
    String secretKey="";
    String endpoint = "";       
    KMSAccount account = new KMSAccount(endpoint,secretId, secretKey);
```
### Initializing Client Configuration
The client uses sha1 signature algorithm by default. The signature algorithm can be called to modify the signature.

```
    account.setSignMethod("sha256");
```

## Key Management
### Creating CMK
#### Method Prototype

```
    public KeyMetadata create_key(String Description,String Alias ,String KeyUsage) throws Exception
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| Description | String | None | CMK description.
| Alias | string | None | Key alias |
| KeyUsage | string | None | CMK usage. Default is encryption/decryption |

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
    String Description = "test";
    String Alias= "test";
    String KeyUsage = "ENCRYPT/DECRYPT";
    KeyMetadata meta = account.create_key(Description , Alias , KeyUsage);
```

### Obtaining CMK Attribute
#### Method Prototype

```
    public KeyMetadata get_key_attributes(String KeyId) throws Exception
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |

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
    meta = account.get_key_attributes(KeyId);
```

### Configuring CMK Attribute
#### Method Prototype

```
    public void set_key_attributes(String KeyId , String Alias) throws Exception
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |
| Alias | string | None | Key alias |

Returned value: None

#### Example

```
    Alias = "for test";
    account.set_key_attributes(KeyId, Alias);
```


### Obtaining CMK List
#### Method Prototype

```
    public void  list_key(int offset, int limit,List<String> KeyList) throws Exception
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| offset | int | 0 | Return list offset value. |
| limit | int | 10 | The limited number of lists returned this time. If left empty, it is 10 by default. |
| KeyList | list | None | KeyId list returned this time. |

#### Example

```
    ArrayList<String> KeyId  = new ArrayList<String>();
    account.list_key(-1,-1,KeyId);
    for(int i = 0 ; i < KeyId.size(); ++i)
    	System.out.println("the " +Integer.toString(i) + "Key id is " + KeyId.get(i));
```
### Generating Data Key
#### Method Prototype

```
    public String generate_data_key(String KeyId, String KeySpec, int NumberOfBytes , String EncryptionContext,String Plaintext ) throws Exception
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID. |
| KeySpec | string | None | Generate data key algorithm. |
| NumberOfBytes | int | None | Specified length of data key to be generated. |
| EncryptionContext | string | None | An additional json key-value provided when data key is generated. |
| Plaintext | string | None | Generated data key plaintext. |

Returned value 

| Parameter Name | Type | Description |
|---------|---------|---------|
| plaintext | string | Generated data key plaintext (returned value of input parameter) |
| ciphertextBlob | string | Generated data key ciphertext |
#### Example

```
   String KeySpec = "AES_128";
   String Plaintext  = "";   		
   String CiphertextBlob = account.generate_data_key(meta.KeyId, KeySpec,1024,"",Plaintext);
   System.out.println("the data key string is " + Plaintext);
   System.out.println("the encrypted data key string is "+CiphertextBlob);
```
### Enabling CMK
#### Method Prototype

```
    public void enable_key(String KeyId) throws Exception
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |

Returned value: None

#### Example

```
    account.enable_key(KeyId);
```
### Disabling CMK
#### Method Prototype

```
    public void disable_key(String KeyId) throws Exception
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |

Returned value: None
#### Example

```
    account.disable_key(KeyId);
```

## Encryption and Decryption
### Encryption
#### Method Prototype

```
    def encrypt(self, KeyId=None, Plaintext="", EncryptionContext=None)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |
| Plaintext | string | Empty string | Plaintext |
| EncryptionContext | string | None | JSON string in key/value pair format. If this parameter is specified, the same parameter is provided when Decrypt API is called. |

Returned value 

| Parameter Name | Type | Description |
|---------|---------|---------|
| ciphertextBlob | string | Generated ciphertext |
#### Example

```
    CiphertextBlob  = account.encrypt(KeyId, Plaintext,"");
    System.out.println("the encrypted data is " + CiphertextBlob);
```
### Decryption
#### Method Prototype

```
    public String decrypt(String CiphertextBlob , String EncryptionContext)throws Exception
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
    Plaintext = account.decrypt( Plaintext,"");
    System.out.println("the decrypted data is " + Plaintext);
```




