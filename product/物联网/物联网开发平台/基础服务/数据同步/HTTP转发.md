

## 操作场景
用户的个性化业务需求需要将产品下所有设备上报的数据传输至用户自有的服务器上进行处理，平台提供了 HTTP 转发服务，将设备上报数据实时 POST 到用户的 HTTP 服务器的能力。


## 操作步骤
1. 登录 [物联网开发平台](https://console.cloud.tencent.com/iotexplorer) ，选择【公共实例】或您购买的【标准企业实例】。
2. 进入项目列表页面，单击【项目 ID】进入项目详情页。
3. 单击左侧菜单【数据同步】 进入数据同步配置页面，数据同步在未设置时，默认生效状态都为关闭，HTTP 服务地址为空。
4. 选择需要设置数据同步的产品，单击设备列表中的【设置】，即可设置该产品需要同步的 HTTP 服务地址。
![](https://main.qcloudimg.com/raw/9a3a485e22c4ef6d305f50bf6c6a7e24.png)
5. 弹出设置弹窗，输入需要设置的 HTTP 服务 URL，并单击【保存】。
![](https://main.qcloudimg.com/raw/fc820cba4e51cc93c9576a0d39484287.png)
6. URL 保存成功后，跳转到列表页，可开启该产品的【生效状态】，完成该产品的数据同步配置。
7. 如需配置项目中的多个产品，需要逐一对产品进行配置。

## 示例
#### 转发报文格式
平台转发至用户 HTTP 服务的报文格式如下：
```
{
	"payload": {
		"clientToken": "DEP****YAS4-38",
		"method": "report",
		"params": {
			"brightness": 58,
			"color": 2,
			"name": "dev001",
			"power_switch": 1
		}
	},
	"seq": 10498444,
	"timestamp": 1579055948,
	"topic": "$thing/up/property/DEP****YAS4/dev001",
	"devicename": "dev001",
	"productid": "DEP****YAS4"
}

```
用户只需根据业务需要，解析上述报文中的 productid、devicename 以及 params 部分的数据，其中 params 部分的数据，即用户在开发平台定义的产品的数据模板。

#### HTTP 接收服务示例
用户可部署在自己的服务器上进行测试，PHP 接收代码示例如下：
```
<?php
ini_set('display_errors',1);            //错误信息  
ini_set('display_startup_errors',1);    //php启动错误信息  
error_reporting(-1);                    //打印出所有的 错误信息  

function microtime_float()
{
        list($usec, $sec) = explode(" ", microtime());
        return ((float)$usec + (float)$sec);
}

function microtime_format($tag, $time)
{
        list($usec, $sec) = explode(".", $time);
        $date = date($tag,$usec);
        return str_replace('x', $sec, $date);
}

function getAllHeaders(){
    $headers = array();
    foreach($_SERVER as $key=>$value){
        if(substr($key, 0, 5)==='HTTP_'){
            $key = substr($key, 5);
            $key = str_replace('_', ' ', $key);
            $key = str_replace(' ', '-', $key);
            $key = strtolower($key);
            $headers[$key] = $value;
        }
    }
    return $headers;
}


#echo microtime() ;
$time = microtime_float();
$strtime = microtime_format('Ymd-His.x ', $time);
$ctype = $_SERVER['CONTENT_TYPE'];
$raw_post_data = file_get_contents('php://input');
echo $strtime , '#post body:' , $raw_post_data , "\r\n";

#var_dump(getAllHeaders());

#error_log($raw_post_data,3,'/var/log/error.log');
file_put_contents("/data/device_report.txt","$strtime TYPE:$ctype BODY: $raw_post_data\r\n",FILE_APPEND);  

?>

```

