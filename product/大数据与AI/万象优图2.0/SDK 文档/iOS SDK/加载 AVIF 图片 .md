
本文提供加载网络以及使用 AVIF 模块两种方式加载 AVIF 图片。

### 方式一：加载网络 AVIF 图片

>! CloudInfinite SDK 版本需要大于等于 v1.3.8。

1. 首先集成 CloudInfinite。

   ```
   pod 'CloudInfinite'
   ```

2. 在 CloudInfinite 模块中构建出请求 AVIF 格式图片的链接，然后与 [SDWebImage](https://cloud.tencent.com/document/product/460/47733) 配合使用，加载网络 AVIF 图片。
   **Objective-C**
    ```
    // 实例化 CloudInfinite，用来构建请求图片请求连接；
    CloudInfinite * cloudInfinite = [CloudInfinite new];
   
    // 根据用户所选万象基础功能 options 进行构建 CIImageLoadRequest；
    CITransformation * transform = [CITransformation new];
    [transform setFormatWith:CIImageTypeAVIF options:CILoadTypeUrlFooter];
   
    // 构建图片 CIImageLoadRequest
    [cloudInfinite requestWithBaseUrl:@"图片链接" transform:transform request:^(CIImageLoadRequest * _Nonnull request) {
        // request 构建成功的 CIImageLoadRequest 实例，
    }];
    ```

   **swift**
    ```
    // 实例化 CloudInfinite，用来构建请求图片请求连接；
    let cloudInfinite = CloudInfinite();
   
    // 根据用户所选的数据万象基础功能 options 进行构建 CIImageLoadRequest；
    let transform = CITransformation();
    transform.setFormatWith(CIImageFormat.typeAVIF, options: CILoadTypeEnum.urlFooter);
    
    // 构建图片 CIImageLoadRequest
    cloudInfinite.request(withBaseUrl: "图片链接", transform: transform) { (request) in
        // request 构建成功的 CIImageLoadRequest 实例，
    }  
    ```

### 方式二：使用 AVIF 模块加载 AVIF 图片

使用 AVIF 模块加载 AVIF 图片 Data 数据，支持加载 AVIF 动图，无需额外处理。

1. 首先集成 AVIF 模块。
   ```
   pod 'CloudInfinite/AVIF'
   ```
2. 如果已经获取到 AVIF 图片 data 数据，则直接使用 AVIF 模块 UIImageView+AVIF 类进行解码并显示。
   **Objective-C**
    ```
    [self.avifImageView setAvifImageWithData:data loadComplete:^(NSData * _Nullable data，UIImage * _Nullable image, NSError * _Nullable error) {

    }];
    ```
   **swift**
    ```
    imageView.setAvifImageWith(data) { (data, image, error) in

    }
    ```



