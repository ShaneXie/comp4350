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
        html = "<h1 class=\"page-header\">About</h1>";
        html+="<div class=\"well well-sm\"><p>Calorie Tracking Syetem by Comp4350 Team7</p><p>Team Members: An Xie, . Nitesh, Hao Chang, Ayobami Idowu, Kenechukwu Igweagu, Billal Kohistani</br></p></div>";
        $("#content").html(html);
    });

    $("#otherItem").click(function(){
        $(".barItem").removeClass("active");
        $(this).addClass("active");
        //$("#content").load("../static/html/bmiCal.html")
    });

    $("#loginForm").submit(function() {

        var url = "/ajax/login/";

        $.ajax({
               type: "POST",
               url: url,
               data: $("#loginForm").serialize(), // serializes the form's elements.
               success: function(response)
               {
                   alert(response);
                   $('#loginModal').modal('hide')
               }
             });

        return false; // avoid to execute the actual submit of the form.
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
        bmi = (w/(h*h))*10000;
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