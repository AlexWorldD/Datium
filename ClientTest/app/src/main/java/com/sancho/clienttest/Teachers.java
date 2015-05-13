package com.sancho.clienttest;

import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.ArrayAdapter;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;

import retrofit.RestAdapter;
import retrofit.http.GET;
import retrofit.http.Header;


public class Teachers extends ActionBarActivity {
    RestAdapter restAdapter = new RestAdapter.Builder()
            .setEndpoint(Api.URL)
            .build();
    Api api = restAdapter.create(Api.class);


    SharedPreferences sPref;
    String jwtToken;

    List<teachers> teachersList = new ArrayList<>();

    List<String> TeachersTexxt = new ArrayList<>();
    ArrayAdapter<String> adapter;
    int count=0;

    public class teachers {

        String  first_name, last_name, patronymic, email, phone, cabinet;


        public teachers( String first_name,String last_name, String patronymic, String email, String phone, String cabinet){
            //this.id=id;
            this.first_name=first_name;
            this.last_name=last_name;
            this.patronymic=patronymic;
            this.email=email;
            this.phone=phone;
            this.cabinet=cabinet;
        }
        public teachers (){}

        // public String getId(){return id;}
        public String getFirst_name(){return first_name;}

        public String getLast_name() {
            return last_name;
        }

        public String getPatronymic() {
            return patronymic;
        }
        public String getCabinet(){return cabinet;}
    }

    public interface Api{
        public static final String URL ="http://178.62.42.66/api/v1";
        public static final String TEACHERS = "/teachers/";
        @GET(TEACHERS)
        List<teachers> getTeachers(@Header("Authorization") String jwtToken);
    }

    private void getTeachers(){
        Runnable runnable = new Runnable() {
            public void run() {

                teachersList = api.getTeachers(jwtToken);
                //news5 = api.getNews(jwtToken);

                //String text = newsList.get(1).getTitle();



            }
        };
        Thread thread = new Thread(runnable);
        thread.start();
        try {
            thread.join();

            // text = news5.getTitle();
        } catch (InterruptedException e) {
            Toast.makeText(Teachers.this, "Error", Toast.LENGTH_SHORT).show();
            e.printStackTrace();
        }
        //text=newsList.get(0).getTitle();
        //String newtext=text;
        String test;
       // test=;

        ListView listview = (ListView) findViewById(R.id.listViewTeach);

        for(int i=0; i<teachersList.size();i++)
        {
            String temp;
            temp = teachersList.get(i).getFirst_name();
            temp += " ";
            temp += teachersList.get(i).getPatronymic();

            temp += " ";
            temp += teachersList.get(i).getLast_name();
            temp += "\n";
          //  temp += "Class " + teachersList.get(i).getCabinet();

            TeachersTexxt.add(temp);
        }


        adapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1, TeachersTexxt);
        listview.setAdapter(adapter);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.teachers);
        sPref = getSharedPreferences("MyPref",MODE_PRIVATE);
        String savedText = sPref.getString("token","");
        jwtToken = "JWT "+savedText;
        getTeachers();
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {

        // Inflate the menu; this adds items to the action bar if it is present.
        //getMenuInflater().inflate(R.menu.menu_success_log, menu);
        menu.add("Profile");
        menu.add("News");
        menu.add("Teachers");
        //return true;
        return super.onCreateOptionsMenu(menu);
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();
        if (item.getTitle() == "Profile"){
            Toast.makeText(Teachers.this, "Profile", Toast.LENGTH_SHORT).show();
            startActivity(new Intent(Teachers.this, SuccessLog.class));
        }

        if (item.getTitle() == "News"){Toast.makeText(Teachers.this, "News", Toast.LENGTH_SHORT).show();
            startActivity(new Intent(Teachers.this, News.class));}
        if (item.getTitle() == "Teachers"){
            Toast.makeText(Teachers.this, "Teachers", Toast.LENGTH_SHORT).show();
            startActivity(new Intent(Teachers.this, Teachers.class));
        }


        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
