# PHP sdk
## Preparations for Development

### Related Resources
-[GitHub Address](https://github.com/tencentyun/kms-php-sdk.git). Welcome to share codes and report problems.

-[Download PHP SDK locally]()
### Development Environment
1. Supported environment: PHP 5.3.0 or above
2. Obtain APP ID, SecretID, SecretKey from the console.

### Historical Version

## Generating Client Object

``` 
    //Cloud API key information queried from Tencent Cloud official website
    $secretId = "";
    $secretKey = "";
    $endPoint = "";
    $kms_account = new KMSAccount($endPoint,$secretId,$secretKey);
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
    public function create_key($Alias = NULL, $Description = NULL, $KeyUsage="ENCRYPT/DECRYPT")
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| Description | String | NULL | CMK description.
| Alias | string | NULL | CMK alias |
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
    $Description = "test";
    $Alias = "test";
    $KeyUsage= "ENCRYPT/DECRYPT";
    $kms_meta = $kms_account->create_key($Alias,$Description,$KeyUsage);
```

### Obtaining CMK Attribute
#### Method Prototype

```
    public function get_key_attributes($KeyId = NULL)
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
    KeyMetadata meta;
    string keyId=""  # Enter your keyId
    $kms_meta = $kms_account->get_key_attributes($keyId);
```

### Configuring CMK Attribute
#### Method Prototype

```
    public function set_key_attributes($KeyId = NULL, $Alias)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |
| Alias | string | None | Configured CMK alias |

Returned value: None

#### Example

```
    $Alias = "for test" ;
    $kms_account->set_key_attributes($kms_meta->KeyId,$Alias);
```

### Obtaining CMK List
#### Method Prototype

```
    public function list_key($offset = 0, $limit = 10)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyIds | vector | None | Return keyid vector |
| offset | int | 0 | Return list offset value |
| limit | int | 10 | The limited number of lists returned this time. If left empty, it is 10 by default |

#### Example

```
     $ret_pkg = $kms_account->list_key(); 
```
### Generating Data Key
#### Method Prototype

```
    public function generate_data_key($KeyId = NULL, $KeySpec = "", $NumberOfBytes = 1024,$EncryptionContext =NULL)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |
| KeySpec | string | "" | Generate data key algorithm |
| NumberOfBytes | int | 1024 | Specified length of data key to be generated |
| EncryptionContext | string | NULL | An additional json key-value provided when data key is generated |

In returned field:

| Parameter Name | Type | Description |
|---------|---------|---------|
| plaintext | string | Generated data key plaintext (returned value of input parameter) |
| ciphertextBlob | string | Generated data key ciphertext |

#### Example

```
       $KeySpec = "AES_128";
       $ret_pkg = $kms_account->generate_data_key($kms_meta->KeyId,$KeySpec,1024,"");
       $Plaintext = $ret_pkg['plaintext'];
       $CiphertextBlob = $ret_pkg['ciphertextBlob'];
```
### Enabling CMK
#### Method Prototype

```
    public function enable_key($KeyId = NULL)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |

Returned value: None

#### Example

```
    $KeyId= ""  // Enter your keyId;
    $kms_account->enable_key($KeyId);
```
### Disabling CMK
#### Method Prototype

```
    public function disable_key($KeyId= NULL)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | None | CMK ID |

Returned value: None
#### Example

```
    $KeyId= ""  // Enter your keyId;
    $kms_account->disable_key($KeyId);
```

## Encryption and Decryption
### Encryption
#### Method Prototype

```
    public function encrypt($KeyId = NULL, $Plaintext=NULL,$EncryptionContext =NULL)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| keyId | string | NULL | CMK ID |
| Plaintext | string | NULL | Plaintext |
| EncryptionContext | string | NULL | JSON string in key/value pair format. If this parameter is specified, the same parameter is provided when Decrypt API is called |

Returned value

| Parameter Name | Type | Description |
|---------|---------|---------|
| ciphertextBlob | string | Generated ciphertext |
#### Example

```
    $CiphertextBlob = $kms_account->encrypt($KeyId,$Plaintext);
```
### Decryption
#### Method Prototype

```
    public function decrypt($CiphertextBlob = NULL,$EncryptionContext = NULL)
```

#### Parameter Description

| Parameter Name | Type | Default Value | Description |
|---------|---------|---------|---------|
| CiphertextBlob | string | NULL | Ciphertext |
| EncryptionContext | string | NULL | JSON string in key/value pair format. If this parameter is specified, the same parameter is provided when Decrypt API is called. |

Returned value  

| Parameter Name | Type | Description |
|---------|---------|---------|
| plaintext | string | Plaintext obtained through decryption of ciphertext |
#### Example

```
     $Plaintext = $kms_account->decrypt($CiphertextBlob);
```




