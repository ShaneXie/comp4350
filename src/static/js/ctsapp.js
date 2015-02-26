(function() {
  var app = angular.module('cts', []).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
  });

  app.controller('foodListController', f['$http', function($http){
  var foodList = this;
  foodList.foods = [];

    $http.get('/api/getAllFood').success(function(data){
      foodList.foods = data;
    });
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
      };
      var msg=""
      this.result+=(this.bmi+" You are ");
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

  app.controller('NavController', function() {
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
      this.contentURL = "../static/html/bmiCal.html";
    };

    this.showAbout = function(){
      this.item = 3;
      this.contentURL = "../static/html/about.html";
    };
    
  });

})();