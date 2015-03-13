describe('userProfileCtrlSpec', function(){
    var $httpBackend, rootScope,data, controller, scope;

    beforeEach(function () {
        module('cts');
        inject(function ($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            $httpBackend = $injector.get('$httpBackend');
            jasmine.getJSONFixtures().fixturesPath='/Users/niteshsinghania/GitHub/Comp4350/src/test/jasmine/fixtures/'
            data = getJSONFixture('userProfileTestData.json');
            controller = $injector.get('$controller')("userProfileController",{$scope: scope});
            $httpBackend.whenGET('/api/getProfile/').respond(data);

        });
    });
    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });
    describe("Generate request to get user profile", function(){
        it('should get valid user profile', function(){
            $httpBackend.expectGET('/api/getProfile/');
            $httpBackend.flush();
            expect(scope.profileData).toBeDefined();

        });
        it('should get the food list', function(){
            $httpBackend.expectGET('/api/getProfile/');
            $httpBackend.flush();
            expect(scope.profileData.weight).toBe(150);
            expect(scope.profileData.height).toBe(150);
            expect(scope.profileData.gender).toBe('Male');
            expect(scope.profileData.age).toBe(20);
            expect(scope.profileData.amtOfExc).toBeNull();
        });
    });
    describe("Generate request to get user profile", function(){
        it('should get user BMI', function(){
            $httpBackend.expectGET('/api/getProfile/');
            $httpBackend.flush();
            scope.$digest();
            expect(scope.userBMI()).toBeDefined();
            expect(scope.userBMI()).toBe(66.67);
        });
    });

});
