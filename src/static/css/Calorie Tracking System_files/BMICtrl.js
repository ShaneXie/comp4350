app.controller('bmiController',['$scope' , function($scope){
    $scope.isStd = false;
    $scope.stdHgt;
    $scope.stdWgt;
    $scope.mtrHgt;
    $scope.mtrWgt;
    $scope.bmi;
    var msg="";

    $scope.result = "Your BMI is ";
    $scope.resultReady = false;

    $scope.calc = function(){
      $scope.result = "Your BMI is ";
      if ($scope.isStd) {
        $scope.bmi = ($scope.stdWgt/($scope.stdHgt*$scope.stdHgt))*703;
      } else {
        $scope.bmi = ($scope.mtrWgt/($scope.mtrHgt*$scope.mtrHgt))*10000;
      }
      $scope.bmi = Math.round($scope.bmi * 100) / 100
      $scope.result+=($scope.bmi+" You are ");
      if($scope.bmi<=18.5){
          msg = "Underweight";
      }else if($scope.bmi>18.5&&$scope.bmi<25){
          msg = "Normal weight";
      }else if($scope.bmi>=25&&$scope.bmi<=29.9){
          msg = "Overweight";
      }else{
          msg = "Obese";
      }
      $scope.result+=msg;
      $scope.resultReady = true;
    };

  }]);

