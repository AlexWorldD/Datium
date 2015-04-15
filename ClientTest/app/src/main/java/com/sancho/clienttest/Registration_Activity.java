package com.sancho.clienttest;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.EditText;

import com.androidquery.AQuery;
import com.androidquery.callback.AjaxCallback;
import com.androidquery.callback.AjaxStatus;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;


public class Registration_Activity extends ActionBarActivity {

    EditText regUsername;
    EditText regPassword;
    EditText regEmail;
    String username;
    String password;
    String email;
    private static final String URL ="http://178.62.42.66/api/v1/users/";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.registration);

        regUsername = (EditText) findViewById(R.id.regUsername);
        regEmail = (EditText) findViewById(R.id.regEmail);
        regPassword = (EditText) findViewById(R.id.regPassword);
        findViewById(R.id.button4).setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                username = regUsername.getText().toString();
                email = regEmail.getText().toString();
                password = regPassword.getText().toString();
                signup(username,email,password);

            }
        });
    }

    private void signup(String username, String email,String password){
        AQuery aq = new AQuery(this);
        Map<String, Object> params = new HashMap<String, Object>();
        params.put("username", username);
        params.put("email",email);
        params.put("password", password);
        aq.ajax(URL, params, JSONObject.class, new AjaxCallback<JSONObject>() {

            @Override
            public void callback(String url, JSONObject json, AjaxStatus status) {

                if(json !=null){
                    startActivity(new Intent(Registration_Activity.this, SuccessReg.class));

                }
            }
        });

    }


    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_registration_, menu);
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
