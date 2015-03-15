describe('foodListControllerAddFood', function(){
    var $httpBackend, rootScope, data, controller, scope;

    beforeEach(function () {
        module('cts');
        inject(function ($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            $httpBackend = $injector.get('$httpBackend');
            jasmine.getJSONFixtures().fixturesPath='/Users/niteshsinghania/GitHub/Comp4350/src/test/jasmine/fixtures/';
            data = getJSONFixture('foodListTestData.json');
            controller = $injector.get('$controller')("foodListController",{$scope: scope});
            $httpBackend.whenGET('/api/getAllFood').respond(data, 200, 'success');
            $httpBackend.when('POST','/ajax/addFood/',
                function(postData) {
                    paramData=jQuery.param(scope.food);
                    expect(paramData).toBe(postData);
                    expect(scope.food.fType).toBe(data[0].fields.fType);
                    expect(scope.food.fCalorie).toBe(data[0].fields.fCalorie);
                    expect(scope.food.fName).toBe(data[0].fields.fName);
                    expect(scope.food.csrfmiddlewaretoken).toBe('ABC');
                    return true;
                }).respond(200, 'success');
        });

        spyOn(scope,'setCookies');
        spyOn(scope,'succesAlertMessge');
        spyOn(scope,'resetForm');
    });
    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });

    describe("Add food to the list", function() {
        it('should add food to the list', function () {

            scope.food = {fType: "d", fCalorie: 100, fName: "Chicken Burger",csrfmiddlewaretoken:'ABC'};
            expect(scope.setCookies).not.toHaveBeenCalled();
            expect(scope.succesAlertMessge).not.toHaveBeenCalled();
            expect(scope.resetForm).not.toHaveBeenCalled();
            scope.addFood();
            expect(scope.setCookies).toHaveBeenCalled();
            expect(scope).toBeTruthy();
            expect(scope).toBeDefined();
            $httpBackend.flush();
            expect(scope.succesAlertMessge).toHaveBeenCalled();
            expect(scope.resetForm).toHaveBeenCalled();

        });
    });
});
