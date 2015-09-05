(function () {
  'use strict';

  angular
    .module('application.teacherdetail.controllers')
    .controller('TeacherDetailController', function (Teachers, $scope, $routeParams) {
        var vm = this;
        vm.id = $routeParams.teacherId;

        Teachers.one(vm.id).then(function(data){
           vm.profile = data;
        });

        vm.update = function () {
            Teachers.update(vm.profile);
        };

        vm.remove = function () {
          if (!confirm("Вы действительно хотите удалить профиль?")) {
          } else {
              Teachers.remove(vm.id);
          }
        }

  });
})();