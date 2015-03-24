/**
 * Created by anx on 23/03/15.
 */
app.controller('recordController', ['$scope', '$http', '$cookies',function($scope,$http,$cookies){

    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;

    $scope.allFoods = [];
    $scope.records = [];
    $scope.record = {};

    $http.get('/api/getAllFood').success(function(data){
        $scope.allFoods = data.foods;
    });

    $scope.reloadRecord = function(){
        $http.get('/api/getRecord').success(function(data){
            $scope.records = data.records;
        });
    };

    $http.get('/api/getRecord').success(function(data){
        $scope.records = data.records;
    });

    $scope.setCookies =function() {
        $scope.record.csrfmiddlewaretoken = $cookies.csrftoken;
    };

    $scope.succesAlertMessge = function(){
        $.scojs_message('New Record Added!', $.scojs_message.TYPE_OK);
    };

    $scope.failAlertMessge = function(response){
             $.scojs_message(response, $.scojs_message.TYPE_ERROR);
    };

    $scope.resetForm = function(){
        $scope.record = {};
        $scope.newRecordForm.$setPristine();
    };

    $scope.addRecord = function (){
      $scope.setCookies();
      data=jQuery.param($scope.record);
      $http.post('/ajax/addRecord/',data).success(function (response) {
        if(response=="success"){
             $scope.succesAlertMessge();
             $('#newRecordForm').trigger("reset");
             $scope.resetForm();
         }else{
            $scope.failAlertMessge(response);
         }

      });
      $scope.reloadRecord();
    }
}]);