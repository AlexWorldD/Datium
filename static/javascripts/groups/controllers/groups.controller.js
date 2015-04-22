(function () {
  'use strict';

  angular
    .module('application.groups.controllers')
    .controller('GroupsController', GroupsController);

  GroupsController.$inject = ['Groups', '$http'];

  function GroupsController($scope, $http) {
    var vm = this;
    vm.hello = "Hello World";
    vm.groups = [];

      $http.get("/api/v1/groups/").success(function (data) {
          vm.groups = data;
      })
  }
})();