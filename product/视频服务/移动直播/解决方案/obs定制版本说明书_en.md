## OBS Feature Description

Please download [OBS Studio](http://dldir1.qq.com/hudongzhibo/xiaozhibo/obs_distribute_question.zip) modified by Tencent Cloud. This customized OBS is mainly used in Chongding Quiz mode. For specific technical document, please see solution 1 of [LVB Quiz (Chongding Mode)](https://cloud.tencent.com/document/product/454/13863).

**Demo effect**
![](https://mc.qcloudimg.com/static/img/c33ead292783bd4061ef069665b78a38/capture.gif)

## What to do?

- Understand and learn how to use this customized OBS for question assignment, which is the main content of this document. Two modes are available: the local quiz file mode and the server transparent transmission mode.
- Build a quiz system to collect and process users' quiz requests.
- Add the corresponding HTTP server API to your quiz system to communicate with our customized OBS. In this way, you can not only assign questions, but also deliver answers in real time with our customized OBS. In addition, the transparent transmission of custom messages is supported as well.

## How to push?
Instructions on OBS will not be discussed here, but the following should be noted:
- **1. Enter a push URL as follows:**
    For example, here is a legal push URL:`rtmp://3891.livepush.myqcloud.com/live/3891_rexchang?bizid=3891&txSecret=d436dc53e5ab06a12313c736f7d533c91&txTime=5A6B507F`
    ![](https://mc.qcloudimg.com/static/img/5c132c243e2659befd69cae4537aead6/image.jpg)

- **2. Set GOP (with the interval of I frame) to 1**
  ![](https://mc.qcloudimg.com/static/img/204d041289f535ef9355ca8b45780e5d/image.jpg)

- **3. Select economic and suitable encoding parameters**
  ![](https://mc.qcloudimg.com/static/img/3c4a53b596e1663b5d12e4779922045a/image.jpg)
  ![](https://mc.qcloudimg.com/static/img/2516df29225a4e13db1c0a217dc0996c/image.jpg)

| Recommended Configuration | Resolution | Video Bitrate | Frame Rate | Number of Channels | Sampling Rate | Audio Bitrate |
| ------ | ------- | -------- | ---- | ---- | ---- | ------ |
| Image quality priority | 540x960 | 1,000 Kbps | 25 | 1 | 48k | 72 Kbps |
| Cost priority | 360x640 | 600 Kbps | 20 | 1 | 48k | 72 Kbps |

## How to configure server?
We have added the **"Question Assignment"** button to the **"Tools"** menu bar in OBS. Click this button and select the **Server Configuration** tab to set your server address:
![](https://mc.qcloudimg.com/static/img/912ebc5bf4ac55cd2bce8aa9cee5f1ba/server.jpg)
After clicking **Save Configuration**, a config.ini file is generated in the running directory of obs32.exe to store the corresponding configuration, which is directly read for the next run.

```
[config]
distributeInterval=0
distributeNum=1
server=http://jww.qcloud.com/dabaa
```
## How to use the local quiz file mode?
- **How to assign a question?**
  Select the **"Local Quiz File"** tab to load the ini file for quiz.
  Questions can be edited beforehand in the ini file which must be UTF-8-encoded in the following format:

  ```
    [1] 
    question="Which Summer Olympic Games was held in Beijing in 2008?"
    answer_1="29"
    answer_2="30"
    answer_3="31"

    [2]
    question="Which letter follows S in the English alphabet?"
    answer_1="R"
    answer_2="T"
    answer_3="X"
  ```

  The content is displayed in the following figure after loading:
  ![](https://mc.qcloudimg.com/static/img/f2ae42fdbb886d85c7404755bc836018/ini.jpg)
  In live scenarios, the host reads a question according to the cue card. The program director in the studio is responsible for selecting a specified question. After clicking the **"Assign Question"** button in OBS, the selected question is transmitted into the audio/video stream.
  The specific transmission format is:

  ```
  {
  "id" = "1",
  "question": "Which Summer Olympic Games was held in Beijing in 2008?"
  "answer_1": "29",
  "answer_2": "30",
  "answer_3": "31"
  }
  ```
- **How to deliver an answer?**
  Due to Tencent Cloud's PAAS positioning, we will not actually implement the quiz system which should be implemented by your business backend. In this case, how does our customized OBS deliver the answer to each question to viewers?
  Your server needs to provide an HTTP API, and then communicates with OBS in terms of questions, answers and the number of people in the specified json format, so as to deliver questions and answers smoothly.
  In live scenarios, to deliver an answer to the viewer end, the program director needs to select the specified question and click the **"Answer"** button, and then the customized OBS will send the following HTTP GET request ("/subject/statics/1" is constructed by OBS, where 1 is the question ID) to your server.

  ```
  GET http://jww.qcloud.com/dabaa/subject/statics/1 HTTP/1.1
  ```

  We expect that your server can deliver answers to OBS in the following format:

  ```
  {
    "id": 1,
    "answer_1": 2334,
    "answer_2": 345,
    "answer_3": 89,
    "conrrect_index": 1
  }
  ```

  However, you can also customize answers, because our customized OBS only inserts the json message returned from the server into the audio/video stream, instead of resolving any content.

- **How to use a custom message?**

  You are allowed to send custom messages to the viewer end. After you select a specified question and click the **Custom Message** button, the customized OBS will send the following HTTP GET request ("/subject/custom/1" is constructed by OBS, where 1 is the question ID) to your server.

  ```
  GET http://jww.qcloud.com/dabaa/subject/custom/1 HTTP/1.1
  ```

  If your custom message is irrelevant to the question ID, you can click the **Custom Message** button without selecting any question. We will send the following HTTP GET request to your server with the question ID replaced with 0.	

  ```
  GET http://jww.qcloud.com/dabaa/subject/custom/0 HTTP/1.1
  ```

  The json message returned from the server will be inserted into the audio/video stream.

## How to use the server transparent transmission mode?
In this mode, the local quiz ini file is not required. The questions are sent after they have been pulled from your server by our customized OBS.

- **How to assign a question?**

  Select the **"Server Configuration"** tab, and **Server Transparent Transmission** is shown as below:

  ![](https://mc.qcloudimg.com/static/img/73e7af835f437a3c70565d55c50befe4/servermode.jpg)

  This mode must be supported by your HTTP server. In live scenarios, to assign a question to the viewer end, the program director needs to adjust only the value of the question ID and click the **"Assign Question"** button, and then the customized OBS will send the following HTTP GET request ("/subject/question/1" is constructed by OBS, where 1 is the ID of the question) to your server.

  ```
  GET http://jww.qcloud.com/dabaa/subject/question/1 HTTP/1.1
  ```

  You can also customize questions, because our customized OBS only inserts the json message returned from the server into the audio/video stream, instead of resolving any content.


- **How to deliver an answer?**

  The server transparent transmission mode is similar to the local quiz file mode. The only difference is that in the server transparent transmission mode, you do not need to select any specified question, but to make sure the value of the question ID is correct. After clicking the **"Answer"** button, the customized OBS will send the following HTTP GET request ("/subject/statics/1" is constructed by OBS, where 1 is the question) to your server.

  ```
  GET http://jww.qcloud.com/dabaa/subject/statics/1 HTTP/1.1
  ```

  The json message returned from the server will be inserted into the audio/video stream.



- **How to use a custom message?**

  The server transparent transmission mode is similar to the local quiz file mode. The only difference is that in the server transparent transmission mode, you do not need to select any specified question, but to make sure the value of the question ID is correct. After clicking the **"Custom Message"** button, the customized OBS will send the following HTTP GET request ("/subject/custom/1" is constructed by OBS, where 1 is the question) to your server.

  ```
  GET http://jww.qcloud.com/dabaa/subject/custom/1 HTTP/1.1
  ```

  The json message returned from the server will be inserted into the audio/video stream.
  If your custom message is irrelevant to the question ID, you can ignore this ID field after receiving a request.

## How does the APP end receive a question?

Please see our connection documents ([iOS Platform](https://cloud.tencent.com/document/product/454/7880#Message) | [Android Platform](https://cloud.tencent.com/document/product/454/7886#Message)).

## Is it reliable to place questions in the audio/video stream?

The customized OBS is primarily designed to insert questions into the audio/video stream. However, is it a problem in case of audio/video stutters?
In fact, it is a problem. Like the process of fertilization, the solution is to insert the same question into the audio/video stream evenly on a regular basis. The question can always be delivered to the viewer end only if stutters do not sustained.
![](https://mc.qcloudimg.com/static/img/3ef35d5f920c7231127128d504775f23/interval.jpg)

 The configurations in the above figure include a specific interval (in ms) at which a question is delivered and a total number of times that this question is delivered. The recommended configuration is "500 ms + 6 times".
 If this solution is adopted, it is required to **eliminate repetitions** at the App end to prevent the same question from being displayed repeatedly.

