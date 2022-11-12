package com.example.team28_cse551;


import android.annotation.SuppressLint;
import android.app.Activity;
import android.app.Service;
import android.content.Intent;
import java.text.SimpleDateFormat;
import android.os.Binder;
import android.os.Handler;
import android.os.IBinder;
import android.os.Looper;
import android.os.SystemClock;
import java.util.Date;
import java.util.Map;
import java.util.Objects;
import java.util.concurrent.ConcurrentHashMap;

public class ServActService extends Service {
    private final IBinder mBinder = new LocalBinder();
    private static final int ONE_SECOND = 1000;
    private final Map<Activity, InterfaceListenerFunctions> clients = new ConcurrentHashMap<>();
    public ServActService() {
    }
    @Override
    public void onCreate() {
        super.onCreate();
        new Thread(currentTimeRunner).start();
    }

   private void updateTimeOnClient(final Activity client) {
       final String time = getCurrentTime();
       try {
           Handler lo = new Handler(Looper.getMainLooper());
           lo.post(() -> {
               InterfaceListenerFunctions callback = clients.get(client);
               Objects.requireNonNull(callback).setTime(time);
           });

       } catch (Throwable t) {
           t.printStackTrace();
       }
   }
   private final Runnable currentTimeRunner = () -> {
       while (true) {
           for (Activity client : clients.keySet()) {
               updateTimeOnClient(client);
           }
           SystemClock.sleep(ONE_SECOND);
       }

   };
   private String getCurrentTime() {
       @SuppressLint("SimpleDateFormat") SimpleDateFormat formatter= new SimpleDateFormat("HH:mm z");
       Date date = new Date(System.currentTimeMillis());
       return formatter.format(date);
   }
    @Override
    public IBinder onBind(Intent intent) {
        return mBinder;
    }
    public class LocalBinder extends Binder implements InterfaceServiceFunctions {
        public void registerActivity(Activity activity, InterfaceListenerFunctions callback) {
            clients.put(activity, callback);
        }
        public void unregisterActivity(Activity activity) {
            clients.remove(activity);
        }
        public String getTime() {
            return getCurrentTime();
        }
    }
}