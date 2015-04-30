(function () {
  'use strict';

  angular
    .module('application.static.controllers')
    .controller('SidebarController', SidebarController);

  SidebarController.$inject = ['Auth'];

  function SidebarController(Auth, $scope) {
      var vm = this;

      vm.isLoggedIn = !!Auth.getToken();
      vm.menuitems = [
          {
              item: 'Main',
              url: '/index'
          },
          {
              item: 'Profile',
              url: '/profile'
          },
          {
              item: 'Our group',
              url: '/users'
          },
          {
              item: 'Staff',
              url: '/teachers'
          },
          {
              item: 'Library',
              url: '/'
          }
      ];
    vm.logout = logout;

    function logout() {
      Auth.logout();
    }
  }
})();
