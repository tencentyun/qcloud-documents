## 说明
### 通讯说明
- 所有接口均使用 HTTPS 通信，数据包格式为 json（HTTP 请求的 content-type 字段必须使用 application/json）。
- 请求必须传认证或签名信息。其中退款请求，可以传签名和签名算法，也可以传认证码和认证算法，二选一，其他请求传认证码和认证算法。
- 对响应要验证认证码。
- 所有接口参数名使用的字母均为小写。

### 发送请求举例（使用 libcurl 实现）
```
/*
用于接受响应数据的回调函数
*/
size_t recv_data(char *ptr, size_t size, size_t nmemb, void *parm)
{
    size_t length = size * nmemb;
    std::string *data = (std::string*)parm;
    data->append(ptr, length);
    return length;
}
/*
将 request 用 POST 方式发送到 url，响应包填充到 response 指向的 string 中
返回是否 POST 请求是否成功
*/
bool post(const std::string &request, const std::string &url, std::string *response)
{
    CURL *hnd = curl_easy_init();

    curl_easy_setopt(hnd, CURLOPT_CUSTOMREQUEST, "POST");
    curl_easy_setopt(hnd, CURLOPT_URL, url);

    struct curl_slist *headers = curl_slist_append(NULL, "content-type: application/json");
    curl_easy_setopt(hnd, CURLOPT_HTTPHEADER, headers);

    curl_easy_setopt(hnd, CURLOPT_POSTFIELDS, request);

    // 设置云支付根证书
    curl_easy_setopt(hnd, CURLOPT_SSL_VERIFYPEER, 1);
    curl_easy_setopt(hnd, CURLOPT_SSL_VERIFYHOST, 2);
    curl_easy_setopt(hnd, CURLOPT_CAINFO, "./cloudpayrootca.pem");

    curl_easy_setopt(hnd, CURLOPT_WRITEFUNCTION, recv_data);
    std::string rc;
    curl_easy_setopt(hnd, CURLOPT_WRITEDATA, (void *)&rc);

    CURLcode ret = curl_easy_perform(hnd);
    if (CURLE_OK != ret) {
		curl_slist_free_all(headers);
		curl_easy_cleanup(hnd);
        return false;
    }
    *response = rc;

    curl_slist_free_all(headers);
    curl_easy_cleanup(hnd);
    return true;
}
```
### 数据包格式说明
- 请求包含两个字段：authen\_info 和 request\_content，前者表示签名或认证信息，后者表示请求具体内容，均为 json 结构。
- 响应包含两个字段：authen\_info 和 response\_content，前者表示认证信息，后者表示响应具体内容，均为 json 结构。
- 签名生成算法：RSASSA-PSS-2048-SHA256，私钥为服务商在云支付录入商户时，在网页上生成的签名私钥（该私钥只有服务商知道，云支付不知道，请妥善保存）。
- 认证码生成算法：HMAC-SHA256，认证密钥为服务商在云支付录入商户时，在网页上生成的认证密钥。
- 如果不填非必填字段，则不要设置该字段，如需清空该字段，需上传内容为空的该字段。

### 计算认证码举例（使用 OpenSSL 实现）
```
/*
返回是否成功，成功时认证码存放于 hmac 指向的 string
*/
bool calc_HMAC_SHA256(const std::string &key, const std::string &input, std::string *hmac)
{
    unsigned char md[SHA256_DIGEST_LENGTH] = {0};//32 bytes
    char format_md[65] = {0};

    unsigned int md_len = sizeof(md);

    HMAC_CTX ctx;
    HMAC_CTX_init(&ctx);
    if (!HMAC_Init_ex(&ctx, key.data(), (int)key.length(), EVP_sha256(), NULL)  ||
        !HMAC_Update(&ctx, (const unsigned char *)input.data(), input.length()) ||
        !HMAC_Final(&ctx, md, &md_len)) {

        HMAC_CTX_cleanup(&ctx);
        return false;
    }
    HMAC_CTX_cleanup(&ctx);

    for (int i = 0; i < 32; i++) {
        snprintf(&format_md[i * 2], 3, "%02x", md[i]); //二进制转为十六进制大写
    }
    hmac->assign(format_md);

    // 转大写
    transform(hmac->begin(), hmac->end(), hmac->begin(), ::toupper);
    return true;
}
```
### 计算签名举例（使用 OpenSSL 实现）
```
/*
对计算得到的签名进行 base64 编码之后输出
返回是否成功，成功时签名存放于 sign_base64encode 指向的 string
*/
bool calc_RSASSA_PSS_2048_SHA256(const std::string &key,
                                 const std::string &content,
                                 std::string *sign_base64encode)
{
    unsigned char digest[SHA256_DIGEST_LENGTH] = {0}; //32 bytes
    int digest_len = sizeof(digest);

    std::shared_ptr<BIO> bio(BIO_new_mem_buf((void *)key.c_str(), (int)key.length()), BIO_free);
    if (!bio) {
        return false;
    }

    std::shared_ptr<RSA> rsa(PEM_read_bio_RSAPrivateKey(bio.get(), NULL, NULL, NULL);, RSA_free);
    if (!rsa) {
        return false;
    }

    EVP_MD_CTX md_ctx; //当前使用 1.0.2e 版本
    EVP_MD_CTX_init   (&md_ctx);

    if (!EVP_DigestInit(&md_ctx, EVP_sha256())                                     ||
        !EVP_DigestUpdate(&md_ctx, (const void*)content.c_str(), content.length()) ||
        !EVP_DigestFinal(&md_ctx, digest, (unsigned int *)&digest_len)) {

        EVP_MD_CTX_cleanup(&md_ctx);
        return false;
    }

    EVP_MD_CTX_cleanup(&md_ctx);

    unsigned char em[256] = {0};
    unsigned char sign[256] = {0};
    int status = RSA_padding_add_PKCS1_PSS(rsa.get(), em, digest, EVP_sha256(), -2 /* maximum salt length*/);
    if (!status) {
        return false;
    }

    status = RSA_private_encrypt(sizeof(em), em, sign, rsa.get(), RSA_NO_PADDING);
    if (-1 == status) {
        return false;
    }

    *sign_base64encode = base64_encode(sign, sizeof(sign));
    return true;
}
```
### 构造请求举例（以刷卡支付为例）

```
{
		Json::Value pay_mch_key;      // 构造 pay_mch_key
		pay_mch_key["pay_platform"]   = 1;
		pay_mch_key["out_mch_id"]     = "sz013NzuonO6CMJd0rCB";
		pay_mch_key["out_sub_mch_id"] = "sz01ELTR281OFpmdAp6J";
		pay_mch_key["out_shop_id"]    = "sz01qyoPJmd3j1hWmul4";

		Json::Value pay_content;      // 构造 pay_content
		pay_content["out_trade_no"]   = "sz0100lmnx20171228151031";
		pay_content["author_code"]    = "134680423163089456";
		pay_content["total_fee"]      = 1;
		pay_content["fee_type"]       = "CNY";
		pay_content["attach"]         = "attach";

		Json::Value order_client;        // 构造 order_client
		order_client["machine_no"]       = "32-62-A8-14-B3-C0";
		order_client["sdk_version"]      = "1.0";
		order_client["device_id"]        = 1;
		order_client["spbill_create_ip"] = "192.168.100.75";
		order_client["staff_id"]         = "1003";
		order_client["terminal_type"]    = 2;

		Json::Value request_content;     // 构造 request_content
		request_content["pay_mch_key"]   = pay_mch_key;
		request_content["pay_content"]   = pay_content;
		request_content["order_client"]  = order_client;
		request_content["nonce_str"]     = "416492026bc84091bcaf7e74ea90ceba";

		Json::FastWriter w;
		std::string request_content_str = w.write(request_content);

		Json::Value authen;
		authen["authen_code"] = hmac_sha256(authen_key, request_content_str); //计算认证码
		authen["authen_type"] = 1; //hmac_sha256 为1

		Json::Value authen_info;
		authen_info["a"] = authen;  //认证码，签名是s

		Json::Value request;       //构造最终发给服务器的请求
		request["request_content"] = request_content_str;
		request["authen_info"]     = authen_info;

		std::string request_str = w.write(request);

		return request_str;
	}
```

### 响应举例（以刷卡支付为例）
- 把响应包从 string 转成 json，取出 json 里面的 response\_content 和 authen\_info，具体如下：

```
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
```
- 对 response\_content 计算认证码，并将该认证码与 authen\_info 的 authen\_code 进行比较。

### 接口调用说明
- 交易接口中的门店信息，必须和子商户在云支付手机端商户管理系统设置的一致。

### 订单和退款单号说明
- 为了保护不同商户的订单号不重复，云支付为每个服务商录入的子商户分配了 “云支付订单前缀”，在云支付后台的商户详情中可以看到，该商户的订单和退款单必须以云支付子商户号做前缀。

## 交易接口
### 刷卡支付
#### 接口地址
`https://pay.qcloud.com/cpay/micro_pay`

content\_type：application/json
#### 输入参数
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
      <td>请求内容，详见<b>本节 RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### RequestContent 结构
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
      <td>支付商户信息，详见 PayMchKey</td>
   </tr>
   <tr>
      <td>pay_content</td>
      <td>是</td>
      <td>PayContent</td>
      <td>订单信息，详见 PayContent</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见 OrderClient</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

#### 返回参数
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
      <td>请求内容，详见<b>本节 ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### ResponseContent 结构
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
      <td>错误码，详见 Status。0：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
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
      <td>authen_info 存在时必填。详见 MicroPayResponse</td>
   </tr>
</table>

#### MicroPayResponse 结构
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
      <td>支付商户信息，status 为0时必填。详见 PayMchKey</td>
   </tr>
   <tr>
      <td>order_content</td>
      <td>否</td>
      <td>OrderContent</td>
      <td>订单信息，status 为0时必填。详见 OrderContent</td>
   </tr>
</table>

#### 构造刷卡支付请求例子
```
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
    const int         &terminal_type,
    const std::string &machine_no,
    const std::string &sdk_version,
    const std::string &spbill_create_ip,
    const std::string &authen_key
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
    order_client["staff_id"]         = staff_id;
    order_client["terminal_type"]    = terminal_type;
    order_client["machine_no"]       = machine_no;
    order_client["sdk_version"]      = sdk_version;
    order_client["spbill_create_ip"] = spbill_create_ip;
    request_content["order_client"]  = order_client;

    Json::FastWriter w;
    const std::string &rc = w.write(request_content);

    Json::Value authen_info, a;
    a["authen_type"] = 1;
    // 使用计算认证码举例（使用 OpenSSL 实现）中的函数计算认证码
    std::string authen_code;
    if (!calc_HMAC_SHA256(authen_key, rc, &authen_code)) {
        // 计算失败
        return "";
    }
    a["authen_code"] = authen_code;
    authen_info["a"] = a;

    Json::Value request;
    request["request_content"] = rc;
    request["authen_info"] = authen_info;

    return w.write(request);
}
/*
构造请求完毕之后，将请求通过 POST 方法发送到云支付接口对应的URL
使用了发送请求举例（使用 libcurl 实现）中的 post 函数
*/
std::string response;
post(request, "https://pay.qcloud.com/cpay/micro_pay", &response);
```
### 扫码支付
#### 接口地址
`https://pay.qcloud.com/cpay/scan_code_pay`

content_type：application/json
#### 输入参数
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
      <td>请求内容，详见<b>本节 RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### RequestContent 结构
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
      <td>支付商户信息，详见 PayMchKey</td>
   </tr>
   <tr>
      <td>pay_content</td>
      <td>是</td>
      <td>PayContent</td>
      <td>订单信息，详见 PayContent</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见 OrderClient</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

#### 返回参数
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
      <td>请求内容，详见<b>本节 ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### ResponseContent 结构
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
      <td>错误码，详见 Status。0：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
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
      <td>消息 id</td>
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
      <td>authen_info 存在时必填。详见 ScanCodePayResponse</td>
   </tr>
</table>

#### ScanCodePayResponse 结构
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
      <td>status 为0时必填。用于扫码支付时转换成支付二维码 </td>
   </tr>
</table>

#### 构造扫码支付请求例子
```
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
    const int         &terminal_type,
    const std::string &machine_no,
    const std::string &sdk_version,
    const std::string &spbill_create_ip,
    const std::string &authen_key
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
    order_client["staff_id"]         = staff_id;
    order_client["terminal_type"]    = terminal_type;
    order_client["machine_no"]       = machine_no;
    order_client["sdk_version"]      = sdk_version;
    order_client["spbill_create_ip"] = spbill_create_ip;
    request_content["order_client"]  = order_client;

    Json::FastWriter w;
    const std::string &rc = w.write(request_content);

    Json::Value authen_info, a;
    a["authen_type"] = 1;
    // 使用计算认证码举例（使用 OpenSSL 实现）中的函数计算认证码
    std::string authen_code;
    if (!calc_HMAC_SHA256(authen_key, rc, &authen_code)) {
        // 计算失败
        return "";
    }
    a["authen_code"] = authen_code;
    authen_info["a"] = a;

    Json::Value request;
    request["request_content"] = rc;
    request["authen_info"] = authen_info;

    return w.write(request);
}
/*
构造请求完毕之后，将请求通过 POST 方法发送到云支付接口对应的 URL
使用了发送请求举例（使用libcurl实现）中的 post 函数
*/
std::string response;
post(request, "https://pay.qcloud.com/cpay/scan_code_pay", &response);
```
### 申请退款
#### 接口地址
`https://pay.qcloud.com/cpay/refund`

content_type：application/json
#### 输入参数
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
      <td>请求内容，详见<b>本节 RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### RequestContent 结构
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
      <td>支付商户信息，详见 PayMchKey</td>
   </tr>
   <tr>
      <td>refund_content</td>
      <td>是</td>
      <td>RefundContent</td>
      <td>订单信息，详见 RefundContent</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见 OrderClient</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

#### 返回参数
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
      <td>请求内容，详见<b>本节 ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### ResponseContent结构
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
      <td>错误码，详见 Status。0：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
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
      <td>消息 id</td>
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
      <td>authen_info 存在时必填。详见 RefundResponse</td>
   </tr>
</table>

#### RefundResponse 结构
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
      <td>支付商户信息，status 为0时必填。详见 PayMchKey</td>
   </tr>
   <tr>
      <td>refund_order_content</td>
      <td>否</td>
      <td>RefundOrderContent</td>
      <td>订单信息，status 为0时必填。详见 RefundOrderContent</td>
   </tr>
</table>

#### 构造申请退款请求例子
```
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
    const int64_t     &total_fee,
    const int64_t     &refund_fee,
    const std::string &refund_fee_type,
    const std::string &device_id,
    const std::string &staff_id,
    const int         &terminal_type,
    const std::string &machine_no,
    const std::string &sdk_version,
    const std::string &spbill_create_ip,
    const std::string &signing_key
)
{
    Json::Value request_content;
    request_content["nonce_str"] = generate_random_nonce_str();

    Json::Value pay_mch_key, refund_content, order_client;

    pay_mch_key["pay_platform"]    = pay_platform;
    pay_mch_key["out_mch_id"]      = out_mch_id;
    pay_mch_key["out_sub_mch_id"]  = out_sub_mch_id;
    pay_mch_key["out_shop_id"]     = out_shop_id;
    request_content["pay_mch_key"] = pay_mch_key;

    refund_content["out_trade_no"]    = out_trade_no;
    refund_content["out_refund_no"]   = out_refund_no;
    refund_content["total_fee"]       = total_fee;
    refund_content["refund_fee"]      = refund_fee;
    refund_content["refund_fee_type"] = refund_fee_type;
    request_content["refund_content"] = refund_content;

    order_client["device_id"]        = device_id;
    order_client["staff_id"]         = staff_id;
    order_client["terminal_type"]    = terminal_type;
    order_client["machine_no"]       = machine_no;
    order_client["sdk_version"]      = sdk_version;
    order_client["spbill_create_ip"] = spbill_create_ip;
    request_content["order_client"]  = order_client;

    Json::FastWriter w;
    const std::string &rc = w.write(request_content);

    //方式一：计算签名
    Json::Value authen_info, s;
    s["sign_type"] = 1;
    // 使用计算签名举例（使用 OpenSSL 实现）中的函数计算签名
    std::string sign;
    if (!calc_RSASSA_PSS_2048_SHA256(signing_key, rc, &sign)) {
        // 计算失败
        return "";
    }
    s["sign"] = sign;
    authen_info["s"] = s;

    Json::Value request;
    request["request_content"] = rc;
    request["authen_info"] = authen_info;
    return w.write(request);
    
/** 方式二：计算认证码，退款也可以按如下计算认证码打包，签名和认证码二选一即可。    
    Json::Value authen_info, a;
    a["authen_type"] = 1;

    std::string authen_code;
    if (!calc_HMAC_SHA256(authen_key, rc, &authen_code)) {
        return "";
    }
    a["authen_code"] = authen_code;
    authen_info["a"] = a;

    Json::Value request;
    request["request_content"] = rc;
    request["authen_info"] = authen_info;
    return w.write(request);
*/    
}
/*
构造请求完毕之后，将请求通过 POST 方法发送到云支付接口对应的 URL
使用了发送请求举例（使用 libcurl 实现）中的 post 函数
*/
std::string response;
post(request, "https://pay.qcloud.com/cpay/refund", &response);
```
### 关闭订单
#### 接口地址
`https://pay.qcloud.com/cpay/close_order`

content_type：application/json
#### 输入参数
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
      <td>请求内容，详见<b>本节 RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### RequestContent 结构
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
      <td>支付商户信息，详见 PayMchKey</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见 OrderClient</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的订单号，前缀必须是云支付订单前缀</td>
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
      <td>交易类型，枚举值详见 TradeType</td>
   </tr>
</table>

#### 返回参数
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
      <td>请求内容，详见本节 ResponseContent</td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### ResponseContent 结构
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
      <td>错误码，详见 Status。0：成功；非 0：失败或者需要重试，具体见实际返回的错误码</td>
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
      <td>消息 id</td>
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
      <td>authen_info 存在时必填。详见 CloseOrderResponse</td>
   </tr>
</table>

#### CloseOrderResponse 结构
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

#### 构造关闭订单请求例子
```
/*
构造请求字符串
*/
std::string gen_cloud_pay_close_order(
    const int         &pay_platform,
    const std::string &out_mch_id,
    const std::string &out_sub_mch_id,
    const std::string &out_shop_id,
    const std::string &out_trade_no,
    const int         &trade_type,
    const std::string &device_id,
    const std::string &staff_id,
    const int         &terminal_type,
    const std::string &machine_no,
    const std::string &sdk_version,
    const std::string &spbill_create_ip,
    const std::string &authen_key
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
    order_client["staff_id"]         = staff_id;
    order_client["terminal_type"]    = terminal_type;
    order_client["machine_no"]       = machine_no;
    order_client["sdk_version"]      = sdk_version;
    order_client["spbill_create_ip"] = spbill_create_ip;
    request_content["order_client"]  = order_client;

    Json::FastWriter w;
    const std::string &rc = w.write(request_content);

    Json::Value authen_info, s;
    a["authen_type"] = 1;
    // 使用计算认证码举例（使用 OpenSSL 实现）中的函数计算认证码
    std::string authen_code;
    if (!calc_HMAC_SHA256(authen_key, rc, &authen_code)) {
        // 计算失败
        return "";
    }
    a["authen_code"] = authen_code;
    authen_info["a"] = a;

    Json::Value request;
    request["request_content"] = rc;
    request["authen_info"] = authen_info;

    return w.write(request);
}
/*
构造请求完毕之后，将请求通过 POST 方法发送到云支付接口对应的 URL
使用了发送请求举例（使用 libcurl 实现）中的 post 函数
*/
std::string response;
post(request, "https://pay.qcloud.com/cpay/reverse", &response);
```
### 查询订单
### 接口地址
`https://pay.qcloud.com/cpay/query_order`

content_type：application/json
#### 输入参数
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
      <td>请求内容，详见本节 RequestContent</td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### RequestContent 结构
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
      <td>支付商户信息，详见 PayMchKey</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见 OrderClient</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的订单号，前缀必须是云支付订单前缀</td>
   </tr>
   <tr>
      <td>trade_type</td>
      <td>是</td>
      <td>TradeType</td>
      <td>交易类型，枚举值详见 TradeType</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

#### 返回参数
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
      <td>请求内容，详见<b>本节 ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### ResponseContent结构
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
      <td>错误码，详见 Status。0：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
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
      <td>消息 id</td>
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
      <td>authen_info 存在时必填。详见 QueryOrderResponse</td>
   </tr>
</table>

#### QueryOrderResponse 结构
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
      <td>支付商户信息，status 为0时必填。详见 PayMchKey</td>
   </tr>
   <tr>
      <td>order_content</td>
      <td>否</td>
      <td>OrderContent</td>
      <td>订单信息，status 为0时必填。详见 OrderContent</td>
   </tr>
</table>

#### 构造查询订单请求例子
```
/*
构造请求字符串
*/
std::string gen_cloud_pay_query_order(
    const int         &pay_platform,
    const std::string &out_mch_id,
    const std::string &out_sub_mch_id,
    const std::string &out_shop_id,
    const std::string &out_trade_no,
    const int         &trade_type,
    const std::string &device_id,
    const std::string &staff_id,
    const int         &terminal_type,
    const std::string &machine_no,
    const std::string &sdk_version,
    const std::string &spbill_create_ip,
    const std::string &authen_key
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
    order_client["staff_id"]         = staff_id;
    order_client["terminal_type"]    = terminal_type;
    order_client["machine_no"]       = machine_no;
    order_client["sdk_version"]      = sdk_version;
    order_client["spbill_create_ip"] = spbill_create_ip;
    request_content["order_client"]  = order_client;

    Json::FastWriter w;
    const std::string &rc = w.write(request_content);

    Json::Value authen_info, s;
    a["authen_type"] = 1;
    // 使用计算认证码举例（使用 OpenSSL 实现）中的函数计算认证码
    std::string authen_code;
    if (!calc_HMAC_SHA256(authen_key, rc, &authen_code)) {
        // 计算失败
        return "";
    }
    a["authen_code"] = authen_code;
    authen_info["a"] = a;

    Json::Value request;
    request["request_content"] = rc;
    request["authen_info"] = authen_info;

    return w.write(request);
}
/*
构造请求完毕之后，将请求通过 POST 方法发送到云支付接口对应的 URL
使用了发送请求举例（使用 libcurl 实现）中的 post 函数
*/
std::string response;
post(request, "https://pay.qcloud.com/cpay/query_order", &response);
```
### 查询退款单
#### 接口地址
`https://pay.qcloud.com/cpay/query_refund_order`

content_type：application/json
#### 输入参数
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
      <td>请求内容，详见<b>本节 RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### RequestContent结构
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
      <td>支付商户信息，详见 PayMchKey</td>
   </tr>
   <tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>客户端信息，详见 OrderClient</td>
   </tr>
   <tr>
      <td>out_trade_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的订单号，前缀必须是云支付订单前缀</td>
   </tr>
   <tr>
      <td>out_refund_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的退款单号，前缀必须是云支付订单前缀</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

#### 返回参数
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
      <td>请求内容，详见<b>本节 ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### ResponseContent结构
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
      <td>错误码，详见 Status。0：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
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
      <td>消息 id</td>
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
      <td>authen_info 存在时，必填。详见 QueryRefundOrderResponse</td>
   </tr>
</table>

#### QueryRefundOrderResponse 结构
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
      <td>支付商户信息，status 为0时必填。详见 PayMchKey</td>
   </tr>
   <tr>
      <td>refund_order_content</td>
      <td>否</td>
      <td>RefundOrderContent[]</td>
      <td>订单信息，status 为0时必填。详见 RefundOrderContent</td>
   </tr>
</table>

#### 构造查询退款单请求例子
```
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
    const int         &terminal_type,
    const std::string &machine_no,
    const std::string &sdk_version,
    const std::string &spbill_create_ip,
    const std::string &authen_key
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
    order_client["staff_id"]         = staff_id;
    order_client["terminal_type"]    = terminal_type;
    order_client["machine_no"]       = machine_no;
    order_client["sdk_version"]      = sdk_version;
    order_client["spbill_create_ip"] = spbill_create_ip;
    request_content["order_client"]  = order_client;

    Json::FastWriter w;
    const std::string &rc = w.write(request_content);

    Json::Value authen_info, s;
    a["authen_type"] = 1;
    // 使用计算认证码举例（使用 OpenSSL 实现）中的函数计算认证码
    std::string authen_code;
    if (!calc_HMAC_SHA256(authen_key, rc, &authen_code)) {
        // 计算失败
        return "";
    }
    a["authen_code"] = authen_code;
    authen_info["a"] = a;

    Json::Value request;
    request["request_content"] = rc;
    request["authen_info"] = authen_info;

    return w.write(request);
}
/*
构造请求完毕之后，将请求通过 POST 方法发送到云支付接口对应的 URL
使用了发送请求举例（使用 libcurl 实现）中的 post 函数
*/
std::string response;
post(request, "https://pay.qcloud.com/cpay/query_refund_order", &response);
```
### 支付成功回调
#### 接口地址
服务商在云支付管理后台配置的回调地址（HTTPS），即“交易完成回调 URL”。
content_type：application/json
#### 输入参数
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
      <td>请求内容，详见<b>本节 RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### RequestContent 结构
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
      <td>支付商户信息，详见 PayMchKey</td>
   </tr>
   <tr>
      <td>order_content</td>
      <td>是</td>
      <td>OrderContent</td>
      <td>订单信息，详见 OrderContent</td>
   </tr>
<tr>
      <td>order_client</td>
      <td>是</td>
      <td>OrderClient</td>
      <td>订单信息，详见 OrderClient</td>
   </tr>
</table>

#### 返回参数
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
      <td>请求内容，详见本节 ResponseContent</td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### ResponseContent 结构
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
      <td>错误码。0：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
   </tr>
   <tr>
      <td>description</td>
      <td>否</td>
      <td>String(255)</td>
      <td>错误描述</td>
   </tr>
</table>

### 多条件查询订单信息

#### 接口地址

- `https://pay.qcloud.com/cpay/client_order_detail`
- `content_type：application/json`

#### 输入参数

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
| `request_content` | 是 | RequestContent | 请求内容，详见本节 RequestContent |
| `authen_info` | 是 | AuthenInfo | 认证信息，详见 AuthenInfo |

**RequestContent 结构**

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
| `pay_platform` | 否 | Number(32) | 第三方支付平台，详见 PayPlatform |
| `out_sub_mch_id` | 是 | String  | 云支付分配的子商户 ID |
| `out_shop_id` | 否 | String | 云支付分配的门店全局 ID |
| `staff_id` | 否 | String | 门店内店员的编号 |
| `device_id` | 否  | String | 子商户自定义的终端设备编号 |
| `query_order_type` | 是 | Number(32) | 查询订单类型; 详细定义见本节 QueryOrderType；默认为3 |
| `start_time` | 否 | Number(64) | 查询开始时间；unix 时间戳；默认为0 |
| `end_time` | 是 | Number(64) | 查询结束时间；unix 时间戳；默认为当前时间 |
| `page_num` | 是 | Number(32) | 页码（从1开始计数）|
| `page_size` | 是 | Number(32) | 单页条数 |
| `nonce_str` | 否 | String(32) | 随机字符串 |

**QueryOrderType** 取值：

- 1：订单
- 2：退款单
- 3：订单和退款单

>!
- 如果需要查询子商户的订单，`out_shop_id`、`staff_id`、`device_id`不传
- 如果需要查询门店的订单，`out_shop_id`必传；`staff_id`、`device_id`不传
- 如果需要查询店员的订单，`out_shop_id`、`staff_id`都必传

#### 返回参数

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
| `response_content` | 是 | ResponseContent | 请求内容，详见本节 ResponseContent |
| `authen_info` | 是 | AuthenInfo | 认证信息，详见 AuthenInfo |

**ResponseContent 结构**

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
| `status` | 是 | Status | 错误码，详见 Status |
| `description` | 否 | String(255) | 错误描述信息 |
| `log_id` | 是 | Number(32) | 消息 ID |
| `internal_status` | 是 | Number(32) | 调试使用，调用者可以不予理会 |
| `order_detail_query` | 否 | OrderDetailQueryResponse | 订单信息，详细见本节 |

**OrderDetailQueryResponse** 结构如下：

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
| `total_count` | 否 | Number(32) | 符合条件的订单总条数；**不是本次返回的订单条数** |
| `order_details` | 否 | OrderDetail [] | 订单详细信息，详细见本节 |

**OrderDetail** 结构如下：

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
| `shop_info` | 否 | ShopInfo | 门店信息，详细见 ShopInfo |
| `shop_staff_info` | 否 | StaffInfo | 店员信息，详细见 StaffInfo |
| `receipt` | 否 | Receipt | 订单信息，详细结构如下 |

**Receipt** 结构如下：

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
| `order` | 否 | Order | 支付订单信息 |
| `refund_order` | 否 | RefundOrder | 退款单信息 |

**Order** 结构如下：

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
| `order_mch` | 是 | OrderMch | 支付商户信息，详细见 OrderMch |
| `order_content` | 是 | OrderContent | 订单信息，详细见 OrderContent |
| `order_client` | 是 | OrderClient | 客户端信息，详细见 OrderClient |
| `authen_info` | 是 | AuthenInfo | 认证信息，详细见 AuthenInfo |

**RefundOrder** 结构如下：

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
| `refund_order_mch` | 是 | OrderMch | 支付商户信息，详细见 OrderMch |
| `refund_order_content` | 是 | RefundOrderContent | 订单信息，详细见 OrderContent |
| `order_client` | 是 | OrderClient | 客户端信息，详细见 OrderClient |
| `authen_info` | 是 | AuthenInfo | 认证信息，详细见 AuthenInfo |


## 门店接口
### 查询门店信息
#### 接口地址
`https://pay.qcloud.com/cpay/query_sub_mch_shop_info`

content_type：application/json
#### 输入参数
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
      <td>请求内容，详见<b>本节 RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### RequestContent 结构
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
      <td>云支付分配给服务商的帐号</td>
   </tr>
   <tr>
      <td>out_sub_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给子商户的帐号</td>
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
      <td>页码（从1开始）</td>
   </tr>
   <tr>
      <td>page_size</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>单页条数</td>
   </tr>
</table>

#### 返回参数
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
      <td>请求内容，详见<b>本节 ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### ResponseContent 结构
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
      <td>错误码，详见 Status。0：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
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
      <td>消息 id</td>
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
      <td>authen_info 存在时必填。详见 QueryShopInfoResponse</td>
   </tr>
</table>

#### QueryShopInfoResponse 结构
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
      <td><b>status 为0时返回以下参数：</b></td>
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

#### 构造查询门店信息请求例子
```
/*
构造请求字符串
*/
std::string gen_cloud_pay_query_sub_mch_shop_info(
    const std::string &out_mch_id,
    const std::string &out_sub_mch_id,
    const int          page_num,
    const int          page_size,
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
    // 使用计算认证码举例（使用 OpenSSL 实现）中的函数计算认证码
    std::string authen_code;
    if (!calc_HMAC_SHA256(authen_key, rc, &authen_code)) {
        // 计算失败
        return "";
    }
    a["authen_code"] = authen_code;
    authen_info["a"] = a;

    Json::Value request;
    request["request_content"] = rc;
    request["authen_info"] = authen_info;

    return w.write(request);
}
/*
构造请求完毕之后，将请求通过 POST 方法发送到云支付接口对应的 URL
使用了发送请求举例（使用 libcurl 实现）中的 post 函数
*/
std::string response;
post(request, "https://pay.qcloud.com/cpay/query_sub_mch_shop_info", &response);
```

### 查询子商户信息
#### 接口地址
`https://pay.qcloud.com/cpay/sdk_query_sub_mch_info`

content_type：application/json
#### 输入参数
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
      <td>请求内容，详见<b>本节 RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### RequestContent 结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>out_sub_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给子商户的帐号</td>
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
      <td>页码，请填1，当前只支持查询一个子商户信息</td>
   </tr>
   <tr>
      <td>page_size</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>单页条数，请填1，当前只支持查询一个子商户信息</td>
   </tr>
</table>

#### 返回参数
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
      <td>请求内容，详见<b>本节 ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### ResponseContent 结构
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
      <td>错误码，详见 Status。0：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
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
      <td>消息 id</td>
   </tr>
   <tr>
      <td>internal_status</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>调试使用，调用者可以不予理会</td>
   </tr>
   <tr>
      <td>query_sub_mch_info</td>
      <td>否</td>
      <td>QuerySubMchInfoResponse</td>
      <td>authen_info 存在时必填。<b>详见本节 QuerySubMchInfoResponse</b></td>
   </tr>
</table>

#### QuerySubMchInfoResponse 结构
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
      <td><b>status 为0时返回以下参数：</b></td>
   </tr>
   <tr>
      <td>sub_mch_infos</td>
      <td>否</td>
      <td>SubMch[]</td>
      <td>子商户信息，<b>详见本节 SubMch</b></td>
   </tr>
   <tr>
      <td>total_count</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>数据总数</td>
   </tr>
</table>

#### SubMch结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>第三方支付平台分配给服务商的帐号</td>
   </tr>
   <tr>
      <td>pay_platform</td>
      <td>是</td>
      <td>PayPlatform</td>
      <td>第三方支付类型，详见 PayPlatform</td>
   </tr>
   <tr>
      <td>company_name</td>
      <td>是</td>
      <td>String(255)</td>
      <td>服务商在第三方平台登记的公司名称</td>
   </tr>
   <tr>
      <td>mch_sub_uin</td>
      <td>是</td>
      <td>String(32)</td>
      <td>子服务商 uin</td>
   </tr>
   <tr>
      <td>mch_sub_company_name</td>
      <td>是</td>
      <td>String(255)</td>
      <td>子服务商公司名</td>
   </tr>
   <tr>
      <td>sub_mch_infos</td>
      <td>否</td>
      <td>SubMchInfo[]</td>
      <td>子商户信息，详见 SubMchInfo</td>
   </tr>
   <tr>
      <td>out_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>服务商 out id</td>
   </tr>
</table>

## 监控上报接口
### 上报客户端接口监控信息
#### 接口地址
`https://pay.qcloud.com/cpay/upload_client_monitor_info`

content_type：application/json
#### 输入参数
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
      <td>请求内容，详见<b>本节 RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### RequestContent 结构
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
      <td>云支付分配给子商户的帐号</td>
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
      <td>客户端信息，详见 OrderClient</td>
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
      <td>压缩算法类型，is_compress 为 true 时必填，详见 CompressType</td>
   </tr>
   <tr>
      <td>compressed_monitor_info<br><br>uncompressed_monitor_info</td>
      <td>二选一</td>
      <td>String<br><br>UncompressedMonitorInfo</td>
      <td>压缩数据<br><br>未压缩数据，详见 UncompressedMonitorInfo</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

#### UncompressedMonitorInfo 结构
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
      <td>客户端接口调用结果，详见 ClientIntResult</td>
   </tr>
   <tr>
      <td>machine_info</td>
      <td>是</td>
      <td>String</td>
      <td>CPU 使用率，内存使用率，磁盘使用情况等，json 结构</td>
   </tr>
</table>

#### ClientIntResult 结构
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
      <td>接口类型，详见 Interface</td>
   </tr>
   <tr>
      <td>status</td>
      <td>是</td>
      <td>Status</td>
      <td>错误码，详见 Status。0：成功，非0：失败或者需要重试，具体见实际返回的错误码</td>
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
      <td>后台生成的 log_id，方便对齐日志</td>
   </tr>
   <tr>
      <td>domain_name</td>
      <td>是</td>
      <td>String(1024)</td>
      <td>服务端域名</td>
   </tr>
</table>

#### 返回参数
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
      <td>请求内容，详见<b>本节 ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### ResponseContent 结构
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
      <td>错误码，详见 Status。0：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
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
      <td>authen_info 存在时，必填。详见 UploadClientMonitorInfoResponse</td>
   </tr>
</table>

#### UploadClientMonitorInfoResponse 结构
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
      <td>status 为0时必填。期望上报间隔，单位：s。<br>0表示不用改变当前上报间隔</td>
   </tr>
</table>

#### 构造上报客户端接口监控信息请求例子
```
/*
构造请求字符串
*/
std::string gen_cloud_pay_upload_client_monitor_info(
    const std::string &out_mch_id,
    const std::string &out_sub_mch_id,
    const std::string &out_shop_id,
    const std::string &device_id,
    const std::string &staff_id,
    const int         &terminal_type,
    const std::string &machine_no,
    const std::string &sdk_version,
    const std::string &spbill_create_ip,
    const int          interval,
    const std::string &machine_info,
    const std::string &authen_key
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
    order_client["staff_id"]         = staff_id;
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
    // 使用计算认证码举例（使用 OpenSSL 实现）中的函数计算认证码
    std::string authen_code;
    if (!calc_HMAC_SHA256(authen_key, rc, &authen_code)) {
        // 计算失败
        return "";
    }
    a["authen_code"] = authen_code;
    authen_info["a"] = a;

    Json::Value request;
    request["request_content"] = rc;
    request["authen_info"] = authen_info;

    return w.write(request);
}
/*
构造请求完毕之后，将请求通过 POST 方法发送到云支付接口对应的 URL
使用了发送请求举例（使用 libcurl 实现）中的 post 函数
*/
std::string response;
post(request, "https://pay.qcloud.com/cpay/upload_client_monitor_info", &response);
```
### 上报客户端机器配置信息
#### 接口地址
`https://pay.qcloud.com/cpay/upload_client_conf_info`

content_type：application/json
#### 输入参数
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
      <td>请求内容，详见<b>本节 RequestContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>是</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### RequestContent 结构
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
      <td>云支付分配给服务商的帐号</td>
   </tr>
   <tr>
      <td>out_sub_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给子商户的帐号</td>
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
      <td>客户端信息，详见 OrderClient</td>
   </tr>
   <tr>
      <td>machine_info</td>
      <td>是</td>
      <td>String</td>
      <td>主机信息，如主机名，磁盘，CPU，内存信息等，json 结构</td>
   </tr>
   <tr>
      <td>nonce_str</td>
      <td>是</td>
      <td>String(32)</td>
      <td>随机字符串</td>
   </tr>
</table>

#### 返回参数
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
      <td>请求内容，详见<b>本节 ResponseContent</b></td>
   </tr>
   <tr>
      <td>authen_info</td>
      <td>否</td>
      <td>AuthenInfo</td>
      <td>认证信息，详见 AuthenInfo</td>
   </tr>
</table>

#### ResponseContent 结构
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
      <td>错误码，详见 Status。0：成功；非0：失败或者需要重试，具体见实际返回的错误码</td>
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
      <td>消息 id</td>
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
      <td>authen_info 存在时必填。详见 UploadClientConfInfoResponse</td>
   </tr>
</table>

#### UploadClientConfInfoResponse 结构
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

#### 构造上报客户端机器配置信息请求例子
```
/*
构造请求字符串
*/
std::string gen_cloud_pay_upload_client_conf_info(
    const std::string &out_mch_id,
    const std::string &out_sub_mch_id,
    const std::string &out_shop_id,
    const std::string &device_id,
    const std::string &staff_id,
    const int         &terminal_type,
    const std::string &machine_no,
    const std::string &sdk_version,
    const std::string &spbill_create_ip,
    const std::string &machine_info,
    const std::string &authen_key
)
{
    Json::Value request_content;
    request_content["out_mch_id"] = out_mch_id;
    request_content["out_sub_mch_id"] = out_sub_mch_id;
    request_content["out_shop_id"] = out_shop_id;

    request_content["nonce_str"] = generate_random_nonce_str();

    Json::Value order_client;
    order_client["device_id"]        = device_id;
    order_client["staff_id"]         = staff_id;
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
    // 使用计算认证码举例（使用 OpenSSL 实现）中的函数计算认证码
    std::string authen_code;
    if (!calc_HMAC_SHA256(authen_key, rc, &authen_code)) {
        // 计算失败
        return "";
    }
    a["authen_code"] = authen_code;
    authen_info["a"] = a;

    Json::Value request;
    request["request_content"] = rc;
    request["authen_info"] = authen_info;

    return w.write(request);
}
/*
构造请求完毕之后，将请求通过 POST 方法发送到云支付接口对应的 URL
使用了发送请求举例（使用 libcurl 实现）中的 post 函数
*/
std::string response;
post(request, "https://pay.qcloud.com/cpay/upload_client_conf_info", &response);
```
## 公共数据结构
### 认证签名信息
#### AuthenInfo 结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>a<br><br>s</td>
      <td>退款接口使用签名,其他接口使用认证码</td>
      <td>Authen<br><br>Signature</td>
      <td>认证信息，详见 Authen<br><br>签名信息，详见 Signature</td>
   </tr>
</table>

#### Authen 结构
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
      <td>认证算法，详见 AuthenType</td>
   </tr>
   <tr>
      <td>authen_code</td>
      <td>是</td>
      <td>String(2048)</td>
      <td>认证码</td>
   </tr>
</table>

#### Signature 结构
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
      <td>签名算法，详见 Signature</td>
   </tr>
   <tr>
      <td>sign</td>
      <td>是</td>
      <td>String(2048)</td>
      <td>签名内容</td>
   </tr>
</table>

### 订单信息
#### OrderContent 结构（仅作为返回参数）
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
      <td>交易类型，详见 TradeType</td>
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
      <td>第三方支付平台回调 url（刷卡支付不需要该字段）</td>
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
      <td>货币类型（目前只支持人民币，请填 CNY）</td>
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
      <td>现金支付货币类型（目前只支持人民币，请填 CNY）</td>
   </tr>
   <tr>
      <td>settlement_total_fee</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>应结支付金额，单位分</td>
   </tr>
   <tr>
      <td>refunded_fee</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>已退款金额，单位分，只有接口 client_order_detail 返回这个字段，接口 query_order 不返回</td>
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
      <td>商品详细列表，详见 Detail</td>
   </tr>
   <tr>
      <td>coupon_infos</td>
      <td>否</td>
      <td>CouponInfo</td>
      <td>代金券信息，详见 CouponInfo</td>
   </tr>
   <tr>
      <td>wxpay_order_content_ext</td>
      <td>否</td>
      <td>WxpayOrderContentExt</td>
      <td>微信支付扩展信息，详见 WxpayOrderContentExt</td>
   </tr>
   <tr>
      <td>alipay_order_content_ext</td>
      <td>否</td>
      <td>AlipayOrderContentExt</td>
      <td>支付宝扩展信息，详见 AlipayOrderContentExt</td>
   </tr>
   <tr>
      <td>card_order_content_ext</td>
      <td>否</td>
      <td>CardOrderContentExt</td>
      <td>会员卡扩展信息，详见 CardOrderContentExt</td>
   </tr>
</table>

#### CouponInfo 结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>coupon_id</td>
      <td>否</td>
      <td>String(20)</td>
      <td>代金券或立减优惠 id<br>使用微信支付代金券时有返回</td>
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
      <td>代金券类型，CASH--充值代金券<br>NO_CASH---非充值代金券<br>使用代金券时有返回</td>
   </tr>
   <tr>
      <td>contribute_type</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>资金来源，1：商户 2：平台 3：其他</td>
   </tr>
</table>

#### WxpayOrderContentExt 结构
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
      <td>订单当前状态，详见 WxpayOrderState</td>
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
      <td>已废弃，请使用 OrderContent 下的 coupon_infos 字段<br>代金券信息，详见 WxpayCouponInfo</td>
   </tr>
   <tr>
      <td>product_id</td>
      <td>否</td>
      <td>String(32)</td>
      <td>商品 id，子商户自定义，扫码支付时必传</td>
   </tr>
   <tr>
      <td>prepare_id</td>
      <td>否</td>
      <td>String(64)</td>
      <td>公众号或 APP 支付时，下单后用于拉起支付的预支付会话标识</td>
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

#### WxpayCouponInfo 结构
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
      <td>代金券或立减优惠批次 id</td>
   </tr>
   <tr>
      <td>coupon_id</td>
      <td>否</td>
      <td>String(20)</td>
      <td>代金券或立减优惠 id</td>
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

#### AlipayOrderContentExt 结构
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
      <td>订单当前状态，详见 AlipayOrderState</td>
   </tr>
   <tr>
      <td>voucher_detail_list</td>
      <td>否</td>
      <td>AlipayVoucherDetail</td>
      <td>代金券列表，支付宝回包的内容，详见 AlipayVoucherDetail，示例：<br>"voucher_detail_list": [<br>{
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
      <td>支付渠道，支付宝回包的内容，详见 AlipayFundBill，示例："fund_bill_list": [
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
      <td>json 的分账信息</td>
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
      <td>不可用渠道，格式同 enable_pay_channels</td>
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

#### AlipayVoucherDetail 结构
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
      <td>券 id</td>
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

#### AlipayFundBill 结构
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
      <td>是否发生了资金变化，示例：Y</td>
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

#### CardOrderContentExt 结构
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
      <td>订单当前状态，详见 CardOrderState</td>
   </tr>
   <tr>
      <td>membership_number</td>
      <td>是</td>
      <td>String(32)</td>
      <td>会员卡号</td>
   </tr>
</table>

### 退款单信息
#### RefundOrderContent 结构（仅作为返回参数）
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
      <td>交易类型，详见 TradeType</td>
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
      <td>本次退款总金额货币类型（目前只支持人民币，请填 CNY）</td>
   </tr>
   <tr>
      <td>refund_reason</td>
      <td>否</td>
      <td>String(255)</td>
      <td>退款原因</td>
   </tr>
   <tr>
      <td>coupon_infos</td>
      <td>否</td>
      <td>CouponInfo</td>
      <td>退款代金券信息，详见 CouponInfo</td>
   </tr>
   <tr>
      <td>wxpay_refund_order_content_ext</td>
      <td>是</td>
      <td>WxpayRefundOrderContentExt</td>
      <td>微信支付扩展信息，详见 WxpayRefundOrderContentExt</td>
   </tr>
   <tr>
      <td>alipay_refund_order_content_ext</td>
      <td>是</td>
      <td>AlipayRefundOrderContentExt</td>
      <td>支付宝扩展信息，详见 AlipayRefundOrderContentExt</td>
   </tr>
   <tr>
      <td>card_refund_order_content_ext</td>
      <td>是</td>
      <td>CardRefundOrderContentExt</td>
      <td>会员卡扩展信息，详见 CardRefundOrderContentExt</td>
   </tr>
</table>

#### WxpayRefundOrderContentExt结构
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
      <td>退款状态，详见 WxpayRefundOrderState</td>
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
      <td>去掉非充值代金券退款金额后的退款金额，单位：分。<br>退款金额 = 申请退款金额 - 非充值代金券退款金额，退款金额 <= 申请退款金额<br>退款金额 = 申请退款金额 - 非充值代金券退款金额                                                                       退款金额 <= 申请退款金额</td>
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
      <td>已废弃，请使用 RefundOrderContent 下的 coupon_infos 字段<br>退款代金券信息，详见 WxpayCouponInfo</td>
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
      <td>取当前退款单的退款入账方<br>1. 退回银行卡：{银行名称}{卡类型}{卡尾号}<br>2. 退回支付用户零钱:支付用户零钱</td>
   </tr>
</table>

#### AlipayRefundOrderContentExt 结构
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
      <td>是否发生了资金变化，示例：Y</td>
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

#### CardRefundOrderContentExt 结构
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
      <td>CardRefundOrderState(枚举类型)</td>
      <td>退款状态，详见 CardRefundOrderState</td>
   </tr>
</table>

### 查询订单时商户信息

**OrderMch** 结构

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
|`pay_platform` | 是 | Number(32) | 第三方支付平台；详细见 PayPlatform |
| `out_mch_id` | 否 | String | 云支付分配的服务商 ID |
| `out_sub_mch_id` | 否 | String | 云支付分配的子商户 ID |
| `out_shop_id` | 否 | String | 云支付分配的门店全局 ID |
| `out_channel_id` | 否 | String |云支付分配给渠道商的 ID |
| `out_card_id` | 否 | String |会员卡 ID |
| `sub_mch_pay_info` | 否 | String |商户下单时存在订单中的特定信息 |
| `mch_uin` | 否 | String | 服务商的腾讯云账号 ID |
| `mch_sub_uin` | 否 | String | 子服务商的腾讯云账号 ID |
| `using_stream_sub_mch` | 否 | bool | 是否使用银行商户 |
| `upstream_order_mch_ext` | 否 | UpstreamOrderMchExt | 银行渠道相关信息|
| `wxpay_order_mch_ext` | 否 | WxpayOrderMchExt| 微信支付服务商扩展信息 |
| `alipay_order_mch_ext` | 否 | AlipayOrderMchExt| 支付宝服务商扩展信息 |
| `card_order_mch_ext` | 否 | CardOrderMchExt| 会员卡服务商扩展信息 |

**WxpayOrderMchExt** 结构

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
| `mch_id` | 否 | String | 微信支付分配给服务商的账号 |
| `sub_mch_id` | 否 | String | 微信支付分配给子商户的账号 |
| `shop_id` | 否 | String | 微信支付分配给门店的编号 |
| `app_id` | 否 | String | 微信支付分配给服务商的公众号 ID |
| `sub_app_id` | 否 | String | 微信支付分配给子商户的公众号 ID |
| `open_id` | 否 | String | 顾客在服务商公众号下的唯一标识 |
| `sub_open_id` | 否 | String | 顾客在子商户公众号下的唯一标识 |
| `is_subscribe` | 否 | bool | 用户是否关注了服务商公众号 |
| `sub_is_subscribe` | 否 | bool | 用户是否关注了子商户的公众号 |
| `is_bill` | 否 | bool | 是否为微信买单商户 |
| `use_bill` | 否 | bool | 是否走微信买单渠道 |
| `bill_channel_id` | 否 | String | 微信买单渠道号 |
| `bill_shop_id` | 否 | String | 微信买单默认门店号 |
| `is_macro` | 否 | bool | 是否是小微商户 |

**AlipayOrderMchExt** 结构

| 参数名 | 是否必填 | 类型 | 说明 |
| -- | -- | -- | -- |
| `app_id` | 否 | String | 支付宝分配给服务商的 APP ID|
| `sub_app_id` | 否 | String | 支付宝分配给子商户的 APP ID|
| `user_id` | 否 | String | 顾客的用户号 |
| `sub_mch_id` | 否 | String | 支付宝的子商户号，银行服务商使用|

### 交易请求时的商户信息
#### PayMchKey 结构
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
      <td>第三方支付类型，详见 PayPlatform</td>
   </tr>
   <tr>
      <td>out_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给服务商的帐号</td>
   </tr>
   <tr>
      <td>out_sub_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配给子商户的帐号</td>
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
      <td>关注本次操作的店员/店长在服务商微信公众号下的 open_id。可选。数组</td>
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

#### WxpayPayMchKeyExt 结构
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

#### AlipayPayMchKeyExt 结构
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

### 交易请求时的支付订单信息
#### PayContent 结构（仅交易请求使用）
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
      <td>由客户端生成的订单号，前缀必须是云支付订单前缀</td>
   </tr>
   <tr>
      <td>author_code</td>
      <td>否</td>
      <td>String(128)</td>
      <td>刷卡支付时的授权码（刷卡支付必填，其他不填）；可以使用授权码前缀判断支付平台：微信支付为10~15开头，支付宝为25~30开头，会员卡为99开头</td>
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
      <td>货币类型（目前只支持人民币，请填 CNY）</td>
   </tr>
   <tr>
      <td>body</td>
      <td>是</td>
      <td>String(128)</td>
      <td>商品或订单简要描述<br>商品描述交易字段格式根据不同的应用场景按照以下格式：<br>（1）PC 网站——传入浏览器打开的网站主页 title 名-实际商品名称，例如：腾讯充值中心-QQ 会员充值；<br>（2） 公众号——传入公众号名称-实际商品名称，例如：腾讯形象店- image-QQ 公仔；<br>（3） H5——应用在浏览器网页上的场景，传入浏览器打开的移动网页的主页 title 名-实际商品名称，例如：腾讯充值中心-QQ 会员充值；<br>（4） 线下门店——门店品牌名-城市分店名-实际商品名称，例如： image 形象店-深圳腾大-QQ 公仔）<br>（5） APP——需传入应用市场上的 APP 名字-实际商品名称，天天爱消除-游戏充值。</td>
   </tr>
   <tr>
      <td>detail</td>
      <td>否</td>
      <td>String(6000)</td>
      <td>商品详细列表，由 json 转化而来，详见 Detail。</td>
   </tr>
   <tr>
      <td>wxpay_pay_content_ext</td>
      <td>否</td>
      <td>WxpayPayContentExt</td>
      <td>微信支付扩展信息，详见 WxpayPayContentExt</td>
   </tr>
   <tr>
      <td>alipay_pay_content_ext</td>
      <td>否</td>
      <td>AlipayPayContentExt</td>
      <td>支付宝扩展信息，详见 AlipayPayContentExt</td>
   </tr>
</table>

#### Detail 结构
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
      <td>商家小票 ID</td>
   </tr>
   <tr>
      <td>goods_detail</td>
      <td>必填</td>
      <td>GoodsDetail[]</td>
      <td>商品详情，详见 GoodsDetail</td>
   </tr>
</table>

#### GoodsDetail 结构
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
      <td>商品单价，如果商户有优惠，需传输商户优惠后的单价<br>单品总金额应 <= 订单总金额total_fee，否则会无法享受优惠</td>
   </tr>
</table>

#### WxpayPayContentExt 结构
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
      <td>商品 id，子商户自定义（扫码支付必填，刷卡支付不填，其他可选）</td>
   </tr>
   <tr>
      <td>limit_pay</td>
      <td>否</td>
      <td>String(32)</td>
      <td>定支付方式，目前只能是：no_credit，指定不能使用信用卡支付</td>
   </tr>
</table>

#### AlipayPayContentExt 结构
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

### 退款请求时的退款单信息
#### RefundContent 结构（仅退款请求使用）
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
      <td>由客户端生成的订单号，前缀必须是云支付订单前缀</td>
   </tr>
   <tr>
      <td>out_refund_no</td>
      <td>是</td>
      <td>String(32)</td>
      <td>由客户端生成的退款单号，前缀必须是云支付订单前缀</td>
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
      <td>本次退款总金额货币类型（目前只支持人民币，请填 CNY）</td>
   </tr>
   <tr>
      <td>wxpay_refund_content_ext</td>
      <td>否</td>
      <td>WxpayRefundOrderContentExt</td>
      <td>微信支付扩展信息，详见 WxpayRefundOrderContentExt</td>
   </tr>
   <tr>
      <td>alipay_refund_order_content_ext</td>
      <td>否</td>
      <td>AlipayRefundOrderContentExt</td>
      <td>支付宝扩展信息，详见 AlipayRefundOrderContentExt</td>
   </tr>
</table>

#### WxpayRefundOrderContentExt 结构
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
      <td>退款状态，详见 WxpayRefundOrderState</td>
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
      <td>去掉非充值代金券退款金额后的退款金额，单位：分。<br>退款金额 = 申请退款金额 - 非充值代金券退款金额，退款金额 <= 申请退款金额<br>退款金额 = 申请退款金额 - 非充值代金券退款金额                                                                       退款金额 <= 申请退款金额</td>
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
      <td>退款代金券信息，详见 WxpayCouponInfo</td>
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
      <td>取当前退款单的退款入账方<br>1. 退回银行卡：{银行名称}{卡类型}{卡尾号}<br>2. 退回支付用户零钱:支付用户零钱</td>
   </tr>
</table>

#### AlipayRefundOrderContentExt 结构
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
      <td>是否发生了资金变化，示例：Y</td>
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

### 客户端信息
#### OrderClient 结构
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
      <td>子商户自定义，店员 ID</td>
   </tr>
   <tr>
      <td>terminal_type</td>
      <td>是</td>
      <td>Number(32)</td>
      <td>终端类型，1：windows，2：andriod，3：iso，4：linux，100：其他</td>
   </tr>
   <tr>
      <td>sub_terminal_type</td>
      <td>否</td>
      <td>Number(32)</td>
      <td>子终端类型，代表一个机具品牌，具体值可以联系云支付分配</td>
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
      <td>云支付 SDK 版本号</td>
   </tr>
   <tr>
      <td>spbill_create_ip</td>
      <td>是</td>
      <td>String(16)</td>
      <td>调用云支付 API 的机器 IP</td>
   </tr>
   <tr>
      <td>sn_code</td>
      <td>否</td>
      <td>String(64)</td>
      <td>使用云支付机具配置方式的，刷卡支付、查询订单、申请退款、退款查询四个接口需要填机具的 sn 号</td>
   </tr>
</table>

### 门店信息
#### ShopInfo 结构
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
      <td>外部可见的商户门店号，云支付内全局唯一，可用于生成门店固定二维码，仅返回时有该字段</td>
   </tr>
   <tr>
      <td>out_shop_id_url</td>
      <td>否·</td>
      <td>String(128)</td>
      <td>门店二维码，仅返回时有该字段</td>
   </tr>
   <tr>
      <td>device_infos</td>
      <td>否</td>
      <td>DeviceInfo[]</td>
      <td>门店设备信息列表，详见 DeviceInfo</td>
   </tr>
   <tr>
      <td>staff_infos</td>
      <td>否</td>
      <td>StaffInfo[]</td>
      <td>门店店员信息列表，详见 StaffInfo</td>
   </tr>
   <tr>
      <td>fee_type</td>
      <td>否</td>
      <td>String(20)</td>
      <td>门店支持的币种，如果不填，默认为 CNY</td>
   </tr>
</table>

#### DeviceInfo 结构
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
      <td>设备类型<br>1：刷卡支付；2：扫码支付；3：混合支付，支持刷卡支付+扫码支付；4：固定二维码支付</td>
   </tr>
   <tr>
      <td>remark</td>
      <td>否</td>
      <td>String(64)</td>
      <td>子商户自定义备注信息</td>
   </tr>
   <tr>
      <td>device_name</td>
      <td>是</td>
      <td>String</td>
      <td>设备名称</td>
   </tr>
</table>

#### StaffInfo 结构
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

### 子商户信息
#### SubMchInfo 结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>sub_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>微信支付分配的子商户号</td>
   </tr>
   <tr>
      <td>company_name</td>
      <td>是</td>
      <td>String(255)</td>
      <td>子商户在第三方支付平台登记的公司名称</td>
   </tr>
   <tr>
      <td>desc</td>
      <td>否</td>
      <td>String(255)</td>
      <td>子商户描述</td>
   </tr>
   <tr>
      <td>cloud_cashier_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配的唯一订单前缀，<b>下单时商户的订单号需要以这个 id 开头</b></td>
   </tr>
   <tr>
      <td>out_sub_mch_id</td>
      <td>是</td>
      <td>String(32)</td>
      <td>云支付分配的商户 id</td>
   </tr>
   <tr>
      <td>default_order_body</td>
      <td>否</td>
      <td>String</td>
      <td>默认的商品或订单简要描述,固定二维码支付时使用</td>
   </tr>
   <tr>
      <td>sub_mch_admin_infos</td>
      <td>否</td>
      <td>SubMchAdminInfo</td>
      <td>商户管理者的信息列表，<b>详见本节 SubMchAdminInfo</b></td>
   </tr>
   <tr>
      <td>out_sub_mch_id_url</td>
      <td>是</td>
      <td>String(128)</td>
      <td>子商户二维码</td>
   </tr>
   <tr>
      <td>merchant_name</td>
      <td>是</td>
      <td>String(256)</td>
      <td>子商户在第三方支付平台的商户名</td>
   </tr>
   <tr>
      <td>logo</td>
      <td>否</td>
      <td>String</td>
      <td>商户 logo</td>
   </tr>
   <tr>
      <td>admin_email </td>
      <td>否</td>
      <td>String(255)</td>
      <td>商户管理员邮箱</td>
   </tr>
   <tr>
      <td>phone</td>
      <td>否</td>
      <td>String(255)</td>
      <td>商户联系电话</td>
   </tr>
   <tr>
      <td>one_code_pay_ad_info</td>
      <td>否</td>
      <td>OneCodePayAdInfo</td>
      <td>一码支付中，顾客完成支付后的广告信息,<b>详见本节 OneCodePayAdInfo</b></td>
   </tr>
   <tr>
      <td>is_use_cpay_shop_system</td>
      <td>否</td>
      <td>Bool</td>
      <td>是否使用云支付门店管理系统</td>
   </tr>
   <tr>
      <td>ad_page_url</td>
      <td>否</td>
      <td>String</td>
      <td>支付成功后广告页面 url</td>
   </tr>
   <tr>
      <td>buslic_id</td>
      <td>否</td>
      <td>String(32)</td>
      <td>营业执照 ID</td>
   </tr>
   <tr>
      <td>sub_mch_source</td>
      <td>否</td>
      <td>UInt</td>
      <td>子商户来源</td>
   </tr>
   <tr>
      <td>direct</td>
      <td>是</td>
      <td>Bool</td>
      <td>false 时使用 upstream_out_channel_id 做转发</td>
   </tr>
   <tr>
      <td>upstream_out_channel_id</td>
      <td>否</td>
      <td>String</td>
      <td>将这一商户的支付请求通过这一渠道转发至其他（相关联的）商户</td>
   </tr>
   <tr>
      <td>upstream_company_name</td>
      <td>否</td>
      <td>String</td>
      <td>上游服务商的公司名</td>
   </tr>
   <tr>
      <td>selectable_upstream_sub_mchs</td>
      <td>否</td>
      <td>UpstreamSubMchInfo</td>
      <td>可选择的上游子商户,不包含各种 key，<b>详见本节 UpstreamSubMchInfo</b></td>
   </tr>
   <tr>
      <td>bank_rate</td>
      <td>否</td>
      <td>UInt</td>
      <td>商户进件后，银行收取的费率 1/1000000</td>
   </tr>
   <tr>
      <td>wxpay_sub_mch_info_ext</td>
      <td>否</td>
      <td>WxpaySubMchInfoExt</td>
      <td>微信支付子商户扩展信息，<b>详见本节 WxpaySubMchInfoExt</b></td>
   </tr>
   <tr>
      <td>alipay_sub_mch_info_ext</td>
      <td>否</td>
      <td>AlipaySubMchInfoExt</td>
      <td>支付宝子商户扩展信息，<b>详见本节 AlipaySubMchInfoExt</b></td>
   </tr>
</table>

#### SubMchAdminInfo 结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>name</td>
      <td>是</td>
      <td>String</td>
      <td>真实姓名</td>
   </tr>
   <tr>
      <td>receive_one_code_pay_notify</td>
      <td>否</td>
      <td>Bool</td>
      <td>是否接收一码支付的成功消息通知</td>
   </tr>
</table>

#### OneCodePayAdInfo 结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>picture</td>
      <td>是</td>
      <td>String(64)</td>
      <td>广告图片内容</td>
   </tr>
   <tr>
      <td>url</td>
      <td>否</td>
      <td>String(64)</td>
      <td>单击广告图片后的跳转链接，如没有，则图片无法单击</td>
   </tr>
</table>

#### UpstreamSubMchInfo 结构
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>upstream_out_sub_mch_id</td>
      <td>是</td>
      <td>String(64)</td>
      <td>上游云支付子商户帐号</td>
   </tr>
   <tr>
      <td>upstream_out_mch_id</td>
      <td>是</td>
      <td>String</td>
      <td>上游云支付服务商帐号</td>
   </tr>
   <tr>
      <td>upstream_out_channel_id</td>
      <td>是</td>
      <td>String</td>
      <td>上游服务商渠道 id</td>
   </tr>
   <tr>
      <td>cached_buslic_id</td>
      <td>是</td>
      <td>String</td>
      <td>上游子商户营业执照 id</td>
   </tr>
   <tr>
      <td>cached_cloud_cashier_id</td>
      <td>是</td>
      <td>String</td>
      <td>上游子商户商户订单号前缀</td>
   </tr>
   <tr>
      <td>cached_mch_company_name</td>
      <td>是</td>
      <td>String</td>
      <td>上游服务商的公司名</td>
   </tr>
</table>

#### WxpaySubMchInfoExt 微信支付子商户扩展信息
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>sub_app_id</td>
      <td>否</td>
      <td>String(32)</td>
      <td>第三方支付平台分配给子商户的帐号</td>
   </tr>
</table>

#### AlipaySubMchInfoExt 支付宝子商户扩展信息
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>参数名</td>
      <td>必填</td>
      <td>类型</td>
      <td>说明</td>
   </tr>
   <tr>
      <td>sub_mch_user_id</td>
      <td>否</td>
      <td>String(64)</td>
      <td>子商户在支付宝平台的用户 id 即 uid</td>
   </tr>
   <tr>
      <td>ali_authorization_url</td>
      <td>否</td>
      <td>String</td>
      <td>子商户支付宝授权二维码</td>
   </tr>
</table>


## 枚举值定义
### 交易相关信息
#### PayPlatform 枚举变量
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
   <tr>
      <td>3</td>
      <td>会员卡</td>
   </tr>
</table>

#### TradeType 枚举变量
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

#### WxpayOrderState 枚举变量
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

#### AlipayOrderState 枚举变量
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
      <td>4</td>
      <td>等待用户支付</td>
   </tr>
   <tr>
      <td>5</td>
      <td>已关闭,或者已退款</td>
   </tr>
   <tr>
      <td>6</td>
      <td>交易结束，不可退款</td>
   </tr>
   <tr>
      <td>7</td>
      <td>订单不存在</td>
   </tr>
</table>

#### CardOrderState 枚举变量
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
      <td>已退款</td>
   </tr>
   <tr>
      <td>5</td>
      <td>已关单</td>
   </tr>
</table>

#### WxpayRefundOrderState 枚举变量
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

#### AlipayRefundOrderState 枚举变量
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

#### CardRefundOrderState 枚举变量
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

### 认证加密信息
#### AuthenType 枚举变量
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

#### SignType 枚举变量
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

#### EncrytType 枚举变量
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

### 接口相关信息
#### Status 枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>操作结果</td>
      <td>返回内容是否带认证码</td>
      <td>原请求是否能重试</td>
      <td>用户操作建议</td>      
   </tr>
   <tr>
      <td>0</td>
      <td>成功</td>
      <td>是</td>
      <td>是</td>
      <td>-</td>	   
   </tr>
   <tr>
      <td>3</td>
      <td>未知</td>
      <td>否</td>
      <td>是</td>
      <td>原请求重试</td>      
   </tr>
   <tr>
      <td>101</td>
      <td>失败</td>
      <td>否</td>
      <td>否</td>
      <td>根据 description 字段内容，检查调用逻辑是否有问题，如认证码计算错误</td>
   </tr>
   <tr>
      <td>102</td>
      <td>失败</td>
      <td>是</td>
      <td>否</td>
      <td>换新单号重试，并根据 description 字段内容，检查调用逻辑是否有问题，如单号重复</td>
   </tr>
   <tr>
      <td>103</td>
      <td>未知</td>
      <td>是</td>
      <td>是</td>
      <td>隔3秒后原请求重试或查询结果</td>
   </tr>
   <tr>
      <td>104</td>
      <td>失败</td>
      <td>是</td>
      <td>否</td>
      <td>根据 description 字段内容操作，如退款时顾客余额不足</td>
   </tr>
</table>

#### Interface 枚举变量
<table  border="0" cellspacing="0" cellpadding="0">
   <tr>
      <td>枚举值</td>
      <td>说明</td>
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

### 其他信息
#### CompressType
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
