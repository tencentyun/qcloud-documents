如果您要开通腾讯云微信小程序开发者工具解决方案，可以阅读[《开通指引》](/document/product/619/11447)；

您还可以查看[《开发环境和生产环境》](/document/product/619/11446)了解开发环境和生产环境的区别；

如果本文还不能解决您的问题，您可以到腾讯云[问答](https://cloud.tencent.com/developer/ask)提问，我们将尽快跟进解答。

## 如何打印和下载日志

Wafer2 针对 PHP 的开发情况专门优化了日志的下载，为了兼容，您必须将日志输出在 `application/logs` 目录下。同时，日志的文件名也必须遵循 `log-[YYYY]-[MM]-[DD].log` 模式，YYYY 为完整年份，MM 为完整月份数字，DD 为完整日期，例如：`log-2017-10-16.log`。具体的日志输出代码您可以参考 [SDK 內建的 Logger](https://github.com/tencentyun/wafer-php-server-sdk/blob/master/lib/Helper/Logger.php)。

您可以在[腾讯云小程序控制台](https://console.cloud.tencent.com/lav2/dev)下载日志，系统将会自动取**当天**最后 1000 条日志。

## 如何快速新建路由

Wafer2 服务端 Demo 采用 CI 框架编写，关于 CI 框架的路由匹配模式，您可以查看 CI 框架的[文档](http://codeigniter.org.cn/user_guide/general/controllers.html)。

只需要在 `application/controllers` 目录下新建一个文件，例如为 `Demo.php`，写入如下代码：

```php
<?php
defined('BASEPATH') OR exit('No direct script access allowed');

class Demo extends CI_Controller {
    public function index() {
        $this->json([
            'code' => 0,
            'data' => [
                'msg' => 'Hello World'
            ]
        ]);
    }
}
```

接着点击右上角的【腾讯云】按钮，选择【上传测试代码】，勾选【普通上传】，点击确定即可上传代码，等到提示开发环境部署成功了之后，打开浏览器，访问 `https://腾讯云分配的域名/weapp/demo`，即可看到刚刚编写的返回，是一个 JSON 字符串：

```json
{"code":0,"data":{"msg":"Hello World"}}
```

## 如何使用服务端 SDK 连接和操作数据库

服务端 SDK 基于 PDO 进行了一下简单的封装，您可以直接使用 `QCloud_WeApp_SDK\Mysql` 命名空间，具体使用方法可以查看 [API 文档](https://github.com/tencentyun/wafer-php-server-sdk/blob/master/API.md)：

```javascript
use QCloud_WeApp_SDK\Mysql\Mysql as DB;

DB::insert('tableName', [
    'nickname' => 'Jason',
  	'age' => 21
]); // => 1
```

## Error: 未找到 project.config.json 中的 svr 字段。错误：10080

如果您想使用腾讯云微信小程序一站式解决方案，并使用微信开发者工具一键部署，微信开发者工具打开的目录必须包含 `project.config.json` 文件，文件必须是个 JSON 字符串并包含 `miniprogramRoot` 和 `qcloudRoot` 两个 `key`。实例文件如下：

```json
{
  "miniprogramRoot": "./client",
  "qcloudRoot": "./server"
}
```

文件中的 `miniprogramRoot` 表示小程序端代码，`qcloudRoot` 表示服务器端代码。点击腾讯云相关操作（如上传测试代码）的时候，只会把 `qcloudRoot` 指向的目录下的代码上传到开发（或生产）环境。具体可以查看[微信开发者工具官方文档](https://mp.weixin.qq.com/debug/wxadoc/dev/devtools/edit.html#项目配置文件)。

## 如何连接上服务器

新版小程序解决方案目前**暂无**计划支持开发服务器连接能力，您只能通过微信开发者工具上传、部署、调试代码。

## 真机预览的时候提示网络出错

<img src="https://mc.qcloudimg.com/static/img/049a1f8b5a477ebda6f088828f290e3c/8.png" width="240px" alt="真机预览的时候提示网络出错">

这种问题是因为开发域名不在安全域名列表里，可以点击界面右上角的三个小点，选择开启调试，就会绕过域名的验证

<img src="https://mc.qcloudimg.com/static/img/b192942b7593bcc344dfe89bd7fa2d3e/9.jpg" width="240px" alt="真机预览打开调试">