(function () {
  'use strict';

  angular
    .module('application.teachers.controllers')
    .controller('TeachersController', function (Teachers, $scope) {
    var vm = this;

    Teachers.all().then(function (data) {
        vm.teachers = data;
    });

  });
})();