## 功能说明
1. PHP Server SDK 将一些常用的 REST API 封装成了函数，并以接口类的方式暴露给开发者，具体参见 TimRestInterface.php 文件中的 TimRestInterface 类；
2. 提供工具 TimRestApiGear.php 可直接访问 RestAPI。

## PHP Server SDK 集成

[独立模式](/doc/product/269/独立模式) 和 [托管模式](/doc/product/269/托管模式) 的集成存在轻微差别，唯一的差别在于 user_sig 的设置方式。
1. 对于独立模式，需要调用`generate_user_sig`生成user_sig；
2. 对于托管模式，需要先依照 [下载UserSig](/doc/product/269/下载UserSig) 的指引下载 user_sig，然后再调用 `set_user_sig` 设置 user_sig。

### API集成示例代码（独立模式）

```
// 设置 REST API 调用基本参数
$sdkappid = 1400000478;
$identifier = "myadmin";
$private_key_path = "/path/to/private/key";
$signature = "/signature/linux-signature64";

// 初始化API
$api = createRestAPI();
$api->init($sdkappid, $identifier);

// 生成签名，有效期一天
// 对于FastCGI，可以一直复用同一个签名，但是必须在签名过期之前重新生成签名
$ret = $api->generate_user_sig($identifier, '86400', $private_pem_path, $signature);
if ($ret == null)
{
	// 签名生成失败
	return -10;
}
// 调用api的成员函数，实现REST API的调用，以下单发消息，群组内发送文本消息，通用接口为示例：
// 单发消息
$ret = $api->openim_send_msg("myadmin", "lilei", "hello");

// 群组内发送消息
$ret = $api->group_send_group_msg("lilei", "@TGS#2QJXRPAE3", "hello");

// 通用接口，在当前版本没有提供用户需要的REST API集成SDK的时候，才考虑使用该接口，
// 用户可以使用该接口直接调用REST API， 需要用户构造REST API需要的请求包体
// 以调用REST API group_get_group_member_info 为例：
$req_body = array(
        "GroupId" => "@TGS#2QJXRPAE3",      //群组ID
        "Limit" => 20,           //Limit限制回包中群组的个数，不得超过10000
        "Offset" => 5           //Offset控制从整个群组列表中的第多少个群组开始拉取信息
        );
$ret = $api->comm_rest("group_open_http_svc", "group_get_group_member_info", $req_body);
```

### API 集成示例代码（托管模式）

```
// 设置REST API调用基本参数
$sdkappid = 1400000478;
$identifier = "myadmin";
$user_sig = "eJx1zkFvgjAYxvE7...";

// 初始化API
$api = createRestAPI();
$api->init($sdkappid, $identifier);

// 设置签名
// 对于FastCGI，可以一直复用同一个签名，但是必须在签名过期之前重新下载签名
$ret = $api->set_user_sig($user_sig);
if ($ret == false)
{
	// 签名设置失败
	return -10;
}
// 调用api的成员函数，实现REST API的调用，以下单发消息，群组内发送文本消息，通用接口为示例：
// 单发消息
$ret = $api->openim_send_msg("myadmin", "lilei", "hello");

// 群组内发送消息
$ret = $api->group_send_group_msg("lilei", "@TGS#2QJXRPAE3", "hello");

// 通用接口，在当前版本没有提供用户需要的REST API集成SDK的时候，可以考虑使用该接口，用户可以
// 通过该接口直接调用REST API的接口， 需要用户构造REST API要求的请求包体
// 以调用REST API group_get_group_member_info 为例：
$req_body = array(
        "GroupId" => "@TGS#2QJXRPAE3",      //群组ID
        "Limit" => 20,           //Limit限制回包中群组的个数，不得超过10000
        "Offset" => 5           //Offset控制从整个群组列表中的第多少个群组开始拉取信息
        );
$ret = $api->comm_rest("group_open_http_svc", "group_get_group_member_info", $req_body);
```

## TimRestApiGear.php 使用说明
### 独立模式
1. 配置 TimRestApiConfig.json 文件，其中： identifier 为 App 管理者账户；private_pem_path 为本地私钥位置；user_sig 请填""。
2. 查看 signature 文件夹中对应脚本使用权限，如果无可执行权限，需要修改权限使其可被执行。
3. 执行 PHP TimRestApiGear.php 可看到该工具访问命令(用法)。 详情请见：代码包中 README 文件。

### 托管模式
1. 配置 TimRestApiConfig.json 文件，其中： identifier 为App管理者账户； user_sig 为托管模式用户下载到的用户凭证，下载方式参见 [下载 UserSig](/doc/product/269/下载UserSig)；private_pem_path 请填""。
2. 执行 PHP TimRestApiGear.php 可看到该工具访问命令（用法）。 详情请见：代码包中 README 文件。

## SDK下载
您可通过如下两种方式下载：
1. [直接单击下载](http://share.weiyun.com/7528e49c4602425d88ce3b91ccde3b9b)；
2. 到 [github](https://github.com/tencentyun/imsdk_restapi-php-sdk)下载。
