Video processing has the following characteristics:

- **Many Input Parameters**: There may exist many input parameters for a single video processing operation. If all the parameters need to be carried for each video processing operation, the API calling must be very complicated. For example, there are dozens of control parameters for the transcoding operation.
- **Various Types of Processing**: There may exist many different processing methods for the same video. If each operation requires a separate API to call, then the access process for developers must be very complicated. For example, the same video may be transcoded in three ways such as standard definition, high definition, and super definition, and then screencapped for image sprites.
- **Complex Processing Flow**: Dependencies may exist between different processing operations on the same video. If only an atomized video processing API is provided, then the developer needs to rely on the video processing callback for logic decisions. For example, the number of transcoding channels is decided according to the original video bitrate, and whether transcoding is required is decided according to the porn detection results.

[Parameter templates](#.E5.8F.82.E6.95.B0.E6.A8.A1.E6.9D.BF) and [task flows](#.E4.BB.BB.E5.8A.A1.E6.B5.81) are exactly the solutions of the VOD system for above video processing issues. Among them, the parameter templates deal with the first issue, and the task flow the rest two.

The relationship between parameters, templates, and task flows is shown in the following figure:
![Parameters - Templates - Task Flows](//mc.qcloudimg.com/static/img/06cc3e175e8fce4ae44b68c6fb3173c4/image.png)

## Parameter Template

The so-called parameter template is a template (or parameter container) in which multiple video processing parameters are encapsulated. Each template is assigned with an ID. During the video processing, a set of video processing parameters can be represented by one template ID.

The VOD system provides pre-defined parameter templates, and also allows developers to customize their parameter templates. Please see:

- [Transcoding Template](https://cloud.tencent.com/document/product/266/11701#.E8.BD.AC.E7.A0.81.E6.A8.A1.E6.9D.BF)
- [Re-wrapping Template](https://cloud.tencent.com/document/product/266/11701#.E8.A7.86.E9.A2.91.E8.BD.AC.E5.B0.81.E8.A3.85)
- [Watermark Template](https://cloud.tencent.com/document/product/266/11701#.E6.B0.B4.E5.8D.B0.E6.A8.A1.E6.9D.BF)
- [Templates for Capturing Screenshots at Specified Time](https://cloud.tencent.com/document/product/266/11702#.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)
- [Template for Sampling Screenshot](https://cloud.tencent.com/document/product/266/11702#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)
- [Image Sprite Screenshot Template](https://cloud.tencent.com/document/product/266/11702#.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF)
- [Video Encryption Template](/document/product/266/9645)

## Task Flow

The parameter template implements the parameter encapsulation of **single** video processing operation, while the task flow implements the integration of **a group of** video processing operations based on the parameter template.

- The task flow divides the processing of a single video into a series of serial **stages** (as shown in the following figure).
- Each stage contains a set of **sub-tasks**, each of which is responsible for only one atomized video processing operation, and the sub-tasks within the same stage can be executed concurrently.
- Developers can define and control which subtasks are fixedly executed at each stage, thus to achieve the programmatic control of the video processing flow, that is, to decide video processing operations in next stage according to the processing result of the previous stage.

![Each Stage of Task Flow](//mc.qcloudimg.com/static/img/6319b1a7d78997d4585e86436d6cdcb8/image.png)

The task flow can be seen essentially as a configuration or script that describes how to handle a set of video. The VOD system provides two types of task flow configurations:
- [**JSON Task Flow**](#json.E4.BB.BB.E5.8A.A1.E6.B5.81): It describes what processing operations are involved in each phase of video processing in JSON configuration, and does not accept additional input parameters. It is suitable for the video processing with fixed process and no conditional branch. For example, all videos are transcoded in three ways such as standard definition, high definition, and super definition, and then screencapped for image sprites.
- [**Lua Task Flow**](#lua.E4.BB.BB.E5.8A.A1.E6.B5.81): It describes which video processing operations are performed at each stage in the Lua scripts, and can accept additional input parameters; with the Lua's powerful logic expression ability, the video processing logic can have conditional branches. For example, SD transcoding is performed only on videos with bitrate higher than 512 kbps.

### Task Flow Template

For a JSON task flow, the content of the task flow is a piece of JSON configuration, and a piece of Lua code for a Lua task flow.

For usability and security purposes, the VOD system introduces the concept of task flow template. Specifically, a short string is used as the template name, and the template content is either JSON configuration or Lua code. When processing videos by using task streams, you need to specify the name of task flow template rather than its content.

At present, the VOD system temporarily does not support self-configuration of task flow template. If you need to customize the task flow template, please submit a ticket.


<!-- 

The VOD system provides a set of server APIs to manage task flows:

- Create a task flow template;
- Update the task flow template;
- Query the task flow template list and details;
- Delete the task flow template.

> Note:
> - For security reasons, the VOD system temporarily does not support the developer-defined Lua task flow templates. -->

### JSON Task Flow 

JSON task flow describes what operations are involved in each phase of video processing in JSON configuration, which is the most simple and direct method for video processing logic arrangement.

<!-- See: Reference for JSON Task Flow Template.

TODO-leckie: Complete hyperlinks. -->

### Lua Task Flow

The Lua task flow describes which video processing operations are performed at each stage in the Lua 5.1 scripting language, and can accept additional input parameters.

> Note:
> - For Lua 5.1, you can refer to: [Lua 5.1 Reference Manual (English Version)](https://www.lua.org/manual/5.1/), or [Lua 5.1 Reference Manual (Chinese Version)](https://www.codingnow.com/2000/download/lua_manual.html).

Assuming a certain Lua task flow has the name `MyFirstProcedure`, and its content is as below:


```lua
------------------------------------------
--- Lua task flow sample code with template name:MyFirstProcedure
------------------------------------------

-- Define the task flow processing class
VodProcedure = NewProcedureClass()

-- Define the constructor
function VodProcedure:constructor()
    -- ...
end

-- Define the operations at video processing stage
function VodProcedure:handleProcess()
    -- The collection of video processing operations at this stage
    local processActionSet = ProcessActionSet:new()

    -- Transcoding operations
    local transcodeAction = TranscodeAction:new()

    -- Transcoding operations
    -- ...

    processActionSet:addAction(transcodeAction)
    return processActionSet
end

-- The operations at other stages of task flow
-- ...

-- The entry point function of task flow, which supports for entering one parameter - the priority of the task
function CreateProcedure(priority)
    local procedure = VodProcedure:new()

    if type(priority) == 'number' then
        procedure.setPriority(priority)
    end

    return procedure
end
```

The code structure of Lua task flow is as follows:

- The processing logic of task flow is implemented by a class (the `VodProcedure` class in the sample codes), which defines what operations are performed by the task flow at each stage;
- Task flow implementation class (the `VodProcedure` class in the sample codes) must be created via `NewProcedureClass`, so as to ensure it inherits from the 'BaseProcedure' class built into VOD system;
- Task flow implementation class can define a `constructor`, so as to complete the necessary initialization operation;
- An entry function named `CreateProcedure` must be provided in the Lua script, which is a factory function that returns a specific instance (i.e. object) of the task flow implementation class.
- The entry function `CreateProcedure` can accept additional input parameters (the parameter `priority` is passed in the sample code).

When using the Lua task flow to process videos, you must proceed with the template name of Lua task flow. Please note:
- If only the name of Lua task flow template is passed, the entry function `CreateProcedure` will be called without any parameters;
- If '()' is added after the name of the Lua task flow template when it is passed, you can pass the parameters in '()' to the task flow (similar as the function calling method); the passing method of parameters is the same as the functional parameter passing method in the Lua language, and the parameters are separated by commas. Four types of parameters are supported, such as Number, String, Boolean, and Table.

For example, call the [ProcessFileByProcedure](https://cloud.tencent.com/document/product/266/9045) API to process the videos by calling the server APIs:

Example 1: Call MyFirstProcedure to process the video, without passing parameters.
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=ProcessFileByProcedure
&fileId=12345
&procedure=MyFirstProcedure
&COMMON_PARAMS
</pre>

Example 2: Call MyFirstProcedure to process the video, passing the priority parameter (the priority of this task is set to 5).
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=ProcessFileByProcedure
&fileId=12345
&procedure=MyFirstProcedure(5)
&COMMON_PARAMS
</pre>

## Introduction to each stage of task flow

The VOD system divides task flow into the following group of stages, which are executed in turn from the first stage to the last stage. The operations within each stage are independent of each other, and executed concurrently. A certain stage may not contain any operation.

### Video Generation
The video generation process determines the source videos processed thereafter. There are several ways to generate source videos:

- Specify the existing videos in the media asset library (the FileID remains unchanged);
- Clip the existing videos in the media asset library to generate new videos (generate new FileIDs);
- Remotely pull videos from other platforms to the VOD platform (generate new FileIDs).

### Get Meta-information

Get the meta-information of videos, such as length, bitrate, resolution, encoding and so on. In the Lua task flow, you can control video processing operations for subsequent stages based on the video meta-information.

After the video meta-information is obtained successfully, the result will be written into the media asset system, which can be obtained by  calling API [GetVideoInfo](https://cloud.tencent.com/document/product/266/8586).

### AI Video Review

The AI video review process includes the following capabilities:
- Porn detection in video;
- Sensitive word recognition in video;
- Sensitive image recognition in video.

Subsequent processing of task flow is determined by the review result. For example, developers can set "Terminate processing immediately after the video is found to be porn-related", or set "Transfer to manual porn detection after the video is found to be porn-related".

### Manual Video Review

The so-called manual video review means that the VOD system can send all videos (or suspected sensitive videos) to the video review team of the app, then the video review is conducted by the full-time staff. The follow-up video processing and distribution operations are then determined based on the review result.

### Video Processing

The processing on videos includes:
- [Transcoding](https://cloud.tencent.com/document/product/266/11701#.E8.A7.86.E9.A2.91.E8.BD.AC.E7.A0.81) (including [watermark](https://cloud.tencent.com/document/product/266/11701#.E8.A7.86.E9.A2.91.E6.B0.B4.E5.8D.B0), [encryption](https://cloud.tencent.com/document/product/266/9638), [re-wrapping](https://cloud.tencent.com/document/product/266/11701#.E8.A7.86.E9.A2.91.E8.BD.AC.E5.B0.81.E8.A3.85) and other functions);
- [Capture screenshots at a specified time](https://cloud.tencent.com/document/product/266/11702#.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE);
- [Use screenshots captured at specified time as cover](https://cloud.tencent.com/document/product/266/11702#.E4.BD.BF.E7.94.A8.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E4.BD.9C.E4.B8.BA.E5.B0.81.E9.9D.A2);
- [Sampling screenshot](https://cloud.tencent.com/document/product/266/11702#.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE);
- [Image Sprite screenshot](https://cloud.tencent.com/document/product/266/11702#.E9.9B.AA.E7.A2.A7.E5.9B.BE(imagesprite)).

All the outputs of above video processing operations will be written into the media asset system, which can be obtained by the API [GetVideoInfo](https://cloud.tencent.com/document/product/266/8586).

#### Video Distribution

The process of video distribution includes:
- Video upload in WeChat.

## Use Task Flow to Process Videos

Developers can use task flow to process videos in the following ways:

- Process existing videos
- When uploading videos, specify the video processing method, including:
    - Specify the task flow when uploading from client side
    - Specify the task flow when uploading from server side
    - Specify the task flow when pulling video offline
    - Specify the task flow when recording LVB
- Generate videos and process them using task flow

### Process Existing Videos
#### Process Existing Videos on the Console
The document is to be completed.

#### Process Existing Videos via Server API

For more information, please see:
- Server API: [Process the video files according to the specified process (ProcessFileByProcedure)](https://cloud.tencent.com/document/product/266/9045)
- Server API: [Use task flow to process the videos (RunProcedure)](https://cloud.tencent.com/document/product/266/11030)
- Server API: [Process the video files (ProcessFile)](https://cloud.tencent.com/document/product/266/9642)

Note:
> The difference between the three APIs is:
> - Both ProcessFileByProcedure and ProcessFile can be used only to process the existing videos (that is, no "video generation" phase exists and no new FileID is generated); RunProcedure can be used to generate new videos;
> - The inputs of both ProcessFileByProcedure and RunProcedure are task flow template names. JSON task flow and Lua task flow are supported;
> - ProcessFile only supports the "video processing" phase of a task flow, and its input parameter is not the task flow template name, but the specific video processing parameter template.


### Specifying the Task Flow When Uploading from Client Side
The document is to be completed.

### Specifying the Task Flow When Uploading from Server Side
The document is to be completed.

### Specifying the Task Flow When Pulling Video Offline
The document is to be completed.

### Specifying the Task Flow When Recording LVB
The document is to be completed.

### Generating Videos and Process them Using Task Flow
The document is to be completed.

## Getting the Task Flow Execution Results

The so-called task flow execution results refer to the outputs of each video processing operation, such as transcoding, path of screenshot output file, video porn detection result, etc.
Developers can get the task flow execution results in the following ways:
1. Perceive the task flow execution results (or status changes) through the task flow event notification: See [Event Notification](#.E4.BA.8B.E4.BB.B6.E9.80.9A.E7.9F.A5);
2. Get the task flow execution results through the status query API: see [Status Query](#.E4.BB.BB.E5.8A.A1.E7.AE.A1.E7.90.86);
3. Get the task flow execution results through the media asset management API: The operation results of some sub-tasks in the task flow will be written into the media asset system, and the results of video transcoding, screenshot taking and other operations can be obtained through Server API [GetVideoInfo](https://cloud.tencent.com/document/product/266/8586).

## Event Notification and Task Management

Processing videos by using task flows is essentially implemented offline. After the video processing operation is initialized through the task flow, this operation will be performed in the VOD backend as an offline task, and the VOD backend will return the task ID to the caller.

Developers can perceive the task execution through the event notification mechanism, and query the execution status of a certain task through the task management mechanism. See [Event Notification and Task Management](https://cloud.tencent.com/document/product/266/7829).

### Event Notification

For the video processing tasks initiated by the task flow, their event notification is divided into two types:
1. Status Change Notification for Task Flow Execution: The event notification is triggered after each sub-task in each stage of the task flow is executed (for example, a notification is triggered after each transcoding of specific format of is completed); it is suitable for the scenarios where the video processing result is to be obtained quickly;
2. Notification for the End of Task Flow Execution: The event notification is triggered only when the entire task execution is completed, regardless of the intermediate process of task execution.

For more information, please see [Status Change Notification for Task Flow Execution](https://cloud.tencent.com/document/product/266/9636).

### Task Management

You can query the task flow execution status (queuing/executing/completed) and the results (the output result of each sub-operation) based on the task ID.

For more information, please see [Task Management](https://cloud.tencent.com/document/product/266/7829#.E4.BB.BB.E5.8A.A1.E7.AE.A1.E7.90.86).

# VOD Built-in Task Flow Template

### QCVB_SimpleProcessFile

This task flow template is of Lua task flow, which supports some simple video processing operations as follows:
- Video transcoding, including:
    - Specify the output format of transcoding through the input parameters of task flow;
    - Use the default output format of transcoding in the console;
- Adding watermarks during the transcoding;
- Capturing the first frame as the video cover;
- Sampling screenshots.

The task flow supports four input parameters, and its entry function is named as follows:

```lua
------------------------------------------
--- The entry function of the preset task flow QCVB_SimpleProcessFile
------------------------------------------
function CreateProcedure(transcodeDefinition, watermarkDefinition, 
    coverBySnapshotDefinition, sampleSnapshotDefinition)
```

The meaning of each parameter is described as follows:
<table>
    <tr>
        <th>
            Parameter
        </th>
        <th>
            Description
        </th>
    </tr>
    <tr>
        <td>
            transcodeDefinition
        </td>
        <td>
            <p>The transcoding control parameter. It supports the following input methods:</p>
            <li>Use the default transcoding settings in the console for transcoding: Fill this parameter with an integer 1;</li>
            <li>Use the specified transcoding template ID for transcoding: Fill this parameter with an array of integers, with each element in the array as a target transcoding template ID;</li>
            <li>No transcoding: Fill it with the value "nil" or "0".</li>
        </td>
    </tr>
    <tr>
        <td>
            watermarkDefinition
        </td>
        <td>
            <p>The watermark control parameter. It supports the following input methods:</p>
            <li>Use the default watermark settings in the console for transcoding: Fill this parameter with an integer 1;</li>
            <li>Use the specified watermark ID for transcoding: Fill this parameter with the watermark ID (integer);</li>
            <li>No watermarking: Fill it with the value "nil" or "0".</li>
        </td>
    </tr>
    <tr>
        <td>
            coverBySnapshotDefinition
        </td>
        <td>
            <p>The control parameter for capturing the first frame as cover. It supports the following input methods:</p>
            <li>Use the specific screenshot template to capture the first frame, and set it as the cover: Fill this parameter with the screenshot template ID (an integer);</li>
            <li>Not capturing the first frame as cover: Fill it with the value "nil" or "0".</li>
        </td>
    </tr>
    <tr>
        <td>
            sampleSnapshotDefinition
        </td>
        <td>
            <p>The control parameter for sampling screenshots. It supports the following input methods:</p>
            <li>Use the specific template for sampling screenshot to take screenshots: Fill this parameter with the ID of the template for sampling screenshots (an integer);</li>
            <li>Not sampling screenshot: Fill it with the value "nil" or "0".</li>
        </td>
    </tr>
</table>


#### Example: Use the Preset Task Flow `QCVB_SimpleProcessFile` to Process Videos

Example 1: Use the default transcoding and watermark parameters in the console for transcoding:
<pre>
QCVB_SimpleProcessFile(1, 1)
</pre>

Example 2: Capture the first frame as cover, and use the screenshot template 10, without other processing:
<pre>
QCVB_SimpleProcessFile(0, 0, 10)
</pre>

Example 3: Use the transcoding templates 10 and 20 for transcoding; use the watermark template 150 to set watermarks in transcoding process; use the screenshot template 10 to capture the first frame as cover; use the template 10 for sampling screenshots to take screenshot samples:
<pre>
QCVB_SimpleProcessFile({10, 20}, 150, 10, 10)
</pre>


<!-- ### TODO: Re-wrapping -->
