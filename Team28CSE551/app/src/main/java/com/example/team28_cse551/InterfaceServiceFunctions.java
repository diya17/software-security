package com.example.team28_cse551;

import android.app.Activity;

public interface InterfaceServiceFunctions {
    void registerActivity(Activity activity, InterfaceListenerFunctions callback);

    void unregisterActivity(Activity activity);

    String getTime();
}
