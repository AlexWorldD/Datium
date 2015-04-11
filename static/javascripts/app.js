(function () {
  'use strict';

  angular
    .module('application', [
      'application.config',
      'application.routes',
      'application.auth',
      'application.static'
    ]);  

  angular
    .module('application.config', []);  

  angular
    .module('application.routes', ['ngRoute']);  
})();
