# API中心
各大企业每天都有大量的API增长，同时越来越多公司开始公开Web API，API的使用场景正在累积。现在，每日API调用量在不断飙升，如何能够安全有效将这些API管理起来对于企业而言并不容易。
千帆鹊桥iPaaS提供API发布功能，可以一键将已发布的应用打包生成API，方便用户进行管理和调用；同时提供了API管理能力，可以针对API进行访问权限管控和流量调度。

## API管理主页

API管理页面的入口为“主页”-“API中心”-“API管理”标签。进入之后则可以看到API管理的主页面。
页面内可以进行API的创建和查看工作，API列表中展示有API服务名称，API服务状态，API服务分组，API服务域名，API更新时间，API服务的数据统计，endpoint统计，API服务的鉴权方式以及操作等内容。同时，每个API服务均可展开，查看下属的endpoint的信息和状态。
![](https://qcloudimg.tencent-cloud.cn/raw/81d0ed9b1e717945803d60303af05892.png)
## 创建API服务

API管理功能支持 3.0.0 版本的 OpenAPI 规范。

用户可以通过点击“创建API服务”按钮进入API的创建界面。

创建API服务可以通过API描述文件创建，也可以通过页面配置完成。

### 通过页面手动创建

完整的手动创建流程需要分两步完成。

1. 配置API服务的基本配置，包括API服务名称，API服务支持的协议类型，API服务的版本号以及对此API服务的一些简单描述（非必填）。同时，如果有分组的需要，希望日后可以通过标签来进行快速的API服务筛选工作，还可以配置标签信息。
![API创建](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/%E5%88%9B%E5%BB%BAAPI%E6%9C%8D%E5%8A%A1.png)
2. 配置API服务的策略信息，包括API服务的鉴权策略，黑白名单策略以及频控、流控策略。鉴权策略此处暂时支持basic Auth，OAuth2.0和无验证（即不填写检测策略）；黑白名单策略则需要按需开启，开启后可以输入多条IP进行黑白名单的访问限制；请求频率策略指从配置时间起，每单位时间内允许的最大请求次数，填写范围为1-1000；访问限制策略则指从配置时间算起，每单位自然时间内允许的最大访问次数，填写范围为1-1000。
![API服务策略](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/API%E6%9C%8D%E5%8A%A1%E7%AD%96%E7%95%A5.png)

- OpenAPI 3.0.0 规范的对象定义请参考 [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.0.md)。

### 通过API描述文件创建

通过描述文件创建API服务，用户可以选择上传一个YAML或者JSON类型的文件，若解析成功，则可以直接通过此文件生成对应的API服务。
![通过描述文件创建](https://qcloudimg.tencent-cloud.cn/raw/7fdab4f0144886a0db4399417b4c0ad8.png)
## API Endpoint管理

当我们创建好一个API服务之后，则代表此API已经生成，可以开始编辑其具体行为了。API Endpoint指一个API服务可以连接的后端服务信息，包括API的访问路径（API Path），API的调用方式，分组，API endpoint绑定的后端服务类型，最近修改时间以及一些操作。
![endpoint](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/endpoint.png)

默认新创建好的API服务是没有已绑定的Endpoint信息的，需要进行创建完成首次的绑定工作。点击“添加API Endpoint”按钮，开启此编辑工作。创建一个完整的API Endpont一共有三步：

1. 基本配置：填写endpoint的基本信息，包括访问路径，后端服务类型（支持选择现成的集成流或者绑定第三方的BASE URL）和后端服务地址。
![APIendpoint基本配置](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/APIendpoint%E5%9F%BA%E6%9C%AC%E9%85%8D%E7%BD%AE.png)

- 请注意，访问路径必须要以“/”开头。
- 当选择的后端服务为“集成流”模式时，集成流只可以选择已发布的，并且配置了拥有http监听能力组件的流。

2. 策略信息：与API服务的策略信息配置方式类似，允许用户在此endpoint所归属的API服务的策略限制基础上，配置第二层策略限制。两层限制共同生效。用户可以选择点击“同步服务策略”按钮，一键同步上层的API服务策略，或者手动填写新的管理策略。需要注意的是，此处可选择的鉴权策略范围为上层API服务的鉴权策略，即若上层API服务只允许OAuth 2.0的鉴权方式，则下层的API Endpoint只允许配置OAuth 2.0,而不能配置Basic Auth。
![endpoint策略](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/endpoint%E7%AD%96%E7%95%A5.png)

3. 参数信息：在此步骤中，我们允许用户配置访问此API endpoint时可以选用的方法（API Method）和每种方法对应的调用参数信息。

   ![endpoint参数](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/endpoint%E5%8F%82%E6%95%B0.png)

   - API调用方法可以多选，若想取消，则可以反选想要删除的方法。

   - 每一个参数后都提供了一系列操作，分别为：向上移动，向下移动，删除此参数，为此参数添加备注以及选择该参数是否必填。

   当上述三步全部配置完成之后，点击“完成”按钮，则会返回API列表，同时已经创建好的endpoint信息将会展现在此。

## API测试与运维

千帆鹊桥iPaaS API管理平台同时还提供了完整的运维方案。通过点击API服务列表中的数据统计图标，可以进入我们的运维窗口

![](https://qcloudimg.tencent-cloud.cn/raw/4a5abe9aed6974a72b1aaa5e8bd27cf9.png)

进入之后，则可以查看此API在规定时间范围内的请求记录和状态汇总。

![API日志](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/API%E6%97%A5%E5%BF%97.png)

同时，为了方便用户对配置完成的API进行在线的调试，我们还提供了通过控制台实时发送测试请求并且获取模拟测试结果的机制。

功能入口：

![](https://qcloudimg.tencent-cloud.cn/raw/bf5175bc271b36caaeb2164802bc30ad.png)

进入之后，可以配置此API endpoint的请求header和body内容，并点击发送请求

![](https://qcloudimg.tencent-cloud.cn/raw/9b2f590152d6d03f7295c76a5d5e8792.png)
随后即可获取到测试的结果。我们会将后端服务返回的response状态码和结果返回给用户，方便进行进一步的调试工作。

![测试结果](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/%E6%B5%8B%E8%AF%95%E7%BB%93%E6%9E%9C.png)

## API用户中心

鹊桥平台会根据用户已经配置完成的API服务（包括其endpoint）生成用户可以调用的开放API。在API用户中心中，我们将会帮助您更好的管理每个API服务的用户，以及分配用户对于API的使用权限。

API用户中心首页是以列表的形式展示当前可以配置的所有API服务信息，但是展示维度与“API管理”略有不同。
![](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/API%E7%94%A8%E6%88%B7%E4%B8%AD%E5%BF%83.png)

### 用户管理

“用户管理“功能允许API的提供者帮助其用户添加及管理账号、分配权限，并获取请求API时所需要的所有必要信息。

API服务提供方可以将会以类似管理者的视角去统一管理用户，允许查看用户的OAuth信息并分享给用户以便用户调用，或者进行用户的封禁和启用。

![用户管理](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86.png)

添加用户的时候需要提供以下用户信息，以便能够更好的记录和维护。同时，此处的用户名称和用户密码也将作为对应API服务的basic auth验证方式。

![添加用户](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/%E6%B7%BB%E5%8A%A0%E7%94%A8%E6%88%B7.png)

当创建好用户之后，则可以通过“查看详细信息”按钮获取到用户的client ID，client Secret等内容

![oauth信息](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/oauth%E4%BF%A1%E6%81%AF.png)

当前仅支持API服务提供方手动帮助客户添加成员信息和账户信息，而客户的自助注册的能力将在近期开放，尽请期待！



## 使用流程

1. 创建API服务及其API Endpoint，流程参考上方页面介绍
2. 获取API请求地址

  2.1 在API服务列表中获取API服务的域名
![](https://qcloudimg.tencent-cloud.cn/raw/7446bbcc7d139f9f3e03c90426857839.png)

  2.2 在API Endpoint列表中获取需要请求的endpoint路径
![获取路径](https://qcloudimg.tencent-cloud.cn/raw/28c050b0218db15495270a6b148836ca.png)

  2.3 将endpoint路径拼接在API服务域名后面，即可获取完整的API请求域名。请将此域名保存，并在第四步中使用。

3. 获取用户请求API的权限

 3.1 在API用户中心首页点击“用户管理”按钮
![点击用户管理](https://qcloudimg.tencent-cloud.cn/raw/7025461e49259b0af42c03866fcbf5e2.png)
 3.2 添加用户
![用户管理界面添加用户](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/%E7%94%A8%E6%88%B7%E7%AE%A1%E7%90%86%E7%95%8C%E9%9D%A2%E6%B7%BB%E5%8A%A0%E7%94%A8%E6%88%B7.png)

 3.3 帮助用户填写必要信息并选择需要访问的API服务名称
![用户信息](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/%E7%94%A8%E6%88%B7%E4%BF%A1%E6%81%AF.png)

 3.4 绑定好API服务之后，返回用户管理列表获取此用户的OAuth信息（当前系统会默认给添加的用户进行自动审批，所以无需手动审批操作），并复制保存OAuth的Token获取地址、Client ID、Client Secret等信息，连同用户的账号和密码一同分享给用户
![获取OAuth](https://qcloudimg.tencent-cloud.cn/raw/fa03ba2d0bade028ab97c1776ccc20fa.png)


4. 从用户侧调用API（以postman为例）

   4.1 API服务无需验证的情况
    ![noauth](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/noauth.png)

   4.2 API服务需要basic Auth的情况
   ![basicauth](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/basicauth.png)

   4.3 API服务需要OAuth 2.0的情况

   首先在用户信息处获取Client ID和Client Secret，在待访问的API服务页面获取Access Token URL
	 ![获取OAuth信息](https://qcloudimg.tencent-cloud.cn/raw/1af24df69318189138461b114fec41cb.png)
	 ![获取token地址](https://qcloudimg.tencent-cloud.cn/raw/77aeacb3f8a34540e209742a6910b3cb.png)
   ![token地址](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/token%E5%9C%B0%E5%9D%80.png)

   复制之后，在postman中创建一个新的请求，填写入上方的token获取地址并使用“GET”方法。请注意，此处的鉴权方式应为“NoAuth”。随后选择Params标签页，输入client信息。输入方式：

   - 第一列key为client_id，value为从上方复制的Client ID对应的内容
   
   - 第二轮key为client_sectet，value为从上方复制的Client Secret对应的内容
   
   ![获取token](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/%E8%8E%B7%E5%8F%96token.png)
   
   随后点击“send”按钮，从界面下方的“body”处复制“access_token”字段的值。此即为本次调用时需要用到的token信息。
	 ![取得token](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/%E5%8F%96%E5%BE%97token.png)
   
   最后，重新打开一个请求界面，填入需要请求的API域名，并选择Bearer Token模式。在右侧的“Token”处输入前面获得的token，点击“send”，即可看到访问结果！
	 ![调用API](https://document-1259649581.cos.ap-guangzhou.myqcloud.com/%E5%BD%92%E6%A1%A3/%E8%B0%83%E7%94%A8API.png)
   


