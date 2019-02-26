### Description
Identify the page source by adding [ADTAG=Channel ID] parameter to the landing page, which is generally used to track the effects of marketing activities and sharing links.
### Application Scenarios
- **Effect analysis of external channels**
When visitors are redirected from marketing activities, sharing links, ads and other pages to H5 Apps, add channel ID in the URL to identify channel effect.
- **Same source page, different entries**
For example, you can be redirected to page B by clicking either button A1 or A2 on page A. To differentiate the traffic brought by A1 and A2, channel IDs must be added respectively.
### Tips on Usage
Log in to [Mobile Tencent Analytics Console](http://mta.qq.com/mta/overview/ctr_all_app_new), select **HTML5 App** and click on your App. Add channels in [**Channel List**](http://mta.qq.com/h5/visitor) in the left menu bar, and the channel ID is generated after a channel is added. [ADTAG=Channel ID] must be added when you share H5 links. Channels are divided into four levels. Level 1 represents the basic channel source, and level 2, 3 and 4 represent different entries under the same channel source.
### Channel Example
Level 1: Tencent
Level 2: WeChat
Level 3: WeChat's "Moments"
Generated channel ID: `tx.wx.pyq`
Add the channel ID when sharing the H5 link: `www.test.com/test.html?ADTAG=tx.wx.pyq`
### Viewing Channel Effect
1. Click level 1 channel identifier (acting as the root level identifier) to display the effect analysis of level 2, 3 and 4 channel identifiers in a tree view.
2. The root level identifier displays a collection of effects of the same level 1 channel.

### Notes
1. The channel identifier can be subdivided into four levels at most.
2. The channel name can only contain letters and numbers.
3. ADTAG must be capitalized.
4. ADTAG must be placed after "?" in the URL.
5. Make sure the landing page allows the addition of "?" parameter.
6. Make sure that the "?" parameter in the landing page is not lost because of redirection.
7. "mta js sdk" must be embedded in the landing page.

