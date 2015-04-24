(function () {
  'use strict';

  angular
    .module('application.auth.controllers')
    .controller('LoginController', function (Auth) {
    var vm = this;

    vm.login = login;

    function login() {
        Auth.login(vm.username, vm.password);
    }
  })
})();
