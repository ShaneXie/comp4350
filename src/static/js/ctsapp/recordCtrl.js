/**
 * Created by anx on 23/03/15.
 */
app.controller('recordController', ['$scope', '$http', '$cookies',function($scope,$http,$cookies){

    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;

    $scope.allFoods = [];
    $scope.record = {};

    $http.get('/api/getAllFood').success(function(data){
        $scope.allFoods = data.foods;
    });

    $scope.setCookies =function() {
        $scope.record.csrfmiddlewaretoken = $cookies.csrftoken;
    };

    $scope.succesAlertMessge = function(){
        $.scojs_message('New Food Added!', $.scojs_message.TYPE_OK);
    };

    $scope.failAlertMessge = function(response){
             $.scojs_message(response, $.scojs_message.TYPE_ERROR);
    };

    $scope.resetForm = function(){
        $scope.record = {};
        $scope.addFoodForm.$setPristine();
    };

    $scope.addRecord = function (){
      $scope.setCookies();
      data=jQuery.param($scope.record);
      $http.post('/ajax/addRecord/',data).success(function (response) {
        if(response=="success"){
             $scope.succesAlertMessge();
             //$("#content").load("/ajax/getAllFood");
             newFood = '<tr><td>'+$('#addFoodName').val()+'</td><td>'+$('#addFoodCal').val()+'</td><td>'+$('#addFoodType option:selected').text()+'</td></tr>';
             $("#foodTable tr:first").after(newFood);
             $('#addFoodForm').trigger("reset");
             $scope.resetForm();
         }else{
            $scope.failAlertMessge(response);
         }

      });
    }
}]);