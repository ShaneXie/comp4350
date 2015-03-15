describe('navCtrlRegisterRequest', function(){
    var $httpBackend, rootScope,userData,userProfileData, controller, scope;

    beforeEach(function () {
        module('cts');
        inject(function ($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            $httpBackend = $injector.get('$httpBackend');
            jasmine.getJSONFixtures().fixturesPath='/Users/niteshsinghania/GitHub/Comp4350/src/test/jasmine/fixtures/';
            userData = getJSONFixture('userTestData.json');
            userProfileData = getJSONFixture('userProfileTestData.json');
            controller = $injector.get('$controller')("NavController",{$scope: scope});
            $httpBackend.when('POST','/ajax/register/',
                function(postData) {
                    paramData=jQuery.param(scope.regInfo);
                    expect(paramData).toBe(postData);
                    expect(scope.regInfo.genName).toBe(userProfileData[0].fields.gender);
                    expect(scope.regInfo.regEmailName).toBe(userData[0].fields.username);
                    expect(scope.regInfo.regFirstName).toBe(userData[0].fields.first_name);
                    expect(scope.regInfo.regHgtName).toBe(userProfileData[0].fields.height);
                    expect(scope.regInfo.regLastName).toBe(userData[0].fields.last_name);
                    expect(scope.regInfo.regPwdName).toBe(userData[0].fields.password);
                    expect(scope.regInfo.regWgtName).toBe(userProfileData[0].fields.weight);
                    expect(scope.regInfo.csrfmiddlewaretoken).toBe('ABC');
                    return true;
                }).respond(200, 'success');
        });
        spyOn(scope,'reloadPage');
        spyOn(scope,'setCookies');

    });
    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });

    describe("Register user", function() {
        it('should Register the user', function () {

            scope.regInfo = {genName: "Male", regEmailName: "test@hotmail.com",regFirstName: "FnameTest",regHgtName: 150,regLastName: "LnameTest",regPwdName: "testing", regWgtName: 150,csrfmiddlewaretoken:'ABC'};
            expect(scope.setCookies).not.toHaveBeenCalled();
            scope.reg();
            expect(scope.setCookies).toHaveBeenCalled();
            expect(scope).toBeTruthy();
            expect(scope).toBeDefined();
            expect(scope.contentURL).toBe('/ajax/getAllFood');
            expect(scope.isSet(1)).toBe(true);
            expect(scope.reloadPage).not.toHaveBeenCalled();
            $httpBackend.flush();
            expect(scope.reloadPage).toHaveBeenCalled();
            expect(scope.contentURL).toBe('/ajax/getAllFood');

        });
    });
});
