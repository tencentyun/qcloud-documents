## SDK集成
1. 页面中引入js脚本 
https://qzonestyle.gtimg.cn/open/qcloud/js/vod/sdk/uploaderh5V3.js

2. 服务器端部署 [calculator_worker_sha1.js](http://video.qcloud.com/calculator_worker_sha1.js), 该文件用于计算待上传文件的sha1，一般情况把直接该js文件下载到上传服务同域名根目录下即可。之所以有同域的限制，是因为SDK使用了html5 worker异步计算SHA1，优化上传体验，而同域是html5 worker本身的限制。

## 本地视频上传

### 上传组件初始化

```javascript
var ErrorCode = qcVideo.get('ErrorCode');
ErrorCode.UN_SUPPORT_BROWSE !== qcVideo.uploader.init(
        //1: 上传基础条件
        {
            web_upload_url: 'https://vod2.qcloud.com/v2/index.php',
            upBtnId: upBtnId, //上传按钮ID（任意页面元素ID）
            secretId: secretId, // 云api secretId
            secretKey: secretKey, //云api secretKey: [选填参数] （secretKey不能暴露给外部用户，建议只在内部系统或者测试时使用该参数）
            /*
                @desc 获取签名的方法  [选填参数]
                server端实现要求：
                对argStr用secretKey进行sha1操作，其结果与原argStr拼接后再进行标准base64编码
                php示例：
                    base64_encode(hash_hmac('sha1', $argStr, $secretKey, true).$argStr);
            */
            getSignature: function(argStr,done){
                $.ajax({
                    'dataType': 'json',
                    'url': 'http://计算签名的服务器地址?args='+encodeURIComponent(argStr),
                    'success': function(signature) {
                        done(signature);
                    }
                });
            },

            ,after_sha_start_upload: false //上传分为两个阶段，sha计算和文件网络传输；这个选项设置是否在sha计算完成后，立即进行网络传输上传 (默认非立即上传)
            ,sha1js_path: 'http://您的域名/您的设置目录/计算sha1脚本.js' //计算sha1的位置  ，默认为 'http://你的域名/calculator_worker_sha1.js'
            ,isUGC: true
            ,expiredAfter: 1000 * 60 * 60 * 6 // 视频文件签名过期时间，默认6小时
            ,uid: '12345' // 自定义用户标识
        }
        //2: 回调函数
        , {
            /**
            * 更新文件状态和进度
            * @param args { id: 文件ID, size: 文件大小, name: 文件名称, status: 状态, percent: 进度,speed: 速度, errorCode: 错误码 }
            */
            onFileUpdate: function (args) {
                console.log(args);
            },
            /**
            * 文件状态发生变化
            * @param info  { done: 完成数量 , fail: 失败数量 , sha: 计算SHA或者等待计算SHA中的数量 , wait: 等待上传数量 , uploading: 上传中的数量 }
            */
            onFileStatus: function (info) {
                console.log('各状态总数' , info);
            },
            /**
            *  上传时错误文件过滤提示
            * @param args {code:{-1: 文件类型异常,-2: 文件名异常} , message: 错误原因 ， solution: 解决方法 }
            */
            onFilterError: function (args) {
                console.log('message:' + args.message + (args.solution ? (';solution==' + args.solution) : ''));
            }
        }
    ));
```

## demo
```javascript
qcVideo.uploader.init(
        {
            upBtnId: upBtnId,
            secretId: secretId,
            getSignature: function(argStr,done){
                $.ajax({
                    'dataType': 'json',
                    'url': 'http://yourdomain?args='+encodeURIComponent(argStr),
                    'success': function(signature) {
                        done(signature);
                    }
                });
            },
            ,isUGC: true
            ,uid: '12345'
        }
        , {
            onFileUpdate: function (args) {
                console.log('文件信息', args);
            },
            onFileStatus: function (info) {
                console.log('各状态总数' , info);
            },
            onFilterError: function (args) {
                console.log(args)
            }
        }
    ));
```

### API

```
qcVideo.uploader.startUpload()
功能： 启动上传 
参数： 无; 
返回： 无;
```

```
qcVideo.uploader.stopUpload()
功能： 停止上传 
参数： 无; 
返回： 无;
```
	
```
qcVideo.uploader.reUpload()

功能： 恢复上传（错误文件重新上传） 
参数： 无; 
返回： 无;
```

```
qcVideo.uploader.deleteFile(fid)

功能： 删除本地上传任务 
参数： fid 文件id; 
返回： 无;
```

```
qcVideo.uploader.getOriginalFile(fid)

功能： 获取本地文件对象 
参数： 无; 
返回： FILE对象;
```

## 兼容性

该SDK当前仅支持HTML5上传，主流浏览器比如chrome, safari等经测试可正常使用，受限于各厂商对HTML5实现不一致，个别机型如无法正常使用，需要具体情况具体分析。