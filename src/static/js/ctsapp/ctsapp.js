
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

  app.controller('NavController', ['$http','$cookies',function($http,$cookies){
    //  0 ---- Login
    //  1 ---- Food List
    //  2 ---- BMI Calculator
    //  3 ---- About
    this.item = 1;
    this.contentURL = '/ajax/getAllFood';

    this.setItem = function(newValue){
      this.item = newValue;
    };

    this.isSet = function(theItem){
      return this.item === theItem;
    };

    this.showFoodList = function(){
      this.item = 1;
      this.contentURL = '/ajax/getAllFood';
    };

    this.showBMICal = function(){
      this.item = 2;
      var url = "../static/html/bmiCal.html?v="+Date.now();
      this.contentURL = url;
    };

    this.showAbout = function(){
      this.item = 3;
      var url = "../static/html/about.html?v="+Date.now();
      this.contentURL = url;
    };
    this.showProfile = function(){
      this.item = 4;
      this.contentURL = '/ajax/getProfile';
    };

    this.logout =function(){
        $http.get('/ajax/logout/').success(function (response) {
            if(response=="success") {
               alert("Bye Bye");
               location.reload();

           }else{
               alert("Logout Ajax Error");
           }
        });
      };
    
  }]);

