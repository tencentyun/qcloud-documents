## 开发准备
安装 PHP SDK 前，需要先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretId 和 SecretKey，SecretId 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

### 开发环境
PHP 7.2 

### 通过 Composer 安装（推荐）
通过 Composer 获取安装是使用 PHP SDK 的推荐方法，Composer 是 PHP 的依赖管理工具，支持您项目所需的依赖项，并将其安装到项目中。关于 Composer 详细可参考 Composer 官网 。
1. 安装 Composer：
    - Windows 环境请访问 [Composer 官网](https://getcomposer.org/download/) 下载安装包安装。
    - Unix 环境在命令行中执行以下命令安装。
```
curl -sS https://getcomposer.org/installer | php
```

2. 在 composer.json 的 require 结构体中加入依赖。以 3.0.6 版本为例，您可以在 Composer 仓库上看到最新的版本号：
```
 "tencentcloud/tencentcloud-sdk-php": "3.0.6"
```
3. 运行`composer install`下载安装 PHP SDK。
4. 添加以下引用代码，引用方法可参考示例。
```
require 'vendor/autoload.php';
```


### 通过源码包安装
1. 前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-php) 下载源码压缩包。
2. 解压源码包到您项目合适的位置。
3. 添加以下引用代码，引用方法可参考示例。
```
require_once '../TCloudAutoLoader.php';
```


## 接口列表

| 接口名称 | 接口功能                            |
| :--- | :------------------------------------ |
| [CreateFunction](https://cloud.tencent.com/document/api/583/18586)   | 创建函数          |
| [DeleteFunction](https://cloud.tencent.com/document/api/583/18585)   | 删除函数        |
| [GetFunction](https://cloud.tencent.com/document/api/583/18584)      | 获取函数详细信息   |
| [GetFunctionLogs](https://cloud.tencent.com/document/api/583/18583)  | 获取函数运行日志   |
| [Invoke](https://cloud.tencent.com/document/api/583/17243)           | 运行函数          |
| [ListFunctions](https://cloud.tencent.com/document/api/583/18582)    | 获取函数列表       |
| [UpdateFunctionCode](https://cloud.tencent.com/document/api/583/18581)  | 更新函数代码    |
| [UpdateFunctionConfiguration](https://cloud.tencent.com/document/api/583/18580)  | 更新函数配置|

## 示例

```
setEndpoint("scf.tencentcloudapi.com");
      
    		$clientProfile = new ClientProfile();
    		$clientProfile->setHttpProfile($httpProfile);
    		// 实例化要请求产品的client对象，以及函数所在的地域
    		$client = new ScfClient($cred, "ap-shanghai", $clientProfile);

    		$req = new InvokeRequest();
            // 接口参数,输入需要调用的函数名，RequestResponse(同步) 和 Event(异步)
    		$params = '{"FunctionName":"test_python", "InvocationType":"RequestResponse"}';
    		$req->fromJsonString($params);

    		$resp = $client->Invoke($req);

   		print_r($resp->toJsonString());
	}
	catch(TencentCloudSDKException $e) {
    echo $e;
	}
    return "hello";
}

?>
```
## 打包部署
如果需要在云函数控制台中部署函数，并使用 SDK 调用其他函数，则需要把 tencentcloud 的库和函数代码一起打包成zip 文件。

- 注意在控制台创建函数时的执行方法，需要和 zip 文件里的代码文件和执行函数对应。
- 最终生成的 zip 包如果大于50MB，需要通过 COS 上传。
- 云 API 默认限频为每秒20次，如果需要开大并发，可以 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=668&source=0&data_title=%E6%97%A0%E6%9C%8D%E5%8A%A1%E5%99%A8%E4%BA%91%E5%87%BD%E6%95%B0%20SCF&step=1) 申请。
