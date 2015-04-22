(function () {
  'use strict';

  angular
    .module('application', [
        'application.config',
        'application.routes',
        'application.auth',
        'application.static',
        'application.users',
        'application.teachers',
        'application.profile',
        'application.groups'
    ]);  

  angular
    .module('application.config', []);  

  angular
    .module('application.routes', ['ngRoute']);  
})();
