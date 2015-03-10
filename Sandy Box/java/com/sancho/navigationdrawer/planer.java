package com.sancho.navigationdrawer;

import android.support.v4.app.Fragment;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.CalendarView;
import android.view.ViewGroup;

/**
 * Created by Sancho on 08.03.2015.
 */
public class planer extends Fragment {

    /*@Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        CalendarView calendar = new CalendarView(this);
        setContentView(calendar);
    }*/

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {

        View rootView = inflater.inflate(R.layout.planer_layout, container, false);
        return rootView;
    }
}
