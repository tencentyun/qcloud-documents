Hybrid App refers to an App that contains native pages and html5 pages. MTA hybrid supports tracking of data for Apps developed with Android/iOS+webview.
### Feature Overview
MTA supports connection of hybrid app to offer a better data service to users. After the connection is completed, users can:
1. Track all the data in the App, eliminating the need to view data by jumping to another page, which breaks the boundary between App and H5.
2. Connect the key path between App and H5, making event funnel more complete.
3. Track data on H5 pages, making the access path more complete.

### How It Works
H5 uses JavaScript SDK to collect and send data to App. After receiving the data sent by JavaScript SDK, App SDK adds the collected default attributes (public attributes are also added if they are set on App). When hybrid tracking feature is enabled, html5 pages loaded in App can report page visit events and custom kv events by using Native method.

When hybrid tracking feature is used, iOS, Android and HTML ends should be connected with corresponding SDK at the same time.
**iOS SDK:** The latest version must be used ([Download Beta SDK](http://mta.qq.com/mta/resource/download/sdk/mta-ios-stats-sdk-2.0.9-beta.zip))
**Android SDK:** The latest version must be used ([Download Beta SDK](http://mta.qq.com/mta/resource/download/sdk/mta-android-sdk-3.3.0-beta.zip))
**JavaScript SDK:** [Click to view](https://cloud.tencent.com/document/product/549/12903)
Hybrid tracking is based on native tracking. Before getting started, make sure that MTA Android SDK configuration and initialization process have been connected as instructed in MTA official website.

