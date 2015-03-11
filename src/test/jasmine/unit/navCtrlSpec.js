describe("NavControllerSpec",function(){
    //  0 ---- Login
    //  1 ---- Food List
    //  2 ---- BMI Calculator
    //  3 ---- About
    var rootScope,
        scope,
        controller;
    beforeEach(function () {
        module('cts');

        inject(function($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            controller = $injector.get('$controller')("NavController",{$scope: scope});
        });
    });

    describe("Initialization", function(){
       it("Should instantiate item and contentURL", function(){
           expect(scope.item).toEqual(1);
           expect(scope.contentURL).toEqual('/ajax/getAllFood');

       }) ;
    });

    describe("setItem to Login", function(){
       it("Should navigate to Login", function(){
            expect(scope.item).toBe(1);
            scope.setItem(0);
            scope.$digest();
            expect(scope.item).toEqual(0);
       }) ;
    });


    describe("setItem to Food List", function(){
       it("Should navigate to Food List", function(){
            expect(scope.item).toBe(1);
            scope.setItem(1);
            scope.$digest();
            expect(scope.item).toEqual(1);
       }) ;
    });


    describe("setItem to BMI Calculator", function(){
       it("Should navigate to Food List", function(){
            expect(scope.item).toBe(1);
            scope.setItem(2);
            scope.$digest();
            expect(scope.item).toEqual(2);
       }) ;
    });

    describe("setItem to About", function(){
       it("Should navigate to About", function(){
            expect(scope.item).toBe(1);
            scope.setItem(3);
            scope.$digest();
            expect(scope.item).toEqual(3);
       }) ;
    });


    describe("setItem from About to Food List", function(){
       it("Should navigate from About to Food List", function(){
            expect(scope.item).toBe(1);
            scope.setItem(3);
            scope.$digest();
            expect(scope.item).toEqual(3);
            scope.setItem(1);
            scope.$digest();
            expect(scope.item).toEqual(1);

       }) ;
    });

    describe("isSet to Food List", function(){
       it("Should check if current page is Food List page", function(){
            expect(scope.item).toBe(1);
            var itemAt = scope.isSet(1);
            scope.$digest();
            expect(itemAt).toBe(true);
       }) ;
    });

    describe("isSet to Food List", function(){
       it("Should check if current page is BMI Calculator page", function(){
            expect(scope.item).toBe(1);
            scope.setItem(3);
            var itemAt = scope.isSet(3);
            scope.$digest();
            expect(itemAt).toBe(true);
       }) ;
    });

    describe("showFoodList shows Food List", function(){
       it("Should check if item and contentURL are for Food List", function(){
            scope.showFoodList();
            scope.$digest();
            expect(scope.item).toBe(1);
            expect(scope.contentURL).toBe('/ajax/getAllFood');

       }) ;
    });

    describe("showBMICal shows BMI Calculator", function(){
       it("Should check if item and contentURL are for BMI Calculator", function(){
            scope.showBMICal();
            scope.$digest();
            expect(scope.item).toBe(2);
            expect(scope.contentURL).toBe("../static/html/bmiCal.html?v="+html_version);
       }) ;
    });

    describe("showAbout shows About", function(){
       it("Should check if item and contentURL are for About", function(){
            scope.showAbout();
            scope.$digest();
            expect(scope.item).toBe(3);
            expect(scope.contentURL).toBe("../static/html/about.html?v="+html_version);
       }) ;
    });

    describe("showProfile shows User Profile", function(){
       it("Should check if item and contentURL are for User Profile", function(){
            scope.showProfile();
            scope.$digest();
            expect(scope.item).toBe(4);
            expect(scope.contentURL).toBe('/ajax/getProfile');
       }) ;
    });
});