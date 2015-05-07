(function () {
  'use strict';

  angular
    .module('application.users.controllers')
    .controller('UsersController', function (Users, $scope) {
    var vm = this;

    Users.all().then(function (data) {
        vm.users = data;
    });

      vm.profile = function (id) {
        return Users.getById(id);
      }

  });
})();