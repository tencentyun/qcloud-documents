
本文提供加载网络以及使用 TPG 模块两种方式加载 TPG 图片。

### 方式一：加载网络 TPG 图片

1. 首先集成 CloudInfinite。

   ```
   pod 'CloudInfinite'
   ```

2. 在 CloudInfinite 模块中构建出请求 TPG 格式图片的链接，然后与 [SDWebImage](https://cloud.tencent.com/document/product/460/47733) 配合使用，加载网络 TPG 图片。
    **Objective-C**
    ```
    // 实例化 CloudInfinite，用来构建请求图片请求连接；
    CloudInfinite * cloudInfinite = [CloudInfinite new];
   
    // 根据用户所选万象基础功能 options 进行构建 CIImageLoadRequest；
    CITransformation * transform = [CITransformation new];
    [transform setFormatWith:CIImageTypeTPG options:CILoadTypeUrlFooter];
   
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
    transform.setFormatWith(CIImageFormat.typeTPG, options: CILoadTypeEnum.urlFooter);
    
    // 构建图片 CIImageLoadRequest
    cloudInfinite.request(withBaseUrl: "图片链接", transform: transform) { (request) in
        // request 构建成功的 CIImageLoadRequest 实例，
    }  
    ```

### 方式二：使用 TPG 模块加载 TPG 图片

使用 TPG 模块加载 TPG 图片 Data 数据，支持加载 TPG 动图，无需额外处理。

1. 首先集成 TPG 模块。
   ```
   pod 'CloudInfinite/TPG'
   ```
2. 如果已经获取到 TPG 图片 data 数据，则直接使用 TPG 模块 UIImageView+TPG 类进行解码并显示。

    **Objective-C**
    ```
        [self.tpgImageView setTpgImageWithData:data loadComplete:^(NSData * _Nullable data，UIImage * _Nullable image, NSError * _Nullable error) {

        }];
    ```
    **swift**
    ```
        imageView.setTpgImageWith(data) { (data, image, error) in

        }
    ```



