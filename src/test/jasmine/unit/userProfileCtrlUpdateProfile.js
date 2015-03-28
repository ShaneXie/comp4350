describe('userProfileCtrlUpdateProfile', function() {
    var $httpBackend, rootScope, updatedDate, originalData, controller, scope;

    beforeEach(function () {
        module('cts');
        inject(function ($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            $httpBackend = $injector.get('$httpBackend');
            jasmine.getJSONFixtures().fixturesPath = 'base/test/jasmine/fixtures/';
            arr = getJSONFixture('userProfileUpdate.json');
            updatedDate = {};
            updatedDate['profile'] = arr;
            arr = getJSONFixture('userProfileTestData.json');
            originalData = {};
            originalData['profile'] = arr;
            controller = $injector.get('$controller')("userProfileController", {$scope: scope});
            $httpBackend.whenGET('/api/getProfile/').respond(originalData, 200, 'success');
            $httpBackend.when('POST', '/ajax/updateProfile/',
                function (postData) {
                    paramData = jQuery.param(scope.profileData);
                    expect(paramData).toBe(postData);
                    expect(scope.profileData.weight).toBe(updatedDate.profile[0].weight);
                    expect(scope.profileData.height).toBe(updatedDate.profile[0].height);
                    expect(scope.profileData.gender).toBe(updatedDate.profile[0].gender);
                    return true;
                }).respond(200, 'success');
        });

        spyOn(scope, 'succesAlertMessge');
        spyOn(scope, 'userBMI').and.callThrough();
    });
    afterEach(function () {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });

    describe("Generate request to update user profile", function () {
        it('should update user profile', function () {
            $httpBackend.expectGET('/api/getProfile/');
            $httpBackend.flush();
            expect(scope.profileData.weight).toBe(150);
            expect(scope.profileData.height).toBe(150);
            expect(scope.profileData.gender).toBe('Male');
            scope.userBMI();
            expect(scope.userBMI).toHaveBeenCalled();
            expect(scope.userBMI()).toBe(66.67);
            expect(scope.suggestion).toBe('You need to see a doctor as soon as possible.');

            scope.profileData = {weight: 40, height: 120, gender: "Female"};
            expect(scope.succesAlertMessge).not.toHaveBeenCalled();
            scope.saveTable();
            scope.userBMI();
            $httpBackend.flush();
            expect(scope.succesAlertMessge).toHaveBeenCalled();
            expect(scope.profileData.weight).toBe(40);
            expect(scope.profileData.height).toBe(120);
            expect(scope.profileData.gender).toBe('Female');
            expect(scope.userBMI).toHaveBeenCalled();
            expect(scope.userBMI()).toBe(27.78);
            expect(scope.suggestion).toBe('You are overweight, you should consider exercising more and eating less.');

        });
    });
});