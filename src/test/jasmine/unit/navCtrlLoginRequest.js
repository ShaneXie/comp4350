describe('navCtrlRequest', function(){
    var $httpBackend, rootScope,data, controller, scope;

    beforeEach(function () {
        module('cts');
        inject(function ($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            $httpBackend = $injector.get('$httpBackend');
            jasmine.getJSONFixtures().fixturesPath='/Users/niteshsinghania/GitHub/Comp4350/src/test/jasmine/fixtures/'
            data = getJSONFixture('userTestData.json');
            controller = $injector.get('$controller')("NavController",{$scope: scope});
            $httpBackend.when('POST','/ajax/login/', {username: 'user', password: 'pass'}, { withCredentials: true}).respond(200, 'success');
        });
        spyOn(scope,'reloadPage');

    });
   afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });

    it('should get login success',function() {
        scope.login('niteshsinghania@hotmail.com', 'test');
        $httpBackend.expect('POST','/ajax/login/').respond(200, "success");
        expect(scope).toBeDefined();
        expect(scope).toBeTruthy();
        expect(scope.contentURL).toBe('/ajax/getAllFood');
        expect(scope.isSet(1)).toBe(true);
        expect(scope.reloadPage).not.toHaveBeenCalled();
        $httpBackend.flush();
        expect(scope.reloadPage).toHaveBeenCalled();

    });
});