package com.example.team28_cse551;

import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Handler;
import android.os.Looper;
import android.widget.Toast;
public class BroadReceiver extends BroadcastReceiver {
    @Override
    public void onReceive(final Context context, final Intent intent) {
        new Handler(Looper.getMainLooper()).post(new Runnable() {
            @Override
            public void run() {
                //Toast.makeText("Service").show();
                Toast.makeText(context,intent.getStringExtra("msg"),Toast.LENGTH_SHORT).show();
            }
        });
    }
}