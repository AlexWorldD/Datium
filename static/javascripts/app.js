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
        'application.groups',
        'xeditable'
    ]).run(function(editableOptions) {
        editableOptions.theme = 'bs3'; // bootstrap3 theme. Can be also 'bs2', 'default'
      });

  angular
    .module('application.config', []);  

  angular
    .module('application.routes', ['ngRoute']);  
})();
