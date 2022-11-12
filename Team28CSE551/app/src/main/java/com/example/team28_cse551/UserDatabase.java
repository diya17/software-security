package com.example.team28_cse551;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.util.Log;
public class UserDatabase extends SQLiteOpenHelper {
    public static final String DB_NAME = "user_data";
    //Constants for table and columns
    public static final String TABLE = "user";
    public static final String ID = "_id";
    public static final String NAME = "name";
    public static final String PHONE = "phone";
    private static final String CREATE_TABLE_TUTORIALS = "create table " + TABLE +
            " (" + ID + " integer primary key autoincrement, " + NAME
            + " text, " + PHONE + " text );";
    private static final String DB_SCHEMA = CREATE_TABLE_TUTORIALS;
    public static final String[] ALL_COLUMNS =
            {ID, NAME, PHONE};
    @Override
    public void onCreate(SQLiteDatabase db) {
        db.execSQL(DB_SCHEMA);
    }
    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        Log.w("Student database", "Upgrading database. Existing contents will be"
                +"lost. ["
                + oldVersion + "]->[" + newVersion + "]");
        db.execSQL("DROP TABLE IF EXISTS " + "student");
        onCreate(db);
    }
    public UserDatabase(Context context) {
        super(context, DB_NAME, null, 1);
    }
}
