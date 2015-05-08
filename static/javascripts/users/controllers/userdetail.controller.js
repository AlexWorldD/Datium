(function () {
  'use strict';

  angular
    .module('application.users.controllers')
    .controller('UserDetailController', function (Users, $scope, $routeParams) {
    var vm = this;
    vm.id = $routeParams.userId;

    Users.getById(vm.id).then(function(data){
       vm.profile = data;
    });

  });
})();