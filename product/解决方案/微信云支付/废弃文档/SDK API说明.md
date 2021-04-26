## Windows C++ SDK 介绍
云支付提供了五类接口，初始化和结束 SDK 类接口、门店类接口、支付类接口、其他。具体为：  

- 初始化和结束类 SDK 接口，进程启动时需要调用 SDK 的初始化接口，和结束进程时需要调用 SDK 的结束接口；   
- 门店类接口包含查询门店信息；刷卡支付接口需要用到门店/设备/员工 ID 信息，可通过两种方式获取：
	- 调用者先初始化 SDK，然后调用查询门店接口查询门店相关的信息。
	- 直接在手机端子商户管理系统上获取相关信息，然后初始化 SDK。
- 支付类接口包含刷卡支付、查询订单、扫码支付、申请退款、退款查询、交易明细等接口；其中刷卡支付和扫码支付接口成功代表提交下单成功，支付结果需要通过查询订单去获取。申请退款成功只表示退款受理成功，退款的结果需要通过退款查询去获取； 
- 其他接口：如果上述接口返回失败，可以通过获取错误描述接口来得到错误信息。 获取微信支付或支付宝的付款码前缀。获取交易明细接口。获取交易统计接口。
	
## 初始化和结束 SDK 类接口  

### 普通初始化接口

#### 接口定义
使用云支付类接口时需要在进程启动时调用初始化函数，函数定义如下：

	/**
	*	注意事项
	*   1 请求结构全部用JSON结构 JSON仅支持UTF-8字符集, 调用方需要保证字符集
	*   2 如果接口调用失败，可以通过 cloud_pay_get_errmsg 获取错误码
	*/
	
	/**
	* 进程启动时调这个进行初始化
	* 参数conf:
	*          见文件cloud_pay_sdk.proto 的结构CloudPayConf, 按这个格式打包成json
	*/
	CLOUDPAYAPI_SDK_CPP_API int cloud_pay_init(const char *conf);

#### 构造初始化请求参数例子
	std::string gen_cloud_pay_init_conf(
		const std::string &out_mch_id, 
		const std::string &out_sub_mch_id, 
		const std::string &out_shop_id,
		const std::string &device_id,
		const std::string &staff_id,
		const std::string &authen_key,
		const std::string &private_key
	)
	{
		Json::Value root;

		root["common_conf"]["prober_dns"] = 0;
		root["common_conf"]["scan_code_pay_query_order_count"] = 5;

		root["trade_conf"]["device_id"] = device_id;
		root["trade_conf"]["staff_id"] = staff_id;
		root["trade_conf"]["authen_type"] = 1;
		root["trade_conf"]["authen_key"] = authen_key;
		root["trade_conf"]["sign_type"] = 1;
		root["trade_conf"]["private_key"] = private_key;
		root["trade_conf"]["out_shop_id"] = out_shop_id;
		root["trade_conf"]["out_mch_id"] = out_mch_id;
		root["trade_conf"]["out_sub_mch_id"] = out_sub_mch_id;

		Json::FastWriter w;
		std::string json = w.write(root);

		return json;
	}

### 结束 SDK 接口

#### 接口定义
	/**
	* 进程退出时调这个回收DLL中使用的资源
	*/
	CLOUDPAYAPI_SDK_CPP_API int cloud_pay_fini(void);

## 门店类接口

### 门店查询

#### 接口定义
	/**
	* 查询门店（同步调用云支持系统）
	* 请求参数 req:
	*				见文件cloud_pay_sdk.proto 的结构QueryShopInfoRequest, 按这个格式打包成json
	*          shop_info:
	*				 这里需要调用方自己先申请内存，返回门店相关的信息，见文件cloud_pay_sdk.proto 的结构QueryShopInfoResponse
	*          length:
	*				shop_info申请的内存空间长度, 建议申请64K内存
	* 返回值  0  查询门店成功
	*         -1 查询门店失败
	*         -2 结果未知
	*         -3 如sdk内部错误，请使用cloud_pay_get_errmsg获取错误信息
	*/
	CLOUDPAYAPI_SDK_CPP_API int cloud_pay_query_shop_info(const char *req, char *shop_info, int length);

#### 构造门店查询请求参数例子
	std::string gen_cloud_pay_query_shop(const std::string &out_shop_id)
	{
		Json::Value root;

		root["page_num"]  = 1;
		root["page_size"] = 100;
		if (!out_shop_id.empty()){
			root["out_shop_id"] = out_shop_id;
		}

		Json::FastWriter w;
		std::string json = w.write(root);

		return json;
	}

## 支付类接口

### 刷卡支付

#### 接口定义
	/**
	* 刷卡支付。 注意本接口调用成功,只是表示下单受理成功,下单的结果需要调用查单接口去确定。
	* 请求参数 req:
	*				见文件cloud_pay_sdk.proto 的结构MicroPaySdkRequest, 按这个格式打包成json
	*          resp:
	*               如果受理成功 resp 会返回支付平台的类型, json格式的, 需要使用者自己去解析这个平台类型, 调用查单的时候需要用到
	*               如果调用方知道平台类型, 可以不用关心这个值
	* 返回值  0  受理成功，请使用QueryOrder接口获取支付结果
	*        -1 受理失败，请使用cloud_pay_get_errmsg获取受理错误信息 
	*        [ 请注意: 如果是受理失败, 请不要调用撤单接口. 
	*          比如，重入失败(订单号一样，其他请求参数不一样的请求), 如果撤单, 会对之前受理成功的单进行撤单
	*        ]
	*/
	CLOUDPAYAPI_SDK_CPP_API int cloud_pay_micro_pay(const char *req, char *resp, int length);

#### 构造刷卡支付请求参数例子
	std::string gen_cloud_pay_micropay(
		const std::string &out_trade_no,
		const std::string &author_code,
		const int64_t     &total_fee, 
		const std::string &fee_type, 
		const std::string &attach,
		const std::string &goods_tag,
		const std::string &body,
		const std::string &goods_id,
		const std::string &goods_name,
		const int64_t 	  &quantity,
		const int64_t 	  &price
	)
	{
		Json::Value root;

		root["out_trade_no"] = out_trade_no;
		root["author_code"]  = author_code;
		root["total_fee"]    = total_fee;
		root["fee_type"]     = fee_type;
		root["attach"]       = attach;
		root["goods_tag"]    = goods_tag;

		root["body"] = body;

		Json::Value detail;
		detail["goods_id"]   = goods_id;
		detail["goods_name"] = goods_name;
		detail["quantity"]   = quantity;
		detail["price"]      = price;

		root["detail"]["goods_detail"].append(detail);

		Json::FastWriter w;
		std::string json = w.write(root);

		return json;
	}

### 查询订单接口

#### 接口定义
	/**
	* 查询订单. 
	* 请求参数 req:
	*				见文件cloud_pay_sdk.proto 的结构QueryOrderSdkRequest, 按这个格式打包成json
	*          order:
	*				 这里需要调用方自己先申请内存, 结构见 见文件cloud_pay_sdk.proto 的结构OrderSdk
	*          length:
	*				order申请的内存空间长度, 建议申请4K内存
	* 返回值  0  用户支付成功，成功的订单用order返回
	*        -1  支付失败，失败的订单用order返回,
	*                      失败的原因请使用cloud_pay_get_errmsg获取错误信息
	*        -2  结果未知，需要继续查单
	*        -3 非 支付类失败的 失败 如sdk内部错误/订单不存在等，请使用cloud_pay_get_errmsg获取错误信息
	*        -4  已退款或撤单或关单
	*        -5  扫码支付 预下单成功， 通过order获取code_url给用户扫描二维码
	*        -6  重入错误。 返回这个错误码后， 请一定不要对这笔单进行撤单操作。
	*        -7  订单不存在。
	*/
	CLOUDPAYAPI_SDK_CPP_API int cloud_pay_query_order(const char *req, char *order, int length);

#### 构造查询订单请求参数例子
	std::string gen_cloud_pay_query_order(const std::string &out_trade_no, int trade_type, int pay_platform)
	{
		Json::Value root;

		root["trade_type"]   = trade_type;
		root["pay_platform"] = pay_platform;
		root["out_trade_no"] = out_trade_no;

		Json::FastWriter w;
		std::string json = w.write(root);
		return json;
	}

### 扫码支付

#### 接口定义
	/**
	* 扫码支付
	* 请求参数 req:
	*				见文件cloud_pay_sdk.proto 的结构ScanCodePaySdkRequest, 按这个格式打包成json
	* 返回值  0  受理成功，请使用QueryOrder接口获取预下单结果, 如果预下单成功，请从订单信息里获取code_url 进行支付。
	*         -1 受理失败，请使用cloud_pay_get_errmsg获取受理错误信息
	*/
	CLOUDPAYAPI_SDK_CPP_API int cloud_pay_scan_code_pay(const char *req);

#### 构造扫码支付请求参数例子
	std::string gen_cloud_pay_scancodepay(
		const std::string &out_trade_no,
		const std::string &product_id,
		const int64_t 	  &total_fee,
		const std::string &fee_type,
		const std::string &attach,
		const std::string &goods_tag,
		const std::string &body,
		const std::string &goods_id,
		const std::string &goods_name,
		const int64_t     &quantity,
		const int64_t	  &price,
		int pay_platform
	)
	{
		Json::Value root;

		root["pay_platform"] = pay_platform;
		root["out_trade_no"] = out_trade_no;
		root["product_id"]   = product_id;
		root["total_fee"]    = total_fee;
		root["fee_type"]     = fee_type;
		root["attach"]       = attach;
		root["goods_tag"]    = goods_tag;
		root["body"]         = body;

		Json::Value detail;
		detail["goods_id"] = goods_id;
		detail["quantity"] = quantity;
		detail["price"]    = price;
		
		root["detail"]["goods_detail"].append(detail);

		Json::FastWriter w;
		std::string json = w.write(root);

		return json;
	}

### 申请退款

#### 接口定义
	/**
	* 申请退款
	* 请求参数 req:
	*				见文件cloud_pay_sdk.proto 的结构RefundSdkRequest, 按这个格式打包成json
	* 返回值  0  退款受理成功; 退款的状态需要通过查询退款单确认实际退款结果
	*         -1 退款受理失败
	*         -2 结果未知
	*         -3 如sdk内部错误，请使用cloud_pay_get_errmsg获取错误信息
	*/
	CLOUDPAYAPI_SDK_CPP_API int cloud_pay_refund(const char *req);

#### 构造申请退款请求参数例子
	std::string gen_cloud_pay_refund(const std::string &out_trade_no,
		const std::string &out_refund_no,
		const int64_t     &total_fee,
		const int64_t     &refund_fee,
		const std::string &refund_fee_type,
		int               pay_platform,
		const std::string &refund_reason)
	{
		Json::Value root;

		root["pay_platform"] = pay_platform;
		root["out_trade_no"] = out_trade_no;

		if (!out_refund_no.empty())
			root["out_refund_no"] = out_refund_no;

		root["total_fee"] 		= total_fee.c_str();
		root["refund_fee"] 		= refund_fee.c_str();
		root["refund_fee_type"] = refund_fee_type;
		root["refund_reason"] 	= refund_reason;
		Json::FastWriter w;
		std::string json = w.write(root);

		return json;
	}

### 退款查询

#### 接口定义
	/**
	* 查询退款单
	* 请求参数 req:
	*				见文件cloud_pay_sdk.proto 的结构QueryRefundSdkRequest, 按这个格式打包成json
	*          refund_order:
	*				 这里需要调用方自己先申请内存, 结构见 见文件cloud_pay_sdk.proto 的结构RefundOrderSdk
	*          length:
	*				refund_order申请的内存空间长度, 建议申请4K内存
	* 返回值  0  查询退款单成功，退款单用refund_order返回, 退款的结果需要看退款的状态字段。
	*        -1  查询退款单失败，请使用cloud_pay_get_errmsg获取错误信息
	*        -2  结果未知，需要继续查单
	*        -3  sdk内部错误等，请使用cloud_pay_get_errmsg获取错误信息
	*/
	CLOUDPAYAPI_SDK_CPP_API int cloud_pay_query_refund(const char *req, char *refund_order, int length);

#### 构造退款查询请求参数例子
	std::string gen_cloud_pay_query_refund(const std::string &out_trade_no, const std::string &out_refund_no, int pay_platform)
	{
		Json::Value root;

		root["pay_platform"]  = pay_platform;
		root["out_trade_no"]  = out_trade_no;
		root["out_refund_no"] = out_refund_no;
		Json::FastWriter w;
		std::string json = w.write(root);

		return json;
	}

### 交易明细查询

#### 接口定义
	/**
	* 交易明细查询.
	* 请求参数 req:
	*				见文件cloud_pay_sdk.proto 的结构OrderDetailRequest, 按这个格式打包成json
	*          order_details:
	*				 这里需要调用方自己先申请内存, 结构见 见文件cloud_pay_sdk.proto 的结构OrderDetailAllSdk
	*          length:
	*				order_details申请的内存空间长度, 按照请求的page_size来确定，一个订单，建议分配2K内存
	* 返回值  0  交易明细查询成功，成功的订单用order_details返回
	*        -1  交易明细查询失败。失败的原因请使用cloud_pay_get_errmsg获取错误信息
	*        -2  结果未知，需要继续查询交易明细
	*        -3 sdk内部错误等，请使用cloud_pay_get_errmsg获取错误信息
	*/
	CLOUDPAYAPI_SDK_CPP_API int cloud_pay_order_detail(const char *req, char *order_details, int length);

#### 构造交易明细查询请求参数例子
	std::string gen_cloud_pay_detail(
		int pay_platform,
		int query_order_type,
		int query_cashier_type,
		uint32_t page_num,
		uint32_t page_size,
		std::string out_shop_id,
		uint64_t start_time,
		uint64_t end_time,
		std::string staff_id
	)
	{
		Json::Value root;

		root["page_num"] 		   = page_num;
		root["page_size"]          = page_size;
		root["pay_platform"]       = pay_platform;
		root["query_order_type"]   = query_order_type;
		root["query_cashier_type"] = query_cashier_type;
		root["start_time"] 		   = start_time;
		root["end_time"] 		   = end_time;

		if (!out_shop_id.empty())
			root["out_shop_id"]  = out_shop_id;

		if (!out_shop_id.empty() && !staff_id.empty()) {
			root["staff_id"]     = staff_id;
		}

		Json::FastWriter w;
		std::string json = w.write(root);

		return json;
	}

### 交易统计查询

#### 接口定义
	/**
	* 交易明细查询.
	* 请求参数 req:
	*				见文件cloud_pay_sdk.proto 的结构OrderStatRequest, 按这个格式打包成json
	*          order_stat:
	*				 这里需要调用方自己先申请内存, 结构见 见文件cloud_pay_sdk.proto 的结构OrderStatDetail
	*          length:
	*				order_stat申请的内存空间长度, 按照请求的page_size来确定，一个订单，建议分配64K内存
	* 返回值  0  交易统计查询成功，成功的订单用order_stat返回
	*        -1  交易统计查询失败。失败的原因请使用cloud_pay_get_errmsg获取错误信息
	*        -2  结果未知，需要继续查询交易order_stat
	*        -3 sdk内部错误等，请使用cloud_pay_get_errmsg获取错误信息
	*/
	CLOUDPAYAPI_SDK_CPP_API int __stdcall cloud_pay_order_stat(const char *req, char *order_stat, int length);

#### 构造交易统计查询请求参数例子
	static std::string gen_cloud_pay_stat(
		int pay_platform,
		uint32_t page_num,
		uint32_t page_size,
		std::string out_shop_id,
		uint64_t start_time,
		uint64_t end_time
	)
	{
		Json::Value root;

		root["page_num"]     = page_num;
		root["page_size"]    = page_size;
		root["pay_platform"] = pay_platform;
		root["start_time"]   = start_time;
		root["end_time"]     = end_time;

		if (!out_shop_id.empty()) {
			root["out_shop_id"].append(out_shop_id);
		}

		Json::FastWriter w;
		std::string json = w.write(root);

		return json;
	}

## 其他类接口

### 获取错误描述信息

#### 接口定义
	/**
	* 获取具体的错误信息
	*/
	CLOUDPAYAPI_SDK_CPP_API const char* cloud_pay_get_errmsg();

### 获取支付宝和微信支付的付款码前缀
#### 接口定义
	/**
	*  获取支付宝和微信支付的付款码前缀
	*  请求参数 resp:
	*				这里需要调用方自己先申请内存, 内存的长度为length; 用于返回付款码前缀，返回的格式为json格式, { wx_author_code_prefi["","",""],ali_author_code_prefix:["","",""], author_code_prefix:[{1,["","",""]},{2,["","",""]},{3,""}]}，author_code_prefix包含所有的平台
	*          length:
	*				resp申请的内存空间长度, 建议申请256字节内存
	*  返回值  0 获取付款码前缀成功，从resp解析各支付平台前缀
	*          其他 获取付款码前缀失败 , 请使用cloud_pay_get_errmsg获取错误信息
	*/
	CLOUDPAYAPI_SDK_CPP_API int cloud_pay_security_author_code_prefix(char *resp, int length);
