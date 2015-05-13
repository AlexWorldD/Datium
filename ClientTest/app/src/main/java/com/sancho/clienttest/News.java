package com.sancho.clienttest;

import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
import android.widget.Toast;

import com.androidquery.AQuery;
import com.androidquery.callback.AjaxCallback;
import com.androidquery.callback.AjaxStatus;

import org.json.JSONObject;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import retrofit.Callback;
import retrofit.RestAdapter;
import retrofit.RetrofitError;
import retrofit.client.Response;
import retrofit.http.Body;
import retrofit.http.GET;
import retrofit.http.Header;
import retrofit.http.POST;


public class News extends ActionBarActivity {

    RestAdapter restAdapter = new RestAdapter.Builder()
            .setEndpoint(Api.URL)
            .build();
    Api api = restAdapter.create(Api.class);

    TextView newsText;
    SharedPreferences sPref;
    String jwtToken;
    String text;
    List<news> newsList = new ArrayList<>();
    news news5;
    List<String> newsTexxt = new ArrayList<>();
     ArrayAdapter<String> adapter;
    int count=0;

    public class news {

        String  title, text, user, group, tags, comments;
        String [] documents;

        public news( String title,String text, String user, String group, String tags, String comments, String[] documents){
            //this.id=id;
            this.title=title;
            this.text=text;
            this.user=user;
            this.group=group;
            this.tags=tags;
            this.comments=comments;
            this.documents=documents;
        }
        public news (){}

       // public String getId(){return id;}
        public String getTitle(){return title;}

        public String getText() {
            return text;
        }

        public String getComments() {
            return comments;
        }
    }

    public class sendNews {

        String  title, text;

        public sendNews( String title,String text){
            //this.id=id;
            this.title=title;
            this.text=text;

        }
        public sendNews (){}

        // public String getId(){return id;}
        public String getTitle(){return title;}

        public String getText() {
            return text;
        }

        public void setTitle(String title){this.title=title;}
        public void setText(String text){this.text=text;}


    }

    public interface Api{

        public static final String URL ="http://178.62.42.66/api/v1";
        public final String NEWS="/news/";

        @GET(NEWS)
        List<news> getNews(@Header("Authorization") String jwtToken);
        //news getNews(@Header("Authorization") String jwtToken);
        //List<news> getNews(@Header("Authorization") String jwtToken);

        @POST(NEWS)
        void post(@Header("Authorization") String jwtToken, @Body sendNews sednews, Callback<news> callback);


    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.news);

        //newsText = (TextView)findViewById(R.id.TextNew);

        sPref = getSharedPreferences("MyPref",MODE_PRIVATE);
        String savedText = sPref.getString("token","");
        jwtToken = "JWT "+savedText;
        String url = "http://178.62.42.66/api/v1/news/";




      /*  AQuery aq = new AQuery(this);
        AjaxCallback<JSONObject> cb = new AjaxCallback<JSONObject>()  {

            @Override
            public void callback(String url, JSONObject json, AjaxStatus status) {

                if(json != null){

                    //successful ajax call, show status code and json content
                    String text;
                    text=json.toString();
                    newsText.setText(text);

                }else{

                    //ajax error, show error code
                    Toast.makeText(News.this, "Error", Toast.LENGTH_SHORT).show();
                    //Toast.makeText(aq.getContext(), "Error:" + status.getCode(), Toast.LENGTH_LONG).show();
                }
            }
        };
        cb.url(url).type(JSONObject.class).weakHandler(this, "cb");

        cb.header("Authorization", jwtToken);


        aq.ajax(cb);*/
        //String url = "http://178.62.42.66/api/v1/news/";
      /*  AQuery aq = new AQuery(this);

            aq.ajax(url, JSONObject.class, new AjaxCallback<JSONObject>() {

                @Override
                public void callback(String url, JSONObject json, AjaxStatus status) {

                    if(json != null){

                        //successful ajax call, show status code and json content
                        String text;
                        newsText.setText(json.toString());

                    }else{

                        //ajax error, show error code
                        Toast.makeText(News.this, "Error", Toast.LENGTH_SHORT).show();
                        //Toast.makeText(aq.getContext(), "Error:" + status.getCode(), Toast.LENGTH_LONG).show();
                    }
                }
            });*/



          Runnable runnable = new Runnable() {
            public void run() {

                newsList = api.getNews(jwtToken);
                //news5 = api.getNews(jwtToken);

        //String text = newsList.get(1).getTitle();
                String lol;
                lol="123";


            }
        };
        Thread thread = new Thread(runnable);
        thread.start();
        try {
            thread.join();

            // text = news5.getTitle();
        } catch (InterruptedException e) {
            Toast.makeText(News.this, "Error", Toast.LENGTH_SHORT).show();
            e.printStackTrace();
        }
        text=newsList.get(0).getTitle();
        String newtext=text;

        ListView listview = (ListView) findViewById(R.id.listView);

        for(int i=0; i<newsList.size();i++)
        {
            String temp;
            temp = newsList.get(i).getTitle();
            temp += "\n";
            temp += newsList.get(i).getText();

            newsTexxt.add(temp);
        }


        adapter = new ArrayAdapter<String>(this,
                android.R.layout.simple_list_item_1, newsTexxt);
        listview.setAdapter(adapter);

        findViewById(R.id.btnSend).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                sendNews();
                count++;


            }
        });




       // news [] news1;


      // news1 = api.getNews(jwtToken);
        // String text = news1[1].getTitle();
       //newsText.setText(newtext);
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
            Toast.makeText(News.this, "Profile", Toast.LENGTH_SHORT).show();
            startActivity(new Intent(News.this, SuccessLog.class));
        }

        if (item.getTitle() == "News"){Toast.makeText(News.this, "News", Toast.LENGTH_SHORT).show();
            startActivity(new Intent(News.this, News.class));}
        if (item.getTitle() == "Teachers"){
            Toast.makeText(News.this, "Teachers", Toast.LENGTH_SHORT).show();
            startActivity(new Intent(News.this, Teachers.class));
        }


        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }

    private void sendNews(){
       // AQuery aq = new AQuery(this);
        //Map<String, Object> params = new HashMap<String, Object>();

        EditText entry = (EditText) findViewById(R.id.edtNews);
        String temp = entry.getText().toString();
        if (count >0) entry.setText("");
        final String title = "Post via Android app";
        sendNews news1 = new sendNews();
        news1.setTitle(title);
        news1.setText(temp);


        api.post(jwtToken,news1, new Callback<news>(){

                    @Override
                    public void success(news signResponse, Response response){

                        Toast.makeText(News.this, "Succes", Toast.LENGTH_SHORT).show();
                        String lngNews;
                        lngNews=signResponse.getTitle()+"\n"+signResponse.getText();
                        newsTexxt.add(lngNews);
                        adapter.notifyDataSetChanged();





                    }

                    @Override
                    public void failure(RetrofitError error){

                    }
                }




        );
      /*  params.put("title", title);
        params.put("text", temp);
        String URL = "http://178.62.42.66/api/v1/news/";
        aq.ajax(URL, params, JSONObject.class, new AjaxCallback<JSONObject>() {

            @Override
            public void callback(String url, JSONObject json, AjaxStatus status) {

                if(json !=null){
                    Toast.makeText(News.this, "Succes", Toast.LENGTH_SHORT).show();
                    //startActivity(new Intent(Registration_Activity.this, SuccessReg.class));

                }
            }
        });*/

    }


}
