(function () {
  'use strict';

  angular
    .module('application.users.controllers')
    .controller('UsersController', function (Users, $scope) {
    var vm = this;

    Users.all().then(function (data) {
        vm.users = data;
    });

<<<<<<< HEAD
          vm.profile = function (id) {
              Users.getById(id).then(function (data) {
                  return data;
              })
          }
=======
      vm.profile = function (id) {
        return Users.getById(id);
      }
>>>>>>> dc631699d0d78df45585744ed871e301eab6a45c

  });
})();