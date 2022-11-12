package com.example.team28_cse551;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ComponentName;
import android.content.Intent;
import android.content.ServiceConnection;
import android.os.Bundle;
import android.os.IBinder;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;


public class ServiceActivity extends AppCompatActivity {
    private TextView time;
    private InterfaceServiceFunctions service = null;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_service);
        Button start = findViewById(R.id.start);
        Button stop = findViewById(R.id.stop);
        time = findViewById(R.id.time);
        start.setOnClickListener(view -> {
            time.setVisibility(View.VISIBLE);
            String time = service.getTime();
            setInterface(time);
        });
        stop.setOnClickListener(view -> time.setVisibility(View.INVISIBLE));
        startService(new Intent(this, ServActService.class));
        bindService(new Intent(this, ServActService.class), svcConn, BIND_AUTO_CREATE);
    }
    private final ServiceConnection svcConn = new ServiceConnection() {
        public void onServiceConnected(ComponentName className, IBinder binder) {
            service = (InterfaceServiceFunctions) binder;

            try {
                service.registerActivity(ServiceActivity.this, listener);
            } catch (Throwable ignored) {
            }
        }

        public void onServiceDisconnected(ComponentName className) {
            service = null;
        }
    };
    private void setInterface(String currentTime) {
        time.setText(currentTime);
    }
    @Override
    public void onDestroy() {
        super.onDestroy();
        service.unregisterActivity(this);
        unbindService(svcConn);
    }
    private final InterfaceListenerFunctions listener = this::setInterface;
}