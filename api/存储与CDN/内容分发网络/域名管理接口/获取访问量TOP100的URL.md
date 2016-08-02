## 1. 接口描述
域名:cdn.api.qcloud.com
接口名:GetCdnStatTop

获取访问量TOP100的URL

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| startDate | 是 | String | 查询开始时间|
| endDate | 是 | String | 查询结束时间|
| hosts.n (hosts 为数组，此处入参需要填写数组元素 ) | 否 | String | hosts为空时输出全部hosts的数据,输入一个host输出这单个host的数据,输入大于1个host输出为输入的hosts的和的数据|
| projects.n (projects 为数组，此处入参需要填写数组元素 ) | 是 | String | host对应项目的项目id|
| statType | 是 | String | 统计类型，为flux或者bandwidth|
| period | 是 | int | 查询时间粒度|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | Array | 域名在各省份的使用情况以及Top100 URL域名的用量 |
| data.province_data | Array | 指定域名在各省份的使用情况| 
| data.isp_data | Array | 指定域名在各运营商的使用情况| 
| data.url_data | Array | 指定域名下Top100 URL的用量| 
| data. start_datetime|string| 查询开始时间| 
| data.start_datetime | string | 查询结束时间| 
| data.period | int | 查询粒度| 



## 4. 示例
输入
```
https://cdn.api.qcloud.com/v2/index.php?Action=GetCdnStatTop
&startDate=2016-02-15
&endDate=2016-02-16
&statType=bandwidth
&projects.0=0
&hosts.0=testcdn.cig.com.cn
&hosts.1=ping.cdn.qcloud.com
```
输出
```
{
    "code":"0",
    "message":"",
    "data":{
        "province_data":[],
        "url_data":[],
        "start_datetime":,
        "end_datetime":,
        "stat_type":,
        "period":
    }
}
```
##php 示例

function getCdn_StatTop($req_interface, $startDate, $endDate, $hosts, $projects, $statType, $secret_key, $secret_id) {
    // 基础参数
    $args = array(
        "Action" => "GetCdnStatTop",
        "Nonce" => rand(),
        "SecretId" => $secret_id,
        "Timestamp" => time(),
        "startDate" => $startDate,
        "endDate"   => $endDate,
        "statType"  => $statType
    );

    //需要查询的hosts

    // 添加要刷新的url
    $host_idx = 0;
    foreach($hosts as $host) {
        $args["hosts." . $host_idx] = $host;
        $host_idx++;
    }
    $project_idx = 0;
    foreach($projects as $project) {
        $args["projects." . $project_idx] = $project;
        $project_idx++;
    }


    // 参数排序
    ksort($args);
    // 生成参数串
    $args_pairs = array();
    foreach($args as $key => $val) {
        $args_pairs[] = $key . "=" . $val;
    }
    $args_str = implode("&", $args_pairs);
    $src_str = "GET" . $req_interface . "?" . $args_str;
    // 计算signature
    $sig = base64_encode(hash_hmac('sha1', $src_str, $secret_key, true));

    // signature加入参数
    $args["Signature"] = $sig;
    // 参数排序
    ksort($args);
    // 生成最终请求的参数串
    $args_pairs = array();
    foreach($args as $key => $val) {
        $arg_val = $key==="Signature"?urlencode($val):$val;
        $args_pairs[] = $key . "=" . $arg_val;
    }
    $args_str = implode("&", $args_pairs);

    // 最终的请求
    $req_url = "https://" . $req_interface . "?" . $args_str;
    $ret = file_get_contents($req_url);
    echo "$ret";
}

$req_interface = "cdn.api.qcloud.com/v2/index.php";
$projets  = array("0");
$hosts =array("testcdn.cig.com.cn","ping.cdn.qcloud.com");
$statType = "bandwidth";
$startDate = "start_day";
$endDate = "end_day";
$secret_id  = "YOUR_SECRET_ID";
$secret_key  = "YOUR_SECRET_KEY";
getCdn_StatTop($req_interface, $startDate, $endDate, $hosts, $projects, $statType, $secret_key, $secret_id);
?>



