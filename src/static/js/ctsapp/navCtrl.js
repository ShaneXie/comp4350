

app.controller('NavController', ['$http','$scope','$cookies',function($http,$scope,$cookies){
    //  0 ---- Login
    //  1 ---- Food List
    //  2 ---- BMI Calculator
    //  3 ---- About
    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;

    $scope.item = 1;

    $scope.loginInfo={};
    $scope.regInfo = {};
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
    $scope.login = function (){
        $scope.loginInfo.csrfmiddlewaretoken = $cookies.csrftoken;
        data=jQuery.param($scope.loginInfo);
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