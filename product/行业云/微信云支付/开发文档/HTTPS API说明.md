# 说明
## 通讯说明
- 所有接口均使用https通信，数据包格式为json（http请求的content-type字段必须使用application/json）。
- 请求必须传认证或签名信息。其中撤单和退款请求，传签名和签名算法，其他请求传认证码和认证算法。
- 对响应要验证认证码。
- 所有接口参数名使用的字母均为小写。
## 发送请求举例（使用libcurl实现）
	/*
	用于接受响应数据的回调函数
	*/
	size_t recv_data(char *ptr, size_t size, size_t nmemb, void *parm)
	{
		size_t length = size * nmemb;
		std::string *data = (std::string*)parm;
		data.append(ptr, length);
		return length;
	}
	/*
	将request_str用POST方式发送到url，响应包填充到response指向的string中
	返回是否POST请求是否成功
	*/
	bool post(const std::string &request, const std::string &url, std::string *response)
	{
		CURL *hnd = curl_easy_init();
	
		curl_easy_setopt(hnd, CURLOPT_CUSTOMREQUEST, "POST");
		curl_easy_setopt(hnd, CURLOPT_URL, url);
		
		struct curl_slist *headers = NULL;
		headers = curl_slist_append(headers, "content-type: application/json");
		curl_easy_setopt(hnd, CURLOPT_HTTPHEADER, headers);
		
		curl_easy_setopt(hnd, CURLOPT_POSTFIELDS, request);
		
		// 设置云支付根证书
		curl_easy_setopt(curl,CURLOPT_SSL_VERIFYPEER,1);   
		curl_easy_setopt(curl,CURLOPT_SSL_VERIFYHOST,2);
	    curl_easy_setopt(curl,CURLOPT_CAINFO,"./cloudpayrootca.pem");  
	    
		curl_easy_setopt(curl_handle, CURLOPT_WRITEFUNCTION, recv_data);
		std::string rc;
		curl_easy_setopt(curl_handle, CURLOPT_WRITEDATA, (void *)&rc);		
	
		CURLcode ret = curl_easy_perform(hnd);
		if (CURLE_OK != ret) {
			return false;
		}
		*response = rc;
		curl_easy_cleanup(hnd);
		return true;
	}
## 数据包格式说明
- 请求包含两个字段：authen\_info和request\_content，前者表示签名或认证信息，后者表示请求具体内容，均为json结构。
- 响应包含两个字段：authen\_info和response\_content，前者表示认证信息，后者表示响应具体内容，均为json结构。
- 签名生成算法：RSASSA-PSS-2048-SHA256，私钥为服务商在云支付录入商户时，在网页上生成的签名私钥（该私钥只有服务商知道，云支付不知道，请妥善保存）
- 认证码生成算法：HMAC-SHA256，认证密钥为服务商在云支付录入商户时，在网页上生成的认证密钥
- 如果不填非必填字段，则不要设置该字段，如需清空该字段，需上传内容为空的该字段。
## 计算认证码举例（使用OpenSSL实现）
	/*
	返回是否成功，成功时认证码存放于hmac指向的string
	*/
	bool calc_HMAC_SHA256(const std::string &key, const std::string &input, std::string *hmac)
	{
	    unsigned char md[SHA256_DIGEST_LENGTH];//32 bytes
	    char format_md[65] = {0};
	
	    unsigned int md_len = sizeof(md);
	
	    HMAC_CTX ctx;
	    HMAC_CTX_init(&ctx);
	    if (!HMAC_Init_ex(&ctx, key.data(), (int)key.length(), EVP_sha256(), NULL)       ||
	        !HMAC_Update(&ctx, (const unsigned char *)input.data(), input.length()) ||
	        !HMAC_Final(&ctx, md, &md_len)) {
	
	        HMAC_CTX_cleanup(&ctx);
	        return false;
	    }
	    HMAC_CTX_cleanup(&ctx);
	
	    for (int i = 0; i < 32; i++) {
	        snprintf(&format_md[i * 2], 3, "%02x", md[i]);
	    }
	    hmac->assign(format_md);
	
	    // 转大写
	    transform(hmac->begin(), hmac->end(), hmac->begin(), ::toupper);
	    return true;
	}
## 计算签名举例（使用OpenSSL实现）
	/*
	对计算得到的签名进行base64编码之后输出
	返回是否成功，成功时签名存放于sign_base64encode指向的string
	*/
	bool calc_RSASSA_PSS_2048_SHA256(const std::string &key,
									 const std::string &content, 
	                  				 std::string *sign_base64encode)
	{
	    unsigned char digest[SHA256_DIGEST_LENGTH]; //32 bytes
	    int digest_len = sizeof(digest);
	
	    BIO *p_key_bio = BIO_new_mem_buf((void *)key.c_str(), (int)key.length());
	    std::shared_ptr<BIO> shared_ptr_bio(p_key_bio, BIO_free);
	    if (!p_key_bio) {
	        return false;
	    }
	
	    RSA *p_rsa = PEM_read_bio_RSAPrivateKey(p_key_bio, NULL, NULL, NULL);
	    std::shared_ptr<RSA> shared_ptr_rsa(p_rsa, RSA_free);
	    if (!p_rsa) {
	        return false;
	    }
	
	    EVP_MD_CTX md_ctx; //当前使用1.0.2e版本
	    EVP_MD_CTX_init   (&md_ctx);
	    EVP_DigestInit    (&md_ctx, EVP_sha256());
	    EVP_DigestUpdate  (&md_ctx, (const void*)content.c_str(), content.length());
	    EVP_DigestFinal   (&md_ctx, digest, (unsigned int *)&digest_len);
	    EVP_MD_CTX_cleanup(&md_ctx);
	
	    unsigned char em[256];
	    unsigned char sign[256];
	    int status;
	
	    status = RSA_padding_add_PKCS1_PSS(p_rsa, em, digest, EVP_sha256(), -2 /* maximum salt length*/);
	    if (!status) {
	        return false;
	    }
	
	    status = RSA_private_encrypt(sizeof(em), em, sign, p_rsa, RSA_NO_PADDING);
	    if (status == -1) {
	        return false;
	    }
	
	    *sign_base64encode = base64_encode(sign, sizeof(sign));
	    return true;
	}
## 请求举例（以刷卡支付为例）
- 构造request\_content结构，具体如下：

		{
			request_content":{
				"pay_mch_key":{
					"pay_platform":2,
					"out_mch_id":"1234mcWYS3M5TjKLorAZ',
					"out_sub_mch_id":"12343ycHpBDv8GX]fmSv',
					"out_shop_id":"1234ruQCleTa9w30AaAH'
				},
				"nonce_str":"542AB309ECA042FE92355BDEC4E2D733",
				"order_client":{
					"staff_id":"shop_manage_id_01',
					"machine_no":"34-64-a9-15-b4-cl",
					"terminal_type":1,
					"sdk_version":"1.6",
					"spbill_create_ip":"10.27.14.138",
					"device_id":"device_id_01"
				}
				"pay_content":{
					"author_code":"282129340414399818',
					"out_trade_no":"12341008b320170802191960015",
					"body":"生活用品套餐',
					"total_fee":1,
					"fee_type":"CNY"
				}
			}
		}

- 将request\_content从json转为字符串，根据认证算法计算出认证码，如下：

		A2F2F3C3506F3461212525C4917479B515ABB42BDC5909F7C012B6F74C0C1B99

- 构造authen\_info结构，设置相应的认证算法和认证码，具体如下：

		"authen_info":{
			"a":{
				"authen_type":1,
				"authen_code":"A2F2F3C3506F3461212525C4917479B515ABB42BDC5909F7C012B6F74C0C1B99"
			}
		}

- 构造请求数据包，包含authen\_info和request\_content两个结构，具体如下：

		{
			"request_content":"{
				"pay_mch_key":{
					"pay_platform":2,
					"out_mch_id":"1234mcWYS3M5TjKLorAZ",
					"out_sub_mch_id":"12343ycHpBDv8GXDfmSv",
					"out_shop_id":"1234ruQCleTa9w30AaAH"
				},
				"pay_content":{
					"out_trade_no":"12341008b320170802191960015",
					"author_code":"282129340414399818",
					"total_fee":1,
					"fee_type":"CNY",
					"body":"生活用品套餐"
				}
				"wxpay_pay_content_ext":{
					"attach":"",
					"goods_tag":"",
					"order_client":{
						"device_id":"device_id_01",
						"staff_id":"shop_manage_id_01",
						"terminal_type":1,
						"machine_no":"34-64-a9-15-b4-cl",
						"sdk_version":"1.6",
						"spbill_create_ip":"10.27.14.138"
					}
				},
				"nonce_str":"542AB309ECA042FE92355BDEC4E2D733"
			}",
			"authen_info":{
				"a":{
					"authen_type":1,
					"authen_code":"A2F2FBCB506FB461212525C4917479B515ABB42BDC5909F7C012B6F74C0ClB99"
				}
			}
		}

- 将json转为string，发送给服务器
## 响应举例（以刷卡支付为例）
- 把响应包从string转成json，取出json里面的response\_content和authen\_info，具体如下：

		{
			"response_content":"{
				"status":0,
				"description":"",
				"log_id":18654852,
				"internal_status":0,
				"micro_pay":{
					"pay_mch_key":{
						"pay_platform":2,
						"mch_id":"1900007941",
						"sub_mch_id":"1900008341",
						"out_mch_id":"1234mcWYS3iM5TjKLorAZ",
						"out_sub_mch_id":"12343ycHpBDv8GX]fmSvT7,
						"out_shop_id":"1234ruQCleTa9w30AaAH"
					},
					"order_content":{
						"out_trade_no":"12341008b320170802191960015",
						"transaction_id":"2017080221001004620281091091",
						"trade_type":1,
						"author_code":"282129340414399818",
						"time_expire":1501676124,
						"time_end":1501676005,
						"nonce_str":"542AB309ECA042FE92355BDEC4E2D733",
						"create_time":1501676004,
						"last_update_time":1501676005,
						"is_transforming":false,
						"total_fee":1,
						"fee_type":"CNY",
						"cash_fee":1,
						"settlement_total_fee":1,
						"body":"生活用品套餐",
						"alipay_order_content_ext":{
							"current_trade_state":2,
							"fund_bill_list":[
								{"fund_channel": "ALIPAYACCOUNT","amount": 1}
							],
							"point_amount":0,
							"invoice_amount":1
						}
					},
					"nonce_str":"SmM10CXPlZLalY9PIYdVGVgxcs58wDRG"
				}
			}",
			"authen_info":{
				"a":{
					"authen_type":1,
					"authen_code":"ACD4C1920A6C8646B395D0CBB4AF9B395AC0601D1883D8EF2D7BD7238C2991A5"
				}
			}
		}

- 对response\_content计算认证码，并将该认证码与authen\_info的authen\_code进行比较。
## 接口调用说明
- 如服务商不使用云支付提供的商户后台门店管理系统，需先调用门店接口设置门店信息，才能调用交易接口。
- 交易接口中的门店信息，必须和服务商在云支付后台设置的一致。
## 订单和退款单号说明
- 为了保护不同商户的订单号不重复，云支付为每个服务商录入的子商户分配了“云支付订单前缀”，在云支付后台的商户详情中可以看到，该商户的订单和退款单必须以云支付子商户号做前缀。
# 交易接口
## 刷卡支付
### 接口地址
>https://pay.qcloud.com/cpay/micro_pay  

content\_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>是</td>
      <td>PayMchKey</td>
      <td>支付商户信息，详见PayMchKey</td>
   </tr>
   <tr>
      <td>pay_content</td>
      <td>是</td>
      <td>PayContent</td>
      <td>订单信息，详见PayContent</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见OrderClient</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>消息id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td><b>错误码为407时，说明客户端发生异常，支付时单号重复，但金额等其他信息不重复，被云支付的防重入挡住，此时，请一定不要撤单，否则会造成已支付的订单退款，给商户造成损失。</b>其余错误码不用关注。 </td>
   </tr>
   <tr>
      <td>micro_pay</td>
      <td>否</td>
      <td>MicroPayResponse</td>
      <td>authen_info存在时必填。详见MicroPayResponse</td>
   </tr>
</table>

### MicroPayResponse结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>否</td>
      <td>PayMchKey</td>
      <td>支付商户信息，status为0时必填。详见PayMchKey</td>
   </tr>
   <tr>
      <td>order_content</td>
      <td>否</td>
      <td>OrderContent</td>
      <td>订单信息，status为0时必填。详见OrderContent</td>
   </tr>
</table>

### 构造刷卡支付请求例子
	/*
	构造请求字符串
	*/
	std::string gen_cloud_pay_micropay(
		const int         &pay_platform,
		const std::string &out_mch_id,
		const std::string &out_sub_mch_id,
		const std::string &out_shop_id,
		const std::string &out_trade_no,
		const std::string &author_code,
		const int64_t     &total_fee, 
		const std::string &fee_type, 
		const std::string &device_id,
		const std::string &staff_id,
		const int 		  &terminal_type,
		const std::string &machine_no,
		const std::string &sdk_version,
		const std::string &spbill_create_ip,
		const std::string &authen_key,
	)
	{
		Json::Value request_content;
		request_content["nonce_str"] = generate_random_nonce_str();

		Json::Value pay_mch_key, pay_content, order_client; 

		pay_mch_key["pay_platform"]    = pay_platform;
		pay_mch_key["out_mch_id"]      = out_mch_id;
		pay_mch_key["out_sub_mch_id"]  = out_sub_mch_id;
		pay_mch_key["out_shop_id"]     = out_shop_id;
		request_content["pay_mch_key"] = pay_mch_key;

		pay_content["out_trade_no"]    = out_trade_no;
		pay_content["author_code"]     = author_code;
		pay_content["total_fee"]       = total_fee;
		pay_content["fee_type"]        = fee_type;
		request_content["pay_content"] = pay_content;

		order_client["device_id"]        = device_id;
		order_client["staff_id"]   	     = staff_id;
		order_client["terminal_type"]    = terminal_type;
		order_client["machine_no"]       = machine_no;
		order_client["sdk_version"]      = sdk_version;
		order_client["spbill_create_ip"] = spbill_create_ip;
		request_content["order_client"]  = order_client;
		
		Json::FastWriter w;
		const std::string &rc = w.write(request_content);

		Json::Value authen_info, a;
		a["authen_type"] = 1;
		// 使用计算认证码举例（使用OpenSSL实现）中的函数计算认证码
		std::string authen_code;
		calc_HMAC_SHA256(authen_key, rc, &authen_code);
		a["authen_code"] = authen_code;
		authen_info["a"] = a;

		Json::Value request;
		request["request_content"] = rc;
		request["authen_info"] = authen_info;

		return w.write(request);
	}
	/*
	构造请求完毕之后，将请求通过POST方法发送到云支付接口对应的URL
	使用了发送请求举例（使用libcurl实现）中的post函数
	*/
	std::string response;
	post(request, "https://pay.qcloud.com/cpay/micro_pay", &response);
## 扫码支付
### 接口地址
>https://pay.qcloud.com/cpay/scan\_code\_pay

content_type：application/json
### 输入参数
<table border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>是</td>
      <td>PayMchKey</td>
      <td>支付商户信息，详见PayMchKey</td>
   </tr>
   <tr>
      <td>pay_content</td>
      <td>是</td>
      <td>PayContent</td>
      <td>订单信息，详见PayContent</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见OrderClient</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>消息id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>调试使用，调用者可以不予理会</td>
   </tr>
   <tr>
      <td>scan_code_pay</td>
      <td>否</td>
      <td>ScanCodePayResponse</td>
      <td>authen_info存在时必填。详见ScanCodePayResponse</td>
   </tr>
</table>

### ScanCodePayResponse结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>code_url</td>
      <td>否</td>
      <td>String(64)</td>
      <td>status为0时必填。用于扫码支付时转换成支付二维码 </td>
   </tr>
</table>

### 构造扫码支付请求例子
	/*
	构造请求字符串
	*/
	std::string gen_cloud_pay_scan_code_pay(
		const int         &pay_platform,
		const std::string &out_mch_id,
		const std::string &out_sub_mch_id,
		const std::string &out_shop_id,
		const std::string &out_trade_no,
		const int64_t     &total_fee, 
		const std::string &fee_type,
		const std::string &device_id,
		const std::string &staff_id,
		const int 		  &terminal_type,
		const std::string &machine_no,
		const std::string &sdk_version,
		const std::string &spbill_create_ip,
		const std::string &authen_key,
	)
	{
		Json::Value request_content;
		request_content["nonce_str"] = generate_random_nonce_str();

		Json::Value pay_mch_key, pay_content, order_client; 

		pay_mch_key["pay_platform"]    = pay_platform;
		pay_mch_key["out_mch_id"]      = out_mch_id;
		pay_mch_key["out_sub_mch_id"]  = out_sub_mch_id;
		pay_mch_key["out_shop_id"]     = out_shop_id;
		request_content["pay_mch_key"] = pay_mch_key;

		pay_content["out_trade_no"]    = out_trade_no;
		pay_content["total_fee"]       = total_fee;
		pay_content["fee_type"]        = fee_type;
		request_content["pay_content"] = pay_content;

		order_client["device_id"]        = device_id;
		order_client["staff_id"]   	     = staff_id;
		order_client["terminal_type"]    = terminal_type;
		order_client["machine_no"]       = machine_no;
		order_client["sdk_version"]      = sdk_version;
		order_client["spbill_create_ip"] = spbill_create_ip;
		request_content["order_client"]  = order_client;
		
		Json::FastWriter w;
		const std::string &rc = w.write(request_content);

		Json::Value authen_info, a;
		a["authen_type"] = 1;
		// 使用计算认证码举例（使用OpenSSL实现）中的函数计算认证码
		std::string authen_code;
		calc_HMAC_SHA256(authen_key, rc, &authen_code);
		a["authen_code"] = authen_code;
		authen_info["a"] = a;

		Json::Value request;
		request["request_content"] = rc;
		request["authen_info"] = authen_info;

		return w.write(request);
	}
	/*
	构造请求完毕之后，将请求通过POST方法发送到云支付接口对应的URL
	使用了发送请求举例（使用libcurl实现）中的post函数
	*/
	std::string response;
	post(request, "https://pay.qcloud.com/cpay/scan_code_pay", &response);
## 撤销订单
### 特别说明
- **微信支付只能撤销刷卡支付的订单**
- **支付宝只有发生支付超时或者支付结果未知时可调用撤销**
- **撤单的终端必须和发起支付的终端是同一个（为保证安全）**
### 接口地址
>https://pay.qcloud.com/cpay/reverse

content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>是</td>
      <td>PayMchKey</td>
      <td>支付商户信息，详见PayMchKey</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见OrderClient</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的订单号，前缀必须是云支付子商户号</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>消息id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>调试使用，调用者可以不予理会</td>
   </tr>
   <tr>
      <td>reverse</td>
      <td>否</td>
      <td>ReverseResponse</td>
      <td>authen_info存在时必填。详见ReverseResponse</td>
   </tr>
</table>

### ReverseResponse结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 构造撤销订单请求例子
	/*
	构造请求字符串
	*/
	std::string gen_cloud_pay_reverse(
		const int         &pay_platform,
		const std::string &out_mch_id,
		const std::string &out_sub_mch_id,
		const std::string &out_shop_id,
		const std::string &out_trade_no,
		const std::string &device_id,
		const std::string &staff_id,
		const int 		  &terminal_type,
		const std::string &machine_no,
		const std::string &sdk_version,
		const std::string &spbill_create_ip,
		const std::string &signing_key,
	)
	{
		Json::Value request_content;
		request_content["nonce_str"] = generate_random_nonce_str();
		request_content["out_trade_no"] = out_trade_no;

		Json::Value pay_mch_key, order_client; 

		pay_mch_key["pay_platform"]    = pay_platform;
		pay_mch_key["out_mch_id"]      = out_mch_id;
		pay_mch_key["out_sub_mch_id"]  = out_sub_mch_id;
		pay_mch_key["out_shop_id"]     = out_shop_id;
		request_content["pay_mch_key"] = pay_mch_key;

		order_client["device_id"]        = device_id;
		order_client["staff_id"]   	     = staff_id;
		order_client["terminal_type"]    = terminal_type;
		order_client["machine_no"]       = machine_no;
		order_client["sdk_version"]      = sdk_version;
		order_client["spbill_create_ip"] = spbill_create_ip;
		request_content["order_client"]  = order_client;
		
		Json::FastWriter w;
		const std::string &rc = w.write(request_content);

		Json::Value authen_info, s;
		s["sign_type"] = 1;
		// 使用计算签名举例（使用OpenSSL实现）中的函数计算签名
		std::string signature;
		calc_RSASSA_PSS_2048_SHA256(signing_key, rc, &signature);
		s["signature"] = signature;
		authen_info["s"] = s;

		Json::Value request;
		request["request_content"] = rc;
		request["authen_info"] = authen_info;

		return w.write(request);
	}
	/*
	构造请求完毕之后，将请求通过POST方法发送到云支付接口对应的URL
	使用了发送请求举例（使用libcurl实现）中的post函数
	*/
	std::string response;
	post(request, "https://pay.qcloud.com/cpay/reverse", &response);
## 申请退款
### 接口地址
>https://pay.qcloud.com/cpay/refund

content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>是</td>
      <td>PayMchKey</td>
      <td>支付商户信息，详见PayMchKey</td>
   </tr>
   <tr>
      <td>refund_content</td>
      <td>是</td>
      <td>RefundContent</td>
      <td>订单信息，详见RefundContent</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见OrderClient</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>消息id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>调试使用，调用者可以不予理会</td>
   </tr>
   <tr>
      <td>refund</td>
      <td>否</td>
      <td>RefundResponse</td>
      <td>authen_info存在时必填。详见RefundResponse</td>
   </tr>
</table>

### RefundResponse结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>否</td>
      <td>PayMchKey</td>
      <td>支付商户信息，status为0时必填。详见PayMchKey</td>
   </tr>
   <tr>
      <td>refund_order_content</td>
      <td>否</td>
      <td>RefundOrderContent</td>
      <td>订单信息，status为0时必填。详见RefundOrderContent</td>
   </tr>
</table>

### 构造申请退款请求例子
	/*
	构造请求字符串
	*/
	std::string gen_cloud_pay_refund(
		const int         &pay_platform,
		const std::string &out_mch_id,
		const std::string &out_sub_mch_id,
		const std::string &out_shop_id,
		const std::string &out_trade_no,
		const std::string &out_refund_no,
		const std::string &total_fee,
		const std::string &refund_fee,
		const std::string &refund_fee_type,
		const std::string &device_id,
		const std::string &staff_id,
		const int 		  &terminal_type,
		const std::string &machine_no,
		const std::string &sdk_version,
		const std::string &spbill_create_ip,
		const std::string &signing_key,
	)
	{
		Json::Value request_content;
		request_content["nonce_str"] = generate_random_nonce_str();

		Json::Value pay_mch_key, pay_content, order_client; 

		pay_mch_key["pay_platform"]    = pay_platform;
		pay_mch_key["out_mch_id"]      = out_mch_id;
		pay_mch_key["out_sub_mch_id"]  = out_sub_mch_id;
		pay_mch_key["out_shop_id"]     = out_shop_id;
		request_content["pay_mch_key"] = pay_mch_key;

		pay_content["out_trade_no"]    = out_trade_no;
		pay_content["out_refund_no"]   = out_refund_no;
		pay_content["total_fee"]       = total_fee;
		pay_content["refund_fee"]      = refund_fee;
		pay_content["refund_fee_type"] = refund_fee_type;
		request_content["pay_content"] = pay_content;

		order_client["device_id"]        = device_id;
		order_client["staff_id"]   	     = staff_id;
		order_client["terminal_type"]    = terminal_type;
		order_client["machine_no"]       = machine_no;
		order_client["sdk_version"]      = sdk_version;
		order_client["spbill_create_ip"] = spbill_create_ip;
		request_content["order_client"]  = order_client;
		
		Json::FastWriter w;
		const std::string &rc = w.write(request_content);

		Json::Value authen_info, s;
		s["sign_type"] = 1;
		// 使用计算签名举例（使用OpenSSL实现）中的函数计算签名
		std::string signature;
		calc_RSASSA_PSS_2048_SHA256(signing_key, rc, &signature);
		s["signature"] = signature;
		authen_info["s"] = s;

		Json::Value request;
		request["request_content"] = rc;
		request["authen_info"] = authen_info;

		return w.write(request);
	}
	/*
	构造请求完毕之后，将请求通过POST方法发送到云支付接口对应的URL
	使用了发送请求举例（使用libcurl实现）中的post函数
	*/
	std::string response;
	post(request, "https://pay.qcloud.com/cpay/refund", &response);
## 关闭订单
### 接口地址
>https://pay.qcloud.com/cpay/close_order

content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>是</td>
      <td>PayMchKey</td>
      <td>支付商户信息，详见PayMchKey</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见OrderClient</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的订单号，前缀必须是云支付子商户号</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>trade_type</td>
      <td>是</td>
      <td>TradeType</td>
      <td>交易类型，枚举值详见TradeType</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见本节ResponseContent</td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>消息id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>调试使用，调用者可以不予理会</td>
   </tr>
   <tr>
      <td>close_order</td>
      <td>否</td>
      <td>CloseOrderResponse</td>
      <td>authen_info存在时必填。详见CloseOrderResponse</td>
   </tr>
</table>

### CloseOrderResponse结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 构造关闭订单请求例子
	/*
	构造请求字符串
	*/
	std::string gen_cloud_pay_close_order(
		const int         &pay_platform,
		const std::string &out_mch_id,
		const std::string &out_sub_mch_id,
		const std::string &out_shop_id,
		const std::string &out_trade_no,
		const int 		  &trade_type,
		const std::string &device_id,
		const std::string &staff_id,
		const int 		  &terminal_type,
		const std::string &machine_no,
		const std::string &sdk_version,
		const std::string &spbill_create_ip,
		const std::string &authen_key,
	)
	{
		Json::Value request_content;
		request_content["nonce_str"] = generate_random_nonce_str();
		request_content["out_trade_no"] = out_trade_no;
		request_content["trade_type"] = trade_type;

		Json::Value pay_mch_key, order_client; 

		pay_mch_key["pay_platform"]    = pay_platform;
		pay_mch_key["out_mch_id"]      = out_mch_id;
		pay_mch_key["out_sub_mch_id"]  = out_sub_mch_id;
		pay_mch_key["out_shop_id"]     = out_shop_id;
		request_content["pay_mch_key"] = pay_mch_key;

		order_client["device_id"]        = device_id;
		order_client["staff_id"]   	     = staff_id;
		order_client["terminal_type"]    = terminal_type;
		order_client["machine_no"]       = machine_no;
		order_client["sdk_version"]      = sdk_version;
		order_client["spbill_create_ip"] = spbill_create_ip;
		request_content["order_client"]  = order_client;
		
		Json::FastWriter w;
		const std::string &rc = w.write(request_content);

		Json::Value authen_info, s;
		a["authen_type"] = 1;
		// 使用计算认证码举例（使用OpenSSL实现）中的函数计算认证码
		std::string authen_code;
		calc_HMAC_SHA256(authen_key, rc, &authen_code);
		a["authen_code"] = authen_code;
		authen_info["a"] = a;

		Json::Value request;
		request["request_content"] = rc;
		request["authen_info"] = authen_info;

		return w.write(request);
	}
	/*
	构造请求完毕之后，将请求通过POST方法发送到云支付接口对应的URL
	使用了发送请求举例（使用libcurl实现）中的post函数
	*/
	std::string response;
	post(request, "https://pay.qcloud.com/cpay/reverse", &response);
## 查询订单
### 接口地址
>https://pay.qcloud.com/cpay/query_order

content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见本节RequestContent</td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>是</td>
      <td>PayMchKey</td>
      <td>支付商户信息，详见PayMchKey</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见OrderClient</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的订单号，前缀必须是云支付子商户号</td>
   </tr>
   <tr>
      <td>trade_type</td>
      <td>是</td>
      <td>TradeType</td>
      <td>交易类型，枚举值详见TradeType</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>消息id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>调试使用，调用者可以不予理会</td>
   </tr>
   <tr>
      <td>query_order</td>
      <td>否</td>
      <td>QueryOrderResponse</td>
      <td>authen_info存在时必填。详见QueryOrderResponse</td>
   </tr>
</table>

### QueryOrderResponse结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>否</td>
      <td>PayMchKey</td>
      <td>支付商户信息，status为0时必填。详见PayMchKey</td>
   </tr>
   <tr>
      <td>order_content</td>
      <td>否</td>
      <td>OrderContent</td>
      <td>订单信息，status为0时必填。详见OrderContent</td>
   </tr>
</table>

### 构造查询订单请求例子
	/*
	构造请求字符串
	*/
	std::string gen_cloud_pay_query_order(
		const int         &pay_platform,
		const std::string &out_mch_id,
		const std::string &out_sub_mch_id,
		const std::string &out_shop_id,
		const std::string &out_trade_no,
		const int 		  &trade_type,
		const std::string &device_id,
		const std::string &staff_id,
		const int 		  &terminal_type,
		const std::string &machine_no,
		const std::string &sdk_version,
		const std::string &spbill_create_ip,
		const std::string &authen_key,
	)
	{
		Json::Value request_content;
		request_content["nonce_str"] = generate_random_nonce_str();
		request_content["out_trade_no"] = out_trade_no;
		request_content["trade_type"] = trade_type;

		Json::Value pay_mch_key, order_client; 

		pay_mch_key["pay_platform"]    = pay_platform;
		pay_mch_key["out_mch_id"]      = out_mch_id;
		pay_mch_key["out_sub_mch_id"]  = out_sub_mch_id;
		pay_mch_key["out_shop_id"]     = out_shop_id;
		request_content["pay_mch_key"] = pay_mch_key;

		order_client["device_id"]        = device_id;
		order_client["staff_id"]   	     = staff_id;
		order_client["terminal_type"]    = terminal_type;
		order_client["machine_no"]       = machine_no;
		order_client["sdk_version"]      = sdk_version;
		order_client["spbill_create_ip"] = spbill_create_ip;
		request_content["order_client"]  = order_client;
		
		Json::FastWriter w;
		const std::string &rc = w.write(request_content);

		Json::Value authen_info, s;
		a["authen_type"] = 1;
		// 使用计算认证码举例（使用OpenSSL实现）中的函数计算认证码
		std::string authen_code;
		calc_HMAC_SHA256(authen_key, rc, &authen_code);
		a["authen_code"] = authen_code;
		authen_info["a"] = a;

		Json::Value request;
		request["request_content"] = rc;
		request["authen_info"] = authen_info;

		return w.write(request);
	}
	/*
	构造请求完毕之后，将请求通过POST方法发送到云支付接口对应的URL
	使用了发送请求举例（使用libcurl实现）中的post函数
	*/
	std::string response;
	post(request, "https://pay.qcloud.com/cpay/query_order", &response);
## 查询退款单
### 接口地址
>https://pay.qcloud.com/cpay/query\_refund\_order

content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>是</td>
      <td>PayMchKey</td>
      <td>支付商户信息，详见PayMchKey</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见OrderClient</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的订单号，前缀必须是云支付子商户号</td>
   </tr>
   <tr>
      <td>out_refund_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的退款单号，前缀必须是云支付子商户号</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>消息id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>调试使用，调用者可以不予理会</td>
   </tr>
   <tr>
      <td>query_refund_order</td>
      <td>否</td>
      <td>QueryRefundOrderResponse</td>
      <td>authen_info存在时，必填。详见QueryRefundOrderResponse</td>
   </tr>
</table>

### QueryRefundOrderResponse结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>否</td>
      <td>PayMchKey</td>
      <td>支付商户信息，status为0时必填。详见PayMchKey</td>
   </tr>
   <tr>
      <td>refund_order_content</td>
      <td>否</td>
      <td>RefundOrderContent[]</td>
      <td>订单信息，status为0时必填。详见RefundOrderContent</td>
   </tr>
</table>

### 构造查询退款单请求例子
	/*
	构造请求字符串
	*/
	std::string gen_cloud_pay_query_refund_order(
		const int         &pay_platform,
		const std::string &out_mch_id,
		const std::string &out_sub_mch_id,
		const std::string &out_shop_id,
		const std::string &out_trade_no,
		const std::string &out_refund_no,
		const std::string &device_id,
		const std::string &staff_id,
		const int 		  &terminal_type,
		const std::string &machine_no,
		const std::string &sdk_version,
		const std::string &spbill_create_ip,
		const std::string &authen_key,
	)
	{
		Json::Value request_content;
		request_content["nonce_str"] = generate_random_nonce_str();
		request_content["out_trade_no"] = out_trade_no;
		request_content["out_refund_no"] = out_refund_no;

		Json::Value pay_mch_key, order_client; 

		pay_mch_key["pay_platform"]    = pay_platform;
		pay_mch_key["out_mch_id"]      = out_mch_id;
		pay_mch_key["out_sub_mch_id"]  = out_sub_mch_id;
		pay_mch_key["out_shop_id"]     = out_shop_id;
		request_content["pay_mch_key"] = pay_mch_key;

		order_client["device_id"]        = device_id;
		order_client["staff_id"]   	     = staff_id;
		order_client["terminal_type"]    = terminal_type;
		order_client["machine_no"]       = machine_no;
		order_client["sdk_version"]      = sdk_version;
		order_client["spbill_create_ip"] = spbill_create_ip;
		request_content["order_client"]  = order_client;
		
		Json::FastWriter w;
		const std::string &rc = w.write(request_content);

		Json::Value authen_info, s;
		a["authen_type"] = 1;
		// 使用计算认证码举例（使用OpenSSL实现）中的函数计算认证码
		std::string authen_code;
		calc_HMAC_SHA256(authen_key, rc, &authen_code);
		a["authen_code"] = authen_code;
		authen_info["a"] = a;

		Json::Value request;
		request["request_content"] = rc;
		request["authen_info"] = authen_info;

		return w.write(request);
	}
	/*
	构造请求完毕之后，将请求通过POST方法发送到云支付接口对应的URL
	使用了发送请求举例（使用libcurl实现）中的post函数
	*/
	std::string response;
	post(request, "https://pay.qcloud.com/cpay/query_refund_order", &response);
## 支付成功回调
### 接口地址
服务商在云支付管理后台配置的回调地址（https）  
content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>是</td>
      <td>PayMchKey</td>
      <td>支付商户信息，详见PayMchKey</td>
   </tr>
   <tr>
      <td>order_content</td>
      <td>是</td>
      <td>OrderContent</td>
      <td>订单信息，详见OrderContent</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见本节ResponseContent</td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>错误码。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
</table>

## 撤单成功回调
### 接口地址
服务商在云支付管理后台配置的回调地址（https）  
content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的订单号，前缀必须是云支付子商户号</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>错误码。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
</table>

## 退款成功回调
### 接口地址
服务商在云支付管理后台配置的回调地址（https）  
content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>pay_mch_key</td>
      <td>是</td>
      <td>PayMchKey</td>
      <td>支付商户信息。详见PayMchKey</td>
   </tr>
   <tr>
      <td>refund_order_content</td>
      <td>是</td>
      <td>RefundOrderContent[]</td>
      <td>订单信息。详见RefundOrderContent</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>错误码。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
</table>

# 门店接口
## 设置门店信息
### 特别说明
- 如使用接口配置门店信息，则不要再使用云支付提供的商户管理后台页面配置门店信息，否则会造成云支付和服务商系统的门店信息不一致。
### 接口地址
>https://pay.qcloud.com/cpay/set\_sub\_mch\_shop\_info

content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>out_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给服务商的帐号，固定20个数字或者字母</td>
   </tr>
   <tr>
      <td>out_sub_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给子商户的帐号，固定20个数字或者字母</td>
   </tr>
   <tr>
      <td>is_all</td>
      <td>是</td>
      <td>Bool</td>
      <td><b>True表示设置全量门店信息，会删除未在请求中的门店。<br>False表示设置增量门店信息，只会修改或增加门店。</b></td>
   </tr>

   <tr>
      <td>shop_infos</td>
      <td>是</td>
      <td>ShopInfo[]</td>
      <td>门店信息列表。详见ShopInfo</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>消息id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>调试使用，调用者可以不予理会</td>
   </tr>
   <tr>
      <td>set_shop_info</td>
      <td>否</td>
      <td>SetShopInfoResponse</td>
      <td>authen_info存在时必填。详见SetShopInfoResponse</td>
   </tr>
</table>

### SetShopInfoResponse结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>set_shop_infos</td>
      <td>是</td>
      <td>ShopInfo[]</td>
      <td>设置门店完成功后，所有的门店信息列表。详见ShopInfo </td>
   </tr>
</table>

### 构造设置门店请求例子
	/*
	构造请求字符串
	*/
	std::string gen_cloud_pay_set_sub_mch_shop_info(
		const std::string &out_mch_id,
		const std::string &out_sub_mch_id,
		bool 			  is_all，
		const std::string &authen_key
	)
	{
		Json::Value request_content;
		request_content["nonce_str"] = generate_random_nonce_str();
		request_content["out_mch_id"] = out_mch_id;
		request_content["out_sub_mch_id"] = out_sub_mch_id;
		request_content["is_all"] = is_all;

		Json::Value shop_infos; 

		Json::Value shop1, shop2;
		shop1["shop_name"] = "shop1";
		Json::Value shop1_devices, shop1_staffs, tmp_device1, tmp_staff1;
		tmp_device1["device_id"] = "1";
		tmp_device1["device_type"] = 3;// 3: 混合支付设备，支持刷卡支付+扫码支付
		shop1_devices.append(tmp_device1);
		shop1["device_infos"] = shop1_devices;
		tmp_staff1["staff_id"] = "1";
		tmp_staff1["staff_name"] = "staff1";
		tmp_staff1["shop_manager"] = true;
		shop1_staffs.append(tmp_staff1);
		shop1["staff_infos"] = shop1_staffs;
		shop_infos.append(shop1);

		shop2["shop_name"] = "shop2";
		Json::Value shop2_devices, shop2_staffs, tmp_device2, tmp_staff2;
		tmp_device2["device_id"] = "1";
		tmp_device2["device_type"] = 3;// 3: 混合支付设备，支持刷卡支付+扫码支付
		shop2_devices.append(tmp_device2);
		shop2["device_infos"] = shop2_devices;
		tmp_staff2["staff_id"] = "1";
		tmp_staff2["staff_name"] = "staff2";
		tmp_staff2["shop_manager"] = true;
		shop2_staffs.append(tmp_staff2);
		shop2["staff_infos"] = shop2_staffs;
		shop_infos.append(shop2);
		
		request_content["shop_infos"] = shop_infos;
		
		Json::FastWriter w;
		const std::string &rc = w.write(request_content);

		Json::Value authen_info, s;
		a["authen_type"] = 1;
		// 使用计算认证码举例（使用OpenSSL实现）中的函数计算认证码
		std::string authen_code;
		calc_HMAC_SHA256(authen_key, rc, &authen_code);
		a["authen_code"] = authen_code;
		authen_info["a"] = a;

		Json::Value request;
		request["request_content"] = rc;
		request["authen_info"] = authen_info;

		return w.write(request);
	}
	/*
	构造请求完毕之后，将请求通过POST方法发送到云支付接口对应的URL
	使用了发送请求举例（使用libcurl实现）中的post函数
	*/
	std::string response;
	post(request, "https://pay.qcloud.com/cpay/set_sub_mch_shop_info", &response);
## 查询门店信息
### 接口地址
>https://pay.qcloud.com/cpay/query\_sub\_mch\_shop\_info

content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>out_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给服务商的帐号，固定20个数字或者字母</td>
   </tr>
   <tr>
      <td>out_sub_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给子商户的帐号，固定20个数字或者字母</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随即字符串</td>
   </tr>
   <tr>
      <td>page_num</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>页码</td>
   </tr>
   <tr>
      <td>page_size</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>单页条数</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>消息id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>调试使用，调用者可以不予理会</td>
   </tr>
   <tr>
      <td>query_shop_info</td>
      <td>否</td>
      <td>QueryShopInfoResponse</td>
      <td>authen_info存在时必填。详见QueryShopInfoResponse</td>
   </tr>
</table>

### QueryShopInfoResponse结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td><b>status为0时返回以下参数：</b></td>
   </tr>
   <tr>
      <td>shop_infos</td>
      <td>否</td>
      <td>ShopInfo []</td>
      <td>子商户信息，详见 ShopInfo</td>
   </tr>
   <tr>
      <td>total_count</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>数据总数</td>
   </tr>
</table>

### 构造查询门店信息请求例子
	/*
	构造请求字符串
	*/
	std::string gen_cloud_pay_query_sub_mch_shop_info(
		const std::string &out_mch_id,
		const std::string &out_sub_mch_id,
		const int 		   page_num,
		const int 		   page_size,
		const std::string &authen_key
	)
	{
		Json::Value request_content;
		request_content["nonce_str"] = generate_random_nonce_str();
		request_content["out_mch_id"] = out_mch_id;
		request_content["out_sub_mch_id"] = out_sub_mch_id;
		request_content["page_num"] = page_num;
		request_content["page_size"] = page_size;
		
		Json::FastWriter w;
		const std::string &rc = w.write(request_content);

		Json::Value authen_info, s;
		a["authen_type"] = 1;
		// 使用计算认证码举例（使用OpenSSL实现）中的函数计算认证码
		std::string authen_code;
		calc_HMAC_SHA256(authen_key, rc, &authen_code);
		a["authen_code"] = authen_code;
		authen_info["a"] = a;

		Json::Value request;
		request["request_content"] = rc;
		request["authen_info"] = authen_info;

		return w.write(request);
	}
	/*
	构造请求完毕之后，将请求通过POST方法发送到云支付接口对应的URL
	使用了发送请求举例（使用libcurl实现）中的post函数
	*/
	std::string response;
	post(request, "https://pay.qcloud.com/cpay/query_sub_mch_shop_info", &response);
# 监控上报接口
## 上报客户端接口监控信息
### 接口地址
>https://pay.qcloud.com/cpay/upload\_client\_monitor\_info

content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>out_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付给服务商的帐号</td>
   </tr>
   <tr>
      <td>out_sub_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给子商户的帐号，固定20个数字或者字母</td>
   </tr>
   <tr>
      <td>out_shop_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给门店的账号</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见OrderClient</td>
   </tr>
   <tr>
      <td>interval</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>上报间隔，单位：s</td>
   </tr>
   <tr>
      <td>is_compress</td>
      <td>是</td>
      <td>bool</td>
      <td>客户端根据日志大小判断是否需要压缩</td>
   </tr>
   <tr>
      <td>compress_type</td>
      <td>否</td>
      <td>CompressType</td>
      <td>压缩算法类型，is_compress为true时必填，详见CompressType</td>
   </tr>
   <tr>
      <td>compressed_monitor_info<br><br>uncompressed_monitor_info</td>
      <td>二选一</td>
      <td>String<br><br>UncompressedMonitorInfo</td>
      <td>压缩数据<br><br>未压缩数据，详见UncompressedMonitorInfo</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### UncompressedMonitorInfo结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>client_int_results</td>
      <td>否</td>
      <td>ClientIntResult</td>
      <td>客户端接口调用结果，详见ClientIntResult</td>
   </tr>
   <tr>
      <td>machine_info</td>
      <td>是</td>
      <td>String</td>
      <td>cpu使用率，内存使用率，磁盘使用情况等，json结构</td>
   </tr>
</table>

### ClientIntResult结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>interface</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>接口类型，详见Interface</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0：成功，非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>是</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>time_cost</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>接口成功平均时延，单位：ms</td>
   </tr>
   <tr>
      <td>start_time</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>接口开始时间，时间戳（秒）</td>
   </tr>
   <tr>
      <td>logs</td>
      <td>否</td>
      <td>String</td>
      <td>接口执行过程中产生的日志列表</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>后台生成的log_id，方便对齐日志</td>
   </tr>
   <tr>
      <td>domain_name</td>
      <td>是</td>
      <td>String(1024)</td>
      <td>服务端域名</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>消息id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>调试使用，调用者可以不予理会</td>
   </tr>
   <tr>
      <td>upload_client_monitor_info</td>
      <td>否</td>
      <td>UploadClientMonitorInfoResponse</td>
      <td>authen_info存在时，必填。详见UploadClientMonitorInfoResponse</td>
   </tr>
</table>

### UploadClientMonitorInfoResponse结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>interval</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>status为0时必填。期望上报间隔，单位：s。<br>0表示不用改变当前上报间隔</td>
   </tr>
</table>

### 构造上报客户端接口监控信息请求例子
	/*
	构造请求字符串
	*/
	std::string gen_cloud_pay_upload_client_monitor_info(
		const std::string &out_mch_id,
		const std::string &out_sub_mch_id,
		const std::string &out_shop_id,
		const std::string &device_id,
		const std::string &staff_id,
		const int 		  &terminal_type,
		const std::string &machine_no,
		const std::string &sdk_version,
		const std::string &spbill_create_ip,
		const int 		   interval,
		const std::string &machine_info,
		const std::string &authen_key,
	)
	{
		Json::Value request_content;
		request_content["out_mch_id"] = out_mch_id;
		request_content["out_sub_mch_id"] = out_sub_mch_id;
		request_content["out_shop_id"] = out_shop_id;
		
		request_content["nonce_str"] = generate_random_nonce_str();
		request_content["interval"] = interval;
		request_content["is_compress"] = false;

		Json::Value order_client; 
		order_client["device_id"]        = device_id;
		order_client["staff_id"]   	     = staff_id;
		order_client["terminal_type"]    = terminal_type;
		order_client["machine_no"]       = machine_no;
		order_client["sdk_version"]      = sdk_version;
		order_client["spbill_create_ip"] = spbill_create_ip;
		request_content["order_client"]  = order_client;

		Json::Value uncompressed_monitor_info, client_int_results, client_int_result1;
		client_int_result1["interface"] = "scan_code_pay";
		client_int_result1["status"] = 0;
		client_int_result1["description"] = "description";
		client_int_result1["time_cost"] = 100;
		client_int_result1["start_time"] = 1505805297;
		client_int_result1["log_id"] = 73648593;
		client_int_result1["domain_name"] = "https://pay.qcloud.com/cpay";
		client_int_results.append(client_int_result1);
		uncompressed_monitor_info["machine_info"] = machine_info;
		request_content["uncompressed_monitor_info"]  = uncompressed_monitor_info;

		Json::FastWriter w;
		const std::string &rc = w.write(request_content);

		Json::Value authen_info, s;
		a["authen_type"] = 1;
		// 使用计算认证码举例（使用OpenSSL实现）中的函数计算认证码
		std::string authen_code;
		calc_HMAC_SHA256(authen_key, rc, &authen_code);
		a["authen_code"] = authen_code;
		authen_info["a"] = a;

		Json::Value request;
		request["request_content"] = rc;
		request["authen_info"] = authen_info;

		return w.write(request);
	}
	/*
	构造请求完毕之后，将请求通过POST方法发送到云支付接口对应的URL
	使用了发送请求举例（使用libcurl实现）中的post函数
	*/
	std::string response;
	post(request, "https://pay.qcloud.com/cpay/upload_client_monitor_info", &response);
## 上报客户端机器配置信息
### 接口地址
>https://pay.qcloud.com/cpay/upload\_client\_conf\_info

content_type：application/json
### 输入参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>request_content</td>
      <td>是</td>
      <td>RequestContent</td>
      <td>请求内容，详见<b>本节RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### RequestContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>out_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给服务商的帐号，固定20个数字或者字母</td>
   </tr>
   <tr>
      <td>out_sub_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给子商户的帐号，固定20个数字或者字母</td>
   </tr>
   <tr>
      <td>out_shop_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付唯一标识门店的账号</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见OrderClient</td>
   </tr>
   <tr>
      <td>machine_info</td>
      <td>是</td>
      <td>String</td>
      <td>主机信息，如主机名，磁盘，CPU，内存信息等，json结构</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 返回参数
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>response_content</td>
      <td>是</td>
      <td>ResponseContent</td>
      <td>请求内容，详见<b>本节ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见AuthenInfo</td>
   </tr>
</table>

### ResponseContent结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见Status。0 ：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
   <tr>
      <td>log_id</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>消息id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>调试使用，调用者可以不予理会</td>
   </tr>
   <tr>
      <td>upload_client_conf_info</td>
      <td>否</td>
      <td>UploadClientConfInfoResponse</td>
      <td>authen_info存在时必填。详见UploadClientConfInfoResponse</td>
   </tr>
</table>

### UploadClientConfInfoResponse结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

### 构造上报客户端机器配置信息请求例子
	/*
	构造请求字符串
	*/
	std::string gen_cloud_pay_upload_client_conf_info(
		const std::string &out_mch_id,
		const std::string &out_sub_mch_id,
		const std::string &out_shop_id,
		const std::string &device_id,
		const std::string &staff_id,
		const int 		  &terminal_type,
		const std::string &machine_no,
		const std::string &sdk_version,
		const std::string &spbill_create_ip,
		const std::string &machine_info,
		const std::string &authen_key,
	)
	{
		Json::Value request_content;
		request_content["out_mch_id"] = out_mch_id;
		request_content["out_sub_mch_id"] = out_sub_mch_id;
		request_content["out_shop_id"] = out_shop_id;
		
		request_content["nonce_str"] = generate_random_nonce_str();

		Json::Value order_client; 
		order_client["device_id"]        = device_id;
		order_client["staff_id"]   	     = staff_id;
		order_client["terminal_type"]    = terminal_type;
		order_client["machine_no"]       = machine_no;
		order_client["sdk_version"]      = sdk_version;
		order_client["spbill_create_ip"] = spbill_create_ip;
		request_content["order_client"]  = order_client;

		request_content["machine_info"]  = machine_info;

		Json::FastWriter w;
		const std::string &rc = w.write(request_content);

		Json::Value authen_info, s;
		a["authen_type"] = 1;
		// 使用计算认证码举例（使用OpenSSL实现）中的函数计算认证码
		std::string authen_code;
		calc_HMAC_SHA256(authen_key, rc, &authen_code);
		a["authen_code"] = authen_code;
		authen_info["a"] = a;

		Json::Value request;
		request["request_content"] = rc;
		request["authen_info"] = authen_info;

		return w.write(request);
	}
	/*
	构造请求完毕之后，将请求通过POST方法发送到云支付接口对应的URL
	使用了发送请求举例（使用libcurl实现）中的post函数
	*/
	std::string response;
	post(request, "https://pay.qcloud.com/cpay/upload_client_conf_info", &response);
# 公共数据结构
## 认证签名信息
### AuthenInfo结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>a<br><br>s</td>
      <td>二选一</td>
      <td>Authen<br><br>Signature</td>
      <td>认证信息，详见Authen<br><br>签名信息，详见Signature</td>
   </tr>
</table>

### Authen结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>authen_type</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>认证算法，详见AuthenType</td>
   </tr>
   <tr>
      <td>authen_code</td>
      <td>是</td>
      <td>String(2048)</td>
      <td>认证码</td>
   </tr>
</table>

### Signature结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>sign_type</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>签名算法，详见Signature</td>
   </tr>
   <tr>
      <td>sign</td>
      <td>是</td>
      <td>String(2048)</td>
      <td>签名内容</td>
   </tr>
</table>

## 订单信息
### OrderContent结构（仅作为返回参数）
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>子商户订单号</td>
   </tr>
   <tr>
      <td>transaction_id</td>
      <td>否</td>
      <td>String(32)</td>
      <td>第三方支付平台的订单号</td>
   </tr>
   <tr>
      <td>trade_type</td>
      <td>否</td>
      <td>TradeType</td>
      <td>交易类型，详见TradeType</td>
   </tr>
   <tr>
      <td>author_code</td>
      <td>否</td>
      <td>String(128)</td>
      <td>刷卡支付时的授权码</td>
   </tr>
   <tr>
      <td>code_url</td>
      <td>否</td>
      <td>String(64)</td>
      <td>扫码支付时，用于扫码支付时转换成支付二维码</td>
   </tr>
   <tr>
      <td>time_expire</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>订单失效时间（刷卡支付不需要该字段），时间戳（秒）</td>
   </tr>
   <tr>
      <td>notify_url</td>
      <td>否</td>
      <td>String(1024)</td>
      <td>第三方支付平台回调url（刷卡支付不需要该字段）</td>
   </tr>
   <tr>
      <td>time_end</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>支付完成时间，时间戳（秒）</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>create_time</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>订单创建时间，时间戳（秒）</td>
   </tr>
   <tr>
      <td>last_update_time</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>订单最近更新时间，时间戳（秒）</td>
   </tr>
   <tr>
      <td>is_transforming</td>
      <td>是</td>
      <td>Bool</td>
      <td>系统是否正在处理中</td>
   </tr>
   <tr>
      <td>total_fee</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>订单总金额，单位分</td>
   </tr>
   <tr>
      <td>fee_type</td>
      <td>否</td>
      <td>String(3)</td>
      <td>货币类型（目前只支持人民币，请填CNY）</td>
   </tr>
   <tr>
      <td>cash_fee</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>现金支付金额，单位分</td>
   </tr>
   <tr>
      <td>cash_fee_type</td>
      <td>否</td>
      <td>String(3)</td>
      <td>现金支付货币类型（目前只支持人民币，请填CNY）</td>
   </tr>
   <tr>
      <td>settlement_total_fee</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>应结支付金额，单位分</td>
   </tr>
   <tr>
      <td>body</td>
      <td>否</td>
      <td>String(128)</td>
      <td>商品或订单简要描述</td>
   </tr>
   <tr>
      <td>detail</td>
      <td>否</td>
      <td>String(6000)</td>
      <td>商品详细列表，详见Detail</td>
   </tr>
   <tr>
      <td>wxpay_order_content_ext</td>
      <td>否</td>
      <td>WxpayOrderContentExt</td>
      <td>微信支付扩展信息，详见WxpayOrderContentExt</td>
   </tr>
   <tr>
      <td>alipay_order_content_ext</td>
      <td>否</td>
      <td>AlipayOrderContentExt</td>
      <td>支付宝扩展信息，详见AlipayOrderContentExt</td>
   </tr>
</table>

### WxpayOrderContentExt结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>current_trade_state</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>订单当前状态，详见WxpayOrderState</td>
   </tr>
   <tr>
      <td>attach</td>
      <td>否</td>
      <td>String(127)</td>
      <td>附加数据，记录子商户自定义数据</td>
   </tr>
   <tr>
      <td>bank_type</td>
      <td>否</td>
      <td>String(16)</td>
      <td>刷卡支付时特有，付款银行类型，遵守字符型银行编码规范</td>
   </tr>
   <tr>
      <td>goods_tag</td>
      <td>否</td>
      <td>String(32)</td>
      <td>商品标记，代金券或立减优惠功能的参数</td>
   </tr>
   <tr>
      <td>coupon_fee</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>代金券金额，等于支付总金额减现金支付金额</td>
   </tr>
   <tr>
      <td>coupon_count</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>代金券数量</td>
   </tr>
   <tr>
      <td>coupon_infos</td>
      <td>否</td>
      <td>WxpayCouponInfo</td>
      <td>代金券信息，详见WxpayCouponInfo</td>
   </tr>
   <tr>
      <td>product_id</td>
      <td>否</td>
      <td>String(32)</td>
      <td>商品id，子商户自定义，扫码支付时必传</td>
   </tr>
   <tr>
      <td>prepare_id</td>
      <td>否</td>
      <td>String(64)</td>
      <td>公众号或APP支付时，下单后用于拉起支付的预支付会话标识</td>
   </tr>
   <tr>
      <td>trade_state_desc</td>
      <td>否</td>
      <td>String(255)</td>
      <td>对当前查询订单状态的描述和下一步操作的指引</td>
   </tr>
   <tr>
      <td>limit_pay</td>
      <td>否</td>
      <td>String(32)</td>
      <td>非刷卡支付时，指定支付方式，目前只能是：no_credit，指定不能使用信用卡支付</td>
   </tr>
</table>

### WxpayCouponInfo结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>coupon_batch_id</td>
      <td>否</td>
      <td>String(20)</td>
      <td>代金券或立减优惠批次id</td>
   </tr>
   <tr>
      <td>coupon_id</td>
      <td>否</td>
      <td>String(20)</td>
      <td>代金券或立减优惠id</td>
   </tr>
   <tr>
      <td>coupon_fee</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>单个代金券或立减优惠支付金额</td>
   </tr>
   <tr>
      <td>coupon_type</td>
      <td>否</td>
      <td>String(8)</td>
      <td>代金券类型，CASH--充值代金券<br>NO_CASH---非充值代金券<br>订单使用代金券时有返回</td>
   </tr>
</table>

### AlipayOrderContentExt结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>current_trade_state</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>订单当前状态，详见AlipayOrderState</td>
   </tr>
   <tr>
      <td>voucher_detail_list</td>
      <td>否</td>
      <td>AlipayVoucherDetail</td>
      <td>代金券列表，支付宝回包的内容，详见AlipayVoucherDetail，示例：<br>"voucher_detail_list": [<br>{
		    <br>&nbsp;&nbsp;"id": "20151026000",
		    <br>&nbsp;&nbsp;"name": "XX超市5折优惠",
		    <br>&nbsp;&nbsp;"type": "ALIPAY_FIX_VOUCHER",
		    <br>&nbsp;&nbsp;"amount": 10,
		    <br>&nbsp;&nbsp;"merchant_contribute": 9,
		    <br>&nbsp;&nbsp;"other_contribute": 1,
		    <br>&nbsp;&nbsp;"memo":"学生专用优惠", 
		    <br>&nbsp;&nbsp;"purchase_buyer_contribute": 2.01,
		    <br>&nbsp;&nbsp;"purchase_merchant_contribute": 1.03,
		    <br>&nbsp;&nbsp;"purchase_ant_contribute": 0.82
		 <br>}]<br></td>
   </tr>
   <tr>
      <td>fund_bill_list</td>
      <td>是</td>
      <td>AlipayFundBill</td>
      <td>支付渠道，支付宝回包的内容，详见AlipayFundBill，示例："fund_bill_list": [
			<br>{
			    <br>&nbsp;&nbsp;"fund_channel":"ALIPAYACCOUNT",
			    <br>&nbsp;&nbsp;"amount": 10,
			    <br>&nbsp;&nbsp;"real_amount": 11.21
			<br>}]<br>
</td>
   </tr>
   <tr>
      <td>discountable_amount</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>参与优惠的金额</td>
   </tr>
   <tr>
      <td>undiscountable_amount</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>不参与优惠的金额</td>
   </tr>
   <tr>
      <td>point_amount</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>积分金额</td>
   </tr>
   <tr>
      <td>invoice_amount</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>可以开具发票的金额</td>
   </tr>
   <tr>
      <td>product_code</td>
      <td>否</td>
      <td>String(32)</td>
      <td>产品码</td>
   </tr>
   <tr>
      <td>royalty_info</td>
      <td>否</td>
      <td>String(64)</td>
      <td>json的分账信息</td>
   </tr>
   <tr>
      <td>send_pay_date</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>该订单打款给卖家的时间</td>
   </tr>
   <tr>
      <td>extend_params</td>
      <td>否</td>
      <td>String(1024)</td>
      <td>扩展信息，花呗相关的逻辑</td>
   </tr>
   <tr>
      <td>enable_pay_channels</td>
      <td>否</td>
      <td>String(1024)</td>
      <td>可用渠道,多个渠道用','分割，如：<br>pay_channels="credit_group,point"</td>
   </tr>
   <tr>
      <td>disable_pay_channels</td>
      <td>否</td>
      <td>String(1024)</td>
      <td>不可用渠道，格式同enable_pay_channels</td>
   </tr>
   <tr>
      <td>discount_goods_detail</td>
      <td>是</td>
      <td>String(1024)</td>
      <td>打折相关信息，示例：[<br>{
		    <br>&nbsp;&nbsp;"goods_id":"STANDARD1026181538",
		    <br>&nbsp;&nbsp;"goods_name":"雪碧",
		    <br>&nbsp;&nbsp;"discount_amount":"100.00",
		    <br>&nbsp;&nbsp;"voucher_id":"2015102600073002039000002D5O"
		}]<br>
</td>
   </tr>
   <tr>
      <td>buyer_logon_id</td>
      <td>是</td>
      <td>String(100)</td>
      <td>买家支付宝账号，回包的内容</td>
   </tr>
   <tr>
      <td>seller_id</td>
      <td>否</td>
      <td>String(100)</td>
      <td>卖家支付宝用户号，回包的内容</td>
   </tr>
   <tr>
      <td>seller_email</td>
      <td>否</td>
      <td>String(64)</td>
      <td>卖家支付宝账号，回包的内容</td>
   </tr>
   <tr>
      <td>gmt_refund</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>交易退款时间</td>
   </tr>
   <tr>
      <td>gmt_close</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>交易结束时间</td>
   </tr>
   <tr>
      <td>refund_fee</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>退款金额</td>
   </tr>
   <tr>
      <td>out_biz_no</td>
      <td>否</td>
      <td>String(64)</td>
      <td>商户业务号，回包的内容</td>
   </tr>
</table>

### AlipayVoucherDetail结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>券id</td>
   </tr>
   <tr>
      <td>name</td>
      <td>是</td>
      <td>String(64)</td>
      <td>券名称</td>
   </tr>
   <tr>
      <td>type</td>
      <td>是</td>
      <td>String(32)</td>
      <td>代金券类型</td>
   </tr>
   <tr>
      <td>amount</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>代金券金额</td>
   </tr>
   <tr>
      <td>merchant_amount</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>商户出资</td>
   </tr>
   <tr>
      <td>other_amount</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>其它出资</td>
   </tr>
   <tr>
      <td>memo</td>
      <td>否</td>
      <td>String(256)</td>
      <td>备注</td>
   </tr>
</table>

### AlipayFundBill结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>fund_channel</td>
      <td>是</td>
      <td>String(32)</td>
      <td>是否发生了资金变化，示例:Y</td>
   </tr>
   <tr>
      <td>amount</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>支付金额</td>
   </tr>
   <tr>
      <td>real_amount</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>实际支付金额</td>
   </tr>
</table>
## 退款单信息
### RefundOrderContent结构（仅作为返回参数）
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>out_refund_no</td>
      <td>是</td>
      <td>String (32)</td>
      <td>子商户退款单号，云支付系统内全局唯一</td>
   </tr>
   <tr>
      <td>refund_id</td>
      <td>否</td>
      <td>String (32)</td>
      <td>第三方支付平台的退款单号</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String (32)</td>
      <td>退款单对应的订单号</td>
   </tr>
   <tr>
      <td>trade_type</td>
      <td>否</td>
      <td>TradeType</td>
      <td>交易类型，详见TradeType</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
   <tr>
      <td>create_time</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>退款单创建时间，时间戳（秒）</td>
   </tr>
   <tr>
      <td>last_update_time</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>退款单最近更新时间，时间戳（秒）</td>
   </tr>
   <tr>
      <td>is_transforming</td>
      <td>是</td>
      <td>Bool</td>
      <td>系统是否正在处理中</td>
   </tr>
   <tr>
      <td>total_fee</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>订单总金额，单位：分</td>
   </tr>
   <tr>
      <td>refund_fee</td>
      <td>是</td>
      <td>Number(64)</td>
      <td>本次退款总金额，单位：分</td>
   </tr>
   <tr>
      <td>refund_fee_type</td>
      <td>是</td>
      <td>String(3)</td>
      <td>本次退款总金额货币类型（目前只支持人民币，请填CNY）</td>
   </tr>
   <tr>
      <td>refund_reason</td>
      <td>否</td>
      <td>String(255)</td>
      <td>退款原因</td>
   </tr>
   <tr>
      <td>wxpay_refund_order_content_ext</td>
      <td>是</td>
      <td>WxpayRefundOrderContentExt</td>
      <td>微信支付扩展信息，详见WxpayRefundOrderContentExt</td>
   </tr>
</table>

### WxpayRefundOrderContentExt结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>state</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>退款状态，详见WxpayRefundOrderState</td>
   </tr>
   <tr>
      <td>cash_refund_fee</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>现金退款金额，单位：分</td>
   </tr>
   <tr>
      <td>settlement_refund_fee</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>去掉非充值代金券退款金额后的退款金额，单位：分。<br>退款金额=申请退款金额-非充值代金券退款金额，退款金额<=申请退款金额<br>退款金额=申请退款金额-非充值代金券退款金额                                                                       退款金额<=申请退款金额</td>
   </tr>
   <tr>
      <td>coupon_refund_fee</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>退款代金券金额，支持多张代金券，单位：分</td>
   </tr>
   <tr>
      <td>coupon_refund_count</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>退款代金券数量</td>
   </tr>
   <tr>
      <td>coupon_refund_infos</td>
      <td>否</td>
      <td>WxpayCouponInfo</td>
      <td>退款代金券信息，详见WxpayCouponInfo</td>
   </tr>
   <tr>
      <td>refund_account</td>
      <td>否</td>
      <td>String(30)</td>
      <td>退款资金来源，仅针对老资金流子商户使用<br>默认使用未结算资金退款<br>REFUND_SOURCE_UNSETTLED_FUNDS：未结算资金退款<br>REFUND_SOURCE_RECHARGE_FUNDS：可用余额退款</td>
   </tr>
   <tr>
      <td>refund_channel</td>
      <td>否</td>
      <td>String(16)</td>
      <td>退款渠道<br>ORIGINAL：原路退款 <br>BALANCE：退回到余额</td>
   </tr>
   <tr>
      <td>refund_recv_account</td>
      <td>否</td>
      <td>String(64)</td>
      <td>取当前退款单的退款入账方<br>1、退回银行卡：{银行名称}{卡类型}{卡尾号}<br>2、退回支付用户零钱:支付用户零钱</td>
   </tr>
</table>

## 交易请求时的商户信息
### PayMchKey结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>pay_platform</td>
      <td>是</td>
      <td>PayPlatform</td>
      <td>第三方支付类型，详见PayPlatform</td>
   </tr>
   <tr>
      <td>out_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给服务商的帐号，固定20个数字或者字母</td>
   </tr>
   <tr>
      <td>out_sub_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给子商户的帐号，固定20个数字或者字母</td>
   </tr>
   <tr>
      <td>out_shop_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付唯一标识门店的账号</td>
   </tr>
   <tr>
      <td>notify_open_ids</td>
      <td>否</td>
      <td>String(255)[]</td>
      <td>关注本次操作的店员/店长在服务商微信公众号下的open_id。可选。数组</td>
   </tr>
   <tr>
      <td>wxpay_pay_mch_key_ext</td>
      <td>否</td>
      <td>WxpayPayMchKeyExt</td>
      <td>微信支付扩展信息</td>
   </tr>
   <tr>
      <td>alipay_pay_mch_key_ext</td>
      <td>否</td>
      <td>AlipayPayMchKeyExt</td>
      <td>支付宝扩展信息</td>
   </tr>
</table>

### WxpayPayMchKeyExt结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>open_id</td>
      <td>否</td>
      <td>String(255)</td>
      <td>用户在服务商微信公众号下的唯一标识</td>
   </tr>
</table>

### AlipayPayMchKeyExt结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>user_id</td>
      <td>否</td>
      <td>String(255)</td>
      <td>用户在支付宝下的唯一标识</td>
   </tr>
</table>

## 交易请求时的支付订单信息
### PayContent结构（仅交易请求使用）
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的订单号，前缀必须是云支付子商户号</td>
   </tr>
   <tr>
      <td>author_code</td>
      <td>否</td>
      <td>String(128)</td>
      <td>刷卡支付时的授权码（刷卡支付必填，其他不填）</td>
   </tr>
   <tr>
      <td>time_expire</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>订单失效时间（刷卡支付不需要该字段），时间戳（秒）</td>
   </tr>
   <tr>
      <td>total_fee</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>订单总金额，单位：分</td>
   </tr>
   <tr>
      <td>fee_type</td>
      <td>是</td>
      <td>String(3)</td>
      <td>货币类型（目前只支持人民币，请填CNY）</td>
   </tr>
   <tr>
      <td>body</td>
      <td>是</td>
      <td>String(128)</td>
      <td>商品或订单简要描述<br>商品描述交易字段格式根据不同的应用场景按照以下格式：<br>（1）PC网站——传入浏览器打开的网站主页title名-实际商品名称，例如：腾讯充值中心-QQ会员充值；<br>（2） 公众号——传入公众号名称-实际商品名称，例如：腾讯形象店- image-QQ公仔；<br>（3） H5——应用在浏览器网页上的场景，传入浏览器打开的移动网页的主页title名-实际商品名称，例如：腾讯充值中心-QQ会员充值；<br>（4） 线下门店——门店品牌名-城市分店名-实际商品名称，例如： image形象店-深圳腾大- QQ公仔）<br>（5） APP——需传入应用市场上的APP名字-实际商品名称，天天爱消除-游戏充值。</td>
   </tr>
   <tr>
      <td>detail</td>
      <td>否</td>
      <td>String(6000)</td>
      <td>商品详细列表，由json转化而来，详见Detail。</td>
   </tr>
   <tr>
      <td>wxpay_pay_content_ext</td>
      <td>否</td>
      <td>WxpayPayContentExt</td>
      <td>微信支付扩展信息，详见WxpayPayContentExt</td>
   </tr>
   <tr>
      <td>alipay_pay_content_ext</td>
      <td>否</td>
      <td>AlipayPayContentExt</td>
      <td>支付宝扩展信息，详见AlipayPayContentExt</td>
   </tr>
</table>

### Detail结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>cost_price</td>
      <td>可选</td>
      <td>Number(32)</td>
      <td>订单原价，商户侧一张小票订单可能被分多次支付，订单原价用于记录整张小票的支付金额。当订单原价与支付金额不相等则被判定为拆单，无法享受优惠。</td>
   </tr>
   <tr>
      <td>receipt_id</td>
      <td>可选</td>
      <td>String(32)</td>
      <td>商家小票ID</td>
   </tr>
   <tr>
      <td>goods_details</td>
      <td>必填</td>
      <td>GoodsDetail[]</td>
      <td>商品详情，详见GoodsDetail</td>
   </tr>
</table>

### GoodsDetail结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>goods_id</td>
      <td>否</td>
      <td>String(32)</td>
      <td>商品的编号</td>
   </tr>
   <tr>
      <td>goods_name</td>
      <td>否</td>
      <td>String(256)</td>
      <td>商品名称</td>
   </tr>
   <tr>
      <td>quantity</td>
      <td>是 </td>
      <td>Number(32)</td>
      <td>商品数量</td>
   </tr>
   <tr>
      <td>price</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>商品单价，如果商户有优惠，需传输商户优惠后的单价<br>单品总金额应<=订单总金额total_fee，否则会无法享受优惠</td>
   </tr>
</table>

### WxpayPayContentExt结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>attach</td>
      <td>否</td>
      <td>String(127)</td>
      <td>附加数据，记录子商户自定义数据</td>
   </tr>
   <tr>
      <td>goods_tag</td>
      <td>否</td>
      <td>String(32)</td>
      <td>商品标记，代金券或立减优惠功能的参数</td>
   </tr>
   <tr>
      <td>product_id</td>
      <td>否</td>
      <td>String(32)</td>
      <td>商品id，子商户自定义（扫码支付必填，刷卡支付不填，其他可选）</td>
   </tr>
   <tr>
      <td>limit_pay</td>
      <td>否</td>
      <td>String(32)</td>
      <td>定支付方式，目前只能是：no_credit，指定不能使用信用卡支付</td>
   </tr>
</table>

### AlipayPayContentExt结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>discountable_amount</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>参与优惠的金额</td>
   </tr>
   <tr>
      <td>undiscountable_amount</td>
      <td>否</td>
      <td>Number(64)</td>
      <td>不参与优惠的金额</td>
   </tr>
   <tr>
      <td>product_code</td>
      <td>否</td>
      <td>String(128)</td>
      <td>产品码</td>
   </tr>
   <tr>
      <td>royalty_info</td>
      <td>否</td>
      <td>String(256)</td>
      <td>分账信息，json结构</td>
   </tr>
   <tr>
      <td>extend_params</td>
      <td>否</td>
      <td>String(256)</td>
      <td>扩展信息，花呗相关的逻辑</td>
   </tr>
   <tr>
      <td>disable_pay_channels</td>
      <td>否</td>
      <td>String(128)</td>
      <td>不可用渠道</td>
   </tr>
</table>

## 退款请求时的退款单信息
### RefundContent结构（仅退款请求使用）
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的订单号，前缀必须是云支付子商户号</td>
   </tr>
   <tr>
      <td>out_refund_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的退款单号，前缀必须是云支付子商户号</td>
   </tr>
   <tr>
      <td>total_fee</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>订单总金额，单位分</td>
   </tr>
   <tr>
      <td>refund_fee</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>本次退款总金额，单位分</td>
   </tr>
   <tr>
      <td>refund_fee_type</td>
      <td>是</td>
      <td>String(3)</td>
      <td>本次退款总金额货币类型（目前只支持人民币，请填CNY）</td>
   </tr>
   <tr>
      <td>wxpay_refund_content_ext</td>
      <td>否</td>
      <td>WxpayRefundOrderContentExt</td>
      <td>微信支付扩展信息，详见WxpayRefundOrderContentExt</td>
   </tr>
   <tr>
      <td>alipay_refund_order_content_ext</td>
      <td>否</td>
      <td>AlipayRefundOrderContentExt</td>
      <td>支付宝扩展信息，详见AlipayRefundOrderContentExt</td>
   </tr>
</table>

### WxpayRefundOrderContentExt结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>refund_account</td>
      <td>否</td>
      <td>String(30)</td>
      <td>退款资金来源，仅针对老资金流子商户使用。默认使用未结算资金退款<br>REFUND_SOURCE_UNSETTLED_FUNDS：未结算资金退款<br>REFUND_SOURCE_RECHARGE_FUNDS：可用余额退款</td>
   </tr>
</table>

### AlipayRefundOrderContentExt结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>fund_change</td>
      <td>是</td>
      <td>String(1)</td>
      <td>是否发生了资金变化，示例:Y</td>
   </tr>
   <tr>
      <td>gmt_refund_pay</td>
      <td>是</td>
      <td>String(32)</td>
      <td>退款时间</td>
   </tr>
   <tr>
      <td>refund_detail_item_list</td>
      <td>否</td>
      <td>AlipayFundBill</td>
      <td>退款渠道，详见 AlipayFundBill</td>
   </tr>
   <tr>
      <td>refund_status</td>
      <td>是</td>
      <td>AlipayRefundOrderState(枚举类型)</td>
      <td>退款状态，详见 AlipayRefundOrderState</td>
   </tr>
</table>

## 客户端信息
### OrderClient结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>device_id</td>
      <td>是</td>
      <td>String(64)</td>
      <td>子商户自定义，终端设备号</td>
   </tr>
   <tr>
      <td>staff_id</td>
      <td>是</td>
      <td>String(64)</td>
      <td>子商户自定义，店员ID</td>
   </tr>
   <tr>
      <td>terminal_type</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>终端类型，1：windows，2：andriod，3：iso，4：linux，100：其他</td>
   </tr>
   <tr>
      <td>machine_no</td>
      <td>否</td>
      <td>String(32)</td>
      <td>刷卡支付特有，每个收银终端的唯一码（刷卡支付必填）</td>
   </tr>
   <tr>
      <td>sdk_version</td>
      <td>是</td>
      <td>String(10)</td>
      <td>云支付SDK版本号</td>
   </tr>
   <tr>
      <td>spbill_create_ip</td>
      <td>是</td>
      <td>String(16)</td>
      <td>调用云支付API的机器IP</td>
   </tr>
</table>

## 门店信息
### ShopInfo结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>shop_id</td>
      <td>是</td>
      <td>Sting(64)</td>
      <td>门店编号</td>
   </tr>
   <tr>
      <td>shop_name</td>
      <td>是</td>
      <td>String(32)</td>
      <td>门店名称</td>
   </tr>
   <tr>
      <td>province</td>
      <td>否</td>
      <td>String(32)</td>
      <td>门店所在省</td>
   </tr>
   <tr>
      <td>city</td>
      <td>否</td>
      <td>String(32)</td>
      <td>门店所在市</td>
   </tr>
   <tr>
      <td>district</td>
      <td>否</td>
      <td>String(32)</td>
      <td>门店所在区</td>
   </tr>
   <tr>
      <td>address</td>
      <td>否</td>
      <td>String(128)</td>
      <td>门店详细地址</td>
   </tr>
   <tr>
      <td>coordinate_type</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>门店坐标类型</td>
   </tr>
   <tr>
      <td>longitude</td>
      <td>否</td>
      <td>String(16)</td>
      <td>门店经度</td>
   </tr>
   <tr>
      <td>latitude</td>
      <td>否</td>
      <td>String(16)</td>
      <td>门店维度</td>
   </tr>
   <tr>
      <td>height</td>
      <td>否</td>
      <td>String(16)</td>
      <td>门店海拔</td>
   </tr>
   <tr>
      <td>phone</td>
      <td>否</td>
      <td>String(64)</td>
      <td>门店联系电话</td>
   </tr>
   <tr>
      <td>out_shop_id</td>
      <td>否</td>
      <td>String(20)</td>
      <td>外部可见的商户门店号，云支付内全局唯一，固定20个字符长，可用于生成门店固定二维码，仅返回时有该字段</td>
   </tr>
   <tr>
      <td>out_shop_id_url</td>
      <td>否·</td>
      <td>String(128)</td>
      <td>门店二维码，仅返回时有该字段</td>
   </tr>
   <tr>
      <td>device_infos</td>
      <td>是</td>
      <td>DeviceInfo[]</td>
      <td>门店设备信息列表，详见DeviceInfo</td>
   </tr>
   <tr>
      <td>staff_infos</td>
      <td>是</td>
      <td>StaffInfo[]</td>
      <td>门店店员信息列表，详见StaffInfo</td>
   </tr>
</table>

### DeviceInfo结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>device_id</td>
      <td>是</td>
      <td>String(64)</td>
      <td>门店内终端编号</td>
   </tr>
   <tr>
      <td>device_type</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>设备类型<br>1: 刷卡支付；2: 扫码支付；3: 混合支付，支持刷卡支付+扫码支付；4: 固定二维码支付</td>
   </tr>
   <tr>
      <td>remark</td>
      <td>否</td>
      <td>String(64)</td>
      <td>子商户自定义备注信息</td>
   </tr>
</table>

### StaffInfo结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>staff_id</td>
      <td>是</td>
      <td>String(64)</td>
      <td>门店内店员编号</td>
   </tr>
   <tr>
      <td>staff_name</td>
      <td>是</td>
      <td>String(64)</td>
      <td>店员名称</td>
   </tr>
   <tr>
      <td>remark</td>
      <td>否</td>
      <td>String(64)</td>
      <td>子商户自定义备注信息</td>
   </tr>
   <tr>
      <td>shop_manager</td>
      <td>是</td>
      <td>Bool</td>
      <td>是否是店长</td>
   </tr>
   <tr>
      <td>receive_one_code_pay_notify</td>
      <td>否</td>
      <td>Bool</td>
      <td>是否接收一码支付的成功消息通知</td>
   </tr>
</table>

# 枚举值定义
## 交易相关信息
### PayPlatform枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>1</td>
      <td>微信支付</td>
   </tr>
   <tr>
      <td>2</td>
      <td>支付宝</td>
   </tr>
</table>

### TradeType枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>1</td>
      <td>刷卡支付</td>
   </tr>
   <tr>
      <td>2</td>
      <td>扫码支付</td>
   </tr>
   <tr>
      <td>3</td>
      <td>公众号支付</td>
   </tr>
   <tr>
      <td>4</td>
      <td>APP支付</td>
   </tr>
   <tr>
      <td>5</td>
      <td>声波支付</td>
   </tr>
   <tr>
      <td>6</td>
      <td>手机网站支付</td>
   </tr>
   <tr>
      <td>8</td>
      <td>一码支付</td>
   </tr>
</table>

### WxpayOrderState枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>1</td>
      <td>订单初始态</td>
   </tr>
   <tr>
      <td>2</td>
      <td>刷卡支付，成功</td>
   </tr>
   <tr>
      <td>3</td>
      <td>统一下单，支付成功</td>
   </tr>
   <tr>
      <td>4</td>
      <td>已转入退款</td>
   </tr>
   <tr>
      <td>5</td>
      <td>刷卡支付，顾客停止支付</td>
   </tr>
   <tr>
      <td>6</td>
      <td>统一下单，待顾客支付</td>
   </tr>
   <tr>
      <td>7</td>
      <td>统一下单，订单已关闭</td>
   </tr>
   <tr>
      <td>8</td>
      <td>刷卡支付，已撤单</td>
   </tr>
   <tr>
      <td>9</td>
      <td>刷卡支付，用户支付中</td>
   </tr>
   <tr>
      <td>10</td>
      <td>刷卡支付，支付错误</td>
   </tr>
   <tr>
      <td>11</td>
      <td>作废状态，表示本地有，第三方支付平台没有的订单</td>
   </tr>
</table>

### AlipayOrderState枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>1</td>
      <td>订单初始态</td>
   </tr>
   <tr>
      <td>2</td>
      <td>成功</td>
   </tr>
   <tr>
      <td>3</td>
      <td>等待用户支付</td>
   </tr>
   <tr>
      <td>4</td>
      <td>已关闭,或者已退款</td>
   </tr>
   <tr>
      <td>5</td>
      <td>交易结束，不可退款</td>
   </tr>
   <tr>
      <td>6</td>
      <td>订单不存在</td>
   </tr>
</table>

### WxpayRefundOrderState枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>1</td>
      <td>退款单初始态</td>
   </tr>
   <tr>
      <td>2</td>
      <td>退款成功</td>
   </tr>
   <tr>
      <td>3</td>
      <td>退款失败</td>
   </tr>
   <tr>
      <td>4</td>
      <td>退款处理中</td>
   </tr>
   <tr>
      <td>5</td>
      <td>转入代发，退款到银行发现用户的卡作废或者冻结了，导致原路退款银行卡失败，资金回流到子商户的现金帐号，需要子商户人工干预，通过线下或者财付通转账的方式进行退款</td>
   </tr>
   <tr>
      <td>6</td>
      <td>作废状态，表示本地有，第三方支付平台没有的订单</td>
   </tr>
</table>

### AlipayRefundOrderState枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>1</td>
      <td>退款单初始态</td>
   </tr>
   <tr>
      <td>2</td>
      <td>退款单成功态</td>
   </tr>
   <tr>
      <td>3</td>
      <td>申请退款失败</td>
   </tr>
</table>

## 认证加密信息
### AuthenType枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>1</td>
      <td>HMAC-SHA256</td>
   </tr>
   <tr>
      <td>2</td>
      <td>MD5</td>
   </tr>
</table>

### SignType枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>1</td>
      <td>RSASSA-PSS-2048-SHA256</td>
   </tr>
</table>

### EncrytType枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>1</td>
      <td>AES-128-GCM</td>
   </tr>
</table>

## 接口相关信息
### Status枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>0</td>
      <td>成功。带认证码，调用者需要验证认证码是否正确</td>
   </tr>
   <tr>
      <td>3</td>
      <td>系统内部错误，操作结果未知，可重试，不带认证码</td>
   </tr>
   <tr>
      <td>101</td>
      <td>操作失败，且不建议重试，不带认证码</td>
   </tr>
   <tr>
      <td>102</td>
      <td>操作失败，且建议换新单号重试，带认证码，调用者需要验证认证码是否正确</td>
   </tr>
   <tr>
      <td>103</td>
      <td>系统内部错误，可重试，带认证码，调用者需要验证认证码是否正确</td>
   </tr>
   <tr>
      <td>104</td>
      <td>操作失败，且不建议重试. 带认证码，调用者需要验证认证码是否正确<br><b>特别提示：在刷卡支付响应包里出现该错误码时，需要判断internal_status字段的值是否是407，如是，则说明说明客户端发生异常，支付时单号重复，但金额等其他信息不重复，被云支付的防重入挡住，此时，请一定不要撤单，否则会造成已支付的订单退款，给商户造成损失。</b></td>
   </tr>
</table>

### Interface枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>13</td>
      <td>设置门店信息</td>
   </tr>
   <tr>
      <td>14</td>
      <td>查询门店信息</td>
   </tr>
   <tr>
      <td>100</td>
      <td>刷卡支付</td>
   </tr>
   <tr>
      <td>101</td>
      <td>扫描支付</td>
   </tr>
   <tr>
      <td>103</td>
      <td>关单</td>
   </tr>
   <tr>
      <td>104</td>
      <td>退款</td>
   </tr>
   <tr>
      <td>106</td>
      <td>查询订单</td>
   </tr>
   <tr>
      <td>107</td>
      <td>查询退款单</td>
   </tr>
   <tr>
      <td>108</td>
      <td>撤单</td>
   </tr>
   <tr>
      <td>202</td>
      <td>接口监控上报</td>
   </tr>
   <tr>
      <td>203</td>
      <td>客户端机器配置上报</td>
   </tr>
</table>

## 其他信息
### CompressType
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>1</td>
      <td>kZip</td>
   </tr>
   <tr>
      <td>2</td>
      <td>kRAR</td>
   </tr>
   <tr>
      <td>3</td>
      <td>kGZip</td>
   </tr>
</table>
