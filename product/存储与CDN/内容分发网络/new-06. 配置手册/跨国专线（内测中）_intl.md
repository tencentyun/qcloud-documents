## Overview

If your origin server is located at home, an overseas acceleration often suffers unstable or slow back-to-origin connection. You can greatly improve cross-border access by using an overseas intermediate node in combination with international private line service. When a user sends a request, it will first reach the edge node. If this node does not have the requested resource, it will send a request to the oversea intermediate node. And if the requested resource is not available at the oversea intermediate node, the intermediate node will need to send a request to a level-three node at home. This cross-border request will be sent via Tencent's private network instead of the public network. If the level-three node at home still does not have the requested resource, the request will go to the origin server. Activating the international private line configuration will significantly improve your international access.

**Note:** You need to enable overseas intermediate node to activate international private line service. Currently, international private line service is only available for users who have activated overseas CDN acceleration. Oversea CDN acceleration service is under beta test. It will become fully available in the future.

## Configuration Instructions

Log in to CDN Console, switch to international acceleration and go to **Domain Management** page. Then click the **Manage** button to the right of the domain to be configured

![](https://mc.qcloudimg.com/static/img/30a0b5830e9e5f11d1ab6d1f6b68ed33/1.png)

You can find **International Private Line** in "Advanced Configuration"

![](https://mc.qcloudimg.com/static/img/0a9eced420dad2687c41fca32155d990/2.png)

**Default configuration:** The intermediate node configuration is disabled by default
