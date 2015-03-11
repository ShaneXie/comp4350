describe("bmiControllerSpec",function(){

    var rootScope,
        scope,
        controller;
    beforeEach(function () {
        module('cts');

        inject(function($injector) {
            rootScope = $injector.get('$rootScope');
            scope = rootScope.$new();
            controller = $injector.get('$controller')("bmiController",{$scope: scope});
        });
    });

    describe("Initialization", function(){
       it("Should instantiate isStd,result and resultReady", function(){
           expect(scope.isStd).toEqual(false);
           expect(scope.result).toEqual("Your BMI is ");
           expect(scope.resultReady).toEqual(false);

       }) ;
    });


    describe("Generate result", function(){
       it("Should generate the result", function(){
           scope.calc();
           scope.$digest();
           expect(scope.resultReady).toEqual(true);

       }) ;
    });

    describe("Generate invalid BMI result", function(){
       it("Should generate invalid BMI result", function(){
           scope.calc();
           scope.$digest();
           expect(scope.resultReady).toEqual(true);
           expect(scope.result).toEqual("Your BMI is NaN You are Obese");

       }) ;
    });

    describe("Generate valid BMI result", function(){
       it("Should generate valid Standard BMI result", function(){
           scope.stdHgt = 150;
           scope.stdWgt = 150;
           scope.isStd = true;
           scope.calc();
           scope.$digest();
           expect(scope.bmi).toEqual(4.69);
           expect(scope.resultReady).toEqual(true);
           expect(scope.result).toEqual("Your BMI is 4.69 You are Underweight");

       }) ;
    });


    describe("Generate valid BMI result", function(){
       it("Should generate valid Metric BMI result", function(){
           scope.mtrHgt = 150;
           scope.mtrWgt = 150;
           scope.isStd = false;
           scope.calc();
           scope.$digest();
           expect(scope.bmi).toEqual(66.67);
           expect(scope.resultReady).toEqual(true);
           expect(scope.result).toEqual("Your BMI is 66.67 You are Obese");

       }) ;
    });
});