package com.example.team28_cse551;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
    public void onTrueBA(View view) {
        Intent intent = new Intent();
        intent.setAction("com.example.team28_cse551");
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