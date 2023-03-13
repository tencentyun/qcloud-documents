    /**

     * 分享来源，ShareSource中的值

     */

    public int shareSource;

    /**

     * 分享目标， ShareTarget中的值

     */

    public int shareTarget;

    /**

     * 分享面板设置的ID，用于区分分享渠道

     */

    public int shareItemId;

    /**

     * 分享标题

     */

    public String title;

    /**

     * 分享摘要

     */

    public String summary;

    /**

     * 分享图片的路径。为本地图片路径或者网络图片路径

     */

    public String sharePicPath;

    /**

     * 是否为本地图片。如果为True，则sharePicPath为本地图片的路径；否则，sharePicPath为网络图片的路径

     */

    public boolean isLocalPic;

    /**

     * 从服务端获取的字段：分享链接

     */

    public String targetUrl;

    /**

     * 小程序包信息

     */

    protected MiniAppInfo miniAppInfo;

