# 开发准备

1. SDK 和 Demo 打包下载：[SDK+Demo](https://main.qcloudimg.com/raw/07f0b2bfd1f8defe6b0aeab14599eee9.zip)；
2. 前往注册： [腾讯云账号注册](https://cloud.tencent.com/register) （详细指引见 [注册腾讯云](https://cloud.tencent.com/document/product/378/9603)）；
3. 取得 `APPID`、`SecretId`、`SecretKey`：请前往 [云API密钥](https://console.cloud.tencent.com/cam/capi) 查看，如无则点击“新建密钥”。

# 快速体验 Demo
1. 打开工程：双击工程根目录下的 `FaceVerifyIdPaaS.xcworkspace` 文件，即可在 Xcode 中打开；
2. 修改：找到 FaceVerifyIdPaaSDemo/Utils/UserInfo.h 文件，填入上面申请到的  `APPID`、`SecretId`、`SecretKey`；
![图片描述](	https://main.qcloudimg.com/raw/684bbf046355183ff69d44a4dd5374ed.png)
3. 运行：选择 `local_debug_demo` scheme 和 对应的机型，点击运行按钮即可体验。
![图片描述](https://main.qcloudimg.com/raw/e92b506465c125fa758b81d67f0d074e.png)

# 集成 SDK 到你的工程中
1. 编译：选择 `local_debug_framework` scheme 和 `Generic iOS Device`，按快捷键  `Cmd+B` 编译，在侧边栏可看到编译出来的 SDK  `FaceVerifyIdPaaSLib.framework`；
![图片描述](	https://main.qcloudimg.com/raw/9bcf1c0aed50ba71790da540de86ab54.png)

2. 集成：把 `FaceVerifyIdPaaSLib.framework` 拖到您的工程中： 
![图片描述](https://main.qcloudimg.com/raw/2566e7dad03619a73048ae2cd6a95069.png)

    提示框中选择 `Copy items if needed` 和 `Create groups`，其中 `Add to targets` 请按实际情况选择  
![图片描述](https://main.qcloudimg.com/raw/f63656d6c454dc23b7c9af79e1b28df9.png)

3. 集成 SDK 完毕，在您的代码中仿照 Demo 中的例子调用即可。

# 快速入门

## 签名获取
所有请求均需要鉴权签名。为了方便测试，SDK 中提供了本地生成签名的方法：

`NSString *sign = [QCLocalAuthorizationGenerator signWithAppId:APP_ID secretId:SECRET_ID secretKey:SECRET_KEY];`  

但是为了不暴露 SecretKey，正式环境下请服务器上进行签名。具体签名算法可参考 [签名与鉴权](https://cloud.tencent.com/document/product/460/6968)。

## 照片核身（通过本地照片文件和身份证信息）
```
// 参考文档 https://cloud.tencent.com/document/product/641/12433
_task = [QCHttpEngine
    postFormDataTo:@"http://recognition.image.myqcloud.com/face/idcardcompare"
           headers:@{@"Authorization": @"aBcD…"}//鉴权签名
            params:@{@"appid": @"0000000", //你申请到的 APPID
                    @"idcard_number": @"440181…", //身份证号码
                    @"idcard_name": @"张三",//姓名
                    @"seq": @"test"}//请求标识
             files:@{@"image": imgPath}//本地照片路径
        onProgress:^(float percent) {
            //进度回调
        }
      onCompletion:^(NSData *data, NSURLResponse *response, NSError *error) {
	      _task = nil;
	      if (error) {
	          //错误处理
	          NSLog(@"onCompletion: error = %@", error);
	      } else {
	         //结果转换成 NSString
	         NSString *string = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
	         NSLog(string);
	         //结果转换成 NSDictionary
	         NSError *e = nil;
	         NSDictionary *dic = [NSJSONSerialization JSONObjectWithData:data options:kNilOptions error:&e];
	         if (!dic) {//转换 NSDictionary 失败
	             NSLog(@"%@ 转换 NSDictionary 失败, error = %@", string, e);
	         } else {
	             NSInteger code = [dic[@"code"] integerValue];
	             if (code != 0) {//返回码不是0
	                 NSLog(@"错误码: %d, 错误信息: %@", code, dic[@"message"]);
	             } else {//成功, 获取内容
	                 CGFloat similarity = [dic[@"data"][@"similarity"] floatValue];
	                 NSLog(@"相似度: %f", similarity);
	             }
	         }
	      }
      }];

// [_task cancel]; //取消请求
```

## 照片核身（通过网络图片和身份证信息）
``` 
// 参考文档 https://cloud.tencent.com/document/product/641/12433
_task = [QCHttpEngine
    postJsonTo:@"http://recognition.image.myqcloud.com/face/idcardcompare"
       headers:@{@"Authorization": @"aBcD…"}//鉴权签名
        params:@{@"appid": @"0000000", //你申请到的 APPID
                @"idcard_number": @"440181…", //身份证号码
                @"idcard_name": @"张三",//姓名
                @"url": @"http://…",//图片url
                @"seq": @"test"}//请求标识
        onProgress:^(float percent) {
            //进度回调
        }
      onCompletion:^(NSData *data, NSURLResponse *response, NSError *error) {
	      _task = nil;
	      if (error) {
	          //错误处理
	          NSLog(@"onCompletion: error = %@", error);
	      } else {
	         //结果转换成 NSString
	         NSString *string = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
	         NSLog(string);
	         //结果转换成 NSDictionary
	         NSError *e = nil;
	         NSDictionary *dic = [NSJSONSerialization JSONObjectWithData:data options:kNilOptions error:&e];
	         if (!dic) {//转换 NSDictionary 失败
	             NSLog(@"%@ 转换 NSDictionary 失败, error = %@", string, e);
	         } else {
	             NSInteger code = [dic[@"code"] integerValue];
	             if (code != 0) {//返回码不是0
	                 NSLog(@"错误码: %d, 错误信息: %@", code, dic[@"message"]);
	             } else {//成功, 获取内容
	                 CGFloat similarity = [dic[@"data"][@"similarity"] floatValue];
	                 NSLog(@"相似度: %f", similarity);
	             }
	         }
	      }
      }];

// [_task cancel]; //取消请求
```
## 获取唇语验证码，用于活体核身 
```
// application/json 类型请求
//参考文档 https://cloud.tencent.com/document/product/641/12431
_task = [QCHttpEngine
    postJsonTo:@"http://recognition.image.myqcloud.com/face/livegetfour"
       headers:@{@"Authorization": @"aBcD…"}//鉴权签名
        params:@{@"appid": @"0000000", //你申请到的 APPID
                @"seq": @"test"}//请求标识
    onProgress:^(float percent) {
        //进度回调
    }
  onCompletion:^(NSData *data, NSURLResponse *response, NSError *error) {
      _task = nil;
      if (error) {
          //错误处理
          NSLog(@"onCompletion: error = %@", error);
      } else {
         //结果转换成 NSString
         NSString *string = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
         NSLog(string);
         //结果转换成 NSDictionary
         NSError *e = nil;
         NSDictionary *dic = [NSJSONSerialization JSONObjectWithData:data options:kNilOptions error:&e];
         if (!dic) {//转换 NSDictionary 失败
             NSLog(@"%@ 转换 NSDictionary 失败, error = %@", string, e);
         } else {
             NSInteger code = [dic[@"code"] integerValue];
             if (code != 0) {//返回码不是0
                 NSLog(@"错误码: %d, 错误信息: %@", code, dic[@"message"]);
             } else {//成功, 获取内容
                 NSString *validate_data = dic[@"data"][@"validate_data"];
                 NSLog(@"唇语验证码: %@", validate_data);
             }
         }
      }
  }];

// [_task cancel]; //取消请求
```

```
// multipart/form-data 类型请求
//参考文档 https://cloud.tencent.com/document/product/641/12431
_task = [QCHttpEngine
    postFormDataTo:@"http://recognition.image.myqcloud.com/face/livegetfour"
           headers:@{@"Authorization": @"aBcD…"}//鉴权签名
            params:@{@"appid": @"0000000", //你申请到的 APPID
                    @"seq": @"test"}//请求标识
             files:nil
        onProgress:^(float percent) {
            //进度回调
        }
      onCompletion:^(NSData *data, NSURLResponse *response, NSError *error) {
	      _task = nil;
	      if (error) {
	          //错误处理
	          NSLog(@"onCompletion: error = %@", error);
	      } else {
	         //结果转换成 NSString
	         NSString *string = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
	         NSLog(string);
	         //结果转换成 NSDictionary
	         NSError *e = nil;
	         NSDictionary *dic = [NSJSONSerialization JSONObjectWithData:data options:kNilOptions error:&e];
	         if (!dic) {//转换 NSDictionary 失败
	             NSLog(@"%@ 转换 NSDictionary 失败, error = %@", string, e);
	         } else {
	             NSInteger code = [dic[@"code"] integerValue];
	             if (code != 0) {//返回码不是0
	                 NSLog(@"错误码: %d, 错误信息: %@", code, dic[@"message"]);
	             } else {//成功, 获取内容
	                 NSString *validate_data = dic[@"data"][@"validate_data"];
	                 NSLog(@"唇语验证码: %@", validate_data);
	             }
	         }
	      }
      }];

// [_task cancel]; //取消请求
```
## 活体核身（通过视频和照片）
```
//参考文档 https://cloud.tencent.com/document/product/641/12432
_task = [QCHttpEngine
  postFormDataTo:@"http://recognition.image.myqcloud.com/face/livedetectfour"
         headers:@{@"Authorization": @"aBcD…"}//鉴权签名
          params:@{@"appid": @"0000000", //你申请到的 APPID
                  @"validate_data": @"1234",//唇语验证码
                  @"compare_flag": @"true",//是否需要对比视频与图片为同一人
                  @"seq": @"test"}//请求标识
           files:@{@"video": videoFilePath,//视频文件路径
                   @"card": imgFilePath}//图片文件路径
      onProgress:^(float percent) {
          	//进度回调
      }
    onCompletion:^(NSData *data, NSURLResponse *response, NSError *error) {
	      _task = nil;
	      if (error) {
	          //错误处理
	          NSLog(@"onCompletion: error = %@", error);
	      } else {
	         //结果转换成 NSString
	         NSString *string = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
	         NSLog(string);
	         //结果转换成 NSDictionary
	         NSError *e = nil;
	         NSDictionary *dic = [NSJSONSerialization JSONObjectWithData:data options:kNilOptions error:&e];
	         if (!dic) {//转换 NSDictionary 失败
	             NSLog(@"%@ 转换 NSDictionary 失败, error = %@", string, e);
	         } else {
	             NSInteger code = [dic[@"code"] integerValue];
	             if (code != 0) {//返回码不是0
	                 NSLog(@"错误码: %d, 错误信息: %@", code, dic[@"message"]);
	             } else {//成功, 获取内容
	                 NSInteger live_status = [dic[@"data"][@"live_status"] integerValue];
	                 NSLog(@"活体核身: %@", live_status == 0?@"通过":@"不通过");
	             }
	         }
	      }
    }];

// [_task cancel]; //取消请求
```
# 活体核身（通过视频和身份证信息）
```
//参考文档 https://cloud.tencent.com/document/product/641/12430
_task = [QCHttpEngine
    postFormDataTo:@"http://recognition.image.myqcloud.com/face/idcardlivedetectfour"
           headers:@{@"Authorization": @"aBcD…"}//鉴权签名
            params:@{@"appid": @"0000000", //你申请到的 APPID
                    @"validate_data": @"1234",//唇语验证码
                    @"idcard_number": @"440181…", //身份证号码
                    @"idcard_name": @"张三",//姓名
                    @"seq": @"test"}//请求标识
             files:@{@"video": videoFilePath}//视频文件路径
        onProgress:^(float percent) {
            //进度回调
        }
      onCompletion:^(NSData *data, NSURLResponse *response, NSError *error) {
	      _task = nil;
	      if (error) {
	          //错误处理
	          NSLog(@"onCompletion: error = %@", error);
	      } else {
	         //结果转换成 NSString
	         NSString *string = [[NSString alloc] initWithData:data encoding:NSUTF8StringEncoding];
	         NSLog(string);
	         //结果转换成 NSDictionary
	         NSError *e = nil;
	         NSDictionary *dic = [NSJSONSerialization JSONObjectWithData:data options:kNilOptions error:&e];
	         if (!dic) {//转换 NSDictionary 失败
	             NSLog(@"%@ 转换 NSDictionary 失败, error = %@", string, e);
	         } else {
	             NSInteger code = [dic[@"code"] integerValue];
	             if (code != 0) {//返回码不是0
	                 NSLog(@"错误码: %d, 错误信息: %@", code, dic[@"message"]);
	             } else {//成功, 获取内容
	                 NSInteger live_status = [dic[@"data"][@"live_status"] integerValue];
	                 NSLog(@"活体核身: %@", live_status == 0?@"通过":@"不通过");
	             }
	         }
	      }
      }];
      
// [_task cancel]; //取消请求
```


