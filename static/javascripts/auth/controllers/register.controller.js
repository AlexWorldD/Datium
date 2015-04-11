(function () {
  'use strict';

  angular
    .module('application.auth.controllers')
    .controller('RegisterController', RegisterController);

  RegisterController.$inject = ['Auth'];

  function RegisterController(Auth) {
    var vm = this;

    vm.register = register;

    function register() {
      Auth.register(vm.username, vm.password, vm.email);
    }
  }
})();
