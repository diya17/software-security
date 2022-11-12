package com.project.team28;

import androidx.appcompat.app.AppCompatActivity;

import android.content.ContentValues;
import android.database.Cursor;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Random;

public class DBActivity extends AppCompatActivity {
    EditText mName;
    EditText mPhone;
    TextView mDBView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dbactivity);
        mName = (EditText) findViewById(R.id.text_name);
        mPhone = (EditText) findViewById(R.id.text_phone);
        mDBView = (TextView) findViewById(R.id.dbview);
    }
    public void onInsert(View view) {
        ContentValues values  = new ContentValues();
        values.put(UserDatabase.ID,new Random().nextInt(100));
        values.put(UserDatabase.NAME,mName.getText().toString());
        values.put(UserDatabase.PHONE,mPhone.getText().toString());

        getApplicationContext().getContentResolver().insert(UserContentProvider.CONTENT_URI,values);
        Toast.makeText(this,"Insert 1 row",Toast.LENGTH_SHORT).show();
        onShow(view);
    }
    public void onClear(View view) {
        int delcount =
                getContentResolver().delete(UserContentProvider.CONTENT_URI,null,null);
        Toast.makeText(this,"Delete " + delcount +
                "rows",Toast.LENGTH_SHORT).show();
        onShow(view);
    }
    public void onShow(View view) {
        Uri uri = UserContentProvider.CONTENT_URI;
        Cursor cursor = this.getContentResolver().query(uri,null,null,null,null);
        StringBuilder sb = new StringBuilder();
        while (cursor.moveToNext()){
            sb.append(cursor.getString(0) + ",");
            sb.append(cursor.getString(1) + ",");
            sb.append(cursor.getString(2) + ",");
            sb.append("\n");
        }
        mDBView.setText(sb.toString());
    }
}