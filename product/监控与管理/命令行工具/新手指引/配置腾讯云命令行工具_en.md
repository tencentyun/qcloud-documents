You need to complete initial configuration before using Tencent Cloud CLI and [Cloud APIs](https://cloud.tencent.com/product/api.html).

## Acquiring Keys
1) Log in to Tencent Cloud [API Key Console](https://console.cloud.tencent.com/capi).

(2) Create a new key or use an existing cloud API key. Click the cloud API key ID to enter the details page, and acquire SecretID and SecretKey.
![Alt text](https://mc.qcloudimg.com/static/img/ab7aea426d53f31f6bb1fc84bd2ce177/1.png)

## Configuring CLI

Execute the following command:

```
$  qcloudcli configure
Qcloud API SecretId [****************cQ]:AKIDwLw1234MMfPRle2g9nR2OTI787aBCDP
Qcloud API SecretKey [****************ArFd]:OxXj7khcV1234dQSSYNABcdCc1LiArFd
Region Id(gz,hk,ca,sh,shjr,bj,sg) [hk]: gz
Output Format(json,table,text) [json]: json
```

You need to enter:

- Cloud API key SecretId;
- Cloud API key SecretKey;
- Default Region Id: `gz, hk, ca, sh, shjr, bj and sg` are supported.
- Output Format: JSON, table, and text are supported.

After the configuration is completed, use a random command to test the result:

- If it is configured correctly, CVM device information is returned.

```
$  qcloudcli cvm DescribeInstances
{
    "instanceSet": [], 
    "totalCount": 0, 
    "message": "", 
    "code": 0, 
    "codeDesc": "Success"
}

```
- Otherwise, "Authentication Failed" is returned.

```
$  qcloudcli cvm DescribeInstances
{
    "codeDesc": "AuthFailure", 
    "message": "Authentication failed. SecretId does not exist", 
    "code": 4100
}
```
## More Configuration Related Commands
### Adding an Account

Use the following command to add an account:

```
$  qcloudcli addprofile
New profile name: test
Qcloud API SecretID: test
Qcloud API SecretKey: test
Region Id: gz
Output format:json 
```
### Querying Account Information

```
$  qcloudcli showconfigure
------------------------------------------------------------------------------------
|                                   showConfigure                                  |
+----------------------------------------------------------------------------------+
||                                    Configure                                   ||
|+--------------------------------------------------------------------------------+|
|||                                default profile                               |||
||+--------------------------------------+---------------------------------------+||
|||                output                |                region                 |||
||+--------------------------------------+---------------------------------------+||
|||   json                               |   hk                                  |||
||+--------------------------------------+---------------------------------------+||
|||                                profile clitest                               |||
||+--------------------------------------+---------------------------------------+||
|||                output                |                region                 |||
||+--------------------------------------+---------------------------------------+||
|||   json                               |   GZ                                  |||
||+--------------------------------------+---------------------------------------+||
||                                SecretId and Key                                ||
|+--------------------------------------------------------------------------------+|
|||                                default profile                               |||
||+----------------------------------------+-------------------------------------+||
|||            qcloud_secretid             |          qcloud_secretkey           |||
||+----------------------------------------+-------------------------------------+||
|||   AKID4LEwBV4wC0EndAvBatIJn88888888s0o |   bYrGzK5SDdOmh7I88888888fiArxjmTS  |||
||+-------------------------------------+----------------------------------------+||
|||                                profile clitest                               |||
||+-------------------------------------+----------------------------------------+||
|||          qcloud_secretid            |           qcloud_secretkey             |||
||+-------------------------------------+----------------------------------------+||
|||   AAABBBCCC                         |   AAABBBCCC                            |||
||+-------------------------------------+----------------------------------------+||

```

### Modifying Account Information

```
$  qcloudcli configure --profile clitest
Qcloud API SecretId [****************BCCC]: test
Qcloud API SecretKey [****************BCCC]: test
Region Id(gz,hk,ca,sh,shjr,bj,sg) [GZ]: gz
Output Format(json,table,text) []: json
```
### Setting the Default Account

```
$  qcloudcli useprofile --name clitest
```



























