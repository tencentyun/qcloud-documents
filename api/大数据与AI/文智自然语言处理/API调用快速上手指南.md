## 1 介绍

腾讯文智自然语言处理（Natural Language Processing）基于并行计算、分布式爬虫系统，结合独特的语义分析技术，一站满足NLP、转码、抽取、数据抓取等需求。基于文智API可实现搜索、推荐、舆情、挖掘等功能。文智同时支持定制化语义分析方案。

腾讯云文智中文语义平台以SDK模块的方式提供服务，多种编程语言都可以轻松使用。在正式使用之前，您需要首先在腾讯云上注册文智账号。

## 2 API调用概述

### 2.1 通信协议和规则

  详见[《腾讯云通信协议和规则》](http://cloud.tencent.com/doc/api/307/%E8%AF%B7%E6%B1%82%E7%BB%93%E6%9E%84)
	
### 2.2 公共参数

  公共参数是用于标识用户和接口鉴权的参数, 每次请求均需要携带这些参数, 才能正常发起请求。
	
<table style="width:771px">
	<tbody>
		<tr>
			<th style="text-align: center; width: 87px;"><strong>名称</strong></th>
			<th style="text-align: center; width: 75px;"><strong>类型</strong></th>
			<th style="text-align: center; width: 509px;"><strong>描述</strong></th>
			<th style="text-align: center; width: 76px;"><strong>必选</strong></th>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">Action</td>
			<td style="text-align: center; width: 75px;">String</td>
			<td style="text-align: center; width: 509px;">接口指令的名称，例如: LexicalAnalysis</td>
			<td style="text-align: center; width: 76px;">是</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">Region</td>
			<td style="text-align: center; width: 75px;">String</td>
			<td style="text-align: center; width: 509px;">区域参数，用来标识希望操作哪个区域的实例。可选: gz:广州; sh:上海;hk:中国香港;等部分云产品并非每个区域都有提供, 获取产品对应的地域列表可以使用<a href="http://cloud.tencent.com/wiki/v2/DescribeProductRegionList" target="_blank">/v2/DescribeProductRegionList</a></td>
			<td style="text-align: center; width: 76px;">是</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">Timestamp</td>
			<td style="text-align: center; width: 75px;">UInt</td>
			<td style="text-align: center; width: 509px;">当前UNIX时间戳</td>
			<td style="text-align: center; width: 76px;">是</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">Nonce</td>
			<td style="text-align: center; width: 75px;">UInt</td>
			<td style="text-align: center; width: 509px;">随机正整数，与Timestamp联合起来, 用于防止重放攻击</td>
			<td style="text-align: center; width: 76px;">是</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">SecretId</td>
			<td style="text-align: center; width: 75px;">String</td>
			<td style="text-align: center; width: 509px;">由腾讯云平台上申请的标识身份的SecretId和SecretKey, 其中SecretKey会用来生成Signature<br />
			具体参考<a href="http://cloud.tencent.com/wiki/%E6%8E%A5%E5%8F%A3%E9%89%B4%E6%9D%83" target="_blank">接口鉴权</a>页面</td>
			<td style="text-align: center; width: 76px;">是</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">Signature</td>
			<td style="text-align: center; width: 75px;">String</td>
			<td style="text-align: center; width: 509px;">请求签名，用来验证此次请求的合法性<br />
			具体参考<a href="http://cloud.tencent.com/wiki/%E6%8E%A5%E5%8F%A3%E9%89%B4%E6%9D%83" target="_blank">接口鉴权</a>页面</td>
			<td style="text-align: center; width: 76px;">是</td>
		</tr>
	</tbody>
</table>



  公共参数详见[《腾讯云公共参数》](http://cloud.tencent.com/wiki/%E5%85%AC%E5%85%B1%E5%8F%82%E6%95%B0)
	
### 2.3 接口鉴权

接口鉴权方法详见[《接口鉴权》](http://cloud.tencent.com/doc/api/307/%E6%8E%A5%E5%8F%A3%E9%89%B4%E6%9D%83)
>注意：在生成签名的过程中，需要将加密字符串中包含的“_”改写成“.”，从而加密产生签名。

### 2.4 异步任务接口返回格式

  详见[《腾讯云异步任务接口返回格式》](http://cloud.tencent.com/doc/api/307/%E5%BC%82%E6%AD%A5%E4%BB%BB%E5%8A%A1%E6%8E%A5%E5%8F%A3%E8%BF%94%E5%9B%9E%E6%A0%BC%E5%BC%8F)
	
### 2.5 错误码

  详见[《调用方式-返回值-错误码》](http://cloud.tencent.com/doc/api/307/%E9%94%99%E8%AF%AF%E7%A0%81)
	
## 3 调用示例

这里将以一个简单的情感分析任务为例，介绍腾讯云SDK文智模块的使用。

### 3.1 首先请在腾讯云官方SDK下载地址

下载或更新最新版本的SDK（本次以php-sdk为例）
- [从 github 获取最新版本 SDK >> ](https://github.com/QcloudApi/qcloudapi-sdk-php)


### 3.2 修改demo.php文件，修改点如下

**a) **SecretId，SecretKey改为自己腾讯云上相应的值，这里查看：

http://manage.qcloud.com/capi/capiManage.php

**b）**$package=array('offset'=>0, 'limit'=>3); 改为：

$package = array("content"=>"李三挺王四：加油！孩儿他娘。");
	
说明：这是文智情感分析接口的参数。

**c）**$a=$cvm->DescribeInstances($package); 改为：

$a = $wenzhi->TextSentiment($package); 

  说明：这是文智模块的相关接口，具体请查看接口列表：
  http://cloud.tencent.com/wiki/v2/API
	
**d）**其他所有地方的$cvm改为$wenzhi，即替换为文智模块。

**修改后的demo.php如下：**

```
<?php
error_reporting(E_ALL ^ E_NOTICE);
require_once './src/QcloudApi/QcloudApi.php';

$config = array('SecretId'        => '您在腾讯云上的SecretId',
             'SecretKey'       => '您在腾讯云上的SecretKey',
             'RequestMethod'  => 'POST',
             'DefaultRegion'    => 'gz');

$wenzhi = QcloudApi::load(QcloudApi::MODULE_WENZHI, $config);

$package = array("content"=>"李三挺王四：加油！孩儿他娘。");

$a = $wenzhi->TextSentiment($package);

if ($a === false) {
    $error = $wenzhi->getError();
    echo "Error code:" . $error->getCode() . ".\n";
    echo "message:" . $error->getMessage() . ".\n";
    echo "ext:" . var_export($error->getExt(), true) . ".\n";
} else {
    var_dump($a);
}

echo "\nRequest :" . $wenzhi->getLastRequest();
echo "\nResponse :" . $wenzhi->getLastResponse();
echo "\n";
```
