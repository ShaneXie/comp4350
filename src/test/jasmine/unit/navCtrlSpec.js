describe("NavControllerSpec",function(){
    //  0 ---- Login
    //  1 ---- Food List
    //  2 ---- BMI Calculator
    //  3 ---- About
    var rootScope,
        scope,
        controller,
        html_version = 1.2;
    beforeEach(function () {
        module('cts');

        inject(function($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            controller = $injector.get('$controller')("NavController",{$scope: scope});
        });
        spyOn(scope,'setItem').and.callThrough();
        spyOn(scope,'isSet').and.callThrough();
        spyOn(scope,'showFoodList').and.callThrough();
        spyOn(scope,'showBMICal').and.callThrough();
        spyOn(scope,'showAbout').and.callThrough();
        spyOn(scope,'showProfile').and.callThrough();

    });

    describe("Initialization", function(){
        it("Should instantiate item and contentURL", function(){
            expect(scope.item).toEqual(1);
            expect(scope.contentURL).toEqual('/ajax/getAllFood');

        }) ;
    });

    it("Should navigate to Login", function(){
        expect(scope.item).toBe(1);
        scope.setItem(0);
        expect(scope.item).toEqual(0);
    }) ;


    it("Should navigate to Food List", function(){
        expect(scope.item).toBe(1);
        scope.setItem(1);
        expect(scope.item).toEqual(1);
    }) ;


    it("Should navigate to BMI calculator", function(){
        expect(scope.item).toBe(1);
        scope.setItem(2);
        expect(scope.item).toEqual(2);
    }) ;

    it("Should navigate to About", function(){
        expect(scope.item).toBe(1);
        scope.setItem(3);
        expect(scope.item).toEqual(3);
    }) ;


    it("Should navigate from About to Food List", function(){
        expect(scope.item).toBe(1);
        scope.setItem(3);
        expect(scope.item).toEqual(3);
        scope.setItem(1);
        expect(scope.item).toEqual(1);

    }) ;

    it("Should check if current page is Food List page", function(){
        expect(scope.item).toBe(1);
        expect(scope.isSet).not.toHaveBeenCalled();
        var itemAt = scope.isSet(1);
        expect(scope.isSet).toHaveBeenCalled();
        expect(itemAt).toBe(true);
    }) ;

    it("Should check if current page is BMI Calculator page", function(){
        expect(scope.item).toBe(1);
        expect(scope.isSet).not.toHaveBeenCalled();
        scope.setItem(3);
        var itemAt = scope.isSet(3);
        expect(scope.isSet).toHaveBeenCalled();
        expect(itemAt).toBe(true);
    }) ;

    it("Should check if item and contentURL are for Food List", function(){
        expect(scope.showFoodList).not.toHaveBeenCalled();
        scope.showFoodList();
        expect(scope.showFoodList).toHaveBeenCalled();
        expect(scope.item).toBe(1);
        expect(scope.contentURL).toBe('/ajax/getAllFood');

    }) ;

    it("Should check if item and contentURL are for BMI Calculator", function(){
        expect(scope.showBMICal).not.toHaveBeenCalled();
        scope.showBMICal();
        expect(scope.showBMICal).toHaveBeenCalled();
        expect(scope.item).toBe(2);
        expect(scope.contentURL).toBe("../static/html/bmiCal.html?v="+html_version);
    }) ;

    it("Should check if item and contentURL are for About", function(){
        expect(scope.showAbout).not.toHaveBeenCalled();
        scope.showAbout();
        expect(scope.showAbout).toHaveBeenCalled();
        expect(scope.item).toBe(3);
        expect(scope.contentURL).toBe("../static/html/about.html?v="+html_version);
    }) ;

    it("Should check if item and contentURL are for User Profile", function(){
        expect(scope.showProfile).not.toHaveBeenCalled();
        scope.showProfile();
        expect(scope.showProfile).toHaveBeenCalled();
        expect(scope.item).toBe(4);
        expect(scope.contentURL).toBe('/ajax/getProfile');
    }) ;
});