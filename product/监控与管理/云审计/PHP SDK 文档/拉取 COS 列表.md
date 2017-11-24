
## SDK 描述
 ListCosBuckets 用于拉取 COS 的 Bucket 列表。
## SDK 使用参数
详见 [公共请求参数](https://cloud.tencent.com/document/api/214/4183)  页面。

## 响应参数


| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| cosBucketsList | Array | COS Bucket 数组 |

其中 cosBucketsList 的参数如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| name | String | COS Bucket 名称 |
| region | String | Bucket 所在的区域 |
| appId | String | 账号 appId 或者项目 appId |
## 实际案例
### SDK 使用示例

```
$config = array('SecretId'       => '你的secretId',
                'SecretKey'      => '你的secretKey',
                'RequestMethod'  => 'GET',
                'DefaultRegion'  => 'gz');
$ca = QcloudApi::load(QcloudApi::MODULE_CA, $config);
$package = array();
$a = $ca->ListCosBuckets($package);
if ($a === false) {
    $error = $ca->getError();
    echo "Error code:" . $error->getCode() . ".\n";
    echo "message:" . $error->getMessage() . ".\n";
    echo "ext:" . var_export($error->getExt(), true) . ".\n";
} else {
    var_dump($a);
}
echo "\nRequest :" . $ca->getLastRequest();
echo "\nResponse :" . $ca->getLastResponse();
echo "\n";
```
### 响应示例

```
{
    "cosBucketsList": [
        {
            "name": "cloudaudit",
            "region": "ap-shanghai",
            "appId": "1254962721"
        },
        {
            "name": "cloudtrail",
            "region": "ap-shanghai",
            "appId": "1254962721"
        },
        {
            "name": "sundehuixxx",
            "region": "ap-shanghai",
            "appId": "1254962721"
        }
    ]
}
```


