(function () {
  'use strict';

  angular
    .module('application.auth.controllers')
    .controller('LoginController', LoginController);

  LoginController.$inject = ['Auth'];

  function LoginController(Auth) {
    var vm = this;

    vm.login = login;

    function login() {
        Auth.login(vm.username, vm.password);
    }
  }
})();
