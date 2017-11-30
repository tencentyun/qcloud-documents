## KMS SDK Instruction
To help developers better use KMS SDK, Tencent Cloud provides the following instructions:


## Example: Python SDK Introduction

### Environment Dependency
Make sure the Python environment is set up

### Downloading and Configuring KMS Python SDK
#### How to Use Cloud API Key
When using a Python SDK, the user's Cloud API key is required to verify the validity of the user's identity. Users can log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), and select "Cloud Services" -> "Cloud API Key" to get the Cloud API key, as shown in the figure below:
![](https://mc.qcloudimg.com/static/img/b04d51df61bc4e9259dcee293981b644/5.png)

Users can create a new Cloud API key or use an existing key. Click key ID and go to the details page to get the secretId of the key and its corresponding secretKey.
![](https://mc.qcloudimg.com/static/img/47b2cf18add4d32a867f115fffb6af48/2.png)

#### endpoint
"endpoint" is the access address for KMS service, and it contains the protocols used. The format of endpoint is as follows:

- Private network: `https://kms-region.api.tencentyun.com`
- Public network: `https://kms-region.api.qcloud.com`


#### region
"region" needs to be replaced with a specific region: gz (Guangzhou), sh (Shanghai), bj (Beijing). The option of different regions allows users to choose a region nearby to enjoy better services. "region" value in the common parameters should be consistent with that of domain name. For any inconsistency, the request is sent to the region specified by the domain name.

#### Differences between Private and Public Networks
If the business process is also deployed on a Tencent Cloud CVM submachine, we strongly recommend that you use a private network endpoint in the same region:
1) The latency is lower for a private network in the same region;
2) Currently, KMS charges a fee for the downstream traffic of public networks, so using a private network can save the cost.


#### Downloading Python SDK
Download the latest [KMS SDK](https://cloud.tencent.com/document/product/573/8908).

### Using KMS Python SDK

The codes below are also samples in Python SDK, demonstrating the whole process of key management operations including Create a CMK, Generate Data Key, Encrypt/Decrypt.


```

    #First, obtain the corresponding secretId, secretKey and endpoint from the console.
    try:
        secretId = "your secret id"
        secretKey = "your secret key"
        endpoint = "your endpoint "

        kms_account = KMSAccount(endpoint, secretId, secretKey)

        # create a custom master key
        Description = "test"
        Alias = "test"
        KeyUsage = "ENCRYPT/DECRYPT"
        kms_meta = kms_account.create_key(Description, Alias, KeyUsage)
        print kms_meta

        # create a data key
        KeySpec = "AES_128"
        Plaintext , CiphertextBlob = kms_account.generate_data_key(kms_meta.KeyId, KeySpec)
        print "the data key : %s \n  the encrypted data key :%s\n" % (Plaintext, CiphertextBlob)

        # encrypt the data string
        Plaintest = "test message data"
        CiphertextBlob = kms_account.encrypt(kms_meta.KeyId, Plaintest)
        print "the encrypted data is :%s \n" % CiphertextBlob

        # decrypt the encrypted data string
        Plaintest = kms_account.decrypt(CiphertextBlob)
        print "the decrypted data is :%s\n" % Plaintest

        # get key attributes
        key_meta = kms_account.get_key_attributes(key_meta.KeyId)
        print key_meta

        # set key attributes
        Alias = "ForTest"
        kms_account.set_key_attributes(key_meta.KeyId, Alias)
        
        # disabke a custom key
        kms_account.disable_key(key_meta.KeyId)
        # enable a custom key
        kms_account.enable_key(key_meta.KeyId)

        # list key
        totalCount, keys = kms_account.list_key()
        print keys

    except KMSExceptionBase, e:
        print "Exception:%s\n" % e
	
```

