describe('recordCtrlSpec', function(){
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
            controller = $injector.get('$controller')("recordController",{$scope: scope});

        });
    });
    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });


    describe("Generate request to get food list", function(){
        it('should get valid response', function(){
            spyOn(scope,'reloadRecord');
            $httpBackend.expectGET('/api/getAllFood');
            $httpBackend.flush();
            expect(scope).toBeDefined();


        });
        it('should get the food list', function(){
            spyOn(scope,'reloadRecord');
            $httpBackend.expectGET('/api/getAllFood').respond(data, 200, "success");
            $httpBackend.flush();
            expect(scope.allFoods instanceof Array).toBeTruthy();
            expect(scope.allFoods.length).toBe(data.foods.length);
            expect(scope.allFoods[0].fType).toBe(data.foods[0].fType);
            expect(scope.allFoods[0].fName).toBe(data.foods[0].fName);
            expect(scope.allFoods[0].fCalorie).toBe(data.foods[0].fCalorie);

        });
    });
});
