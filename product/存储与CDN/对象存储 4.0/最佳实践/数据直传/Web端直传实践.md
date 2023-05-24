## 简介

本文档介绍如何不依赖 SDK，用简单的代码，在网页（Web 端）直传文件到对象存储（Cloud Object Storage，COS）的存储桶。

> ! 本文档内容基于 XML 版本的 [API](https://cloud.tencent.com/document/product/436/7751)。

<span id="1"></span>

## 前提条件

1. 登录 [COS 控制台](https://console.cloud.tencent.com/cos5) 并创建存储桶，得到 Bucket（存储桶名称） 和 Region（地域名称），详情请参见 [创建存储桶](https://cloud.tencent.com/document/product/436/13309) 文档。
2. 进入存储桶详情页，单击**安全管理**页签。下拉页面找到**跨域访问 CORS 设置**配置项，单击**添加规则**，配置示例如下图，详情请参见 [设置跨域访问](https://cloud.tencent.com/document/product/436/13318) 文档。
   ![](https://qcloudimg.tencent-cloud.cn/raw/703301dc63bd24f4051829df63f2919a.png)
3. 登录 [访问管理控制台](https://console.cloud.tencent.com/cam/capi)， 获取您的项目 SecretId 和 SecretKey。

## 方案对比

### 服务端计算签名（推荐）

1. 在前端选择文件，前端将后缀发送给服务端。
2. 服务端根据后缀，生成带时间的随机 COS 文件路径，并计算对应的 PostObject policy 签名，返回 URL 和签名信息给前端。
3. 前端使用 PUT 或 POST 请求，直传文件到 COS。

### 服务端返回临时密钥，前端计算签名

1. 前端请求服务端，服务端返回临时密钥。
2. 前端通过CosAuth和临时密钥计算签名。
3. 前端使用 PUT 或 POST 请求，直传文件到 COS。

## 实践步骤

> ! 正式部署时服务端请加一层您的网站本身的权限检验。

### 获取签名

方式一（推荐）：服务端计算签名返回给前端。

方式二：服务端返回临时密钥，前端利用临时密钥计算签名。

以上两种方式都可以在下方实现方式里查看 demo。

### 获取临时密钥

出于安全考虑，需要在前端计算签名时要使用临时密钥，服务端搭建临时密钥服务可参考 [PHP 示例](https://github.com/tencentyun/cos-js-sdk-v5/blob/master/server/sts.php)、[Nodejs 示例](https://github.com/tencentyun/cos-js-sdk-v5/blob/master/server/sts.js)。
如有其他语言或自行实现可以参考以下流程：

1. 向服务端获取临时密钥，服务端首先使用固定密钥 SecretId、SecretKey 向 STS 服务获取临时密钥，得到临时密钥 tmpSecretId、tmpSecretKey、sessionToken，详情请参考 [临时密钥生成及使用指引](https://cloud.tencent.com/document/product/436/14048) 或 [cos-sts-sdk](https://github.com/tencentyun/qcloud-cos-sts-sdk) 文档。

> !根据使用的请求是 put 还是 post，STS 的 policy action 要加上允许 "name/cos:PutObject"或"name/cos:PostObject"。

2. 前端通过 tmpSecretId、tmpSecretKey，以及 method、pathname 计算签名，可参考下文使用 [cos-auth.js](https://unpkg.com/cos-js-sdk-v5/demo/common/cos-auth.min.js) 来计算签名。
3. 如果使用 PutObject 接口上传文件，将签名和 sessionToken，分别放到发请求时 header 的 authorization 和 x-cos-security-token 字段里。
   如果使用 PostObject 接口上传文件，则将签名和 sessionToken，分别放到发请求时表单的 Signature 和 x-cos-security-token 字段里。

## 实现方式

以下代码同时举例了 [PUT Object ](https://cloud.tencent.com/document/product/436/7749) 接口（推荐使用）和[POST Object ](https://cloud.tencent.com/document/product/436/14690) 接口，操作指引如下：

### 方式一：服务端计算签名（推荐）

注意：服务端计算签名的方式中文件的上传路径由服务端指定，安全性更高。

#### 使用 AJAX PUT 上传

AJAX 上传需要浏览器支持基本的 HTML5 特性，当前方案使用 [PUT Object ](https://cloud.tencent.com/document/product/436/7749) 文档，操作指引如下：

1. 按照 [前提条件](#1) 的步骤，准备存储桶的相关配置。
2. 创建`test.html`文件，修改下方代码的 Bucket 和 Region，并复制到`test.html`文件。
3. 部署后端的签名服务，并修改`test.html`里的签名服务地址。
4. 将`test.html`放在 Web 服务器下，并通过浏览器访问页面，测试文件上传功能。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Ajax Put 上传（服务端计算签名）</title>
    <style>
      h1,
      h2 {
        font-weight: normal;
      }

      #msg {
        margin-top: 10px;
      }
    </style>
  </head>
  <body>
    <h1>Ajax Put 上传（服务端计算签名）</h1>

    <input id="fileSelector" type="file" />
    <input id="submitBtn" type="submit" />

    <div id="msg"></div>

    <script>
      (function () {
        // 对更多字符编码的 url encode 格式
        const camSafeUrlEncode = function (str) {
          return encodeURIComponent(str)
            .replace(/!/g, '%21')
            .replace(/'/g, '%27')
            .replace(/\(/g, '%28')
            .replace(/\)/g, '%29')
            .replace(/\*/g, '%2A');
        };

        // 计算签名
        const getAuthorization = function (opt, callback) {
          // 替换为自己服务端地址 获取put上传签名
          const url = `http://127.0.0.1:3000/put-sign?ext=${opt.ext}`;
          const xhr = new XMLHttpRequest();
          xhr.open('GET', url, true);
          xhr.onload = function (e) {
            let credentials;
            try {
              const result = JSON.parse(e.target.responseText);
              credentials = result;
            } catch (e) {
              callback('获取签名出错');
            }
            if (credentials) {
              callback(null, {
                securityToken: credentials.sessionToken,
                authorization: credentials.authorization,
                cosKey: credentials.cosKey,
                cosHost: credentials.cosHost,
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
        const uploadFile = function (file, callback) {
          const fileName = file.name;
          let ext = '';
          const lastDotIndex = fileName.lastIndexOf('.');
          if (lastDotIndex > -1) {
            // 这里获取文件后缀 由服务端生成最终上传的路径
            ext = fileName.substring(lastDotIndex + 1);
          }
          getAuthorization({ ext }, function (err, info) {
            if (err) {
              alert(err);
              return;
            }
            const auth = info.authorization;
            const securityToken = info.securityToken;
            const Key = info.cosKey;
            const protocol =
              location.protocol === 'https:' ? 'https:' : 'http:';
            const prefix = protocol + '//' + info.cosHost;
            const url =
              prefix + '/' + camSafeUrlEncode(Key).replace(/%2F/g, '/');
            const xhr = new XMLHttpRequest();
            xhr.open('PUT', url, true);
            xhr.setRequestHeader('Authorization', auth);
            securityToken &&
              xhr.setRequestHeader('x-cos-security-token', securityToken);
            xhr.upload.onprogress = function (e) {
              console.log(
                '上传进度 ' +
                  Math.round((e.loaded / e.total) * 10000) / 100 +
                  '%'
              );
            };
            xhr.onload = function () {
              if (/^2\d\d$/.test('' + xhr.status)) {
                const ETag = xhr.getResponseHeader('etag');
                callback(null, { url: url, ETag: ETag });
              } else {
                callback('文件 ' + Key + ' 上传失败，状态码：' + xhr.status);
              }
            };
            xhr.onerror = function () {
              callback(
                '文件 ' + Key + ' 上传失败，请检查是否没配置 CORS 跨域规则'
              );
            };
            xhr.send(file);
          });
        };

        // 监听表单提交
        document.getElementById('submitBtn').onclick = function (e) {
          const file = document.getElementById('fileSelector').files[0];
          if (!file) {
            document.getElementById('msg').innerText = '未选择上传文件';
            return;
          }
          file &&
            uploadFile(file, function (err, data) {
              console.log(err || data);
              document.getElementById('msg').innerText = err
                ? err
                : '上传成功，ETag=' + data.ETag;
            });
        };
      })();
    </script>
  </body>
</html>
```

执行效果如下图：
![Ajax 上传](https://main.qcloudimg.com/raw/4bfc2883d71deddccc76b250ebb6a051.png)

#### 使用 AJAX POST 上传

AJAX 上传需要浏览器支持基本的 HTML5 特性，当前方案使用 [Post Object ](https://cloud.tencent.com/document/product/436/14690) 接口。操作指引：

1. 按照 [前提条件](#1) 的步骤，准备存储桶的相关配置。
2. 创建`test.html`文件，修改下方代码的 Bucket 和 Region，并复制到`test.html`文件。
3. 部署后端的签名服务，并修改`test.html`里的签名服务地址。
4. 将`test.html`放在 Web 服务器下，并通过浏览器访问页面，测试文件上传功能。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Ajax Post 上传（服务端计算签名）</title>
    <style>
      h1,
      h2 {
        font-weight: normal;
      }

      #msg {
        margin-top: 10px;
      }
    </style>
  </head>
  <body>
    <h1>PostObject 上传（服务端计算签名）</h1>

    <input id="fileSelector" type="file" />
    <input id="submitBtn" type="submit" />

    <div id="msg"></div>

    <script>
      (function () {
        let prefix = '';
        let Key = '';

        // 对更多字符编码的 url encode 格式
        const camSafeUrlEncode = function (str) {
          return encodeURIComponent(str)
            .replace(/!/g, '%21')
            .replace(/'/g, '%27')
            .replace(/\(/g, '%28')
            .replace(/\)/g, '%29')
            .replace(/\*/g, '%2A');
        };

        // 获取权限策略
        const getPostPolicyCredentials = function (opt, callback) {
          // 替换为自己服务端地址 获取post上传签名
          const url = `http://127.0.0.1:3000/post-policy?ext=${opt.ext}`;
          const xhr = new XMLHttpRequest();
          xhr.open('GET', url, true);
          xhr.onload = function (e) {
            let credentials;
            try {
              const result = JSON.parse(e.target.responseText);
              credentials = result;
            } catch (e) {
              callback('获取签名出错');
            }
            if (credentials) {
              callback(null, {
                securityToken: credentials.sessionToken,
                cosKey: credentials.cosKey,
                cosHost: credentials.cosHost,
                policy: credentials.policy,
                qAk: credentials.qAk,
                qKeyTime: credentials.qKeyTime,
                qSignAlgorithm: credentials.qSignAlgorithm,
                qSignature: credentials.qSignature,
              });
            } else {
              console.error(xhr.responseText);
              callback('获取签名出错');
            }
          };
          xhr.send();
        };

        // 上传文件
        const uploadFile = function (file, callback) {
          const fileName = file.name;
          let ext = '';
          const lastDotIndex = fileName.lastIndexOf('.');
          if (lastDotIndex > -1) {
            // 这里获取文件后缀 由服务端生成最终上传的路径
            ext = fileName.substring(lastDotIndex + 1);
          }
          getPostPolicyCredentials({ ext }, function (err, credentials) {
            const protocol =
              location.protocol === 'https:' ? 'https:' : 'http:';
            prefix = protocol + '//' + credentials.cosHost;
            Key = credentials.cosKey;
            const fd = new FormData();

            // 在当前目录下放一个空的 empty.html 以便让接口上传完成跳转回来
            fd.append('key', Key);

            // 使用 policy 签名保护格式
            credentials.securityToken &&
              fd.append('x-cos-security-token', credentials.securityToken);
            fd.append('q-sign-algorithm', credentials.qSignAlgorithm);
            fd.append('q-ak', credentials.qAk);
            fd.append('q-key-time', credentials.qKeyTime);
            fd.append('q-signature', credentials.qSignature);
            fd.append('policy', credentials.policy);

            // 文件内容，file 字段放在表单最后，避免文件内容过长影响签名判断和鉴权
            fd.append('file', file);

            // xhr
            const url = prefix;
            const xhr = new XMLHttpRequest();
            xhr.open('POST', url, true);
            xhr.upload.onprogress = function (e) {
              console.log(
                '上传进度 ' +
                  Math.round((e.loaded / e.total) * 10000) / 100 +
                  '%'
              );
            };
            xhr.onload = function () {
              if (Math.floor(xhr.status / 100) === 2) {
                const ETag = xhr.getResponseHeader('etag');
                callback(null, {
                  url:
                    prefix + '/' + camSafeUrlEncode(Key).replace(/%2F/g, '/'),
                  ETag: ETag,
                });
              } else {
                callback('文件 ' + Key + ' 上传失败，状态码：' + xhr.status);
              }
            };
            xhr.onerror = function () {
              callback(
                '文件 ' + Key + ' 上传失败，请检查是否没配置 CORS 跨域规则'
              );
            };
            xhr.send(fd);
          });
        };

        // 监听表单提交
        document.getElementById('submitBtn').onclick = function (e) {
          const file = document.getElementById('fileSelector').files[0];
          if (!file) {
            document.getElementById('msg').innerText = '未选择上传文件';
            return;
          }
          file &&
            uploadFile(file, function (err, data) {
              console.log(err || data);
              document.getElementById('msg').innerText = err
                ? err
                : '上传成功，ETag=' + data.ETag + 'url=' + data.url;
            });
        };
      })();
    </script>
  </body>
</html>
```

执行效果如下图：
![Ajax 上传](https://main.qcloudimg.com/raw/4bfc2883d71deddccc76b250ebb6a051.png)

#### 使用 Form 表单上传

Form 表单上传支持低版本的浏览器的上传（如 IE8），当前方案使用 [Post Object ](https://cloud.tencent.com/document/product/436/14690) 接口。操作指引：

1. 按照 [前提条件](#1) 的步骤，准备存储桶。
2. 创建`test.html`文件，修改下方代码的 Bucket 和 Region，并复制到`test.html`文件。
3. 部署后端的签名服务，并修改`test.html`里的签名服务地址。
4. 在`test.html`同一个目录下，创建一个空的`empty.html`，用于上传成功时跳转回来。
5. 将`test.html`和`empty.html`放在 Web 服务器下，并通过浏览器访问页面，测试文件上传功能。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Form 表单简单上传（兼容 IE8）（服务端计算签名）</title>
    <style>
      h1,
      h2 {
        font-weight: normal;
      }
      #msg {
        margin-top: 10px;
      }
    </style>
  </head>
  <body>
    <h1>Form 表单简单上传（兼容 IE8）（服务端计算签名）</h1>
    <div>最低兼容到 IE6 上传，不支持 onprogress</div>

    <form
      id="form"
      target="submitTarget"
      action=""
      method="post"
      enctype="multipart/form-data"
      accept="*/*"
    >
      <input id="name" name="name" type="hidden" value="" />
      <input name="success_action_status" type="hidden" value="200" />
      <input
        id="success_action_redirect"
        name="success_action_redirect"
        type="hidden"
        value=""
      />
      <input id="key" name="key" type="hidden" value="" />
      <input id="policy" name="policy" type="hidden" value="" />
      <input
        id="q-sign-algorithm"
        name="q-sign-algorithm"
        type="hidden"
        value=""
      />
      <input id="q-ak" name="q-ak" type="hidden" value="" />
      <input id="q-key-time" name="q-key-time" type="hidden" value="" />
      <input id="q-signature" name="q-signature" type="hidden" value="" />
      <input name="Content-Type" type="hidden" value="" />
      <input
        id="x-cos-security-token"
        name="x-cos-security-token"
        type="hidden"
        value=""
      />

      <!-- file 字段放在表单最后，避免文件内容过长影响签名判断和鉴权 -->
      <input id="fileSelector" name="file" type="file" />
      <input id="submitBtn" type="button" value="提交" />
    </form>
    <iframe
      id="submitTarget"
      name="submitTarget"
      style="display: none"
      frameborder="0"
    ></iframe>

    <div id="msg"></div>

    <script>
      (function () {
        const form = document.getElementById('form');
        let prefix = '';

        // 对更多字符编码的 url encode 格式
        const camSafeUrlEncode = function (str) {
          return encodeURIComponent(str)
            .replace(/!/g, '%21')
            .replace(/'/g, '%27')
            .replace(/\(/g, '%28')
            .replace(/\)/g, '%29')
            .replace(/\*/g, '%2A');
        };

        // 计算签名
        const getAuthorization = function (opt, callback) {
          // 替换为自己服务端地址 获取post上传签名
          const url = `http://127.0.0.1:3000/post-policy?ext=${opt.ext || ''}`;
          const xhr = new XMLHttpRequest();
          xhr.open('GET', url, true);
          xhr.onload = function (e) {
            let credentials;
            try {
              const result = JSON.parse(e.target.responseText);
              credentials = result;
            } catch (e) {
              callback('获取签名出错');
            }
            if (credentials) {
              callback(null, {
                securityToken: credentials.sessionToken,
                cosKey: credentials.cosKey,
                cosHost: credentials.cosHost,
                policy: credentials.policy,
                qAk: credentials.qAk,
                qKeyTime: credentials.qKeyTime,
                qSignAlgorithm: credentials.qSignAlgorithm,
                qSignature: credentials.qSignature,
              });
            } else {
              console.error(xhr.responseText);
              callback('获取签名出错');
            }
          };
          xhr.send();
        };

        // 监听上传完成
        let Key;
        const submitTarget = document.getElementById('submitTarget');
        const showMessage = function (err, data) {
          console.log(err || data);
          document.getElementById('msg').innerText = err
            ? err
            : '上传成功，ETag=' + data.ETag;
        };
        submitTarget.onload = function () {
          let search;
          try {
            search = submitTarget.contentWindow.location.search.substr(1);
          } catch (e) {
            showMessage('文件 ' + Key + ' 上传失败');
          }
          if (search) {
            const items = search.split('&');
            let i = 0;
            let arr = [];
            const data = {};
            for (i = 0; i < items.length; i++) {
              arr = items[i].split('=');
              data[arr[0]] = decodeURIComponent(arr[1] || '');
            }
            showMessage(null, {
              url: prefix + camSafeUrlEncode(Key).replace(/%2F/g, '/'),
              ETag: data.etag,
            });
          } else {
          }
        };

        // 发起上传
        document.getElementById('submitBtn').onclick = function (e) {
          const filePath = document.getElementById('fileSelector').value;
          if (!filePath) {
            document.getElementById('msg').innerText = '未选择上传文件';
            return;
          }
          let ext = '';
          const lastDotIndex = filePath.lastIndexOf('.');
          if (lastDotIndex > -1) {
            // 这里获取文件后缀 由服务端生成最终上传的路径
            ext = filePath.substring(lastDotIndex + 1);
          }
          getAuthorization({ ext }, function (err, AuthData) {
            const protocol =
              location.protocol === 'https:' ? 'https:' : 'http:';
            prefix = protocol + '//' + AuthData.cosHost;
            form.action = prefix;
            Key = AuthData.cosKey;
            // 在当前目录下放一个空的 empty.html 以便让接口上传完成跳转回来
            document.getElementById('success_action_redirect').value =
              location.href.substr(0, location.href.lastIndexOf('/') + 1) +
              'empty.html';
            document.getElementById('key').value = AuthData.cosKey;
            document.getElementById('policy').value = AuthData.policy;
            document.getElementById('q-sign-algorithm').value =
              AuthData.qSignAlgorithm;
            document.getElementById('q-ak').value = AuthData.qAk;
            document.getElementById('q-key-time').value = AuthData.qKeyTime;
            document.getElementById('q-signature').value = AuthData.qSignature;
            document.getElementById('x-cos-security-token').value =
              AuthData.securityToken || '';
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

### 方式二：服务端返回临时密钥，前端计算签名

#### 使用 AJAX PUT 上传

与方式一的 AJAX PUT 上传大致相同，区别在于签名放在前端计算，服务端只返回计算签名用的临时秘钥信息。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Ajax Put 上传（前端计算签名）</title>
    <style>
      h1,
      h2 {
        font-weight: normal;
      }

      #msg {
        margin-top: 10px;
      }
    </style>
  </head>
  <body>
    <h1>Ajax Put 上传（前端计算签名）</h1>

    <input id="fileSelector" type="file" />
    <input id="submitBtn" type="submit" />

    <div id="msg"></div>

    <!-- 签名计算 可通过（https://unpkg.com/cos-js-sdk-v5/demo/common/cos-auth.min.js）下载 -->
    <script src="./cos-auth.js"></script>
    <script>
      (function () {
        // 请求用到的参数
        const Bucket = 'test-1300555317'; // 替换为自己的存储桶
        const Region = 'ap-beijing'; // 替换为自己的存储桶地域
        const protocol = location.protocol === 'https:' ? 'https:' : 'http:';
        const prefix =
          protocol + '//' + Bucket + '.cos.' + Region + '.myqcloud.com'; // prefix 用于拼接请求

        // 对更多字符编码的 url encode 格式
        const camSafeUrlEncode = function (str) {
          return encodeURIComponent(str)
            .replace(/!/g, '%21')
            .replace(/'/g, '%27')
            .replace(/\(/g, '%28')
            .replace(/\)/g, '%29')
            .replace(/\*/g, '%2A');
        };

        // 计算签名
        const getauthorization = function (opt, callback) {
          // 替换为自己服务端地址 获取临时密钥
          const url = `http://127.0.0.1:3000/sts`;
          const xhr = new XMLHttpRequest();
          xhr.open('GET', url, true);
          xhr.onload = function (e) {
            let result;
            try {
              result = JSON.parse(e.target.responseText);
            } catch (e) {
              callback('获取签名出错');
            }
            if (result) {
              // 使用CosAuth 利用返回的临时密钥计算签名
              const authorization = CosAuth({
                SecretId: result.credentials.tmpSecretId,
                SecretKey: result.credentials.tmpSecretKey,
                Method: opt.Method,
                Pathname: opt.Pathname,
              });
              callback(null, {
                securityToken: result.credentials.sessionToken,
                authorization: authorization,
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
        const uploadFile = function (file, callback) {
          const Key = file.name;
          getauthorization(
            { Method: 'PUT', Pathname: '/' + Key },
            function (err, info) {
              if (err) {
                alert(err);
                return;
              }
              const auth = info.authorization;
              const securityToken = info.securityToken;
              const url =
                prefix + '/' + camSafeUrlEncode(Key).replace(/%2F/g, '/');
              const xhr = new XMLHttpRequest();
              xhr.open('PUT', url, true);
              xhr.setRequestHeader('authorization', auth);
              securityToken &&
                xhr.setRequestHeader('x-cos-security-token', securityToken);
              xhr.upload.onprogress = function (e) {
                console.log(
                  '上传进度 ' +
                    Math.round((e.loaded / e.total) * 10000) / 100 +
                    '%'
                );
              };
              xhr.onload = function () {
                if (/^2\d\d$/.test('' + xhr.status)) {
                  const ETag = xhr.getResponseHeader('etag');
                  callback(null, { url: url, ETag: ETag });
                } else {
                  callback('文件 ' + Key + ' 上传失败，状态码：' + xhr.status);
                }
              };
              xhr.onerror = function () {
                callback(
                  '文件 ' + Key + ' 上传失败，请检查是否没配置 CORS 跨域规则'
                );
              };
              xhr.send(file);
            }
          );
        };

        // 监听表单提交
        document.getElementById('submitBtn').onclick = function (e) {
          const file = document.getElementById('fileSelector').files[0];
          if (!file) {
            document.getElementById('msg').innerText = '未选择上传文件';
            return;
          }
          file &&
            uploadFile(file, function (err, data) {
              console.log(err || data);
              document.getElementById('msg').innerText = err
                ? err
                : '上传成功，ETag=' + data.ETag + 'url=' + data.url;
            });
        };
      })();
    </script>
  </body>
</html>
```

执行效果如下图：
![Ajax 上传](https://main.qcloudimg.com/raw/4bfc2883d71deddccc76b250ebb6a051.png)

#### 使用 AJAX POST 上传

与方式一的 AJAX POST 上传大致相同，区别在于签名放在前端计算，服务端只返回计算签名用的临时秘钥信息。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Ajax Post 上传（前端计算签名）</title>
    <style>
      h1,
      h2 {
        font-weight: normal;
      }

      #msg {
        margin-top: 10px;
      }
    </style>
  </head>
  <body>
    <h1>PostObject 上传（前端计算签名）</h1>

    <input id="fileSelector" type="file" />
    <input id="submitBtn" type="submit" />

    <div id="msg"></div>

    <!-- 签名计算 可通过（https://unpkg.com/cos-js-sdk-v5/demo/common/cos-auth.min.js）下载 -->
    <script src="./cos-auth.js"></script>
    <script>
      (function () {
        // 请求用到的参数
        const Bucket = 'test-1300555317'; // 替换为自己的存储桶
        const Region = 'ap-beijing'; // 替换为自己的存储桶地域
        const protocol = location.protocol === 'https:' ? 'https:' : 'http:';
        const prefix =
          protocol + '//' + Bucket + '.cos.' + Region + '.myqcloud.com'; // prefix 用于拼接请求

        // 对更多字符编码的 url encode 格式
        const camSafeUrlEncode = function (str) {
          return encodeURIComponent(str)
            .replace(/!/g, '%21')
            .replace(/'/g, '%27')
            .replace(/\(/g, '%28')
            .replace(/\)/g, '%29')
            .replace(/\*/g, '%2A');
        };

        // 获取权限策略
        const getAuthorization = function (opt, callback) {
          // 替换为自己服务端地址 获取临时密钥
          const url = `http://127.0.0.1:3000/sts`;
          const xhr = new XMLHttpRequest();
          xhr.open('GET', url, true);
          xhr.onload = function (e) {
            let result;
            try {
              result = JSON.parse(e.target.responseText);
            } catch (e) {
              callback('获取签名出错');
            }
            if (result) {
              // 使用CosAuth利用返回的临时密钥计算签名
              const policyInfo = CosAuth({
                Version: 'post-object-policy', // 必传 写死 用于post签名计算
                SecretId: result.credentials.tmpSecretId,
                SecretKey: result.credentials.tmpSecretKey,
                Bucket,
                Key: opt.Key,
              });
              callback(null, {
                securityToken: result.credentials.sessionToken,
                policyInfo: policyInfo,
              });
            } else {
              console.error(xhr.responseText);
              callback('获取签名出错');
            }
          };
          xhr.send();
        };

        // 上传文件
        const uploadFile = function (file, callback) {
          const Key = file.name;
          getAuthorization({ Key }, function (err, credentials) {
            const fd = new FormData();

            // 在当前目录下放一个空的 empty.html 以便让接口上传完成跳转回来
            fd.append('key', Key);

            // 使用 policy 签名保护格式
            credentials.securityToken &&
              fd.append('x-cos-security-token', credentials.securityToken);
            fd.append(
              'q-sign-algorithm',
              credentials.policyInfo.qSignAlgorithm
            );
            fd.append('q-ak', credentials.policyInfo.qAk);
            fd.append('q-key-time', credentials.policyInfo.qKeyTime);
            fd.append('q-signature', credentials.policyInfo.qSignature);
            fd.append('policy', credentials.policyInfo.policy);

            // 文件内容，file 字段放在表单最后，避免文件内容过长影响签名判断和鉴权
            fd.append('file', file);

            // xhr
            const url = prefix;
            const xhr = new XMLHttpRequest();
            xhr.open('POST', url, true);
            xhr.upload.onprogress = function (e) {
              console.log(
                '上传进度 ' +
                  Math.round((e.loaded / e.total) * 10000) / 100 +
                  '%'
              );
            };
            xhr.onload = function () {
              if (Math.floor(xhr.status / 100) === 2) {
                const ETag = xhr.getResponseHeader('etag');
                callback(null, {
                  url:
                    prefix + '/' + camSafeUrlEncode(Key).replace(/%2F/g, '/'),
                  ETag: ETag,
                });
              } else {
                callback('文件 ' + Key + ' 上传失败，状态码：' + xhr.status);
              }
            };
            xhr.onerror = function () {
              callback(
                '文件 ' + Key + ' 上传失败，请检查是否没配置 CORS 跨域规则'
              );
            };
            xhr.send(fd);
          });
        };

        // 监听表单提交
        document.getElementById('submitBtn').onclick = function (e) {
          const file = document.getElementById('fileSelector').files[0];
          if (!file) {
            document.getElementById('msg').innerText = '未选择上传文件';
            return;
          }
          file &&
            uploadFile(file, function (err, data) {
              console.log(err || data);
              document.getElementById('msg').innerText = err
                ? err
                : '上传成功，ETag=' + data.ETag + 'url=' + data.url;
            });
        };
      })();
    </script>
  </body>
</html>
```

执行效果如下图：
![Ajax 上传](https://main.qcloudimg.com/raw/4bfc2883d71deddccc76b250ebb6a051.png)

#### 使用 Form 表单上传

与方式一的 Form 表单上传大致相同，区别在于签名放在前端计算，服务端只返回计算签名用的临时秘钥信息。

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Form 表单简单上传（兼容 IE8）（前端计算签名）</title>
    <style>
      h1,
      h2 {
        font-weight: normal;
      }
      #msg {
        margin-top: 10px;
      }
    </style>
  </head>
  <body>
    <h1>Form 表单简单上传（兼容 IE8）（前端计算签名）</h1>
    <div>最低兼容到 IE6 上传，不支持 onprogress</div>

    <form
      id="form"
      target="submitTarget"
      action=""
      method="post"
      enctype="multipart/form-data"
      accept="*/*"
    >
      <input id="name" name="name" type="hidden" value="" />
      <input name="success_action_status" type="hidden" value="200" />
      <input
        id="success_action_redirect"
        name="success_action_redirect"
        type="hidden"
        value=""
      />
      <input id="key" name="key" type="hidden" value="" />
      <input id="policy" name="policy" type="hidden" value="" />
      <input
        id="q-sign-algorithm"
        name="q-sign-algorithm"
        type="hidden"
        value=""
      />
      <input id="q-ak" name="q-ak" type="hidden" value="" />
      <input id="q-key-time" name="q-key-time" type="hidden" value="" />
      <input id="q-signature" name="q-signature" type="hidden" value="" />
      <input name="Content-Type" type="hidden" value="" />
      <input
        id="x-cos-security-token"
        name="x-cos-security-token"
        type="hidden"
        value=""
      />

      <!-- file 字段放在表单最后，避免文件内容过长影响签名判断和鉴权 -->
      <input id="fileSelector" name="file" type="file" />
      <input id="submitBtn" type="button" value="提交" />
    </form>
    <iframe
      id="submitTarget"
      name="submitTarget"
      style="display: none"
      frameborder="0"
    ></iframe>

    <div id="msg"></div>

    <!-- 签名计算 可通过（https://unpkg.com/cos-js-sdk-v5/demo/common/cos-auth.min.js）下载 -->
    <script src="./cos-auth.js"></script>
    <script>
      (function () {
        // 请求用到的参数
        const Bucket = 'test-1300555317'; // 替换为自己的存储桶
        const Region = 'ap-beijing'; // 替换为自己的存储桶地域
        const protocol = location.protocol === 'https:' ? 'https:' : 'http:';
        const prefix =
          protocol + '//' + Bucket + '.cos.' + Region + '.myqcloud.com'; // prefix 用于拼接请求
        const form = document.getElementById('form');
        form.action = prefix;

        // 对更多字符编码的 url encode 格式
        const camSafeUrlEncode = function (str) {
          return encodeURIComponent(str)
            .replace(/!/g, '%21')
            .replace(/'/g, '%27')
            .replace(/\(/g, '%28')
            .replace(/\)/g, '%29')
            .replace(/\*/g, '%2A');
        };

        // 计算签名
        const getAuthorization = function (opt, callback) {
          // 替换为自己服务端地址 获取临时密钥
          const url = `http://127.0.0.1:3000/sts`;
          const xhr = new XMLHttpRequest();
          xhr.open('GET', url, true);
          xhr.onload = function (e) {
            let result;
            try {
              result = JSON.parse(e.target.responseText);
            } catch (e) {
              callback('获取签名出错');
            }
            if (result) {
              // 使用CosAuth 利用返回的临时密钥计算签名
              const policyInfo = CosAuth({
                Version: 'post-object-policy', // 必传 写死 用于post签名计算
                SecretId: result.credentials.tmpSecretId,
                SecretKey: result.credentials.tmpSecretKey,
                Bucket,
                Key: opt.Key,
              });
              callback(null, {
                securityToken: result.credentials.sessionToken,
                policyInfo: policyInfo,
              });
            } else {
              console.error(xhr.responseText);
              callback('获取签名出错');
            }
          };
          xhr.send();
        };

        // 监听上传完成
        let Key;
        const submitTarget = document.getElementById('submitTarget');
        const showMessage = function (err, data) {
          console.log(err || data);
          document.getElementById('msg').innerText = err
            ? err
            : '上传成功，ETag=' + data.ETag;
        };
        submitTarget.onload = function () {
          let search;
          try {
            search = submitTarget.contentWindow.location.search.substr(1);
          } catch (e) {
            showMessage('文件 ' + Key + ' 上传失败');
          }
          if (search) {
            const items = search.split('&');
            let i = 0;
            let arr = [];
            const data = {};
            for (i = 0; i < items.length; i++) {
              arr = items[i].split('=');
              data[arr[0]] = decodeURIComponent(arr[1] || '');
            }
            showMessage(null, {
              url: prefix + camSafeUrlEncode(Key).replace(/%2F/g, '/'),
              ETag: data.etag,
            });
          } else {
          }
        };

        // 发起上传
        document.getElementById('submitBtn').onclick = function (e) {
          const file = document.getElementById('fileSelector').files[0];
          if (!file) {
            document.getElementById('msg').innerText = '未选择上传文件';
            return;
          }
          Key = file.name;
          getAuthorization({ Key }, function (err, AuthData) {
            // 在当前目录下放一个空的 empty.html 以便让接口上传完成跳转回来
            document.getElementById('success_action_redirect').value =
              location.href.substr(0, location.href.lastIndexOf('/') + 1) +
              'empty.html';
            document.getElementById('key').value = Key;
            document.getElementById('policy').value =
              AuthData.policyInfo.policy;
            document.getElementById('q-sign-algorithm').value =
              AuthData.policyInfo.qSignAlgorithm;
            document.getElementById('q-ak').value = AuthData.policyInfo.qAk;
            document.getElementById('q-key-time').value =
              AuthData.policyInfo.qKeyTime;
            document.getElementById('q-signature').value =
              AuthData.policyInfo.qSignature;
            document.getElementById('x-cos-security-token').value =
              AuthData.securityToken || '';
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
