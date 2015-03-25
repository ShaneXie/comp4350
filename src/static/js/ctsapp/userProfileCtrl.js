app.run(function(editableOptions) {
    editableOptions.theme = 'bs3';
});

app.controller('userProfileController', ['$http','$filter', '$scope', function($http,$filter,$scope){

    $scope.profileData = [] ;
    $scope.suggestion = "";

    $http.get('/api/getProfile/').success(function(data){
        $scope.profileData = data.profile[0];

    });
    $scope.genders = [
        {value: 'Male', text: 'Male'},
        {value: 'Female', text: 'Female'}
    ];

    $scope.userBMI = function(){
        var bmi = ($scope.profileData.weight/($scope.profileData.height*$scope.profileData.height))*10000;
        if(bmi<=18.5){
            $scope.suggestion = "You are underweigth, you should consider consuming more calories.";
        }else if(bmi>18.5&&bmi<25){
            $scope.suggestion = "Your weight is normal, no change in diet or extra exercise is required.";
        }else if(bmi>=25&&bmi<=29.9){
            $scope.suggestion = "You are overweight, you should consider exercising more and eating less.";
        }else{
            $scope.suggestion = "You need to see a doctor as soon as possible.";
        }
        return Math.round(bmi * 100) / 100
    };
    $scope.checkWeight = function($data) {
        if ($data < 10 || $data > 700) {
            return "Error: Invalid weight";
        }else{
            $scope.profileData.weight = $data;
        }
    };
    $scope.checkHeight = function($data) {
        if ($data < 50 || $data > 250) {
            return "Error: Invalid height";
        }else{
            $scope.profileData.height = $data;
        }
    };
    $scope.showStatus = function(gender) {
        var selected = [];
        if(gender) {
            selected = $filter('filter')($scope.genders, {value: gender});
        }
        return selected.length ? selected[0].text : 'Not set';
    };

    $scope.succesAlertMessge = function(){
        $.scojs_message('User profile updated.', $.scojs_message.TYPE_OK);
    };

    $scope.failAlertMessge = function(response){
        $.scojs_message(response, $.scojs_message.TYPE_ERROR);
    };

    $scope.saveTable = function() {
        $scope.setCookies();
        data=jQuery.param($scope.profileData);
        $http.post('/ajax/updateProfile/',data).success(function (response) {
            if(response=="success"){
                $scope.succesAlertMessge();
            }else{
                $scope.failAlertMessge(response);
            }

        });
    };
}]);