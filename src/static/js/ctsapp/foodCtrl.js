app.controller('foodListController', ['$scope', '$http', '$cookies',function($scope,$http,$cookies){

    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;

    $scope.foods = [];
    $scope.food = {};
    $scope.food.csrfmiddlewaretoken = $cookies.csrftoken;

    $http.get('/api/getAllFood').success(function(data){
        $scope.foods = angular.fromJson(data);
    });
    $scope.addFood = function (){
      
      data=jQuery.param($scope.food);
      $http.post('/ajax/addFood/',data).success(function (response) {
        if(response=="success"){
             $.scojs_message('New Food Added!', $.scojs_message.TYPE_OK);
             //$("#content").load("/ajax/getAllFood");
             newFood = '<tr><td>'+$('#addFoodName').val()+'</td><td>'+$('#addFoodCal').val()+'</td><td>'+$('#addFoodType option:selected').text()+'</td></tr>';
             $("#foodTable tr:first").after(newFood);
             $('#addFoodForm').trigger("reset");
             $scope.food = {};
             $scope.addFoodForm.$setPristine();
         }else{
             $.scojs_message(response, $.scojs_message.TYPE_ERROR);
         }

      });
    }
}]);