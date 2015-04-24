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
              item: 'Профиль',
              url: '/profile'
          },
          {
              item: 'Группа',
              url: '/users'
          },
          {
              item: 'Преподаватели',
              url: '/teachers'
          },
          {
              item: 'Библиотека',
              url: '/'
          }
      ];
    vm.logout = logout;

    function logout() {
      Auth.logout();
    }
  }
})();
