(function () {
  'use strict';

  angular
    .module('application.users.controllers')
    .controller('UsersController', function (Users, $scope) {
    var vm = this;

    Users.all().then(function (data) {
        vm.users = data;
    });
          
          vm.user_detail = function (id) {
              for(var user in vm.users){
                  if (user.id == id){
                      return user;
                  }
              }
          }
  });
})();