## 背景

本文主要介绍基于腾讯云对象存储（COS）服务，移动端在弱网情况下，如何根据实际情况动态调节上传分块大小，来提高上传成功率。

> ! 该功能目前处于灰度测试阶段，如需支持该功能，请 [提交工单](https://console.cloud.tencent.com/workorder/category) 申请开通白名单。

## 实践须知

1. COS 目前支持最小分块大小为100KB。
2. 分块越小，意味着请求数也多。目前根据测试统计，100KB分块大小的请求耗时是1MB分块大小的2倍左右。
3. 在正常网络下发起请求，建议设置分块大小为1MB及以上。
4. 在网络信号弱等网络环境下上传对象容易导致上传失败，可以考虑将分块大小设置为100KB，再重新上传。
5. 分块大小设置越小，将来下载该文件时可能比较缓慢。

## 示例

#### Android SDK

下面举例在弱网络环境中，使用分块上传对象的示例代码：

```java
import android.content.Context;
import android.os.Handler;
import android.os.Message;
import android.util.Log;

import com.tencent.cos.xml.CosXmlService;
import com.tencent.cos.xml.CosXmlServiceConfig;
import com.tencent.cos.xml.common.ClientErrorCode;
import com.tencent.cos.xml.common.Region;
import com.tencent.cos.xml.exception.CosXmlClientException;
import com.tencent.cos.xml.exception.CosXmlServiceException;
import com.tencent.cos.xml.listener.CosXmlProgressListener;
import com.tencent.cos.xml.listener.CosXmlResultListener;
import com.tencent.cos.xml.model.CosXmlRequest;
import com.tencent.cos.xml.model.CosXmlResult;
import com.tencent.cos.xml.transfer.COSXMLUploadTask;
import com.tencent.cos.xml.transfer.TransferConfig;
import com.tencent.cos.xml.transfer.TransferManager;
import com.tencent.cos.xml.transfer.TransferState;
import com.tencent.cos.xml.transfer.TransferStateListener;
import com.tencent.qcloud.core.auth.QCloudCredentialProvider;
import com.tencent.qcloud.core.auth.ShortTimeCredentialProvider;

public class ResumeHelper {
    private final static String TAG = ResumeHelper.class.getSimpleName();

    private Context context;
    String bucket = "examplebucket-1250000000"; //存储桶，格式 BucketName-APPID, 替换为您的 bucket
    String region = Region.AP_Guangzhou.getRegion(); //存储桶所在地域, 填写您的 bucket 所在的地域
    private CosXmlService cosXmlService;

    private Handler mainHandler;
    private boolean isTriedOnce = false; //是否已重传过，避免无限制重传
    private final int MESSAGE_RETRY = 1;

    public ResumeHelper(Context context){
        this.context = context;
        this.mainHandler = new Handler(context.getMainLooper()){
            @Override
            public void handleMessage(Message msg) {
                super.handleMessage(msg);
                switch (msg.what){
                    case MESSAGE_RETRY:
                        /** 已重传过 */
                        if(isTriedOnce)return;
                        isTriedOnce = true;
                        Parameter parameter = (Parameter) msg.obj;
                        /** 再次上传 */
                        upload(parameter.srcPath, parameter.cosPath, parameter.uploadId, parameter.sliceSize);
                        break;
                }
            }
        };
        initCosXml();
    }

    /**
     * 初始化 CosXmlService
     */
    private void initCosXml(){
        /** 初始化 CosXmlServiceConfig */
        CosXmlServiceConfig cosXmlServiceConfig = new CosXmlServiceConfig.Builder()
                .setDebuggable(true)
                .isHttps(true)
                .setRegion(region)
                .builder();

        //此处为了方便测试，使用了永久密钥，实际应用中建议使用临时密钥
        String secretId = "COS_SECRETID"; //填写您的 云 API 密钥 SecretId
        String secretKey = "COS_SECRETKEY"; //填写您的 云 API 密钥 SecretKey
        /** 初始化 密钥信息 */
        QCloudCredentialProvider qCloudCredentialProvider = new ShortTimeCredentialProvider(secretId, secretKey, 6000);

        /** 初始化 CosXmlService */
        cosXmlService = new CosXmlService(context, cosXmlServiceConfig, qCloudCredentialProvider);
    }

    /**
     * 上传
     * @param srcPath 本地文件路径
     * @param cosPath 存储在 COS 上的路径
     * @param uploadId 是否续传，若无，则为 null
     * @param sliceSize 分块上传时，设置的分块块大小
     */
    public void upload(final String srcPath, final String cosPath, final String uploadId, long sliceSize){

        /** 设置分块上传时，分块块的大小 */
        TransferConfig transferConfig = new TransferConfig.Builder()
                .setSliceSizeForUpload(sliceSize)
                .build();
        /** 初始化TransferManager */
        TransferManager transferManager = new TransferManager(cosXmlService, transferConfig);
        /** 开始上传: 若 uploadId != null,则可以进行续传 */
        final COSXMLUploadTask uploadTask = transferManager.upload(bucket, cosPath, srcPath, uploadId);
        /** 显示任务状态信息 */
        uploadTask.setTransferStateListener(new TransferStateListener() {
            @Override
            public void onStateChanged(TransferState state) {
                Log.d(TAG, "upload task state: " + state.name());
            }
        });
        /** 显示任务上传进度 */
        uploadTask.setCosXmlProgressListener(new CosXmlProgressListener() {
            @Override
            public void onProgress(long complete, long target) {
                Log.d(TAG, "upload task progress: " + complete + "/" + target);
            }
        });
        /** 显示任务上传结果 */
        uploadTask.setCosXmlResultListener(new CosXmlResultListener() {
            /** 任务上传成功 */
            @Override
            public void onSuccess(CosXmlRequest request, CosXmlResult result) {
                COSXMLUploadTask.COSXMLUploadTaskResult uploadTaskResult = (COSXMLUploadTask.COSXMLUploadTaskResult) result;
                Log.d(TAG, "upload task success: " + uploadTaskResult.printResult());
            }

            /** 任务上传失败 */
            @Override
            public void onFail(CosXmlRequest request, CosXmlClientException exception, CosXmlServiceException serviceException) {
                Log.d(TAG, "upload task failed: " + (exception == null ? serviceException.getMessage() :
                        (exception.errorCode + "," + exception.getMessage())));
                if(exception != null){
                    /** 若是因为网络导致失败， 则可尝试将分块大小设置为100KB再运行一遍*/
                    if(exception.errorCode == ClientErrorCode.INTERNAL_ERROR.getCode()
                            || exception.errorCode == ClientErrorCode.IO_ERROR.getCode()
                            || exception.errorCode != ClientErrorCode.POOR_NETWORK.getCode()){
                        Log.d(TAG, "upload task try again");
                        Message msg = mainHandler.obtainMessage();
                        msg.what = MESSAGE_RETRY;
                        Parameter parameter = new Parameter();
                        parameter.cosPath = cosPath;
                        parameter.srcPath = srcPath;
                        parameter.uploadId = uploadTask.getUploadId();
                        parameter.sliceSize = 100 * 1024L;
                        msg.obj = parameter;
                        mainHandler.sendMessage(msg);
                    }
                }
            }
        });
    }

    private static class Parameter{
        private String cosPath;
        private String srcPath;
        private String uploadId;
        private long sliceSize;
    }
}
```

#### iOS SDK

下面举例在弱网络环境中，使用分块上传对象的示例代码：

```objective-c
    QCloudCOSXMLUploadObjectRequest* put = [QCloudCOSXMLUploadObjectRequest new];
    NSURL* url = [NSURL fileURLWithPath:@"filePathURL"];
    put.object = @"text.txt";
    put.bucket = self.bucket;
    put.body =  url;
    [put setSendProcessBlock:^(int64_t bytesSent, int64_t totalBytesSent, int64_t totalBytesExpectedToSend) {
        NSLog(@"upload %lld totalSend %lld aim %lld", bytesSent, totalBytesSent, totalBytesExpectedToSend);
    }];
    [put setFinishBlock:^(QCloudUploadObjectResult *result, NSError *error) {
        /**
         1. 如果是请求超时，则可能是网络过慢导致的，可以从 error 中得到续传相关的信息 resumeData（存储在 QCloudUploadResumeDataKey 字段中）
         2. 调用 QCloudCOSXMLUploadObjectRequest的requestWithRequestData 传入 resumeData，重新生成一个 request。
         2. 根据需要通过 QCloudCOSXMLUploadObjectRequest 的 sliceSize 重新设置分块大小
         3. 开始上传
         */
        if (error.code == -1001) {
            NSData *resumeData =error.userInfo[QCloudUploadResumeDataKey];
            if (resumeData) {
                QCloudCOSXMLUploadObjectRequest* request = [QCloudCOSXMLUploadObjectRequest   requestWithRequestData:resumeData];
                request.sliceSize = 100*1024;
                [request setFinishBlock:^(QCloudUploadObjectResult* outputObject, NSError *error) {
                    NSLog(@"result: %@",outputObject);
                }];
                
                [request setSendProcessBlock:^(int64_t bytesSent, int64_t totalBytesSent, int64_t totalBytesExpectedToSend) {
                    NSLog(@"upload %lld totalSend %lld aim %lld", bytesSent, totalBytesSent, totalBytesExpectedToSend);
                }];
                [[QCloudCOSTransferMangerService defaultCOSTransferManager] UploadObject:request];
            }
        }
    }];
   [[QCloudCOSTransferMangerService defaultCOSTransferManager] UploadObject:put];
    
```
