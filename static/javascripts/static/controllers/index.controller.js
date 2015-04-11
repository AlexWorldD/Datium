(function () {
  'use strict';

  angular
    .module('application.static.controllers')
    .controller('IndexController', IndexController);

  IndexController.$inject = ['$location', 'Auth', 'Users'];

  function IndexController($location, Auth, Users) {
    var vm = this;
  
    vm.users = [];

    activate();

    function activate() {
      if (!Auth.getToken()) {
        $location.path('/login');
      } else {
        Users.all().then(usersSuccessFn);
      }
    }

    function usersSuccessFn(data, status, headers, config) {
      vm.users = data.data.results;
    }  
  }
})();
