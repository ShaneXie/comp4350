describe('navCtrlRequest', function(){
    var $httpBackend, rootScope,data, controller, scope;

    beforeEach(function () {
        module('cts');
        inject(function ($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            $httpBackend = $injector.get('$httpBackend');
            jasmine.getJSONFixtures().fixturesPath='/Users/niteshsinghania/GitHub/Comp4350/src/test/jasmine/fixtures/';
            data = getJSONFixture('userTestData.json');
            controller = $injector.get('$controller')("NavController",{$scope: scope});
            $httpBackend.when('POST','/ajax/login/',
                function(postData) {
                    expect(scope.loginInfo.loginEmailName).toBe(data[0].fields.username);
                    expect(scope.loginInfo.loginPwdName).toBe(data[0].fields.password);
                    expect(scope.loginInfo.csrfmiddlewaretoken).toBe('ABC');
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

    describe("Login user", function() {
        it('should get login success', function () {
            scope.loginInfo = {loginEmailName:'niteshsinghania@hotmail.com', loginPwdName:'testing', csrfmiddlewaretoken:'ABC'};
            expect(scope.setCookies).not.toHaveBeenCalled();
            scope.login();
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
