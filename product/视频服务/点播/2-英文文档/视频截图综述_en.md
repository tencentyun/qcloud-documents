Video screenshots are the images captured from a video at specific positions. The VOD system supports the following methods for capturing video screenshots:

- Capture screenshots at specified time points: capture images in a video at specified time points;
- Capture a screenshot at a specified time point as cover: Capture an image, and use its URL as the cover of the video in the media assert system;
- Capture screenshots by sampling: Capture video screenshots at a fixed time interval or an interval in percentage;
- Capture Image Sprite screenshot: Capture a series of images at a fixed time interval or an interval in percentage, and then organize these images as an Image Sprite.

## Capture Screenshots at Specified Time Points
### Templates for capturing screenshots at specified time points

Capturing screenshots at specified time points involves multiple parameters. The "templates for capturing screenshots at specified time points" can be used as the "containers" for these parameters. (Information of time points are not included in the template and needs to be separately transferred upon the call of API). You only need to specify a template ID to initiate the screenshot capture at specified time points.

VOD system provides a set of preset templates for developers for capturing screenshots at specified time points. For more information, please see [Preset Templates for Capturing Screenshots at Specified Time Points](#.E9.A2.84.E7.BD.AE.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF). If the preset templates do not meet your needs, you can submit a ticket for new templates.

The following table lists the parameters and their controlled items of the templates for capturing screenshots at specified time points:
<table>
	<tr>
        <th style="width:18%">
            Category               
        </th>
        <th style="width:22%">
            Parameter/Controlled Item
        </th>
        <th>
            Description
        </th>
    </tr>
     <tr>
        <td rowspan=3>
            Output image parameters</a>
        </td>
        <td>
            Format
        </td>
        <td>
            Output formats JPG and PNG are supported.
        </td>
    </tr>
    <tr>
        <td>
            Width
        </td>
        <td>
            Range: 128-4096 pixels.
        </td>
    </tr> 
    <tr>
        <td>
            Height
        </td>
        <td>
            Range: 128-4096 pixels.
        </td>
    </tr> 
	<tr>
        <td rowspan=2>
            Screenshot control parameters
        </td>
        <td>
            FillType
        </td>
        <td>
            "Fill" refers to how to process the image in case of a mismatch between the source video resolution and the target image's <b>aspect ratio</b>. The following filling types are supported:
            <li>Stretch: Stretch the image to make it spread across the entire screen. This may result in a "squashed" or "stretched" image.</li>
            <li>Fill with Black: Keep the image's aspect ratio unchanged, with the uncovered areas around the edges filled with black;</li>
            <li>Fill with White: Keep the image's aspect ratio unchanged, with the uncovered areas around the edges filled with white;</li>
            <li>Transparent: Keep the image's aspect ratio unchanged, with the uncovered areas around the edges rendered transparent (only for PNG format output).</li>
        </td>
    </tr>
    <tr>
        <td>
            Auto Zoom
        </td>
        <td>
            Auto zoom in/out according to width or height.
        </td>
    </tr>
</table>

### Initiate capture of screenshots at specified time points

Now, you can only initiate the operation by calling server APIs. See:

- Server APIs: [Capture Screenshots at Specified Time Points (CreateSnapshotByTimeOffset)](https://cloud.tencent.com/document/product/266/8102).

### Obtain the result of capturing screenshots at specified time points

You can obtain the result of the task by the following ways:

- After initiating the task, query the task status and results by task ID. For more information, please see [Event Notification and Task Management](https://cloud.tencent.com/document/product/266/7829);
- When the task is executed successfully, the screenshot capture result is bound to the media asset system. For more information, please see [Server API: Get Video Information (GetVideoInfo)](https://cloud.tencent.com/document/product/266/8586).

## Capture A Screenshot at A Specified Time as Cover
This operation captures a screenshot at a specified time point of the video, and use its URL as the URL of the video cover in the **VOD media asset system**. A VOD player can read and display this cover image.

In addition to capture a screenshot at a specified time point, this operation writes the screenshot result to the media assert system. Its operating parameters are the same as those for capturing screenshots at specified time points. For more information, please see [Overview of Capturing Screenshots at Specified Time Points](#.E6.8C.87.E5.AE.9A.E6.97.B6.E9.97.B4.E7.82.B9.E6.88.AA.E5.9B.BE.E8.83.BD.E5.8A.9B.E7.BB.BC.E8.BF.B0).

### Initiate the task of capturing screenshot as cover
Now, you can only initiate this operation by calling the task flow-related APIs. See also:
- [Process Videos Using Task Flows](https://cloud.tencent.com/document/product/266/11700#.E4.BD.BF.E7.94.A8.E4.BB.BB.E5.8A.A1.E6.B5.81.E5.A4.84.E7.90.86.E8.A7.86.E9.A2.91).

### Obtain the result of capturing screenshot as cover
You can obtain the result of the task by the following ways:

- After initiating the task, query the task status and result by task ID. For more information, please see [Event Notification and Task Management](https://cloud.tencent.com/document/product/266/7829);
- When the task is executed successfully, the screenshot capture result is bound to the basic video information in the media asset system. For more information, please see [Server API: Get Video Information (GetVideoInfo)](https://cloud.tencent.com/document/product/266/8586).

## Capture Screenshots by Sampling
Capturing screenshots by sampling is about sampling the video at an fixed time interval and capturing the video image information at the sampling points to generate multiple images.

### Templates for capturing screenshots by sampling
Capturing screenshots by sampling involves multiple parameters. The "templates for capturing screenshots by sampling" can be used as the "containers" of these parameters. You only need to specify a template ID to initiate the task of capturing screenshots by sampling.

VOD system provides a set of preset templates for developers for capturing screenshots by sampling. For more information, please see [Preset Templates for Capturing Screenshots by Sampling](#.E9.A2.84.E7.BD.AE.E9.87.87.E6.A0.B7.E6.88.AA.E5.9B.BE.E6.A8.A1.E6.9D.BF). If the preset templates do not meet your needs, you can submit a ticket for new templates.

The following table lists the parameters and their controlled items for the templates for capturing screenshots by sampling.

<table>
	<tr>
        <th style="width:18%">
            Category               
        </th>
        <th style="width:22%">
            Parameter/Controlled Item
        </th>
        <th>
            Description
        </th>
    </tr>
    <tr>
        <td rowspan=3>
            Output image parameters</a>
        </td>
        <td>
            Format
        </td>
        <td>
            Output formats JPG and PNG are supported.
        </td>
    </tr>
    <tr>
        <td>
            Width
        </td>
        <td>
            Range: 128-4096 pixels.
        </td>
    </tr> 
    <tr>
        <td>
            Height
        </td>
        <td>
            Range: 128-4096 pixels.
        </td>
    </tr> 
	<tr>
        <td rowspan=3>
            Screenshot control parameters
        </td>
        <td>
            FillType
        </td>
        <td>
            "Fill" refers to how to process the image in case of a mismatch between the source video resolution and the target image's <b>aspect ratio</b>. The following filling types are supported:
            <li>Stretch: Stretch the image to make it spread across the entire screen. This may result in a "squashed" or "stretched" image.</li>
            <li>Fill with Black: Keep the image's aspect ratio unchanged, with the uncovered areas around the edges filled with black;</li>
            <li>Fill with White: Keep the image's aspect ratio unchanged, with the uncovered areas around the edges filled with white;</li>
            <li>Transparent: Keep the image's aspect ratio unchanged, with the uncovered areas around the edges rendered transparent (only for PNG format output).</li>
        </td>
    </tr> 
	<tr>
        <td>
            SampleType
        </td>
        <td>
            Two sampling types are supported:
            <li>Percent: Sampling at a fixed interval in percentage of video duration. For example, a value of 5 means capturing screenshots at an interval of 5% of the video duration and a total of 20 images will be generated.</li>
            <li>Time: Sampling at a fixed time interval. For example, a value of 5 means performing sampling every 5 seconds.</li>
        </td>
    </tr> 
    <tr>
        <td>
            Auto Zoom
        </td>
        <td>
            Auto zoom in/out according to width or height.
        </td>
    </tr>
</table>


### Initiate the task of capturing screenshots by sampling
Now, you can only initiate this operation by calling task flow-related APIs. See also:
- [Process Videos Using Task Flows](https://cloud.tencent.com/document/product/266/11700#.E4.BD.BF.E7.94.A8.E4.BB.BB.E5.8A.A1.E6.B5.81.E5.A4.84.E7.90.86.E8.A7.86.E9.A2.91).

### Obtain the result of capturing screenshots by sampling
You can obtain the result of the task by the following ways:

- After initiating the task, query the task status and result by task ID. For more information, please see [Event Notification and Task Management](https://cloud.tencent.com/document/product/266/7829);
- When the task is executed successfully, the screenshot capture result is bound to the media asset system. For more information, please see [Server API: Get Video Information (GetVideoInfo)](https://cloud.tencent.com/document/product/266/8586).

## Image Sprite
Image Sprite is a technique to merge multiple small images into a large image, and display these images individually. This technique allows you to get the information of multiple images by sending a single request, thus minimizing the number of requests and improving client performance.

> Note:
> The term Image Sprite comes from CSS Image Sprite. The word "Sprite" is also known as a popular drink from Coca-Cola Company.

### Templates for capturing Image Sprite screenshots
Capturing Image Sprite screenshots involves multiple parameters. The "templates for capturing Image Sprite screenshots" can be used as the "containers" of these parameters. You only need to specify a template ID to initiate the capture of Image Sprite screenshots. 

The parameters for this operation are as follows:
![Figure: Diagram of Image Sprite Parameters](//mc.qcloudimg.com/static/img/a108415925bdeb21de9b25f784d9177b/image.png)

VOD system provides a set of preset templates for developers for capturing Image Sprite screenshots. For more information, please see [Preset Templates for Capturing Image Sprite Screenshots](#.E9.A2.84.E7.BD.AE.E9.9B.AA.E7.A2.A7.E5.9B.BE.E6.A8.A1.E6.9D.BF). If the preset templates do not meet your needs, you can submit a ticket for new templates.

The following table lists the parameters and their controlled items of the templates for capturing Image Sprite screenshots.
<table>
	<tr>
        <th style="width:18%">
            Category               
        </th>
        <th style="width:22%">
            Parameter/Controlled Item
        </th>
        <th>
            Description
        </th>
    </tr>
     <tr>
        <td rowspan=5>
            Output image parameters
        </td>
        <td>
            Output format (Format)
        </td>
        <td>
            JPG and PNG are supported.
        </td>
    </tr>
    <tr>
        <td>
            Small image width (Width)
        </td>
        <td>
            Range: The value of "Small image width×Columns" is between 128 and 4096 pixels.
        </td>
    </tr> 
    <tr>
        <td>
            Small image height (Height)
        </td>
        <td>
            Range: The value of "Small image height×Rows" is between 128 and 4096 pixels.
        </td>
    </tr> 
    <tr>
        <td>
            Rows
        </td>
        <td>
            The number of small image rows in the large image. Range: The value of "Rows × Columns" should not exceed 100.
        </td>
    </tr> 
	<tr>
        <td>
            Columns
        </td>
        <td>
            The number of small image columns in the large image. Range: The value of "Rows × Columns" should not exceed 100.
        </td>
    </tr>
	<tr>
        <td rowspan=2>
            Screenshot control parameters
        </td>
        <td>
            Interval
        </td>
        <td>
            The time interval at which a small image is captured (in sec).
        </td>
    </tr>
	<tr>
        <td>
            FillType
        </td>
        <td>
            "Fill" refers to how to process the image in case of a mismatch between the source video resolution and the target image's <b>aspect ratio</b>. The following filling types are supported:
            <li>Stretch: Stretch the image to make it spread across the entire screen. This may result in a "squashed" or "stretched" image.</li>
            <li>Fill with Black: Keep the image's aspect ratio unchanged, with the uncovered areas around the edges filled with black;</li>
            <li>Fill with White: Keep the image's aspect ratio unchanged, with the uncovered areas around the edges filled with white;</li>
            <li>Transparent: Keep the image's aspect ratio unchanged, with the uncovered areas around the edges rendered transparent (only for PNG format output).</li>
        </td>
    </tr>
</table>


### Initiate capture of Image Sprite screenshots
You can initiate this operation by the following ways:
- [Server API: Capture Image Sprite Screenshots](https://cloud.tencent.com/document/product/266/8101);
- [Process Videos Using Task Flows](https://cloud.tencent.com/document/product/266/11700#.E4.BD.BF.E7.94.A8.E4.BB.BB.E5.8A.A1.E6.B5.81.E5.A4.84.E7.90.86.E8.A7.86.E9.A2.91).

### Get the result of capturing Image Sprite screenshots
You can obtain the result of the task by the following ways:

- After initiating the task, query the task status and result by task ID. For more information, please see [Event Notification and Task Management](https://cloud.tencent.com/document/product/266/7829);
- When the task is executed successfully, the screenshot capture result is bound to the media asset system. For more information, please see [Server API: Get Video Information (GetVideoInfo)](https://cloud.tencent.com/document/product/266/8586).

## Preset Templates for Capturing Screenshots
### Preset templates for capturing screenshots at specified time points
| Template ID | Output Format | Width | Height | Fill Type |
|---------|---------|---------|---------|---------|
| 10 | JPG | Same as source | Same as source | N/A |

### Preset templates for capturing screenshots by sampling
| Template ID | Output Format | Width | Height | Sample Type | Interval |
|---------|---------|---------|---------|---------|---------|
| 10 | JPG | Same as source | Same as source | Percent | 10% |

### Preset templates for capturing Image Sprite screenshots
| Template ID | Output Format | Small Image Width | Small Image Height | Rows | Columns | Interval | Fill Type |
|---------|---------|---------|---------|---------|---------|---------|---------|
| 10 | JPG | 142 | 80 | 10 | 10 | 10 sec | Fill with Black |
