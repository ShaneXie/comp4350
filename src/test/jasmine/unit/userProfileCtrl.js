describe('userProfileCtrl', function(){
    var $httpBackend, rootScope,data, controller, scope;

    beforeEach(function () {
        module('cts');
        inject(function ($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            $httpBackend = $injector.get('$httpBackend');
            jasmine.getJSONFixtures().fixturesPath='base/test/jasmine/fixtures/'
            arr = getJSONFixture('userProfileTestData.json');
            data = {}
            data['profile']= arr
            controller = $injector.get('$controller')("userProfileController",{$scope: scope});
            $httpBackend.whenGET('/api/getProfile/').respond(data);
        });
        spyOn(scope,'userBMI').and.callThrough();
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
            expect(controller).toBeDefined();

        });
        it('should get the food list', function(){

            $httpBackend.expectGET('/api/getProfile/');
            $httpBackend.flush();
            expect(scope.profileData.weight).toBe(150);
            expect(scope.profileData.height).toBe(150);
            expect(scope.profileData.gender).toBe('Male');
        });
    });
    describe("Generate request to get user profile", function(){
        it('should get user BMI', function(){
            $httpBackend.expectGET('/api/getProfile/');
            $httpBackend.flush();
            expect(scope.userBMI).not.toHaveBeenCalled();
            scope.userBMI();
            expect(scope.userBMI()).toBeDefined();
            expect(scope.userBMI).toHaveBeenCalled();
            expect(scope.userBMI()).toBe(66.67);
        });
    });
});
