
本文将为您介绍如何接入水印 SDK，本文主要包括 Android、iOS 和 Windows 三个版本的接入指南。
## SDK 准备
下载相关 [Demo 及 SDK](https://main.qcloudimg.com/raw/5066e0eda60b0e00c9e78e0acfa7ec55/%E6%B0%B4%E5%8D%B0SDK.zip)。

## Android 接入
### 预备工作
- 接入 SDK 需要完成以下步骤：
 1. 根据运行平台选择相应的 so 文件，将 so 文件和 jar 文件拷贝到工程目录下并添加依赖。
 2. 调用 SDK 接口函数，生成水印信息。
 3. 发送报文时，将20字节水印信息放在消息体前面。
- SDK 文件包含 so 文件和 jar 文件，目录结构如下：
![](https://main.qcloudimg.com/raw/3936cbb5a6ec5a9e21ad75a12f0ad8e4.png)
- SDK API 说明：
 - 程序包：com.gamesec
 - 类：Mark
- 接口说明：
<table>
<tbody>
<tr>
<th>接口名称</th>
<th>说明</th></tr>
<tr>
<td>CreateSDKBuffFromStr</td>
<td>生成水印</td></tr></tbody></table>

### 接入步骤（Android Studio）
1. 将 sdk/android 文件夹下的内容拷贝到工程目录的 libs 文件夹下：
 ![](https://main.qcloudimg.com/raw/0ca7cbe946a4d8eee2b2ca0cd4e3c808.png)
2. 修改项目的 build.gradle 文件，设置 jni 文件目录，添加 jar 依赖：
```
android {
		sourceSets {
				main {
						jniLibs.srcDirs =['libs/jni'] // 设置 jni 目录
					 }
				   }
			}
		dependencies {
						implementation files('libs/gamesec.jar') // 添加依赖
				     }
```
3. Eclipse 接入方法类似，不需要配置 build.gradle 文件。

### 接口调用
1. 导入程序包。
```
import com.gamesec.*;
```
2. 实例化 Mark 对象。
```
Mark mark = new Mark();
```
3. 调用 CreateSDKBuffFromStr 生成水印。
```
byte [ ] CreateSDKBuffFromStr (String pSDKinfo, String buffer, String uDesIp, int uDesPort)
```
 - **参数说明：**
<table>
<tr>
<th>参数</th>
<th>类型</th>
<th>含义</th>
</tr>
<tr>
<td>pSDKinfo</td>
<td>String</td>
<td>水印防护密钥</td>
</tr>
<tr>
<td>buffer</td>
<td>String</td>
<td>占位参数，传入空字符串即可</td>
</tr>
<tr>
<td>uDeslp</td>
<td>String</td>
<td>服务器 IP，如 “1.2.3.4”</td>
</tr>
<tr>
<td>uDesPort</td>
<td>int</td>
<td>服务器端口</td>
</tr>
</table>
 - **返回值：**
<table>
<tr>
<th>类型</th>
<th>含义</th>
</tr>
<tr>
<td>byte[]</td>
<td>计算的水印信息，取20字节</td>
</tr>
</table>
 - **调用示例：**
```
String pSDKinfo = "566c2dea9420eb37-b6c8-566c2dea9420eb3710525135e8485e80806a2f9c";
String uDesIp = "115.159.147.198";
int uDesPort = 8899 ;
byte[] bytes = mark.CreateSDKBuffFromStr(pSDKinfo, "", uDesIp, uDesPort);
```

4. 添加水印信息到消息体。代码示例如下：
```
Socket s = new Socket(uDesIp, uDesPort);
OutputStream out = s.getOutputStream();
PrintWriter output = new PrintWriter(out, true);
// 先传入水印信息
output.print(bytes); 
output.println("msg msg msg");
BufferedReader input = new BufferedReader(new InputStreamReader(s.getInputStream()));
String msg = input.readLine();
s.close();
```

## iOS 接入
### 预备工作
- 接入 SDK 需要完成以下步骤：
	1. 将 SDK 文件拷贝到工程目录，Swift 工程需要添加桥文件。
	2. 调用 SDK 接口函数，生成水印信息。
	3. 发送报文时，将 20 字节水印信息放在消息体前面。
- SDK 文件包含 a 文件和 h 文件，目录结构如下：
 ![](https://main.qcloudimg.com/raw/11c1012406344128256a363e593bb2ec.png)
- 接口说明：
<table>
<tbody>
<tr>
<th>接口名称</th>
<th>说明</th></tr>
<tr>
<td>CreateSDKBuffFromStr</td>
<td>生成水印</td></tr></tbody></table>

### 接入步骤（Xcode）
1. 将 sdk/ios 文件夹下的内容拷贝到工程目录：
![](https://main.qcloudimg.com/raw/4ab142c35d9d85b6365e9eecce5f66d8.png)
2. 将 SDK 文件添加到 Xcode。右键工程名，单击 “Add Files to”。
![](https://main.qcloudimg.com/raw/babb1d9440fc75f8f79eca4efa007dfe.png)
3. 在对话框中勾选 “Create folder references”，选中 SDK 的两个文件，单击 **Add**。
![](https://main.qcloudimg.com/raw/bb83314a0468f9cc189bb36268ca2853.png)
4. 左键工程名，选择 General，将 a 文件添加到 “Linked Framews and Libraries”：
![](https://main.qcloudimg.com/raw/286f35e15a6e269b62f489fd9c838904.png)
5. 如果是 Swift 项目，需要创建桥文件，Object-C 项目可以跳过此步骤。创建一个 Header File，命名为 bridge.h。并在文件中添加以下代码：
			# import "gamesec.h";
6. 左键工程名，选择 Build Settings，将 bridge.h 添加到 Object-C Bridging Header 中：
![](https://main.qcloudimg.com/raw/d5c8dec743f6743fafae2e932c44163f.png)

### 接口调用
1. Swift 项目可以直接调用生成水印函数，Object-C 项目需要在使用的文件里面添加头文件：
```
# import "gamesec.h";
```
2. 调用 CreateSDKBuffFromStr 生成水印。
```
uint32_t CreateSDKBuffFromStr(char *pSDKinfo, uint8_t *buffer, char* uDstIp, uint16_tuDstPort);
```
**参数说明：**
<table>
<tr>
<th>参数</th>
<th>类型</th>
<th>含义</th>
</tr>
<tr>
<td>pSDKinfo</td>
<td>char *</td>
<td>水印防护密钥</td>
</tr>
<tr>
<td>buffer</td>
<td>uint8_t *</td>
<td>水印指针，输出水印结果</td>
</tr>
<tr>
<td>uDeslp</td>
<td>char *</td>
<td>服务器 IP，如 “1.2.3.4”</td>
</tr>
<tr>
<td>uDesPort</td>
<td>uint16_t</td>
<td>服务器端口</td>
</tr>
</table>
 
 >!水印结果保存在参数 buffer 中，取20字节。
3. 调用示例。
**Swift 调用：**
```
	let pSDKinfo = UnsafeMutablePointer<Int8>(mutating: (
			"566c2dea9420eb37-b6c8-566c2dea9420eb3710525135e8485e80806a2f9c" 
			as NSString).utf8String);
					var buffer = UnsafeMutablePointer<UInt8>.allocate(capacity: 20);
			let uDstIp = UnsafeMutablePointer<Int8>(mutating: (
			"115.159.147.198" as NSString).utf8String);
					let uDstport = UInt16.init("8899")!;

			CreateSDKBuffFromStr(pSDKinfo, buffer, uDstIp, uDstport);

					for i in 0 ..< 20 {
							let b = (buffer+i).pointee;
							// 水印信息在前20字节，注意这里输出的是 uint8
							print(" \(b)");
					}
**Object-C 调用：** 

			char *pSDKinfo = "566c2dea9420eb37-b6c8-566c2dea9420eb3710525135e8485e80806a2f9c";
					uint8_t buffer[20];
					char *uDstIp = "115.159.147.198";
					uint16_t uDstPort = 8899;

					CreateSDKBuffFromStr(pSDKinfo, buffer, uDstIp, uDstPort);

					for(int i=0;i<20;i++)
			{
					// 水印信息在前20字节
							NSLog(@"%d", (int8_t)buffer[i]); 
			}
```
4. 发送报文前，添加 20 字节水印信息到消息体前面。

## Windows 接入
### 预备工作
SDK 为 gamesec.dll 文件，有一个生成水印的函数：
```
uint32_t CreateSDKBuffFromStr(char *pSDKinfo, uint8_t *buffer, char* uDstIp, uint16_t uDstPort);
```
**参数说明：**
<table>
<tr>
<th>参数</th>
<th>类型</th>
<th>含义</th>
</tr>
<tr>
<td>pSDKinfo</td>
<td>char *</td>
<td>水印防护密钥</td>
</tr>
<tr>
<td>buffer</td>
<td>uint8_t *</td>
<td>水印指针，输出水印结果</td>
</tr>
<tr>
<td>uDeslp</td>
<td>char *</td>
<td>服务器 IP，如 “1.2.3.4”</td>
</tr>
<tr>
<td>uDesPort</td>
<td>uint16_t</td>
<td>服务器端口</td>
</tr>
</table>

 >!水印结果保存在参数 buffer 中，取20字节。


### 接口调用
在使用水印函数时，需先导入 dll 文件，可以使用 LoadLibrary 函数（需要添加 Windows.h ）：
```
 // 定义函数指针
    typedef int(*FUNC)(char *, uint8_t *, char* , uint16_t );
    // 设置 dll 路径
    HINSTANCE Hint = ::LoadLibrary(L"E:\\sdk\\gamesec.dll");
    FUNC CreateSDKBuffFromStr = (FUNC)GetProcAddress(Hint, "CreateSDKBuffFromStr");
```
完整调用示例：
```
 // 保存水印
    uint8_t buffer[BUFFER_SIZE];
    memset(buffer, 0, BUFFER_SIZE);
    
    int UDP_TEST_PORT = 8899;
    
    const char * CONST_UDP_SERVER_IP  = "115.159.147.198";
    char * UDP_SERVER_IP = new char[strlen(CONST_UDP_SERVER_IP)];
    strcpy(UDP_SERVER_IP, CONST_UDP_SERVER_IP);
    
    const char * CONST_pSDKinfo = 
    "566c2dea9420eb37-b6c8-566c2dea9420eb3710525135e8485e80806a2f9c";
    char * pSDKinfo = new char[strlen(CONST_pSDKinfo)];
    strcpy(pSDKinfo, CONST_pSDKinfo);
    
    // 调用10次
    for (int i = 0; i < 5; i++) {
    CreateSDKBuffFromStr(pSDKinfo, buffer, (char *)UDP_SERVER_IP, UDP_TEST_PORT);
    
    for (int i = 0; i <= 20; i++)
    {
    // 水印在前20字节
    printf("%d ", (int8_t)buffer[i]);
    }
    printf("\n\n");
    }
```
