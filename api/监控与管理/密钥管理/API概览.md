
## 密钥管理服务

### 加解密相关接口
| 接口功能 | Action ID | 功能描述
|---------|---------|---------|
| [加密](/doc/api/431/5832) | Encrypt|用于加密最多为4KB任意数据，诸如RSA密钥，数据库密钥，或者其他敏感的客户信息。|
| [解密](/doc/api/431/5833) | Decrypt|用于解密密文数据，得到明文数据。|



### 密钥管理相关接口
| 接口功能 | Action ID | 功能描述|
|---------|---------|---------|
| [创建主密钥](/doc/api/431/5837) |CreateKey |创建用户管理数据秘钥的主秘钥CMK（Custom Master Key）。|
| [获取主密钥列表](/doc/api/431/5838) | ListKey | 用于获取用户所有的keyId。|
|[获取主密钥属性](/doc/api/431/5839)  | GetKeyAttributes| 用于获取指定keyId的属性信息。|
| [禁用主密钥](/doc/api/431/5924) | DisableKey |用于禁用一个指定的keyId。|
| [启用主密钥](/doc/api/431/5840) | EnableKey | 用于启用一个指定的keyId。|
| [生成数据密钥](/doc/api/431/5841) |GenerateDataKey| 用于生成一个密钥，用户可以使用该密钥用于本地数据的加密。|
| [修改主密钥属性](/doc/api/431/)|SetKeyAttributes|用于修改指定keyId的属性信息。|


