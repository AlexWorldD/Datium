(function () {
  'use strict';

  angular
    .module('application.users.controllers')
    .controller('UsersController', UsersController);

  UsersController.$inject = ['Users', '$http'];

  function UsersController($scope, $http) {
    var vm = this;
    vm.hello = "Hello World";
    vm.users = [];

      $http.get("/api/v1/users/").success(function (data) {
          vm.users = data;
      })
  }
})();