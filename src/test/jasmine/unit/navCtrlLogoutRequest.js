describe('navCtrlLogoutRequest', function(){
    var $httpBackend, rootScope, controller, scope;

    beforeEach(function () {
        module('cts');
        inject(function ($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            $httpBackend = $injector.get('$httpBackend');
            controller = $injector.get('$controller')("NavController",{$scope: scope});
            $httpBackend.when('GET','/ajax/logout/').respond(200, 'success');
        });
        spyOn(scope,'reloadPage');

    });
    afterEach(function() {
        $httpBackend.verifyNoOutstandingExpectation();
        $httpBackend.verifyNoOutstandingRequest();
    });

    describe("Logout user", function() {
        it('should get logout success', function () {
            scope.logout();
            expect(scope).toBeTruthy();
            expect(scope).toBeDefined();
            expect(scope.reloadPage).not.toHaveBeenCalled();
            $httpBackend.flush();
            expect(scope.reloadPage).toHaveBeenCalled();
            expect(scope.contentURL).toBe('/ajax/getAllFood');

        });
    });
});
