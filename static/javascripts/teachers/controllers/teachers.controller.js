(function () {
  'use strict';

  angular
    .module('application.teachers.controllers')
    .controller('TeachersController', function (Teachers, $scope) {
    var vm = this;

    Teachers.all().then(function (data) {
        vm.teachers = data;
    });

          vm.new_teacher = {}

          vm.add = function () {
              if (vm.new_teacher.last_name){
                    Teachers.add(vm.new_teacher);
              }else{
                  console.log(vm.new_teacher.last_name);
              }
          }

  });
})();