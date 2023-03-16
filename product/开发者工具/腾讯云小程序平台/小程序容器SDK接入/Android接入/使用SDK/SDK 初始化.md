## 调试
1. 通过关键字 TMF_MINI 过滤得到 SDK 日志


   ![raw](https://write-document-release-1258344699.cos.ap-guangzhou.tencentcos.cn/100026263612/a31a0b78b8e711ed9e14525400088f3a.png?q-sign-algorithm=sha1&q-ak=AKIDLqn3DWFzCJq0j014BoVMyeTlcQhdcHtYTk_iFJzLjp5URyFlYjHRVZDnmth-t6xp&q-sign-time=1678688676;1678692276&q-key-time=1678688676;1678692276&q-header-list=&q-url-param-list=&q-signature=ee1b71625934f26d0bfde24b837024f545328b92&x-cos-security-token=5qJ7cubgkNU53ncrOzOtkv478OD7pUjae6713371ac202897f1c9c5caa50e4564Y51bK3q3b9-GLry9lxRQZqVnxW2sokvYu4HUvMUxGk3ZBzvtOsOTIQYHArq-wJubh6ZZlLH3Bz4CwddfjDdTtxyjseWPDSYGVQD6dsGFe20Jjv8kAUWfuSJ3M1HeMzfBPTzZCH27ccinh9LfSWrLcSBiqOECVXyz4H8XgM79dibFCJ-Imo-uNJeVZrTb99sb37ye4cYntTWHOFssVsXMVnq7WFA3kJ_n6dWIzNM4xkPen_GZEbljwszMdECEbtRSIrmFSPnJxu9EpZiAWTuDhk09IxcOpxu61JI6-Rcl5CxHLzVRYsEDY0xQzstnRK67ZOG3uL622LwkwU_NLnd73JozR_P2of3DCAxOIi1wRJsafBg2mmAs1iD98MdS6DVi)

2. 查看小程序 JS 错误日志


   方式一：通过关键字 MINI_JS_LOG 过滤得到JS日志。


   ![raw](https://write-document-release-1258344699.cos.ap-guangzhou.tencentcos.cn/100026263612/b66b5fc5b8e711ed9e14525400088f3a.png?q-sign-algorithm=sha1&q-ak=AKIDgEzNkBpfFw6TS6f7uDBihqxXAxD7bPcYA1R76ZuWnilWpA3fY1lUhbya5BvOdY7W&q-sign-time=1678688676;1678692276&q-key-time=1678688676;1678692276&q-header-list=&q-url-param-list=&q-signature=d9ea0b81a0c35ea6d5a9bebff520c36168e55d75&x-cos-security-token=5qJ7cubgkNU53ncrOzOtkv478OD7pUjaa59ee0721d6c62488c886432178ffac4Y51bK3q3b9-GLry9lxRQZqVnxW2sokvYu4HUvMUxGk3ZBzvtOsOTIQYHArq-wJubh6ZZlLH3Bz4CwddfjDdTtxyjseWPDSYGVQD6dsGFe20Jjv8kAUWfuSJ3M1HeMzfBPTzZCH27ccinh9LfSWrLcSBiqOECVXyz4H8XgM79dibFCJ-Imo-uNJeVZrTb99sblMNfnKFpPBqk4gRsQ6qXDxGMgTl-GI1rNQOnNeFGpkI5xZVwwVIxu71bvdCgU9F2AaWCvUrLlSBAgoSDbrsDhBoLqZOFS9M2WRiONiWd7sLUK668sVoGfate6M4ord2o2WuJn-WvjViWfLNMm3cAWlPaPOdsnpaTL05QZcS7HDDbtIMfNjSQLtm90Jta25HQ)


   方式二：chrome 调试小程序的 JS 是否有错误。


   ![raw](https://write-document-release-1258344699.cos.ap-guangzhou.tencentcos.cn/100026263612/0f5cb3acb8e811eda534525400c56988.png?q-sign-algorithm=sha1&q-ak=AKIDQ0HGVB2hQnQywzq0LeW8YJ6LHx39hjDOBNoI0346cD9aiceuz-QjAL5eMbiS0b2L&q-sign-time=1678688676;1678692276&q-key-time=1678688676;1678692276&q-header-list=&q-url-param-list=&q-signature=7f20a42eb94a3997f24d9a28899cd73356c2cfe5&x-cos-security-token=BR3002b2U42565JB60a8L0hq41GHy34a3cfbe9ec664f2a8e60b79ea6b5ee0c7eG8tPB46LUesAR5gr3Dui3h15B216KTFA68MLMNYzrcrFuDBs2DmvoPZWUc0ONDlsunCovkszhGIM2uvMkgARi_z5x8GnMZyFu97nElxc_rXQisHkIj4gfKjo7U16u6aRuc14V_62skNhJhyMSc_S0EDZ86fM1xFEygWhgyxoELHnAjbzyb_UrpLHDLTacVHRouLBQJ11Q74uSY710N0gznOSG-fE4Po8vvWiZ2F0HMnRksES-xFHa3nm-rK8YvCzjb9_8QkEwV9oXnyUGJVZbP42OygaFPj30iELh7DcazeynRL-dg4Fw4te1wpVdWfAOdRMTEPQW3j23mu_cB5aM6tkZUNPI0o20uPxKApwOOiW-bvear9VNjH1HDAGzUvM)


## SDK 初始化

### 配置文件获取

开发人员从开放平台获取对应 App 的配置文件，该配置文件是一个 json 文件，包含该 App 使用小程序平台的所有信息，将配置文件引入到项目的 assets 根目录。

![raw](https://write-document-release-1258344699.cos.ap-guangzhou.tencentcos.cn/100026263612/79b360b9b8e811ed9e14525400088f3a.png?q-sign-algorithm=sha1&q-ak=AKIDeo_nwrwrliz5D7tTW7gGWHpFsuSaIupQy9sWk0p54XzZAFyQ2iVuHoCKjdErB0b5&q-sign-time=1678688676;1678692276&q-key-time=1678688676;1678692276&q-header-list=&q-url-param-list=&q-signature=db9dc580df6338c7faad2671830d77f64e10460b&x-cos-security-token=5qJ7cubgkNU53ncrOzOtkv478OD7pUjafe7684a2848d8871cc4fdd94eb7763a8Y51bK3q3b9-GLry9lxRQZqVnxW2sokvYu4HUvMUxGk3ZBzvtOsOTIQYHArq-wJubh6ZZlLH3Bz4CwddfjDdTtxyjseWPDSYGVQD6dsGFe20Jjv8kAUWfuSJ3M1HeMzfBPTzZCH27ccinh9LfSWrLcSBiqOECVXyz4H8XgM79dibFCJ-Imo-uNJeVZrTb99sbTe3ndM3MkgM5e-B4WeTfRQydaWMG0E5fYLGlB2PnuBXPI1Mq-U38ikUwindj3hi-HHX9HYutrzhX8aLRaTTe8txEE3kn9aHhj7ocSbPhuT0fX-PjMU3hv_JUzcySfrJ5FeUbLJAeEriLhMtKo--MXd1RR4Zp8P26n3a7DtgD45CeHe17CA0-0rTa7UrZI2pj)

> **注意：**
> 

> 配置文件中的 packageName 必须与应用的包名保持一直，否则 App 运行失败
> 


![raw](https://write-document-release-1258344699.cos.ap-guangzhou.tencentcos.cn/100026263612/8c63cc45b8e811ed9e14525400088f3a.png?q-sign-algorithm=sha1&q-ak=AKIDZ7HbNRncu6WYENUPqVIeLXEwBxbySObrR6TJosfB9CHCr0xeR1znp7DbqxgiZk9Z&q-sign-time=1678688676;1678692276&q-key-time=1678688676;1678692276&q-header-list=&q-url-param-list=&q-signature=5259eaed3cfab1d858ea0b019afeb0e19a366185&x-cos-security-token=Utt7i7mFjfHWFST1Em7Vk3vRxoPea3wa5a2730e11da144225e10b2427ababec5vZX1j-FEnlF2QOemjs_RAqrdumohYJyZVpRQZbZzr5SeR9STICeOOYaC0yJcqdDOAZ9OVMSoWARKoV2uFvxdzvCDeY3VWFwufksvqAvuJPquEw_4qZrNCI0UOgp8whjdhjmHYjKiBW1Lj-WyjfMai6I0ms8jYKQGE8V5ndS4JYZm7KXyZRcC0-N7f7p5w_gdwgp-VSZvx5_YanWf3_iIgujWhYbCmRR0f1S_fu1bNRiWl0r7gmrLpbt7phRxTiISkhCTKuL3A-CTbjXix2LzipkSftPerJoXYgmGvERsR8gS8noHcjBIwdYdxpMDU_V_6ksliJK8ZwfggFnDfYLYINTWg_DcMu6BRt4WVsHGFcDnzmjqHO2VaWnttfIZ3ftQ)

### 配置信息设置

根据配置文件初始化一下MiniInitConfig对象，并使用MiniInitConfig初始化TMF小程序引擎。

参考代码：
``` html
MiniInitConfig.Builder builder = new MiniInitConfig.Builder();
MiniInitConfig config = builder
        .configAssetName("TMF_CONFIGURATIONS")//assets中配置文件名称        
        .imei("IMEI");////配置设备id，⽤于在管理平台上根据设备标识进⾏⼩程序的灰度发布使⽤(可选)        
        .build();
TmfMiniSDK.init(application, config);
```

> **说明：**
> 

> TmfMiniSDK.init 初始化需要在 Application 中初始化。
> 


### 其它初始化动作

设置地区或者账号，方便进行灰度推送时使用。
``` html
/** * 设置账号信息
 * @param userId
  */
public static void setUserId(String userId)
    /**
     * 设置位置信息
     * @param country 
     * @param province 
     * @param city 
     */public static void setLocation(String country, String province, String city)
```

