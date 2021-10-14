常用的聊天软件都是由聊天窗口、会话列表等几个基本的界面组成。TUIKit 提供一套基本的 UI 实现，简化 IM SDK 的集成过程，只需几行代码即可在项目中使用 IM SDK 提供通信功能。

## 初始化

在 `Application` 的 `onCreate` 中进行初始化：

```java
public class DemoApplication extends Application {

    public static final int SDKAPPID = 0; // 您的 SDKAppID

    @Override
    public void onCreate() {
        super.onCreate();

        /**
         * @param context  应用的上下文，一般为对应应用的ApplicationContext
         * @param sdkAppID 您在腾讯云注册应用时分配的sdkAppID
         * @param config  IMSDK 的相关配置项，一般传入 null 使用默认即可，需特殊配置参考API文档
         * @param listener  IMSDK 初始化监听器
         */
        TUIKit.init(this, SDKAPPID, null, null);
    }
}
```

## 登录
初始化成功之后调用以下代码进行登录:
```java
/**
 * @param userId 用户Id
 * @param userSig 从业务服务器获取的usersig
 * @param callback 登录是否成功的回调
 */
TUIKit.login(userId, userSig, new V2TIMCallback() {
    @Override
    public void onError(final int code, final String desc) {
    }

    @Override
    public void onSuccess() {
    }
});
```

## 创建会话列表和联系人界面

会话列表 `TUIConversationFragment` 以及联系人列表 `TUIContactFragment`，其数据的获取、同步、展示以及交互均已在 `TUIKit` 内部封装，会话列表 UI 的使用与 Android 的普通 Fragment 一样方便。
<table>
     <tr>
         <th style="text-align:center">会话列表界面</th>  
         <th style="text-align:center">联系人列表界面</th>  
     </tr>
	 <tr>      
	 <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/9c5af8a0867039e14751bb2d1beb8953.png" width="320"/></td>   
	 <td style="text-align:center"><img src="https://main.qcloudimg.com/raw/ef3ede2b3ba92ca7c38329a5974522db.png" width="320"/></td>   
     </tr> 
	
</table>

### 步骤1：设置 MainActivity 的布局
在 `activity_main.xml` 中添加以下代码：

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">
    
    <androidx.viewpager2.widget.ViewPager2
    android:id="@+id/view_pager"
    android:layout_width="match_parent"
    android:layout_height="0dp"
    android:layout_weight = "1"/>
</LinearLayout>
```
### 步骤2：创建 FragmentAdapter.java 文件
`FragmentAdapter.java` 用来配合 `ViewPager2` 展示会话和联系人界面。
```java
import androidx.annotation.NonNull;
import androidx.fragment.app.Fragment;
import androidx.fragment.app.FragmentActivity;
import androidx.fragment.app.FragmentManager;
import androidx.lifecycle.Lifecycle;
import androidx.viewpager2.adapter.FragmentStateAdapter;


import java.util.List;

public class FragmentAdapter extends FragmentStateAdapter {
    private static final String TAG = FragmentAdapter.class.getSimpleName();

    private List<Fragment> fragmentList;

    public FragmentAdapter(@NonNull FragmentActivity fragmentActivity) {
        super(fragmentActivity);
    }

    public FragmentAdapter(@NonNull Fragment fragment) {
        super(fragment);
    }

    public FragmentAdapter(@NonNull FragmentManager fragmentManager, @NonNull Lifecycle lifecycle) {
        super(fragmentManager, lifecycle);
    }

    public void setFragmentList(List<Fragment> fragmentList) {
        this.fragmentList = fragmentList;
    }

    @NonNull
    @Override
    public Fragment createFragment(int position) {
        if (fragmentList == null || fragmentList.size() <= position) {
            return new Fragment();
        }
        return fragmentList.get(position);
    }

    @Override
    public int getItemCount() {
        return fragmentList == null ? 0 : fragmentList.size();
    }
}
```
### 步骤3：在 MainActivity.java 中创建 TUIConversationFragment 和 TUIContactFragment
在 `MainActivity.java` 的 `onCreate` 方法中添加：

```java
List<Fragment> fragments = new ArrayList<>();
fragments.add(new TUIConversationFragment());
fragments.add(new TUIContactFragment());
ViewPager2 mainViewPager = findViewById(R.id.view_pager);
FragmentAdapter fragmentAdapter = new FragmentAdapter(this);
fragmentAdapter.setFragmentList(fragments);
mainViewPager.setOffscreenPageLimit(2);
mainViewPager.setAdapter(fragmentAdapter);
mainViewPager.setCurrentItem(0, false);
```
