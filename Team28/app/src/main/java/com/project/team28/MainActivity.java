package com.project.team28;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.IntentFilter;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void onTrueBA(View view) {
        Intent intent = new Intent();
        BroadReceiver bReceiver = new BroadReceiver();
        IntentFilter iFilter = new IntentFilter("com.project.team28.homework");
        registerReceiver(bReceiver,iFilter);
        intent.setAction("com.project.team28.homework");
        intent.putExtra("msg", "Broadcast event!");
        sendBroadcast(intent);
    }
    public void onTrueSA(View view) {
        //Toast.makeText(this,"Service Activity", Toast.LENGTH_LONG).show();
        Intent intent = new Intent(this,ServiceActivity.class);
        startActivity(intent);
    }
    public void onTrueCPA(View view) {
        Intent intent = new Intent(this,DBActivity.class);
        startActivity(intent);
    }
}