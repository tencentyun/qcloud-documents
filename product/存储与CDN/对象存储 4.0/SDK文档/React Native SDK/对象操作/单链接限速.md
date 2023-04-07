## 简介

本文档提供关于调用上传下载接口时对链接进行限速。

## 使用说明

限速值设置范围为 **819200 - 838860800**，单位默认为 bit/s，即100KB/s - 100MB/s，如果超出该范围将返回400错误。
通过调用 upload 和 download 方法时传入的 trafficLimit 参数进行限速。

#### 示例代码一：上传时对单链接限速

```ts
    // 存储桶所在地域简称，例如广州地区是 ap-guangzhou
    let region = "COS_REGION";
    // 创建 CosXmlServiceConfig 对象，根据需要修改默认的配置参数
    let serviceConfig = {
        region: region,
        isDebuggable: true,
        isHttps: true,
    };
    // 创建 TransferConfig 对象，根据需要修改默认的配置参数
    // TransferConfig 可以设置智能分块阈值 默认对大于或等于2M的文件自动进行分块上传，可以通过如下代码修改分块阈值
    let transferConfig = {
        forceSimpleUpload: false,
        enableVerification: true,
        divisionForUpload: 2097152, // 设置大于等于 2M 的文件进行分块上传
        sliceSizeForUpload: 1048576, //设置默认分块大小为 1M
    };
    // 注册默认 COS TransferManger
    await Cos.registerDefaultTransferManger(serviceConfig, transferConfig);

    // 获取 CosTransferManger
    let cosTransferManger: CosTransferManger = Cos.getDefaultTransferManger();
    //let cosTransferManger: CosTransferManger = Cos.getTransferManger(newRegion);
    // 存储桶名称，由 bucketname-appid 组成，appid 必须填入，可以在 COS 控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket
    let bucket = "examplebucket-1250000000";
    let cosPath = "exampleobject"; //对象在存储桶中的位置标识符，即称对象键
    let srcPath = "本地文件的路径"; //本地文件的路径
    //若存在初始化分块上传的 UploadId，则赋值对应的 uploadId 值用于续传；否则，赋值 undefined
    let _uploadId = undefined;

    // 上传成功回调
    let successCallBack = (header?: object) => {
      // todo 上传成功后的逻辑
    };
    //上传失败回调
    let failCallBack = (clientError?: CosXmlClientError, serviceError?: CosXmlServiceError) => {
      // todo 上传失败后的逻辑
      if (clientError) {
        console.log(clientError);
      }
      if (serviceError) {
        console.log(serviceError);
      }
    };
    //上传状态回调, 可以查看任务过程
    let stateCallBack = (state: TransferState) => {
      // todo notify transfer state
    };
    //上传进度回调
    let progressCallBack = (complete: number, target: number) => {
      // todo Do something to update progress...
    };
    //初始化分块完成回调
    let initMultipleUploadCallBack = (bucket: string, cosKey: string, uploadId: string) => {
      //用于下次续传上传的 uploadId
      _uploadId = uploadId;
    };
    
    // 设置单链接限速，单位为 bit/s，示例设置为 1M/s
    let _trafficLimit = 1024 * 1024 * 8;

    //开始上传
    let transferTask:TransferTask = await cosTransferManger.upload(
      bucket,
      cosPath,
      srcPath,
      {
        uploadId: _uploadId,
        trafficLimit: _trafficLimit,
        resultListener: {
          successCallBack: successCallBack,
          failCallBack: failCallBack
        },
        stateCallback: stateCallBack,
        progressCallback: progressCallBack,
        initMultipleUploadCallback: initMultipleUploadCallBack,
      }
    );
```

#### 示例代码二：下载时对单链接限速

```ts
    // 高级下载接口支持断点续传，所以会在下载前先发起 HEAD 请求获取文件信息。
    // 如果您使用的是临时密钥或者使用子账号访问，请确保权限列表中包含 HeadObject 的权限。

    // CosTransferManger 支持断点下载，您只需要保证 bucket、cosPath、savePath
    // 参数一致，SDK 便会从上次已经下载的位置继续下载。

    // 获取 CosTransferManger
    let cosTransferManger: CosTransferManger = Cos.getDefaultTransferManger();
    //let cosTransferManger: CosTransferManger = Cos.getTransferManger(newRegion);
    // 存储桶名称，由 bucketname-appid 组成，appid 必须填入，可以在 COS 控制台查看存储桶名称。 https://console.cloud.tencent.com/cos5/bucket
    let bucket = "examplebucket-1250000000";
    let cosPath = "exampleobject"; //对象在存储桶中的位置标识符，即称对象键
    let downliadPath = "本地文件的路径"; //保存到本地文件的路径

    // 下载成功回调
    let successCallBack = (header?: object) => {
      // todo 下载成功后的逻辑
    };
    //下载失败回调
    let failCallBack = (clientError?: CosXmlClientError, serviceError?: CosXmlServiceError) => {
      // todo 下载失败后的逻辑
      if (clientError) {
        console.log(clientError);
      }
      if (serviceError) {
        console.log(serviceError);
      }
    };
    //下载状态回调, 可以查看任务过程
    let stateCallBack = (state: TransferState) => {
      // todo notify transfer state
    };
    //下载进度回调
    let progressCallBack = (complete: number, target: number) => {
      // todo Do something to download progress...
    };

    // 设置单链接限速，单位为 bit/s，示例设置为 1M/s
    let _trafficLimit = 1024 * 1024 * 8;

    //开始下载
    let transferTask:TransferTask = await cosTransferManger.download(
      bucket,
      cosPath,
      downliadPath,
      {
        trafficLimit: _trafficLimit,
        resultListener: {
          successCallBack: successCallBack,
          failCallBack: failCallBack
        },
        stateCallback: stateCallBack,
        progressCallback: progressCallBack
      }
    );
```
