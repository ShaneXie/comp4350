
  var app = angular.module('cts', ['ngCookies']).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
  });

  app.config(['$httpProvider', function($httpProvider) {
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }]);


    app.controller('loginController', ['$http', '$cookies',function($http,$cookies){
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;

        this.loginInfo={};
        this.regInfo = {};

        this.login = function (){
          this.loginInfo.csrfmiddlewaretoken = $cookies.csrftoken;
          data=jQuery.param(this.loginInfo);
          $http.post('/ajax/login/',data).success(function (response) {
            if(response=="success"){
                 alert("Welcome Back!");
                //update csrf token
                $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
                 location.reload();
             }else{
                 alert(response);
             }

          });
      };

      this.reg = function (){
          this.regInfo.csrfmiddlewaretoken = $cookies.csrftoken;
          data=jQuery.param(this.regInfo);
          console.log(data);
          $http.post('/ajax/register/',data).success(function (response) {
            if(response=="success"){
                alert("Welcome to CTS!");
                //update csrf token
                $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
                location.reload();
             }else{
                 alert(response);
             }

          });
      };


    }]);


  

  app.controller('bmiController', function(){
    this.isStd = false;

    this.stdHgt;
    this.stdWgt;
    this.mtrHgt;
    this.mtrWgt;
    this.bmi;

    this.result = "Your BMI is ";
    this.resultReady = false;

    this.calc = function(){
      this.result = "Your BMI is ";
      if (this.isStd) {
        this.bmi = (this.stdWgt/(this.stdHgt*this.stdHgt))*703;
      } else {
        this.bmi = (this.mtrWgt/(this.mtrHgt*this.mtrHgt))*10000;
      }
      var msg="";
      this.result+=(Math.round(this.bmi * 100) / 100+" You are ");
      if(this.bmi<=18.5){
          msg = "Underweight ";
      }else if(this.bmi>18.5&&this.bmi<25){
          msg = "Normal weight";
      }else if(this.bmi>=25&&this.bmi<=29.9){
          msg = "Overweight";
      }else{
          msg = "Obesity";
      }
      this.result+=msg;
      this.resultReady = true;
    };

  });



