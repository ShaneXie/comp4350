/**
 * Created by An on 2/1/2015.
 */

$(document).ready(function() {
    //init page
    $("#content").load("/ajax/getAllFood");

    //load events
    $("#foodlistItem").click(function(){
        $(".barItem").removeClass("active");
        $(this).addClass("active");
        $("#content").load("/ajax/getAllFood")
    });

    $("#bmiItem").click(function(){
        $(".barItem").removeClass("active");
        $(this).addClass("active");
        $("#content").load("../static/html/bmiCal.html")
    });

    $("#aboutItem").click(function(){
        $(".barItem").removeClass("active");
        $(this).addClass("active");
        //$("#content").load("../static/html/bmiCal.html")
    });

    $("#otherItem").click(function(){
        $(".barItem").removeClass("active");
        $(this).addClass("active");
        //$("#content").load("../static/html/bmiCal.html")
    });



});

function calBMI(type){
    var str = "Your BMI is: ";
    var h = 0;
    var w = 0;
    var bmi = 0;
    var msg ="";
    if(type=='std'){
        h = parseInt($("#bmiStdHeight").val());
        w = parseInt($("#bmiStdWeight").val());
        bmi = (w/(h*h))*703;
    }else{
        h = parseInt($("#bmiMtrHeight").val());
        w = parseInt($("#bmiMtrWeight").val());
        bmi = (w/(h*h));
    }
    str+=(bmi+" You are ");
    if(bmi<=18.5){
        msg = "Underweight ";
    }else if(bmi>18.5&&bmi<25){
        msg = "Normal weight";
    }else if(bmi>=25&&bmi<=29.9){
        msg = "Overweight";
    }else{
        msg = "Obesity";
    }
    str+=msg;
    $("#bmiResult").text(str);
};