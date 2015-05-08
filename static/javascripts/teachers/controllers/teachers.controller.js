(function () {
  'use strict';

  angular
    .module('application.teachers.controllers')
    .controller('TeachersController', function (Teachers, $scope) {
    var vm = this;
          vm.test = "test";

    Teachers.all().then(function (data) {
        vm.teachers = data;
    });
          
          vm.add = function () {
              
          }

  });
})();