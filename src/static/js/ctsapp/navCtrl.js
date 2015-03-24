app.controller('NavController', ['$http','$scope','$cookies','$rootScope',function($http,$scope,$rootScope,$cookies){

    $rootScope.html_version = 1.2; //update this when make changes to any static html file
    //  0 ---- Login
    //  1 ---- Food List
    //  2 ---- BMI Calculator
    //  3 ---- About
    //  4 ---- showProfile
    //  5 ---- add new record
    $http.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';
    $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;

    if($('#isLoggedin').length) {
        $scope.item = 5;
        $scope.contentURL = '/ajax/newRecord';
    }else{
        $scope.item = 1;
        $scope.contentURL = '/ajax/getAllFood';
    }
    $scope.loginInfo={};
    $scope.regInfo = {};


    $scope.reloadPage =function() {
        location.reload();
    };
    $scope.setCookies =function() {
        $scope.loginInfo.csrfmiddlewaretoken = $cookies.csrftoken;
    };

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
        var url = "../static/html/bmiCal.html?v="+$rootScope.html_version;
        $scope.contentURL = url;
    };

    $scope.showAbout = function(){
        $scope.item = 3;
        var url = "../static/html/about.html?v="+$rootScope.html_version;
        $scope.contentURL = url;
    };
    $scope.showProfile = function(){
        $scope.item = 4;
        $scope.contentURL = '/ajax/getProfile';
    };
    $scope.showNewRecord = function(){
        $scope.item = 5;
        $scope.contentURL = '/ajax/newRecord';
    };

    $scope.reg = function (){
        $scope.setCookies();
        data=jQuery.param($scope.regInfo);
        $http.post('/ajax/register/',data).success(function (response) {
            if(response=="success"){
                //update csrf token
                $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
                $scope.reloadPage();
            }else{
                $.scojs_message(response, $.scojs_message.TYPE_ERROR);
            }

        });
    };
    $scope.login = function (){
        $scope.setCookies();
        data=jQuery.param($scope.loginInfo);
        $http.post('/ajax/login/',data).success(function (response) {
            if(response=="success"){
                //update csrf token
                $http.defaults.headers.post['X-CSRFToken'] = $cookies.csrftoken;
                $scope.reloadPage();
            }else{
                $.scojs_message(response, $.scojs_message.TYPE_ERROR);
            }

        });
    };
    $scope.logout =function(){
        $http.get('/ajax/logout/').success(function (response) {
            if(response=="success") {
                $scope.reloadPage();
            }else{
                $.scojs_message("Logout fail: Ajax Error", $.scojs_message.TYPE_ERROR);
            }
        });
    };

}]);