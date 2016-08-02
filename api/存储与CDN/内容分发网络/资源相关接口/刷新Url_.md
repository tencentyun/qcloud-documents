## 1.URL刷新
### 1.1 接口描述
 
域名：cdn.api.qcloud.com
接口名: RefreshCdnUrl

更新源文件后，提交文件的Url进行刷新，以达到快速同步文件到CDN节点的效果。

 

### 1.2 输入参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>必选</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> urls.n
<td> 是
<td> String
<td> 需要刷新的url,最多为100个
</tbody></table>

 

### 1.3 输出参数
 
<table class="t"><tbody><tr>
<th><b>参数名称</b></th>
<th><b>类型</b></th>
<th><b>描述</b></th>
<tr>
<td> code
<td> Int
<td> 错误码, 0: 成功, 其他值: 失败
<tr>
<td> message
<td> String
<td> 错误信息
</tbody></table>

 

###  1.4 示例
 
输入
```
  https://domain/v2/index.php?Action=RefreshCdnUrl
  &urls.0=http://www.abd.com
  &urls.1=http://www.abc.cn
```
<span style"color:red">注：此地方必须填写完整的URL链接（必须带上HTTP）</span>

输出
```
  {
      "code":0,
      "message": "",
  }

```


###   1.5 php代码示例 
```
<?php
function referesh_urls($req_interface, $urls, $secret_id, $secret_key) {
    // 基础参数
    $args = array(
            "Action" => "RefreshCdnUrl",
            "Nonce" => rand(),
            "SecretId" => $secret_id,
            "Timestamp" => time(),
            );

    // 添加要刷新的url
    $url_idx = 0;
    foreach($urls as $url) {
        $args["urls." . $url_idx] = $url;
        $url_idx++;
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
$urls  = array("http://foo.bar.baz/a/b/x.js", "http://foo.bar.baz/a/b/y.js", "http://foo.bar.baz/a/b/z.js");
$secret_id  = "YOUR_SECRET_ID";
$secret_key  = "YOUR_SECRET_KEY";
referesh_urls($req_interface, $urls, $secret_id, $secret_key);
?>

```




## 2 目录刷新
接口：/v2/RefreshCdnDir

### 2.1 接口描述
域名：cdn.api.qcloud.com
接口名: RefreshCdnDir

### 2.2 输入参数
dirs.n：必填，字符串，要刷新的目录

### 2.3 输出参数
Code：数字，错误码, 0: 成功, 其他值: 失败
Message：字符串，错误信息

### 2.4 示例
输入
https:// cdn.api.qcloud.com /v2/index.php?Action=RefreshCdnDir
 &dirs.0=http://www.abd.com/a/
 &dirs.1=http://www.abc.cn/b/
注：此地方必须填写完整的URL链接（必须带上HTTP），并且必须为目录（以“/”结尾）

输出
  {
      "code":0,
      "message": "",
  }

