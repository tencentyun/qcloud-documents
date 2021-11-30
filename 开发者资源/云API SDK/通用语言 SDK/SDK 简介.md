
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK 3.0是云 API 3.0平台的配套工具。目前已经支持 CVM、VPC、CBS 等产品，后续所有的云服务产品都会陆续接入。新版 SDK 实现了统一化，具有各个语言版本的 SDK 使用方法相同，接口调用方式相同，错误码相同以及返回包格式相同等优点。

## 支持 SDK 3.0版本的云产品列表

SDK 3.0支持全部 API 3.0下的云产品，本列表可能滞后于实际代码，如有疑问请咨询具体的云产品。

| 云产品名称     | 英文名称及缩写          | SDK 包名     |
| -------- | ----------- | ------------ |
| [云服务器](https://cloud.tencent.com/document/api/213/15689) | Cloud  Virtual Machine，CVM                                  | cvm          |
| [黑石物理服务器1.0](https://cloud.tencent.com/document/api/386/18637) | Cloud  Physical Machine，CPM                                 | bm           |
| [云硬盘](https://cloud.tencent.com/document/api/362/15634)   | Cloud  Block Storage，CBS                                    | cbs          |
| [容器服务](https://cloud.tencent.com/document/api/457/31853) | Tencent  Kubernetes Engine，TKE                              | tke          |
| [弹性伸缩](https://cloud.tencent.com/document/api/377/20423) | Auto  Scaling，AS                                            | as           |
| [云函数](https://cloud.tencent.com/document/api/583/17235)   | Serverless  Cloud Function，SCF                              | scf          |
| [批量计算](https://cloud.tencent.com/document/api/599/15880) | BatchCompute，Batch                                          | batch        |
| [负载均衡](https://cloud.tencent.com/document/api/214/30667) | Cloud  Load Balancer，CLB                                    | clb          |
| [黑石负载均衡](https://cloud.tencent.com/document/product/1027/33225) | -                                                            | bmlb         |
| [私有网络](https://cloud.tencent.com/document/api/215/15755) | Virtual Private  Cloud，VPC                                  | vpc          |
| [黑石私有网络](https://cloud.tencent.com/document/product/1024/34185) | -                                                            | bmvpc        |
| [黑石弹性公网 IP](https://cloud.tencent.com/document/product/1028/32837) | -                                                            | bmeip        |
| [专线接入](https://cloud.tencent.com/document/api/216/18404) | Direct Connect，DC                                           | dc           |
| [云数据库 MySQL](https://cloud.tencent.com/document/api/236/15830) | TencentDB for  MySQL                                         | cdb          |
| [云数据库 Redis](https://cloud.tencent.com/document/api/239/20002) | TencentDB for  Redis                                         | redis        |
| [云数据库 MongoDB](https://cloud.tencent.com/document/api/240/38554) | TencentDB for  MongoDB                                       | mongodb      |
| [数据传输服务](https://cloud.tencent.com/document/api/571/18122) | Data  Transmission Service，DTS                              | dts          |
| [云数据库 MariaDB](https://cloud.tencent.com/document/api/237/16144) | TencentDB for  MariaDB                                       | mariadb      |
| [分布式数据库 TDSQL](https://cloud.tencent.com/document/api/557/16124) | TencentDB for  TDSQL                                         | dcdb         |
| [云数据库 SQL Server](https://cloud.tencent.com/document/api/238/19927) | TencentDB for  SQL Server                                    | sqlserver    |
| [云数据库 PostgreSQL](https://cloud.tencent.com/document/api/409/16761) | TencentDB for PostgreSQL                                     | postgres     |
| [云数据库 Memcached](https://cloud.tencent.com/document/api/241/42210) | TencentDB for  Memcached                                     | memcached    |
| [内容分发网络](https://cloud.tencent.com/document/api/228/30974) | Content  Delivery Network，CDN                               | cdn          |
| [全站加速网络](https://cloud.tencent.com/document/api/570/42480) | Enterprise  Content Delivery Network，ECDN                   | ecdn         |
| [消息队列 CMQ](https://cloud.tencent.com/document/api/406/42642) | Cloud Message  Queue，CMQ                                    | cmq          |
| [消息队列 CKAFKA](https://cloud.tencent.com/document/api/597/40823) | Cloud Kafka，CKAFKA                                          | ckafka       |
| [SSL 证书](https://cloud.tencent.com/document/api/400/41681) | SSL  Certificates                                            | ssl          |
| [主机安全](https://cloud.tencent.com/document/api/296/19825) | Cloud Workload Protection，CWP                               | yunjing      |
| [漏洞扫描服务](https://cloud.tencent.com/document/api/692/16733) | Vulnerability  Scan Service，VSS                             | cws          |
| [移动应用安全](https://cloud.tencent.com/document/api/283/17742) | Mobile  Security，MS                                         | ms           |
| [云点播](https://cloud.tencent.com/document/api/266/31753)   | Video on  Demand，VOD                                        | vod          |
| [云直播](https://cloud.tencent.com/document/api/267/20456)   | Cloud  Streaming Services，CSS                               | live         |
| [小程序 · 云直播](https://cloud.tencent.com/document/api/1078/35028) | Mini Program  Live，MPL                                      | bizlive      |
| [实时音视频](https://cloud.tencent.com/document/api/647/37078) | Tencent  Real-Time Communication，TRTC                       | trtc         |
| [弹性 MapReduce](https://cloud.tencent.com/document/api/589/33971) | Elastic  MapReduce，EMR                                      | emr          |
| [腾讯云搜](https://cloud.tencent.com/document/api/270/42321) | Tencent  Cloud Search，TCS                                   | yunsou       |
| [自然语言处理](https://cloud.tencent.com/document/api/271/35484) | Natural  Language Process，NLP                               | nlp          |
| [机器翻译](https://cloud.tencent.com/document/api/551/15612) | Tencent  Machine Translation，TMT                            | tmt          |
| [智能钛弹性模型服务](https://cloud.tencent.com/document/api/1120/37543) | Tencent  Intelligence Elastic Model Service，TI-EMS          | tiems        |
| [智能钛机器学习平台](https://cloud.tencent.com/document/api/851/42530) | Tencent Intelligence One-Stop Machine Learning Platfoem，TI-ONE | tione        |
| [金融联络机器人](https://cloud.tencent.com/document/api/656/18281) | Finance  Communication Robot，FCR                            | cr           |
| [游戏多媒体引擎](https://cloud.tencent.com/document/api/607/35364) | Game  Multimedia Engine，GME                                 | gme          |
| [智聆口语评测](https://cloud.tencent.com/document/api/884/19310) | Smart Oral  Evaluation，SOE                                  | soe          |
| [短信](https://cloud.tencent.com/document/api/382/38764)     | Short Message  Service，SMS                                  | sms          |
| [号码保护](https://cloud.tencent.com/document/api/610/40967) | Number Privacy  Protection，NPP                              | npp          |
| [物联卡](https://cloud.tencent.com/document/api/636/33864)   | IoT Link                                                     | ic           |
| [物联网通信](https://cloud.tencent.com/document/api/634/19469) | Internet of  Things Hub， IoT Hub                            | iotcloud     |
| [TBaaS](https://cloud.tencent.com/document/api/663/19455)    | Tencent  Blockchain as a Service，TBaaS                      | tbaas        |
| [云监控](https://cloud.tencent.com/document/api/248/30343)   | Cloud  Monitor，CM                                           | monitor      |
| [访问管理](https://cloud.tencent.com/document/api/598/33155) | Cloud Access  Management，CAM                                | cam          |
| [安全凭证服务 ](https://cloud.tencent.com/document/api/598/40384) | -                                                            | sts          |
| [标签](https://cloud.tencent.com/document/api/651/35307)     | -                                                            | tag          |
| [企业组织](https://cloud.tencent.com/document/api/850/38719) | Tencent Cloud Organization                                   | organization |
| [密钥管理系统](https://cloud.tencent.com/document/api/573/34403) | Key Management  Service，KMS                                 | kms          |
| [云审计](https://cloud.tencent.com/document/api/629/35332)   | CloudAudit，CA                                               | cloudaudit   |
| [迁移服务平台](https://cloud.tencent.com/document/api/659/18591) | Migration  Service Platform，MSP                             | msp          |
| [计费相关](https://cloud.tencent.com/document/api/555/19170) | -                                                            | billing      |
| [渠道合作伙伴](https://cloud.tencent.com/document/api/563/16034) | -                                                            | partners     |
| [边缘计算机器](https://cloud.tencent.com/document/api/1108/42576) | Edge Computing  Machine，ECM                                 | ecm          |
| [游戏服务器引擎](https://cloud.tencent.com/document/api/1165/42076) | Game Server  Engine，GSE                                     | gse          |
| [人像变换](https://cloud.tencent.com/document/api/1202/41971) | Face  Transformation，FT                                     | ft           |
| [容器镜像服务](https://cloud.tencent.com/document/api/1141/41605) | Tencent  Container Registry，TCR                             | tcr          |
| [人脸试妆](https://cloud.tencent.com/document/api/1172/40697) | FaceMakeup，FMU                                              | fmu          |
| [凭据管理服务](https://cloud.tencent.com/document/api/1140/40506) | -                                                            | ssm          |
| [企业收付平台](https://cloud.tencent.com/document/api/1122/40639) | Company  Payment Distributor Platform，CPDP                  | cpdp         |
| [营销号码安全](https://cloud.tencent.com/document/api/1127/40301) | Security of  Marketing Phone Number，SMPN                    | smpn         |
| [腾讯云剪](https://cloud.tencent.com/document/api/1156/40338) | Cloud Media  Editor，CME                                     | cme          |
| [正版曲库直通车](https://cloud.tencent.com/document/api/1155/40100) | Authorized  Music Express，AME                               | ame          |
| [互动白板](https://cloud.tencent.com/document/api/1137/40049) | Tencent  Interactive Whiteboard，TIW                         | tiw          |
| [数据库智能管家](https://cloud.tencent.com/document/api/1130/39547) | TencentDB for  DBbrain，DBbrain                              | dbbrain      |
| [云 HDFS](https://cloud.tencent.com/document/api/1105/37347) | Cloud  HDFS，CHDFS                                           | chdfs        |
| [验证码](https://cloud.tencent.com/document/api/1110/36917)  | Captcha                                                      | captcha      |
| [域名注册](https://cloud.tencent.com/document/api/242/38884) | -                                                            | domain       |
| [游戏数据库 TcaplusDB](https://cloud.tencent.com/document/api/596/39648) | Tcaplus DataBase                                             | tcaplusdb    |
| [云拨测](https://cloud.tencent.com/document/api/280/40881)   | Cloud  Automated Testing，CAT                                | cat          |
| [语音识别](https://cloud.tencent.com/document/api/1093/35637) | Automatic  Speech Recognition，ASR                           | asr          |
| [语音合成](https://cloud.tencent.com/document/api/1073/37986) | Text To  Speech，TTS                                         | tts          |
| [业务风险情报](https://cloud.tencent.com/document/api/1064/35622) | Business Risk  Intelligence，BRI                             | bri          |
| [物联网设备身份认证](https://cloud.tencent.com/document/api/1086/35602) | IoT Trust ID                                                 | iottid       |
| [物联网开发平台](https://cloud.tencent.com/document/api/1081/34958) | IoT Explorer                                                 | iotexplorer  |
| [物联网智能视频服务](https://cloud.tencent.com/document/product/1361)                                           | Internet of  Things Video，IoT Video                         | iotvideo     |
| [腾讯智能对话平台](https://cloud.tencent.com/document/api/1060/37428) | Tencent Bot  Platform，TBP                                   | tbp          |
| [数据安全审计](https://cloud.tencent.com/document/api/856/33899) | Data Security  Audit，DSAudit                                | cds          |
| [腾讯微服务平台 TSF](https://cloud.tencent.com/document/api/649/36037) | Tencent  Service Framework，TSF                              | tsf          |
| [视频处理](https://cloud.tencent.com/document/api/862/37569) | Media  Processing Service，MPS                               | mps          |
| [云加密机](https://cloud.tencent.com/document/api/639/41452) | Cloud Hardware  Security Module，CloudHSM                    | cloudhsm     |
| [云开发](https://cloud.tencent.com/document/api/876/34809)   | Tencent Cloud  Base，TCB                                     | tcb          |
| [全球应用加速](https://cloud.tencent.com/document/api/608/36932) | Global  Application Acceleration Platform，GAAP              | gaap         |
| [文件存储](https://cloud.tencent.com/document/api/582/38145) | Cloud File  Storage，CFS                                     | cfs          |
| [人脸核身](https://cloud.tencent.com/document/api/1007/31320) | Face ID                                                      | faceid       |
| [DDoS 高防包](https://cloud.tencent.com/document/api/1021/39215) | Anti-DDoS Pro                                                | dayu         |
| [威胁情报云查服务](https://cloud.tencent.com/document/api/1013/31737) | Threat Intelligence Cloud Services，TICS                     | tics         |
| [英文作文批改](https://cloud.tencent.com/document/api/1076/35201) | English  composition correction，ECC                         | ecc          |
| [数学作业批改](https://cloud.tencent.com/document/api/1004/30607) | Homework  Correction-Math，HCM                               | hcm          |
| [人脸融合](https://cloud.tencent.com/document/api/670/31052) | Face Fusion                                                  | facefusion   |
| [人脸识别](https://cloud.tencent.com/document/api/867/32770) | Face  Recognition                                            | iai          |
| [文字识别](https://cloud.tencent.com/document/api/866/33515) | Optical  Character Recognition，OCR                          | ocr          |
| [图像分析](https://cloud.tencent.com/document/api/865/35462) | Tencent Intelligent Image Analysis，TIIA                     | tiia         |
| [数字版权管理](https://cloud.tencent.com/document/api/1000/30698) | Digital Rights  Management，DRM                              | drm          |
| [Elasticsearch Service](https://cloud.tencent.com/document/api/845/30620) | Elasticsearch  Service，ES                                   | es           |
| [样本智能分析平台](https://cloud.tencent.com/document/product/1012)      | -                                | habo         |
| [腾讯知识图谱](https://cloud.tencent.com/document/product/677)             | Tencent  Knowledge Graph，TKG                                | tkgdq        |
| [文本内容安全](https://cloud.tencent.com/document/product/1124/38207) | Text  Moderation System，TMS                                 | tms          |
| [图片内容安全](https://cloud.tencent.com/document/product/1125/38206) | Image  Moderation System，IMS                                | ims          |
| [电子合同服务](https://cloud.tencent.com/document/product/869/17778) | Digital  Contract                                            | ds           |
| [腾讯智学课堂分析](https://cloud.tencent.com/document/product/1059/35988) | Tencent  Classroom Intellisense                              | tci          |
| [活动防刷](https://cloud.tencent.com/document/product/1189)         | - | aa         |
| [借贷反欺诈](https://cloud.tencent.com/document/product/668)         | AntiFraud | af         |
| [定制建模](https://cloud.tencent.com/document/product/1029)         | Anti Fraud Customized | afc        |
| [音频内容检测](https://cloud.tencent.com/document/product/1219)       | Audio Moderation System | ams        |
| [汽车精准获客服务](https://cloud.tencent.com/document/product/1244)     | Automotive Precise Customer Acquisition Service | apcas      |
| [正版图库直通车](https://cloud.tencent.com/document/product/1181)      | Authorized Picture Express | ape        |
| [API 网关](https://cloud.tencent.com/document/product/628)         | API Gateway | apigateway |
| [应用与服务编排工作流](https://cloud.tencent.com/document/product/1272)   | Application Services Workflow | asw        |
| [网站备案](https://cloud.tencent.com/document/product/243)          | - | ba         |
| [人体分析](https://cloud.tencent.com/document/product/1208)         | Body Analysis | bda        |
| [云呼叫中心](https://cloud.tencent.com/document/product/679)         | Cloud Call Center | ccc        |
| [云防火墙](https://cloud.tencent.com/document/product/1132)         | Cloud Firewall | cfw        |
| [智能保险助手](https://cloud.tencent.com/document/product/1368)       | Cloud Intelligent Insurance | cii        |
| [主机安全](https://cloud.tencent.com/document/product/296)          | - | cwp        |
| [云数据库 CynosDB](https://cloud.tencent.com/document/product/1003) | Cloud Native Database TDSQL-C | cynosdb    |
| [游戏玩家匹配](https://cloud.tencent.com/document/product/1294)       | Game Player Matchmaking | gpm        |
| [云游戏解决方案](https://cloud.tencent.com/document/product/1162)      | - | gs         |
| [智能编辑](https://cloud.tencent.com/document/product/1186)         | Intelligent Editing | ie         |
| [智能识图](https://cloud.tencent.com/document/product/1217)         | Intelligent Image Recognition | iir        |
| [图片内容检测](https://cloud.tencent.com/document/product/1125)       | Image Moderation System | ims        |
| [加速物联网套件](https://cloud.tencent.com/document/product/568)       | - | iot        |
| [轻量应用服务器](https://cloud.tencent.com/document/product/1207)      | Lighthouse | lighthouse |
| [登录保护](https://cloud.tencent.com/document/product/1190)         | - | lp         |
| [游戏联机对战引擎](https://cloud.tencent.com/document/product/1038)     | Mobile Game Online Battle Engine | mgobe      |
| [营销价值判断](https://cloud.tencent.com/document/product)            | - | mvj        |
| [流计算服务](https://cloud.tencent.com/document/product/849)         | Oceanus  | oceanus    |
| [全栈式风控引擎](https://cloud.tencent.com/document/product/1343)      | - | rce        |
| [风险探针](https://cloud.tencent.com/document/product/1169)         | - | rkp        |
| [注册保护](https://cloud.tencent.com/document/product/1191)         | - | rp         |
| [邮件推送](https://cloud.tencent.com/document/product/1288)         | Simple Email Service | ses        |
| [智汇零售](https://cloud.tencent.com/document/product)              | - | solar      |
| [态势感知](https://cloud.tencent.com/document/product/664)          | Security Operation Center | ssa        |
| [SSL 证书监控](https://cloud.tencent.com/document/product/1084)     | SSLPod | sslpod     |
| [流量反欺诈](https://cloud.tencent.com/document/product/1031)        | Traffic Anti-Fraud | taf        |
| [腾讯云自动化助手](https://cloud.tencent.com/document/product/1340)     | TencentCloud Automation Tools | tat        |
| [文件检测](https://cloud.tencent.com/document/product)              | - | tav        |
| [腾讯云释义](https://cloud.tencent.com/document/product/1266)        | Tencent Cloud Explanation | tcex       |
| [分布式消息队列](https://cloud.tencent.com/document/product/1179)      | Tencent Distributed Message Queue | tdmq       |
| [智能钛机器学习](https://cloud.tencent.com/document/product)           | - | tia        |
| [腾讯云IaC平台](https://cloud.tencent.com/document/product/1213)     | - | tic        |
| [智能鉴黄](https://cloud.tencent.com/document/product/864)          | - | ticm       |
| [文本内容安全](https://cloud.tencent.com/document/product/1124)       | Text Moderation System | tms        |
| [腾讯微服务观测平台 TSW](https://cloud.tencent.com/document/product/)    | - | tsw        |
| [视频内容安全](https://cloud.tencent.com/document/product/1265)       | Video Moderation System | vm         |
| [语音消息](https://cloud.tencent.com/document/product/1128)         | Voice Message Service | vms        |
| [SSL证书管理服务](https://cloud.tencent.com/document/product)         | - | wss        |
| [珠玑](https://cloud.tencent.com/document/product)                | - | zj         |
| [区块链可信取证](https://cloud.tencent.com/document/product/1259)           | Blockchain Trusted Obtain Evidence，BTOE | btoe             |
| [数据湖计算](https://cloud.tencent.com/document/product/1342)             | Data Lake Compute，DLC | dlc              |
| [DNSPod](https://cloud.tencent.com/document/product/1427)            | DNSPod | dnspod           |
| [物联网智能视频服务（行业版）](https://cloud.tencent.com/document/product/1361)    | Internet of Things Video，IoT Video（Industry Version） | iotvideoindustry |
| [移动网络加速](https://cloud.tencent.com/document/product/1385)            | Mobile Network Acceleration | mna              |
| [医疗报告结构化](https://cloud.tencent.com/document/product/1314)           | Automatic Structuring of Medical Reports | mrs              |
| [私有域解析 Private DNS](https://cloud.tencent.com/document/product/1338) | Private DNS | privatedns       |
| [弹性微服务](https://cloud.tencent.com/document/product/1371)             | Tencent Cloud Elastic Microservice，TEM | tem              |
| [腾讯云微服务引擎](https://cloud.tencent.com/document/product/1364)          | Tencent Cloud Service Engine，TSE | tse              |

## API Explorer
[API Explorer](https://console.cloud.tencent.com/api/explorer) 提供了在线调用、签名验证、 SDK 代码生成和快速检索接口等能力，能显著降低使用云 API 的难度。

