package com.sancho.clienttest;

import android.content.Intent;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.TextView;

import com.androidquery.AQuery;
import com.androidquery.callback.AjaxCallback;
import com.androidquery.callback.AjaxStatus;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;


public class Registration_Activity extends ActionBarActivity {

    TextView text;
    Spinner groupsSpinner;
    EditText regUsername;
    EditText regPassword;
    EditText regEmail;
    String username;
    String password;
    String email;
    public String selectedGroup;
    String[] groups = { "pm", "mm", "mo", "bio" };
    private static final String URL ="http://178.62.42.66/api/v1/users/";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.registration);


        groupsSpinner = (Spinner) findViewById(R.id.groupSpinner);
        regUsername = (EditText) findViewById(R.id.regUsername);
        regEmail = (EditText) findViewById(R.id.regEmail);
        regPassword = (EditText) findViewById(R.id.regPassword);
       // text = (TextView) findViewById(R.id.textView5);
        ArrayAdapter<String> adapter1 = new ArrayAdapter<String>(getApplicationContext(),
                android.R.layout.simple_dropdown_item_1line, groups);
        groupsSpinner.setAdapter(adapter1);
        groupsSpinner.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
            // When an item is selected from Country Spinner Control
            public void onItemSelected(AdapterView<?> arg0, View arg1,
                                       int arg2, long arg3) {
                // TODO Auto-generated method stub
                //Get selected Item text
               selectedGroup = groupsSpinner.getSelectedItem().toString();
                //text.setText(selectedGroup);
                //Update City Spinner Control with JSON response

            }

            public void onNothingSelected(AdapterView<?> arg0) {
                // TODO Auto-generated method stub
            }
        });
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
        params.put("group", selectedGroup);
        aq.ajax(URL, params, JSONObject.class, new AjaxCallback<JSONObject>() {

            @Override
            public void callback(String url, JSONObject json, AjaxStatus status) {

                if(json !=null){
                    startActivity(new Intent(Registration_Activity.this, SuccessReg.class));

                }
            }
        });

    }



}
