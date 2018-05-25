qcloudapi-sdk-java是为了让Java开发者能够在自己的代码里更快捷方便的使用腾讯云的API而开发的SDK工具包。

### 快速入门
1. 申请安全凭证
在第一次使用云 API 之前，首先需要在腾讯云网站上申请安全凭证，安全凭证包括 SecretId 和 SecretKey, SecretId 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。
2. 使用 SDK
下载 SDK，放入到程序目录，使用方法请参考下面的例子。

```
    public class Demo {
    public static void main(String[] args) {
	/* 如果是循环调用下面举例的接口，需要从此处开始您的循环语句。切记！ */
	TreeMap<String, Object> config = new TreeMap<String, Object>();
	config.put("SecretId", "您的secretId");
	config.put("SecretKey", "您的secretKey");
	/* 请求方法类型 POST、GET */
	config.put("RequestMethod", "GET");
	/* 区域参数，可选: gz:广州; sh:上海; hk:香港; ca:北美;等。 */
	config.put("DefaultRegion", "gz");

	/*
	 * 您将要使用接口所在的模块，可以从 官网->云api文档->XXXX接口->接口描述->域名
	 * 中获取，比如域名：cvm.api.qcloud.com，module就是new Cvm()。
	 */
	/*
	 * DescribeInstances
	 * 的api文档地址：http://cloud.qcloud.com/wiki/v2/DescribeInstances
	 */
	QcloudApiModuleCenter module = new QcloudApiModuleCenter(new Cvm(),config);
	TreeMap<String, Object> params = new TreeMap<String, Object>();
	/* 将需要输入的参数都放入 params 里面，必选参数是必填的。 */
	/* DescribeInstances 接口的部分可选参数如下 */
	params.put("offset", 0);
	params.put("limit", 3);
	/*在这里指定所要用的签名算法，不指定默认为HmacSHA1*/
	//params.put("SignatureMethod", "HmacSHA256");
	/* generateUrl 方法生成请求串，但不发送请求。在正式请求中，可以删除下面这行代码。 */
	// System.out.println(module.generateUrl("DescribeInstances", params));

	String result = null;
	try {
		/* call 方法正式向指定的接口名发送请求，并把请求参数params传入，返回即是接口的请求结果。 */
		result = module.call("DescribeInstances", params);
		JSONObject json_result = new JSONObject(result);
		System.out.println(json_result);
	} catch (Exception e) {
		System.out.println("error..." + e.getMessage());
	}

}
}
```
