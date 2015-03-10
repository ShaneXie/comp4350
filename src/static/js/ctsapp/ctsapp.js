
  var app = angular.module('cts', ['ngCookies']).config(function($interpolateProvider){
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
  });

  app.config(['$httpProvider', function($httpProvider) {
      $httpProvider.defaults.xsrfCookieName = 'csrftoken';
      $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
  }]);


    app.controller('loginController', ['$http', '$scope' ,'$cookies',function($http,$cookies,$scope){
        $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
        $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;

        $scope.loginInfo={};
        $scope.regInfo = {};

        $scope.login = function (){
          $scope.loginInfo.csrfmiddlewaretoken = $cookies.csrftoken;
          data=jQuery.param($scope.loginInfo);
          console.log($scope.loginInfo);
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

      $scope.reg = function (){
          $scope.regInfo.csrfmiddlewaretoken = $cookies.csrftoken;
          data=jQuery.param($scope.regInfo);
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


  


