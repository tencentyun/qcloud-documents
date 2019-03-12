## Example: Introduction to JAVA SDK (Windows)

### Environment Dependency
Please ensure that JDK environment has been installed. If not, please download [JDK Installer](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) on the Oracle website and install it;

### Downloading and Configuring CMQ Java SDK
#### How to Use Cloud API Key
When using a Java SDK, the user's Cloud API key is required to verify the validity of the user's identity. Users can log in to [Tencent Cloud Console](https://console.cloud.tencent.com/), then select account name in the top right corner on the navigation bar, and choose "Cloud API Key" in the drop-down box to access the Cloud API key management page.

![](https://mc.qcloudimg.com/static/img/d32aa65f20cfce5af6f30ba5ee792490/capi_1.jpg)

Users can create a new Cloud API key or use an existing key. Click key ID and go to the details page to get the secretId of the key and its corresponding secretKey.
![](https://mc.qcloudimg.com/static/img/37ad47170aaa854767be60213339da88/image.png)

#### endpoint
endpoint is the access address for CMQ service, and it contains the protocol used. endpoint is formatted as follows:

- Private network:` http://cmq-queue-region.api.tencentyun.com`
- Public network: `https://cmq-queue-region.api.qcloud.com`


#### region
"region" needs to be replaced with a specific region: gz (Guangzhou), sh (Shanghai), bj (Beijing). The option of different regions allows users to choose a region nearby to enjoy better services. "region" value in the common parameters should be consistent with that of domain name. For any inconsistency, the request is sent to the region specified by the domain name.

#### Differences Between Private and Public Networks
If the business process is also deployed on a Tencent Cloud CVM submachine, we strongly recommend that you use a private network endpoint in the same region:
1) The latency is lower for a private network in the same region;
2) For now, message queue charges a fee for the downstream traffic of public networks, so using a private network can save the cost.

Public network domain requests support both http and https, while private network domain requests only support http. For instance, if your business process is deployed on a CVM of Tencent Cloud in Beijing, we recommend that you request an endpoint in Beijing for shorter latency, and use a private network for low costs. Thus, a proper endpoint you can select is `http://cmq-queue-bj.api.tencentyun.com`.

#### Downloading JAVA SDK
Download the latest version of [CMQ Java SDK](http://cmqsdk-10016717.cos.myqcloud.com/qc_cmq_java_sdk_V1.0.1.zip), or download a [jar Package](http://cmqsdk-10016717.cos.myqcloud.com/cmq.jar).

If the java source code is used, directly include the source code in the code directory:
![](https://mc.qcloudimg.com/static/img/997a2dcd9ebddadae8d0fcc17ac185a2/3.png)

If the jar package is used, please add cmq.jar package through "property" dialog box - "Java Build Path" - "Libraries".
![](https://mc.qcloudimg.com/static/img/48efa6b553e9023b8bb94d631892d6d2/4.png)

After the jar package is added, the directory will be as follows:
![](https://mc.qcloudimg.com/static/img/a025253000b587bc35eca6bc1904d81c/6.png)

Then you can run the program. If an error code is returned, please refer to the [Error Codes](https://cloud.tencent.com/doc/api/431/5903) for troubleshooting.

### Using CMQ JAVA SDK

The codes below are also samples in Java SDK, demonstrating the whole process of message queue operations including Create a Queue, Get Queue Attributes, Send Messages, Receive Messages, Delete Messages, and Delete a Queue.

```
	import com.qcloud.cmq.*; 
	import java.lang.*;
	import java.util.ArrayList;
	import java.util.List;
	public class 
	{
	public static void main(String[] args) {
	String secretId="";
	String secretKey="";
	String endpoint = "http://cmq-queue-gz.api.qcloud.com";
	String path = "/v2/index.php";
	String method = "POST";
	
    try
    {
		Account account = new Account(endpoint,secretId, secretKey);
		
	
		account.deleteQueue("queue-test10");
		System.out.println("---------------create queue ...---------------");
		QueueMeta meta = new QueueMeta();
		meta.pollingWaitSeconds = 10;
		meta.visibilityTimeout = 10;
		meta.maxMsgSize = 65536;
		meta.msgRetentionSeconds = 345600;
		account.createQueue("queue-test10",meta);
		System.out.println("queue-test10 created");
		account.createQueue("queue-test11",meta);
		System.out.println("queue-test11 created");
		account.createQueue("queue-test12",meta);
		System.out.println("queue-test12 created");
		
		System.out.println("---------------list queue ...---------------");
		ArrayList<String> vtQueue = new ArrayList<String>();
		int totalCount = account.listQueue("",-1,-1,vtQueue);
		System.out.println("totalCount:" + totalCount);
		for(int i=0;i<vtQueue.size();i++)
		{
			System.out.println("queueName:" + vtQueue.get(i));
		}
		
		System.out.println("---------------delete queue ...---------------");
		account.deleteQueue("queue-test11");
		System.out.println("queue-test11 deleted");
		account.deleteQueue("queue-test12");
		System.out.println("queue-test12 deleted");

		System.out.println("--------------- queue[queue-test10] ---------------");
		Queue queue = account.getQueue("queue-test10");
		
		System.out.println("---------------set queue attributes ...---------------");
		QueueMeta meta1 = new QueueMeta();
		meta1.pollingWaitSeconds = 20;
		queue.setQueueAttributes(meta1);
		System.out.println("pollingWaitSeconds=20 set");
		
		System.out.println("---------------get queue attributes ...---------------");
		QueueMeta meta2 = queue.getQueueAttributes();
		System.out.println("maxMsgHeapNum:" + meta2.maxMsgHeapNum);
		System.out.println("pollingWaitSeconds:" + meta2.pollingWaitSeconds);
		System.out.println("visibilityTimeout:" + meta2.visibilityTimeout);
		System.out.println("maxMsgSize:" + meta2.maxMsgSize);
		System.out.println("createTime:" + meta2.createTime);
		System.out.println("lastModifyTime:" + meta2.lastModifyTime);
		System.out.println("activeMsgNum:" + meta2.activeMsgNum);
		System.out.println("inactiveMsgNum:" + meta2.inactiveMsgNum);
		
		System.out.println("---------------send message ...---------------");
		String msgId = queue.sendMessage("hello world,this is cmq sdk for java");
		System.out.println("[hello world,this is cmq sdk for java] sent");
		
		System.out.println("---------------recv message ...---------------");
		Message msg = queue.receiveMessage(10);
		
		System.out.println("msgId:" + msg.msgId);
		System.out.println("msgBody:" + msg.msgBody);
		System.out.println("receiptHandle:" + msg.receiptHandle);
		System.out.println("enqueueTime:" + msg.enqueueTime);
		System.out.println("nextVisibleTime:" + msg.nextVisibleTime);
		System.out.println("firstDequeueTime:" + msg.firstDequeueTime);
		System.out.println("dequeueCount:" + msg.dequeueCount);
		
		System.out.println("---------------delete message ...---------------");
		queue.deleteMessage(msg.receiptHandle);
		System.out.println("receiptHandle:" + msg.receiptHandle +" deleted");
		
		System.out.println("---------------batch send message ...---------------");
		ArrayList<String> vtMsgBody = new ArrayList<String>();
		String msgBody = "hello world,this is cmq sdk for java 1";
		vtMsgBody.add(msgBody);
		msgBody = "hello world,this is cmq sdk for java 2";
		vtMsgBody.add(msgBody);
		msgBody = "hello world,this is cmq sdk for java 3";
		vtMsgBody.add(msgBody);
		List<String> vtMsgId = queue.batchSendMessage(vtMsgBody);
		for(int i=0;i<vtMsgBody.size();i++)
			System.out.println("[" + vtMsgBody.get(i) + "] sent");	
		for(int i=0;i<vtMsgId.size();i++)
			System.out.println("msgId:" + vtMsgId.get(i));
		
		ArrayList<String> vtReceiptHandle = new ArrayList<String>();
		System.out.println("---------------batch recv message ...---------------");
		List<Message> msgList = queue.batchReceiveMessage(10,10);
		System.out.println("recv msg count:" + msgList.size());
		for(int i=0;i<msgList.size();i++)
		{
			Message msg1 = msgList.get(i);
			System.out.println("msgId:" + msg1.msgId);
			System.out.println("msgBody:" + msg1.msgBody);
			System.out.println("receiptHandle:" + msg1.receiptHandle);
			System.out.println("enqueueTime:" + msg1.enqueueTime);
			System.out.println("nextVisibleTime:" + msg1.nextVisibleTime);
			System.out.println("firstDequeueTime:" + msg1.firstDequeueTime);
			System.out.println("dequeueCount:" + msg1.dequeueCount);
			
			vtReceiptHandle.add(msg1.receiptHandle);
		}
		
		queue.batchDeleteMessage(vtReceiptHandle);
		System.out.println("---------------batch delete message ...---------------");
		for(int i=0;i<vtReceiptHandle.size();i++)
			System.out.println("receiptHandle:" + vtReceiptHandle.get(i) + " deleted");

    }
    catch(CMQServerException e1){
        System.out.println("Server Exception, " + e1.toString());
    } catch(CMQClientException e2){
        System.out.println("Client Exception, " + e2.toString());
    }
	catch (Exception e) {
			System.out.println("error..." + e.toString());
	}
	}
	} 
```
