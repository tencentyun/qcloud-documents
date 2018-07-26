Tencent Cloud LVB Service Level Agreement (SLA) specifies the performance metrics and the compensation scheme of the LVB service provided by Tencent Cloud to customers.
### Definitions
#### 1. Service period
A natural month is counted as a service period, and a duration less than a month will not be counted as a service period.
#### 2. Video playback failure
During a service period, an end user does not get the video information, and thus is unable to watch the video.
The following cases are not considered as a playback failure:
(1) A domain name is blocked or a video stream is banned due to video content violation or other reasons.
(2) A video cannot be played due to a push exception on the pusher end.
(3) A video cannot be played due to a playback exception on the viewer end.
(4) A video cannot be played due to an exception in data centers and networks other than Tencent Cloud's devices.
(5) A video cannot be played due to force majeure and other reasons not attributable to Tencent Cloud (such as natural disaster and war).
(6) A video cannot be played due to hotlink protection and authentication enabled by customers.
(7) A video cannot be played due to reasonable upgrades and changes announced to customers by Tencent Cloud beforehand.
#### 3. Video playback success rate
![](https://main.qcloudimg.com/raw/f73a653f95ca1a04cd5368be32c9d65a.png)
#### 4. Video load time
Video load time refers to the total time taken from the moment a viewer starts to connect to the video request URL distributed by CDN to the moment the first frame of the video plays, in case of successful video playbacks.
#### 5. Stutter request
The difference between the local elapsed time of the CDN distribution server and the video elapsed time greater than 0 indicates a stutter.
(Video elapsed time can be obtained from the transmitted video content).
In a playback request, if the server records that 5 minutes elapses, but only 4 minutes and 59 seconds of video data is transmitted, this is a stutter request.
#### 6. Stutter rate
The statistical period for the stutter rate metric of Tencent Cloud LVB products is 5 minutes. The stutter rate is the rate of the number of stutter requests to the number of total requests for video playback within 5 minutes.
![](https://main.qcloudimg.com/raw/5d64f7fc0d889eec90e146a76c9af287.png)

### Performance Metrics
#### 1. Video load success rate metric
Within a service period, the average video load success rate shall not be lower than 99.60% (inclusive), that is:
![](https://main.qcloudimg.com/raw/7d8a8d8d5a290d21d7d4fc92e188ff6c.png)
#### 2. Video load time metric
The load time of a single video shall not be longer than 850 ms (inclusive).
#### 3. Stutter rate metric
The video stutter rate shall not be higher than 4.00% (inclusive).
![](https://main.qcloudimg.com/raw/287cbd39a39e1ccb0eb95dda34dc8069.png)

### Compensation Scheme
Service Compensation refers to the compensation offered by Tencent Cloud to customers in the event that the Tencent Cloud LVB service purchased by customers fails to conform to the requirement for performance metrics stated in the SLA as a result of failure or design defect of Tencent Cloud's devices or any improper operation performed by Tencent Cloud. The rules of compensation are as follows:

<table >
  <tr>
    <th colspan="2">Performance Metric</th>
    <th></th>
  </tr>
  <tr>
    <td rowspan="2">Video playback success rate</td>
    <td>The average video playback success rate is between 95.0% and 99.6%</td>
    <td>Deduct the total video fee for the current month x (99.60 % - actual playback success rate)</td>
  </tr>
  <tr>
    <td>The playback success rate is lower than 95.0% (inclusive)</td>
    <td>Deduct the total LVB fee for the current month</td>
  </tr>
  <tr>
    <td rowspan="2">Video load time</td>
    <td>The load time is between 850 ms and 2s</td>
    <td>Deduct 1/60 of the total LVB fee for the current month</td>
  </tr>
  <tr>
    <td>The load time is longer than 2s (inclusive)</td>
    <td>Deduct 1/30 of the total LVB fee for the current month</td>
  </tr>
  <tr>
    <td rowspan="2">Stutter rate</td>
    <td>The stutter rate is between 4% and 6%</td>
    <td>Deduct 1/60 of the total LVB fee for the current month</td>
  </tr>
  <tr>
    <td>The stutter rate is higher than 6% (inclusive)</td>
    <td>Deduct 1/30 of the total LVB fee for the current month</td>
  </tr>
</table>

