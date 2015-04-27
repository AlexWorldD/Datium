package com.sancho.clienttest;

import com.androidquery.AQuery;
import com.androidquery.callback.AjaxCallback;
import com.androidquery.callback.AjaxStatus;

import android.content.Intent;
import android.content.SharedPreferences;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;


public class LoginActivity extends ActionBarActivity {

    EditText logUsername;
    EditText logPassword;
    String username;
    String password;
    private static final String URL ="http://178.62.42.66/api/v1/auth/login/";
    SharedPreferences sPref;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.login);

        logUsername = (EditText) findViewById(R.id.logUsername);
        logPassword = (EditText) findViewById(R.id.logPassword);

        findViewById(R.id.btnEnt).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

                username = logUsername.getText().toString();
                password = logPassword.getText().toString();
                sign(username, password);


            }
        });

    }

    private void sign(final String username, String password){
        AQuery aq = new AQuery(this);
        Map<String, Object> params = new HashMap<String, Object>();
        params.put("username", username);
        params.put("password", password);
        aq.ajax(URL, params, JSONObject.class, new AjaxCallback<JSONObject>() {

            @Override
            public void callback(String url, JSONObject json, AjaxStatus status) {

               if(json !=null){
                   try {
                       sPref = getSharedPreferences("MyPref", MODE_PRIVATE);
                       SharedPreferences.Editor ed = sPref.edit();
                       ed.putString("token", json.getString("token"));
                       ed.putString("username",username);
                       ed.commit();
                       Toast.makeText(LoginActivity.this, "Text saved", Toast.LENGTH_SHORT).show();

                       startActivity(new Intent(LoginActivity.this, SuccessLog.class));
                   }
                   catch (JSONException e){
                       e.printStackTrace();

                   }

               }
            }
        });


    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_login, menu);
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
