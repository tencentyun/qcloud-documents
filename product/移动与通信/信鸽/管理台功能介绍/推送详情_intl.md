## Overview

The push details feature helps you to understand the progress and time of the task delivery, push conversion rate, coverage, and timeliness of push after a push is created. Data analysis for full-based push and tag-based push is supported.

## Interface Description
![](//mc.qcloudimg.com/static/img/40570d51bda9ecb6524253e58b53f488/image.png)
### Delivery Progress

The real-time statistics on task delivery. It is refreshed after the task delivery starts.

### Push Conversion Analysis
 
The analysis of push conversion rate. It is classified based on two platforms: Android and iOS.

### [Push to Android]

**Planned push:** The number of devices connected to the server within 90 days after the current App is installed. These devices are the target of this push.
**Device online:** The number of devices connected to the server within the validity period of the push (messages can be pushed normally only if the connection between the device and server is established.)
**Arrival:** The number of message Service arriving at the terminal device.
**Display:** The number of messages to be displayed by calling the system's message display API.
**Click:** The number of messages you click in the notification bar.

### [Push to iOS]

**Planned push:** The total number of valid devices in the system. If the Token returned by APNs is invalid, the corresponding device will be cleared by the system every day.
**Server delivery:** The number of devices with messages actually delivered by XGPush server
**APNs receipt:** The number of devices that have received messages returned by APNs (Apple Push Notification Service)
**Click:** The number of pushed messages you click in the notification bar

### Coverage Analysis

Coverage analysis is to evaluate the coverage of full-based push by comparing push arrivals with the number of active Apps. This feature is available to push to Android only.

**Active coverage on the day:** Arrivals/DAU on the day
**Active coverage within 3 days:** Arrivals/DAU (duplicate removed) in the last 3 days

### Push Timeliness Analysis

In push timeliness analysis, push data is divided by time (in minutes or hours). You can divide the push data by a maximum of 24 hours.

