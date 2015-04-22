(function () {
  'use strict';

  angular
    .module('application.routes')
    .config(config);

  config.$inject = ['$routeProvider'];

  function config($routeProvider) {
    $routeProvider.when('/', {
      controller: 'ProfileController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/static/index.html'
    }).when('/login', {
      controller: 'LoginController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/static/login.html'
    }).when('/register', {
      controller: 'RegisterController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/static/register.html'
    }).when('/users', {
      controller: 'UsersController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/static/users.html'
    }).when('/users/:userId', {
      controller: 'UserDetailController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/static/user-detail.html'
    }).when('/teachers', {
      controller: 'TeachersController',
      controllerAs: 'vm',
      templateUrl: '/static/templates/static/teachers.html'
    }).otherwise({
        redirectTo: '/'
    });
  }
})();
