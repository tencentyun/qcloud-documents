## Overview

Developers need to configure both input file bucket and output file bucket before using Tencent Cloud's video processing capability, so that the Tencent Cloud Video Transcoding Service has the permission to read the input file and write the output file.

## How to Make the Configuration

![COS Bucket permission setting](https://main.qcloudimg.com/raw/ae4be63c286b1b8ffc6d2218284fdd25.png)

### 1. Configure input file bucket
Let's take an input file bucket named **myinputbucket** as an example. It is configured as follows:
1. Log in to the [COS Console](https://console.cloud.tencent.com/cos5/bucket).
2. Go to **myinputbucket**, and select **Permission Management**.
3. In the **Bucket Access Permission** menu, select **Public Read and Private Write** for the **Common Permission**.
4. Click **Save**.

### 2. Configure output file bucket
Let's take an output file bucket named **myoutputbucket** as an example. It is configured as follows:
1. Log in to the [COS Console](https://console.cloud.tencent.com/cos5/bucket).
2. Go to **myoutputbucket**, and select **Permission Management**.
3. In the **Bucket Access Permission** menu, select **Public Read and Private Write** for the **Common Permission**.
4. In **User Permission**, click **Add User**, then enter **2819697038** for the **Root Account ID**, and select **Data Read** and **Data Write**.
5. Click **Save**.
