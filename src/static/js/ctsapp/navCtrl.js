  app.controller('NavController', ['$http','$scope','$cookies',function($http,$scope,$cookies){
    //  0 ---- Login
    //  1 ---- Food List
    //  2 ---- BMI Calculator
    //  3 ---- About
    $scope.item = 1;
    $scope.contentURL = '/ajax/getAllFood';

    $scope.setItem = function(newValue){
      $scope.item = newValue;
    };

    $scope.isSet = function(theItem){
      return $scope.item === theItem;
    };

    $scope.showFoodList = function(){
      $scope.item = 1;
      $scope.contentURL = '/ajax/getAllFood';
    };

    $scope.showBMICal = function(){
      $scope.item = 2;
      var url = "../static/html/bmiCal.html?v="+Date.now();
      $scope.contentURL = url;
    };

    $scope.showAbout = function(){
      $scope.item = 3;
      var url = "../static/html/about.html?v="+Date.now();
      $scope.contentURL = url;
    };
    $scope.showProfile = function(){
      $scope.item = 4;
      $scope.contentURL = '/ajax/getProfile';
    };

    $scope.logout =function(){
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