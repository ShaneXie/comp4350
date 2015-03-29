// Karma configuration
// Generated on Sun Mar 08 2015 13:20:49 GMT-0500 (CDT)

module.exports = function(config) {
    config.set({

        // base path that will be used to resolve all patterns (eg. files, exclude)
        basePath: '../',


        // frameworks to use
        // available frameworks: https://npmjs.org/browse/keyword/karma-adapter
        frameworks: ['jasmine'],


        // list of files / patterns to load in the browser
        files: [

            // fixtures

            'test/jasmine/lib/angular.js',
            'static/js/angular-cookies.js',
            'static/js/jquery-2.1.3.min.js',
            'static/js/xeditable.js',
            'static/js/ctsapp/ctsapp.js',
            'static/js/ctsapp/*.js',
            'test/jasmine/lib/angular-mocks.js',
            'test/jasmine/lib/jasmine-jquery.js',
            'test/jasmine/lib/mock-ajax.js',
            'test/jasmine/unit/*.js',
            // JSON fixture
            { pattern: 'test/jasmine/fixtures/*.json',
                watched:  true,
                served:   true,
                included: false }

        ],


        // list of files to exclude
        exclude: [
        ],


        // preprocess matching files before serving them to the browser
        // available preprocessors: https://npmjs.org/browse/keyword/karma-preprocessor
        preprocessors: {
        },


        // test results reporter to use
        // possible values: 'dots', 'progress'
        // available reporters: https://npmjs.org/browse/keyword/karma-reporter
        reporters: ['progress'],


        // web server port
        port: 9876,


        // enable / disable colors in the output (reporters and logs)
        colors: true,


        // level of logging
        // possible values: config.LOG_DISABLE || config.LOG_ERROR || config.LOG_WARN || config.LOG_INFO || config.LOG_DEBUG
        logLevel: config.LOG_INFO,


        // enable / disable watching file and executing tests whenever any file changes
        autoWatch: true,


        // start these browsers
        // available browser launchers: https://npmjs.org/browse/keyword/karma-launcher
        browsers: ['Chrome'],


        // Continuous Integration mode
        // if true, Karma captures browsers, runs the tests and exits
        singleRun: false
    });
};
