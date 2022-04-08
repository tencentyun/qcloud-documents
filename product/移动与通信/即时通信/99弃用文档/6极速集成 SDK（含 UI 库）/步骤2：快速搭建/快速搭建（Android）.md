常用的聊天软件都是由聊天窗口、会话列表等几个基本的界面组成。TUIKit 提供一套基本的 UI 实现，简化 IM SDK 的集成过程，只需几行代码即可在项目中使用 IM SDK 提供通信功能。

## 预期效果
<table>
     <tr>
         <th style="text-align:center">会话列表界面</th>  
         <th style="text-align:center">联系人列表界面</th>  
     </tr>
	 <tr>      
	 <td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/af813e0bdb5592622a90afa975424d37.png" width="320"/></td>   
	 <td style="text-align:center"><img src="https://qcloudimg.tencent-cloud.cn/raw/5c0d1cf1ff2d7f73d9cf18286bfe77db.png" width="320"/></td>   
     </tr> 
</table>


## 集成指南

### 步骤一：组件登录

```java

// 在程序启动的时候初始化 TUI 组件，通常是在 Application 的 onCreate 中进行初始化：
TUILogin.init(this, SDKAPPID, null, null);
    
// 在用户 UI 点击登录的时候登录 UI 组件：
TUILogin.login(userId, userSig, new V2TIMCallback() {
	@Override
	public void onError(final int code, final String desc) {
	}

	@Override
	public void onSuccess() {
	}
});
```

### 步骤二：创建 viewPager
在 `activity_main.xml` 中添加界面布局：

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">
    
    <androidx.viewpager2.widget.ViewPager2
    android:id="@+id/view_pager"
    android:layout_width="match_parent"
    android:layout_height="0dp"
    android:layout_weight = "1"/>
</LinearLayout>
```
创建 `FragmentAdapter.java` 用来配合 `ViewPager2` 展示会话和联系人界面。

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
### 步骤三：构建核心 Fragment

会话列表 `TUIConversationFragment` 以及联系人列表 `TUIContactFragment` 界面数据的获取、同步、展示以及交互均已在组件内部封装，UI 的使用与 Android 的普通 Fragment 一样方便。

在 `MainActivity.java` 的 `onCreate` 方法中添加：

```java
List<Fragment> fragments = new ArrayList<>();
// tuiconversation 组件提供的会话界面
fragments.add(new TUIConversationFragment());
// tuicontact 组件提供的联系人界面
fragments.add(new TUIContactFragment());
ViewPager2 mainViewPager = findViewById(R.id.view_pager);
FragmentAdapter fragmentAdapter = new FragmentAdapter(this);
fragmentAdapter.setFragmentList(fragments);
mainViewPager.setOffscreenPageLimit(2);
mainViewPager.setAdapter(fragmentAdapter);
mainViewPager.setCurrentItem(0, false);
```