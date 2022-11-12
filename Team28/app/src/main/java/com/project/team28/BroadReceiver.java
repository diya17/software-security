package com.project.team28;

import android.annotation.SuppressLint;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.os.Handler;
import android.os.Looper;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.Date;

public class BroadReceiver extends BroadcastReceiver {

    @Override
    public void onReceive(final Context context, final Intent intent) {
        new Handler(Looper.getMainLooper()).post(() -> {
            @SuppressLint("SimpleDateFormat") SimpleDateFormat dateFormat = new SimpleDateFormat("hh:mm:ss");
            Date date = new Date(System.currentTimeMillis());
            Toast.makeText(context,"Msg=" + intent.getStringExtra("msg")+ " Time= "+ dateFormat.format(date),Toast.LENGTH_SHORT).show();
            context.unregisterReceiver(this);
        });
    }
}