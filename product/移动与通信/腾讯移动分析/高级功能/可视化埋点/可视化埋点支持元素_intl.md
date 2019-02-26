### Supported Android Visualized Event Tracking Elements
Button, EditText, layout, etc.
>**Note:**
>The element attributes must be "click", "selected", and "text_changed" (such as button and edittext), and the value is true, and the element is not covered (transparent layer is also considered as covered).

**Example of elements available for tracking:**
The elements in red and green frames in the figure below are available for tracking, and LinearLayout or button, click are all true.
![](//mc.qcloudimg.com/static/img/a6583b93a85b61c7e6571aa7239c3429/image.png)![](https://main.qcloudimg.com/raw/4db45ad405b850dabdd8335c764e3a64.png)
**Example of elements unavailable for tracking:**
The twelve pillar images and the text under them do not have a click attribute or click is false. So they cannot be tracked.
![](//mc.qcloudimg.com/static/img/ac42e400a2273a8c0975d4693cfd3de1/image.png)
### Supported iOS Visualized Event Tracking Elements
UIButton, UISwitch and UISlider.
>**Note:**
>If they are in TableView or CollectionView, these elements cannot be tracked.

**Example of elements available for tracking:**
The elements in red and green frames in the figure below can be tracked. Four of them are UIButton and are not in the TableView or CollectionView, so they can be tracked.
![](//mc.qcloudimg.com/static/img/744309e903c15219b0f6c29325817e28/image.png)
**Example of elements unavailable for tracking:**
The image above the login button in the figure is not UIButton, UISwitch or UISlider, so it cannot be tracked. The wallpaper, setting and other buttons under the login button are UIButton, but they are in a TableView, so they cannot be tracked.
![](//mc.qcloudimg.com/static/img/9b72b233ba36799451bfeffa5b3498ca/image.png)
