(function () {
  'use strict';

  angular
    .module('application.teachers', [
      'application.teachers.controllers',
      'application.teacherdetail.controllers',
      'application.teachers.services'
    ]);

    angular
        .module('application.teachers.controllers', []);
    angular
        .module('application.teacherdetail.controllers', []);
    angular
        .module('application.teachers.services', []);
})();
