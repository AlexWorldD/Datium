package com.sancho.navigationdrawer;

import android.support.v4.app.Fragment;
import android.media.MediaPlayer;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

/**
 * Created by Sancho on 08.03.2015.
 */
public class music extends Fragment {

    MediaPlayer mySound;
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        View rootView = inflater.inflate(R.layout.music_layout, container, false);
        return rootView;
       // mySound = MediaPlayer.create(this,R.raw.song);
    }

}
