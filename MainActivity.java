package com.example.calculator;

import androidx.appcompat.app.AppCompatActivity;
import android.widget.Button;
import android.os.Bundle;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {
    Button button0,button1,button2,button3,button4,button5,button6,button7,button8,button9,buttondot,buttonadd,buttonsub,buttonmul,buttondiv,buttoneql,buttonC;
    EditText result;
    float mvalueone,mvaluetwo;
    boolean add,sub,mul,div;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        button0=(Button)findViewById(R.id.button0);
        button1=(Button)findViewById(R.id.button1);
        button2=(Button)findViewById(R.id.button2);
        button3=(Button)findViewById(R.id.button3);
        button4=(Button)findViewById(R.id.button4);
        button5=(Button)findViewById(R.id.button5);
        button6=(Button)findViewById(R.id.button6);
        button7=(Button)findViewById(R.id.button7);
        button8=(Button)findViewById(R.id.button8);
        button9=(Button)findViewById(R.id.button9);
        buttondot=(Button)findViewById(R.id.buttondot);
        buttonC=(Button)findViewById(R.id.buttonC);
        buttonadd=(Button)findViewById(R.id.buttonadd);
        buttonsub=(Button)findViewById(R.id.buttonsub);
        buttonmul=(Button)findViewById(R.id.buttonmul);
        buttondiv=(Button)findViewById(R.id.buttondiv);
        buttoneql=(Button)findViewById(R.id.buttoneql);
        result=(EditText) findViewById(R.id.edt1);


    }
}