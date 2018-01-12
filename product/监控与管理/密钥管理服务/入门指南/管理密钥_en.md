## Viewing Key
		
Log in to the [Console](https://console.cloud.tencent.com/kms). Please note that CMK varies depending on different regions. You can view the CMK list of a region by switching the region on the top.

## Enabling and Disabling Key

### Single Operation

You can enabled and disabled a key in the operation area at the right side.

![](https://mc.qcloudimg.com/static/img/aed79eb20ac537f12cb1203f4aef7e4e/manage_1.png)


#### Batch Operation

Multiple keys can be selected. Then, click the button on the top of the list for batch operation. After this, the "operation confirmation" box pops up. Click "OK" to perform a corresponding operation on all selected keys.

![](https://mc.qcloudimg.com/static/img/2187f376513902af6a9e5ec3918ec6ac/manage_2.png)


If you select the keys of different available statuses at a time, the corresponding prompts are displayed in the "operation confirmation" box that pops up when you click the batch "Enable" or "Disable" button. By clicking "OK", the operation is only performed on the keys that meet the requirements. Keys of original available statuses remain unchanged if they do not meet the requirements.

**If a key is disabled, all encryption and decryption operations that rely on it are also disabled. So, you need to verify that no business that relies on the key is running before you disable it.**

## Viewing Details of Key

Click "Key ID/Key name" of a key to enter its "details page", so as to view and modify the key information. "Online Tools" can also be found in this page.

![](https://mc.qcloudimg.com/static/img/5e1ce2bc0bf6745bb5ae41f2b91f0ff9/detail_1.png)

## Modifying Name and Usage

You can change the name and usage of the key in its "details page". Enter the new content in the dialog box that pops up after you click the button at the end of "Key Name" and "Key Usage".

![](https://mc.qcloudimg.com/static/img/a85e0e3c782bd22b2edd4ed185837d3e/detail_2.png)
