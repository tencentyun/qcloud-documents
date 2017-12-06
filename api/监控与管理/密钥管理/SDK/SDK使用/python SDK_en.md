# Python sdk
## Preparations for Development

### Related Resources
-[GitHub Address](https://github.com/tencentyun/kms-python-sdk). Welcome to share codes and report problems.

-[Download Python SDK locally]()
### Environment Dependency
Python3 is not supported for Python2.7

How to get python version:

Linux Shell 

```

    $python -V

    Python 2.7.11
```

Windows CMD

```
   
    D:>python -V
    Python 2.7.11
```

If prompted that it is not an internal or external command, add the absolute path of python to the Windows environment variable PATH first.

### Historical Version

## Generating Client Object

``` 
    secretId='xxxxxx'    #Replaced with user's secretId
    secretKey = 'xxxxxx' #Replaced with user's secretKey
    endpoint = 'https://kms-region.api.tencentyun.com' # Replaced with user's region. For example, sh refers to Shanghai, gz refers to Guangzhou, and bj refers to Beijing.
    kms_account = KMSAccount(endpoint,secretId,secretKey)
```
### Initializing Client Configuration
The client uses sha1 signature algorithm by default. The signature algorithm can be called to modify the signature.

```
    kms_account.set_sign_method('sha256')
```

## Key Management
### Creating CMK
#### Method Prototype

```
    def create_key(self, Description=None, Alias="", KeyUsage='ENCRYPT/DECRYPT')
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| Description | String | None | CMK description.
| Alias | string | Empty string | CMK alias |
| KeyUsage | string | 'ENCRYPT/DECRYPT' | CMK usage. Default is encryption/decryption |

KeyMetadata structure is returned and described as below:

| Attribute Name | Type | Description |
|---------|---------|---------|
| keyId | String | Key ID |
| CreateTime | uinx time | Creation time |
| Description | string | Key description |
| KeyState | string | Key status |
| KeyUsage | string | Key usage |
| Alias | string | Key alias |

#### Example

```
    description ='for test'
    alias = 'kms_test'
    kms_meta = kms_account.create_key(description,alias)
```

### Obtaining CMK Attribute
#### Method Prototype

```
    def get_key_attributes(self, KeyId=None)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |

KeyMetadata structure is returned and described as below:

| Attribute Name | Type | Description |
|---------|---------|---------|
| keyId | String | Key ID |
| CreateTime | uinx time | Creation time |
| Description | string | Key description |
| KeyState | string | Key status |
| KeyUsage | string | Key usage |
| Alias | string | Key alias |

#### Example

```
    keyId=''  # Enter your keyId
    key_meta = kms_account.get_key_attributes("kms-awy8dndb")
    print key_meta
```

### Configuring CMK Attribute
#### Method Prototype

```
    def set_key_attributes(self, KeyId=None, Alias=None)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |
| Alias | string | None | Key alias |

Returned value: None

#### Example

```
    keyId=''  # Enter your keyId
    Alias=''  # Enter your CMK alias
    kms_account.get_key_attributes(keyId,Alias)
```

### Obtaining CMK List
#### Method Prototype

```
    def list_key(self, offset=0, limit=10)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| offset | int | 0 | Return list offset value. |
| limit | int | 10 | The limited number of lists returned this time. If left empty, it is 10 by default. |

KeyMetadata structure is returned and described as below:

| Attribute Name | Type | Description |
|---------|---------|---------|
| totalCount | int | Total number of keys |
| keys | array | key array |

#### Example

```
    totalCount, keys = kms_account.list_key()
    print keys
```
### Generating Data Key
#### Method Prototype

```
    def generate_data_key(self, KeyId=None, KeySpec=None, NumberOfBytes=None, EncryptionContext=None)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID. |
| KeySpec | string | None | Generate data key algorithm. |
| NumberOfBytes | int | None | Specified length of data key to be generated. |
| EncryptionContext | string | None | An additional json key-value provided when data key is generated. |

Returned value 

| Parameter Name | Type | Description |
|---------|---------|---------|
| plaintext | string | Generated data key plaintext |
| ciphertextBlob | string | Generated data key ciphertext |


#### Example

```
        KeySpec = "AES_128"
        Plaintext, CiphertextBlob = kms_account.generate_data_key(KeyId, KeySpec)
        print "the data key : %s \n  the encrypted data key :%s\n" % (Plaintext, CiphertextBlob)
```
### Enabling CMK
#### Method Prototype

```
    def enable_key(self, KeyId=None)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |

Returned value: None

#### Example

```
    kms_account.enable_key(KeyId)
```
### Disabling CMK
#### Method Prototype

```
    def disable_key(self, KeyId=None)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |

Returned value: None
#### Example

```
    kms_account.disable_key(KeyId)
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

Returned value:

| Parameter Name | Type | Description |
|---------|---------|---------|
| ciphertextBlob | string | Generated ciphertext |
#### Example

```
    Plaintest = "test message data"
    CiphertextBlob = kms_account.encrypt(kms_meta.KeyId, Plaintest)
    print "the encrypted data is :%s \n" % CiphertextBlob
```
### Decryption
#### Method Prototype

```
    def decrypt(self, CiphertextBlob="", EncryptionContext=None)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| CiphertextBlob | string | Empty string | Ciphertext |
| EncryptionContext | string | None | JSON string in key/value pair format. If this parameter is specified, the same parameter is provided when Decrypt API is called. |

Returned value:

| Parameter Name | Type | Description |
|---------|---------|---------|
| plaintext | string | Plaintext obtained through decryption of ciphertext |
#### Example

```
    Plaintest = kms_account.decrypt(CiphertextBlob)
    print "the decrypted data is :%s\n" % Plaintest
```




