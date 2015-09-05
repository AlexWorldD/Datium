(function () {
  'use strict';

  angular
    .module('application.config')
    .config(config);

  config.$inject = ['$httpProvider', '$locationProvider'];

  function config($httpProvider, $locationProvider) {
    $httpProvider.interceptors.push('AuthInterceptor');

    $locationProvider.html5Mode(true).hashPrefix('!');  
  }
})();
