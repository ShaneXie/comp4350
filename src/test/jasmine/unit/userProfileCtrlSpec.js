describe('userProfileCtrlSpec', function(){
    var $httpBackend, rootScope,data, controller, scope;

    beforeEach(function () {
        module('cts');
        inject(function ($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            $httpBackend = $injector.get('$httpBackend');
            jasmine.getJSONFixtures().fixturesPath='base/test/jasmine/fixtures/';
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
        it('should get user profile', function(){
            $httpBackend.expectGET('/api/getProfile/');
            $httpBackend.flush();
            expect(scope.profileData).toBeDefined();
            expect(controller).toBeDefined();

        });
        it('should get the valid userprofile', function(){

            $httpBackend.expectGET('/api/getProfile/');
            $httpBackend.flush();
            expect(scope.profileData.weight).toBe(150);
            expect(scope.profileData.height).toBe(150);
            expect(scope.profileData.gender).toBe('Male');
        });
        it('should get user BMI', function(){
            $httpBackend.expectGET('/api/getProfile/');
            $httpBackend.flush();
            expect(scope.userBMI).not.toHaveBeenCalled();
            scope.userBMI();
            expect(scope.userBMI()).toBeDefined();
            expect(scope.userBMI).toHaveBeenCalled();
            expect(scope.userBMI()).toBe(66.67);
        });
        it('should get suggestion based on UserBMI', function(){
            $httpBackend.expectGET('/api/getProfile/');
            $httpBackend.flush();
            expect(scope.suggestion).toBe('');
            scope.userBMI();
            expect(scope.suggestion).toBe('You need to see a doctor as soon as possible.');
        });
    });
});
