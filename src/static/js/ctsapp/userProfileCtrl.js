app.controller('userProfileController', ['$http', '$scope', function($http,$scope){

    $scope.profileData = [] ;

    $http.get('/api/getProfile/').success(function(data){

      $scope.profileData = angular.fromJson(data)[0].fields;

    });

      $scope.userBMI = function(){
          var bmi = ($scope.profileData.weight/($scope.profileData.height*$scope.profileData.height))*10000;
          return Math.round(bmi * 100) / 100
      }

}]);