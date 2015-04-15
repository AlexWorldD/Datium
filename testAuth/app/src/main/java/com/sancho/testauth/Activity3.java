package com.sancho.testauth;

import retrofit.Callback;
import retrofit.RetrofitError;
import retrofit.client.Response;
import retrofit.http.Body;
import retrofit.http.POST;
import retrofit.RestAdapter;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.KeyEvent;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;


public class Activity3 extends ActionBarActivity {

    EditText eName;
    EditText ePassword;
    String username;
    String password;


    public class SignRequest {
        private String username;
        private String password;


        public SignRequest(String login, String password) {
            this.username = login;
            this.password = password;
        }

        public SignRequest() {
        }

        public String getUsername() {
            return username;
        }

        public void setUsername(String username) {
            this.username = username;
        }

        public String getPassword() {
            return password;
        }

        public void setPassword(String password) {
            this.password = password;
        }

        @Override
        public String toString() {
            return "SignRequest{" +
                    "\nUsername='" + username + '\'' +
                    ", \npassword='" + password + '\'' +
                    '}';
        }



    }

    public interface Api{
        public static final String URL ="http://178.62.42.66/api/v1";
         static final String AUTH_SIGNIN = "/auth/login/";


        @POST(AUTH_SIGNIN)
        void sign(@Body SignRequest, Callback<SignResponse> callback);




    }

    private void sign(String username, String password){
        RestAdapter restAdapter = new RestAdapter.Builder()
                .setEndpoint(Api.URL)
                .build();
        Api api = restAdapter.create(Api.class);
        SignRequest request = new SignRequest();
        request.setUsername(username);
        request.setPassword(password);
        api.sign(request,new Callback<SignResponse>(){

                    @Override
                    public void success(SignResponse signResponse, Response response){

                        String name = response.getUsername();
                        Intent intent = new Intent(this, SuccessLog.class);
                        startActivity(intent);

                    }

                    @Override
                public void failure(RetrofitError error){

                    }
                }




        );
    }


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity3);
        eName = (EditText) findViewById(R.id.editText4);
        ePassword = (EditText) findViewById(R.id.editText5);


        findViewById(R.id.button3).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                username = eName.getText().toString();
                password = ePassword.getText().toString();

                sign(username,password);


            }
        });
    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_activity3, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
