(function () {
  'use strict';

  angular
    .module('application.static.controllers')
    .controller('SidebarController', SidebarController);

  SidebarController.$inject = ['Auth'];

  function SidebarController($scope,Auth) {
      var vm = this;

      vm.isLoggedIn = !!Auth.getToken();
      $scope.menuitems = [
          {
              item: 'Главная',
              url: '/'
          },
          {
              item: 'Группа',
              url: '/'
          },
          {
              item: 'Преподаватели',
              url: '/'
          },
          {
              item: 'Библиотека',
              url: '/'
          }
      ]
    vm.logout = logout;

    function logout() {
      Auth.logout();
    }

  }
})();
