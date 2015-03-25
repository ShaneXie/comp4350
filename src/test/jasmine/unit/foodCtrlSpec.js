describe('foodCtrlSpec', function(){
    var $httpBackend, rootScope,data, controller, scope;

    beforeEach(function () {
        module('cts');
        inject(function ($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            $httpBackend = $injector.get('$httpBackend');
            jasmine.getJSONFixtures().fixturesPath='base/test/jasmine/fixtures/';
            arr = getJSONFixture('foodListTestData.json');
            data = {};
	        data["foods"]=arr;
            $httpBackend.whenGET('/api/getAllFood').respond(data, 200, 'success');
            controller = $injector.get('$controller')("foodListController",{$scope: scope});

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
            $httpBackend.expectGET('/api/getAllFood').respond(data, 200, "success");
            $httpBackend.flush();
            expect(scope.foods instanceof Array).toBeTruthy();
            expect(scope.foods.length).toBe(data.foods.length);
            expect(scope.foods[0].fType).toBe(data.foods[0].fType);
            expect(scope.foods[0].fName).toBe(data.foods[0].fName);
            expect(scope.foods[0].fCalorie).toBe(data.foods[0].fCalorie);

        });
    });
});
