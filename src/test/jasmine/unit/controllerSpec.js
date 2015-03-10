describe("true",function(){
	it("should be true", function(){
		expect(true).toBeTruthy();
	});

});

describe("foodListController",function(){
    var $rootScope,
        $scope,
        controller;
    beforeEach(function () {
        module('cts');

        inject(function($injector) {
            $rootScope = $injector.get('$rootScope');
            $scope = $rootScope.$new();
            controller = $injector.get('$controller')("foodListController",{$scope: $scope});
        });
    });

    describe("Initialization", function(){
       it("Should instantiate item to 1", function(){
           expect($scope.item).toEqual(1);
       }) ;
    });

});