(function () {
  'use strict';

  angular
    .module('application.static.controllers')
    .controller('NavbarController', NavbarController);

  NavbarController.$inject = ['Auth'];

  function NavbarController(Auth) {
    var vm = this;

    vm.isLoggedIn = !!Auth.getToken();
    vm.logout = logout;

    function logout() {
      Auth.logout();
    }
  }
})();
