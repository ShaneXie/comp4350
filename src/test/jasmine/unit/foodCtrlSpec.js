describe('foodCtrlSpec', function(){
    var $httpBackend, rootScope,data, controller, scope;

    beforeEach(function () {
        module('cts');
        inject(function ($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            $httpBackend = $injector.get('$httpBackend');
            jasmine.getJSONFixtures().fixturesPath='/Users/niteshsinghania/GitHub/Comp4350/src/test/jasmine/fixtures/'
            data = getJSONFixture('foodListTestData.json');
            //console.log(data);
            controller = $injector.get('$controller')("foodListController",{$scope: scope});
            $httpBackend.whenGET('/api/getAllFood').respond(data);

        });
    });
    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });
    describe("Generate request to get food list", function(){
        it('should get valid response', function(){
            $httpBackend.expectGET('/api/getAllFood');
            $httpBackend.flush();
            expect(scope).toBeDefined();

        });
        it('should get the food list', function(){
            $httpBackend.expectGET('/api/getAllFood');
            $httpBackend.flush();
            expect(scope.foods.length).toBe(8);
            expect(scope.foods[0].fields.fType).toBe('d');
            expect(scope.foods[0].fields.fName).toBe('Chicken Burger');
            expect(scope.foods[0].fields.fCalorie).toBe(100);

        });
    });

});

