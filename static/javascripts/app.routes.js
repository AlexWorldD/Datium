(function () {
  'use strict';

  angular
    .module('application.routes')
    .config(function ($routeProvider) {
          $routeProvider.when('/', {
              controller: 'ProfileController',
              controllerAs: 'vm',
              templateUrl: '/static/templates/static/index.html'
          }).when('/login', {
              controller: 'LoginController',
              controllerAs: 'vm',
              templateUrl: '/static/templates/static/login.html'
          }).when('/profile', {
              controller: 'ProfileController',
              controllerAs: 'vm',
              templateUrl: '/static/templates/static/profile.html'
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
          }).when('/teachers/:teacherId', {
              controller: 'TeacherDetailController',
              controllerAs: 'vm',
              templateUrl: '/static/templates/static/teacher-detail.html'
          }).when('/add_teacher', {
              controller: 'TeacherDetailController',
              controllerAs: 'vm',
              templateUrl: '/static/templates/static/teacher-detail.html'
          }).otherwise({
                  redirectTo: '/'
              })
      }).run(function ($rootScope, $location, Auth) {
          $rootScope.$on("$routeChangeStart", function (event, next, current) {
              if (Auth.getToken() == null){
                  if ((next.templateUrl === "/static/templates/static/register.html") ||
                        (next.templateUrl === "/static/templates/static/login.html")){
                  }else{
                      // no logged user, redirect to /login
                      if (next.templateUrl === "/static/templates/static/login.html") {
                      } else {
                          $location.path("/login");
                      }
                  }
              }
          })
      });
})();
