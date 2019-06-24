## 简介
本文档介绍如何不依赖 SDK，用简单的代码，在网页（Web 端）直传文件到 COS 的存储桶。

>! 本文档内容基于 XML 版本的 API 。

## 实践步骤
<span id="前期准备"></span>
### 1. 前期准备
1）登录  [COS 控制台](https://console.cloud.tencent.com/cos5) 并创建存储桶，得到 Bucket（存储桶名称） 和 Region（地域名称）。
2）登录 [密钥管理控制台](https://console.cloud.tencent.com/cam/capi) 获取您的项目 SecretId 和 SecretKey。
3）在 COS 控制台，进入新建的存储桶，单击【基础配置】页签。
4）下拉页面找到“跨域访问 CORS 设置”配置项，单击【添加规则】，配置示例如下图：
![](https://main.qcloudimg.com/raw/13bd2f5ad9d927b4a6f1f4f4d9605880.png)

>! 正式部署时服务端请加一层您的网站本身的权限检验。

### 3. 获取临时密钥和计算签名
出于安全考虑，签名使用临时密钥，服务端搭建临时密钥服务，可参考 [PHP 示例](https://github.com/tencentyun/cos-js-sdk-v5/blob/master/server/sts.php)、[Nodejs 示例](https://github.com/tencentyun/cos-js-sdk-v5/blob/master/server/sts.js)。
如有其他语言或自行实现可以看以下流程：
1）向服务端获取临时密钥,服务端首先使用固定密钥 SecretId、SecretKey 向 STS 服务获取临时密钥，得到临时密钥 tmpSecretId、tmpSecretKey、sessionToken，详情请参考 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048) 或 [cos-sts-sdk](https://github.com/tencentyun/qcloud-cos-sts-sdk) 文档；
2）前端通过 tmpSecretId、tmpSecretKey，以及 method、pathname 计算签名，可参考下文使用 [cos-auth.js](https://unpkg.com/cos-js-sdk-v5/demo/common/cos-auth.min.js) 来计算签名，如果业务需要也可以放在后端计算签名。
4）前端将 sessionToken 计算得到的签名 authorization，前端将服务端返回的两个值分别放到 header 的 x-cos-security-token 和  authorization 字段里，向 COS API 发出上传请求。

>! 正式部署时服务端请加一层您的网站本身的权限检验。

### 3. 前端上传
#### 方案 A：使用 AJAX 上传
AJAX 上传需要浏览器支持基本的 HTML5 特性，当前方案使用 [PUT Object ](https://cloud.tencent.com/document/product/436/7749)  文档，操作指引如下：
1）按照 [步骤1. 前期准备](#前期准备) 的步骤，准备存储桶的相关配置。
2）创建 `test.html` 文件，修改下方代码的 Bucket 和 Region，并复制到 `test.html` 文件。
3）部署后端的签名服务，并修改 `test.html` 里的签名服务地址。
4）将 `test.html` 放在 Web 服务器下，并通过浏览器访问页面，测试文件上传功能。

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Ajax Put 上传</title>
    <style>
        h1, h2 {
            font-weight: normal;
        }

        #msg {
            margin-top: 10px;
        }
    </style>
</head>
<body>

<h1>Ajax Put 上传</h1>

<input id="fileSelector" type="file">
<input id="submitBtn" type="submit">

<div id="msg"></div>

<script src="https://unpkg.com/cos-js-sdk-v5/demo/common/cos-auth.min.js"></script>
<script>
    (function () {
        // 请求用到的参数
        var Bucket = 'test-1250000000';
        var Region = 'ap-guangzhou';
        var protocol = location.protocol === 'https:' ? 'https:' : 'http:';
        var prefix = protocol + '//' + Bucket + '.cos.' + Region + '.myqcloud.com/';

        // 对更多字符编码的 url encode 格式
        var camSafeUrlEncode = function (str) {
            return encodeURIComponent(str)
                .replace(/!/g, '%21')
                .replace(/'/g, '%27')
                .replace(/\(/g, '%28')
                .replace(/\)/g, '%29')
                .replace(/\*/g, '%2A');
        };

        // 计算签名
        var getAuthorization = function (options, callback) {
            // var url = 'http://127.0.0.1:3000/sts-auth' +
            var url = '../server/sts.php';
            var xhr = new XMLHttpRequest();
            xhr.open('GET', url, true);
            xhr.onload = function (e) {
                var credentials;
                try {
                    credentials = (new Function('return ' + xhr.responseText))().credentials;
                } catch (e) {}
                if (credentials) {
                    callback(null, {
                        XCosSecurityToken: credentials.sessionToken,
                        Authorization: CosAuth({
                            SecretId: credentials.tmpSecretId,
                            SecretKey: credentials.tmpSecretKey,
                            Method: options.Method,
                            Pathname: options.Pathname,
                        })
                    });
                } else {
                    console.error(xhr.responseText);
                    callback('获取签名出错');
                }
            };
            xhr.onerror = function (e) {
                callback('获取签名出错');
            };
            xhr.send();
        };

        // 上传文件
        var uploadFile = function (file, callback) {
            var Key = 'dir/' + file.name; // 这里指定上传目录和文件名
            getAuthorization({Method: 'PUT', Pathname: '/' + Key}, function (err, info) {

                if (err) {
                    alert(err);
                    return;
                }

                var auth = info.Authorization;
                var XCosSecurityToken = info.XCosSecurityToken;
                var url = prefix + camSafeUrlEncode(Key).replace(/%2F/, '/');
                var xhr = new XMLHttpRequest();
                xhr.open('PUT', url, true);
                xhr.setRequestHeader('Authorization', auth);
                XCosSecurityToken && xhr.setRequestHeader('x-cos-security-token', XCosSecurityToken);
                xhr.upload.onprogress = function (e) {
                    console.log('上传进度 ' + (Math.round(e.loaded / e.total * 10000) / 100) + '%');
                };
                xhr.onload = function () {
                    if (xhr.status === 200 || xhr.status === 206) {
                        var ETag = xhr.getResponseHeader('etag');
                        callback(null, {url: url, ETag: ETag});
                    } else {
                        callback('文件 ' + Key + ' 上传失败，状态码：' + xhr.status);
                    }
                };
                xhr.onerror = function () {
                    callback('文件 ' + Key + ' 上传失败，请检查是否没配置 CORS 跨域规则');
                };
                xhr.send(file);
            });
        };

        // 监听表单提交
        document.getElementById('submitBtn').onclick = function (e) {
            var file = document.getElementById('fileSelector').files[0];
            if (!file) {
                document.getElementById('msg').innerText = '未选择上传文件';
                return;
            }
            file && uploadFile(file, function (err, data) {
                console.log(err || data);
                document.getElementById('msg').innerText = err ? err : ('上传成功，ETag=' + data.ETag);
            });
        };
    })();
</script>

</body>
</html>
```

执行效果如下图：
![Ajax 上传](https://main.qcloudimg.com/raw/4bfc2883d71deddccc76b250ebb6a051.png)

#### 方案 B：使用 Form 表单上传
Form 表单上传支持低版本的浏览器的上传（如 IE8），当前方案使用 [XML API 的 PostObject 接口](/doc/product/436/7751)。操作指引：
1）按照 [1. 前期准备](#前期准备) 的步骤，准备存储桶。
2）创建 `test.html` 文件，修改下方代码的 Bucket 和 Region，并复制到 `test.html` 文件。
3）部署后端的签名服务，并修改 `test.html` 里的签名服务地址。
4）在 `test.html` 同一个目录下，创建一个空的 `empty.html`，用于上传成功时跳转回来。
5）将 `test.html` 和 `empty.html` 放在 Web 服务器下，并通过浏览器访问页面，测试文件上传功能。

```html
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Form 表单简单上传</title>
    <style>h1, h2 {font-weight: normal;}#msg {margin-top:10px;}</style>
</head>
<body>

<h1>Form 表单简单上传（兼容 IE8）</h1>
<div>最低兼容到 IE6 上传，不支持 onprogress</div>

<form id="form" target="submitTarget" action="" method="post" enctype="multipart/form-data" accept="*/*">
    <input id="name" name="name" type="hidden" value="">
    <input name="success_action_status" type="hidden" value="200">
    <input id="success_action_redirect" name="success_action_redirect" type="hidden" value="">
    <input id="key" name="key" type="hidden" value="">
    <input id="Signature" name="Signature" type="hidden" value="">
    <input name="Content-Type" type="hidden" value="">
    <input id="x-cos-security-token" name="x-cos-security-token" type="hidden" value="">
    <input id="fileSelector" name="file" type="file">
    <input id="submitBtn" type="button" value="提交">
</form>
<iframe id="submitTarget" name="submitTarget" style="display:none;" frameborder="0"></iframe>

<div id="msg"></div>

<script src="https://unpkg.com/cos-js-sdk-v5/demo/common/cos-auth.min.js"></script>
<script>
    (function () {

        // 请求用到的参数
        var Bucket = 'test-1250000000';
        var Region = 'ap-guangzhou';
        var protocol = location.protocol === 'https:' ? 'https:' : 'http:';
        var prefix = protocol + '//' + Bucket + '.cos.' + Region + '.myqcloud.com/';
        var form = document.getElementById('form');
        form.action = prefix;

        // 对更多字符编码的 url encode 格式
        var camSafeUrlEncode = function (str) {
            return encodeURIComponent(str)
                .replace(/!/g, '%21')
                .replace(/'/g, '%27')
                .replace(/\(/g, '%28')
                .replace(/\)/g, '%29')
                .replace(/\*/g, '%2A');
        };

        // 计算签名
        var getAuthorization = function (options, callback) {
            // var url = 'http://127.0.0.1:3000/sts' +
            var url = '../server/sts.php';
            var xhr = new XMLHttpRequest();
            xhr.open('GET', url, true);
            xhr.onreadystatechange = function (e) {
                if (xhr.readyState === 4) {
                    if (xhr.status === 200) {
                        var credentials;
                        try {
                            credentials = (new Function('return ' + xhr.responseText))().credentials;
                        } catch (e) {}
                        if (credentials) {
                            callback(null, {
                                XCosSecurityToken: credentials.sessionToken,
                                Authorization: CosAuth({
                                    SecretId: credentials.tmpSecretId,
                                    SecretKey: credentials.tmpSecretKey,
                                    Method: options.Method,
                                    Pathname: options.Pathname,
                                })
                            });
                        } else {
                            console.error(xhr.responseText);
                            callback('获取签名出错');
                        }
                    } else {
                        callback('获取签名出错');
                    }
                }
            };
            xhr.send();
        };

        // 监听上传完成
        var Key;
        var submitTarget = document.getElementById('submitTarget');
        var showMessage = function (err, data) {
            console.log(err || data);
            document.getElementById('msg').innerText = err ? err : ('上传成功，ETag=' + data.ETag);
        };
        submitTarget.onload = function () {
            var search;
            try {
                search = submitTarget.contentWindow.location.search.substr(1);
            } catch (e) {
                showMessage('文件 ' + Key + ' 上传失败');
            }
            if (search) {
                var items = search.split('&');
                var i, arr, data = {};
                for (i = 0; i < items.length; i++) {
                    arr = items[i].split('=');
                    data[arr[0]] = decodeURIComponent(arr[1] || '');
                }
                showMessage(null, {url: prefix + camSafeUrlEncode(Key).replace(/%2F/g, '/'), ETag: data.etag});
            } else {
            }
        };

        // 发起上传
        document.getElementById('submitBtn').onclick = function (e) {
            var filePath = document.getElementById('fileSelector').value;
            if (!filePath) {
                document.getElementById('msg').innerText = '未选择上传文件';
                return;
            }
            Key = 'dir/' + filePath.match(/[\\\/]?([^\\\/]+)$/)[1]; // 这里指定上传目录和文件名
            getAuthorization({Method: 'POST', Pathname: '/'}, function (err, AuthData) {
                // 在当前目录下放一个空的 empty.html 以便让接口上传完成跳转回来
                document.getElementById('success_action_redirect').value = location.href.substr(0, location.href.lastIndexOf('/') + 1) + 'empty.html';
                document.getElementById('key').value = Key;
                document.getElementById('Signature').value = AuthData.Authorization;
                document.getElementById('x-cos-security-token').value = AuthData.XCosSecurityToken || '';
                form.submit();
            });
        };
    })();
</script>

</body>
</html>
```
执行效果如下图：
![Form 表单上传](https://main.qcloudimg.com/raw/ef666461bc5f88715f28934393ebe4f4.png)
## 相关文档
若您有更丰富的接口调用需求，请参考以下 JavaScript SDK 文档：
- [JavaScript SDK](https://cloud.tencent.com/document/product/436/11459)
- [JavaScript SDK（历史版本 API）](https://cloud.tencent.com/document/product/436/8095)
