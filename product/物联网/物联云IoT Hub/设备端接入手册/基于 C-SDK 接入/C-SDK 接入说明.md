


为保证安全，物联网平台会验证每个接入设备的合法性，为此提供了多种认证方式，满足不同的使用场景及各种资源的设备接入。您可以观看以下视频了解腾讯云物联网通信设备接入说明。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/2896-54332?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 设备身份信息
从设备密钥形式区分，分为证书设备和密钥设备。证书方式安全性更高，但需要消耗较多的软硬件资源。
 - 证书设备要通过平台的安全认证，必须具备四元组信息：产品 ID（ProductId）、设备名（DeviceName）、设备证书文件（DeviceCert）、设备私钥文件（DevicePrivateKey），其中证书文件和私钥文件由平台生成，且一一对应。
 - 密钥设备要通过平台的安全认证，必须具备三元组信息：产品 ID（ProductId）、设备名（DeviceName）、设备密钥（DeviceSecret），其中设备密钥由平台生成。

设备密钥是创建产品时，通过设置认证方式来确定，如下图所示：
![](https://main.qcloudimg.com/raw/72784b62fe9a415cedd9b916cbf38a6f.png)

## 设备身份信息烧录
设备信息烧录分为预置烧录和动态烧录，两者在应用的便捷性和安全性上有区别。
### 预置烧录
创建产品后，在物联网通信 [控制台](https://cloud.tencent.com/product/iothub) 或者通过 [云 API](https://cloud.tencent.com/document/product/634/19468) 逐个创建设备，并获取对应的设备信息，将上述的四元组或者三元组信息，在设备生产的特定环节，烧录到非易失介质中，设备 SDK 运行时读取存放的设备信息，进行设备认证。

### 动态烧录
 - 预置烧录：需要在量产过程执行个性化生产动作，影响生产效率，为增加应用的便捷性，平台支持动态烧录的方式。实现方式：产品创建后使用产品的动态注册功能，则会生成产品密钥（ProductSecret）。同一产品下的所有设备在生产过程可以烧录统一的产品信息，即产品 ID（ProductId）、产品密钥（ProductSecret）。设备出厂后，通过动态注册的方式获取设备身份信息并保存，然后使用申请到的三元组或者四元组信息进行设备认证。
 - 动态烧录设备名（DeviceName）的生成：若使用动态注册的同时使用自动设备创建，则设备名是可以设备自己生成的，但必须保证同一产品 ID（ProductId）下的设备名不重复，一般取 IMEI 或者 MAC 地址。若使用动态注册的同时不使用自动设备创建，则需要把设备名预先录入平台，设备动态注册时会校验所申请的设备名是否为合法录入的设备名，此种方式能在一定程度降低产品密钥泄露后的安全风险。

>!动态注册需要确保产品密钥（ProductSecret）的安全，否则会产生较大的安全隐患。


## 预置烧录设备认证编程
####  设备信息写入
证书设备实现如下 HAL API：

| HAL_API                            | 说明                                 |
| -----------------------------------| ----------------------------------  |
| HAL_SetProductID                  	| 设置产品 ID，必须存放在非易失性存储介质    |
| HAL_SetDevName                   	| 设置设备名，必须存放在非易失性存储介质    |
| HAL_SetDevCertName                 | 设置设备证书文件名，证书文件需要放置到 certs 文件目录   |
| HAL_SetDevPrivateKeyName           | 设置设备证书私钥文件名，私钥文件需要放置到 certs 文件目录  |

密钥设备实现如下 HAL API：

| HAL_API                            | 说明                                 |
| -----------------------------------| ----------------------------------  |
| HAL_SetProductID                  	| 设置产品 ID，必须存放在非易失性存储介质    |
| HAL_SetDevName                   	| 设置设备名 ，必须存放在非易失性存储介质   |
| HAL_SetDevSec                      | 设置设备密钥，必须存放在非易失性存储介质，建议加密加扰   |

####  设备信息获取
证书设备实现如下 HAL API：

| HAL_API                            | 说明                                 |
| -----------------------------------| ----------------------------------  |
| HAL_GetProductID                  	| 获取产品 ID  |
| HAL_GetDevName                   	|获取设备名   |
| HAL_GetDevCertName                 | 获取设备证书文件名   |
| HAL_GetDevPrivateKeyName           | 获取设备证书私钥文件名 |

密钥设备实现如下 HAL API：

| HAL_API                            | 说明                                 |
| -----------------------------------| ----------------------------------  |
| HAL_GetProductID                  	| 获取产品 ID    |
| HAL_GetDevName                   	| 获取设备名    |
| HAL_GetDevSec                      | 获取设备密钥，若写入时加密加扰，读取时需解密解扰   |	

####  应用示例
-  初始化连接参数

```
static DeviceInfo sg_devInfo;

static int _setup_connect_init_params(MQTTInitParams* initParams)
{
	int ret;
	
	ret = HAL_GetDevInfo((void *)&sg_devInfo);	
	if(QCLOUD_ERR_SUCCESS != ret){
		return ret;
	}
		
	initParams->device_name = sg_devInfo.device_name;
	initParams->product_id = sg_devInfo.product_id;
	 ......
}	
```

-  设备信息获取

```
int HAL_GetDevInfo(void *pdevInfo)
{
	int ret;
	DeviceInfo *devInfo = (DeviceInfo *)pdevInfo;
		
	memset((char *)devInfo, 0, sizeof(DeviceInfo));
	ret = HAL_GetProductID(devInfo->product_id, MAX_SIZE_OF_PRODUCT_ID);
	ret |= HAL_GetDevName(devInfo->device_name, MAX_SIZE_OF_DEVICE_NAME); 
	
#ifdef 	AUTH_MODE_CERT
	ret |= HAL_GetDevCertName(devInfo->devCertFileName, MAX_SIZE_OF_DEVICE_CERT_FILE_NAME);
	ret |= HAL_GetDevPrivateKeyName(devInfo->devPrivateKeyFileName, MAX_SIZE_OF_DEVICE_KEY_FILE_NAME);
#else
	ret |= HAL_GetDevSec(devInfo->devSerc, MAX_SIZE_OF_DEVICE_SERC);
#endif 

	if(QCLOUD_ERR_SUCCESS != ret){
		Log_e("Get device info err");
		ret = QCLOUD_ERR_DEV_INFO;
	}

	return ret;
}
```

-  鉴权参数生成

```
static int _serialize_connect_packet(unsigned char *buf, size_t buf_len, MQTTConnectParams *options, uint32_t *serialized_len) {
			......
			......
    int username_len = strlen(options->client_id) + strlen(QCLOUD_IOT_DEVICE_SDK_APPID) + MAX_CONN_ID_LEN + cur_timesec_len + 4;
    options->username = (char*)HAL_Malloc(username_len);
    get_next_conn_id(options->conn_id);
	HAL_Snprintf(options->username, username_len, "%s;%s;%s;%ld", options->client_id, QCLOUD_IOT_DEVICE_SDK_APPID, options->conn_id, cur_timesec);

#if defined(AUTH_WITH_NOTLS) && defined(AUTH_MODE_KEY)
     if (options->device_secret != NULL && options->username != NULL) {
    	 char                sign[41]   = {0};
    	 utils_hmac_sha1(options->username, strlen(options->username), sign, options->device_secret, options->device_secret_len);
    	 options->password = (char*) HAL_Malloc (51);
    	 if (options->password == NULL) IOT_FUNC_EXIT_RC(QCLOUD_ERR_INVAL);
		 HAL_Snprintf(options->password, 51, "%s;hmacsha1", sign);
     }
#endif
			......
}
```

## 动态烧录设备认证编程
-  判断是否发起动态申请

```
int main(int argc, char **argv) {
			......
	memset((char *)&sDevInfo, 0, sizeof(DeviceInfo));
	ret = HAL_GetProductID(sDevInfo.product_id, MAX_SIZE_OF_PRODUCT_ID);
	ret |= HAL_GetProductKey(sDevInfo.product_key, MAX_SIZE_OF_PRODUCT_KEY);
	ret |= HAL_GetDevName(sDevInfo.device_name, MAX_SIZE_OF_DEVICE_NAME);  //动态注册，建议用设备的唯一标识做设备名，譬如芯片ID、IMEI
	
#ifdef 	AUTH_MODE_CERT
	ret |= HAL_GetDevCertName(sDevInfo.devCertFileName, MAX_SIZE_OF_DEVICE_CERT_FILE_NAME);
	ret |= HAL_GetDevPrivateKeyName(sDevInfo.devPrivateKeyFileName, MAX_SIZE_OF_DEVICE_KEY_FILE_NAME);
	if(QCLOUD_ERR_SUCCESS != ret){
		Log_e("Get device info err");
		return QCLOUD_ERR_FAILURE;
	}
	/*用户需要根据自己的产品情况修改设备信息为空的逻辑，此处仅为示例*/
	if(!strcmp(sDevInfo.devCertFileName, QCLOUD_IOT_NULL_CERT_FILENAME)
		||!strcmp(sDevInfo.devPrivateKeyFileName, QCLOUD_IOT_NULL_KEY_FILENAME)){
		Log_d("dev Cert not exist!");
		infoNullFlag = true;
	}else{
		Log_d("dev Cert exist");
	}
#else
	ret |= HAL_GetDevSec(sDevInfo.devSerc, MAX_SIZE_OF_PRODUCT_KEY);
	if(QCLOUD_ERR_SUCCESS != ret){
		Log_e("Get device info err");
		return QCLOUD_ERR_FAILURE;
	}
	/*用户需要根据自己的产品情况修改设备信息为空的逻辑，此处仅为示例*/
	if(!strcmp(sDevInfo.devSerc, QCLOUD_IOT_NULL_DEVICE_SECRET)){
		Log_d("dev psk not exist!");
		infoNullFlag = true;
	}else{
		Log_d("dev psk exist");
	}
#endif 
			......

}
```

-  发起动态申请，并保存申请的设备信息

```
	/*设备信息为空，发起设备注册 注意：成功注册并完成一次连接后则无法再次发起注册，请做好设备信息的保存*/
	if(infoNullFlag){
		if(QCLOUD_ERR_SUCCESS == qcloud_iot_dyn_reg_dev(&sDevInfo)){
			
			ret = HAL_SetDevName(sDevInfo.device_name);
#ifdef 	AUTH_MODE_CERT
			ret |= HAL_SetDevCertName(sDevInfo.devCertFileName);
			ret |= HAL_SetDevPrivateKeyName(sDevInfo.devPrivateKeyFileName);		
#else
			ret |= HAL_SetDevSec(sDevInfo.devSerc);
#endif
			if(QCLOUD_ERR_SUCCESS != ret){
				Log_e("devices info save fail");
			}else{
#ifdef 	AUTH_MODE_CERT
				Log_d("dynamic register success, productID: %s, devName: %s, CertFile: %s, KeyFile: %s", \
						sDevInfo.product_id, sDevInfo.device_name, sDevInfo.devCertFileName, sDevInfo.devPrivateKeyFileName);
#else
				Log_d("dynamic register success,productID: %s, devName: %s, devSerc: %s", \
					    sDevInfo.product_id, sDevInfo.device_name, sDevInfo.devSerc);
#endif
			}
		}else{
			Log_e("%s dynamic register fail", sDevInfo.device_name);
		}
	}
```

设备信息动态申请成功后，即完成预置烧录的功能。后续的认证流程与预置烧录的流程一致。
