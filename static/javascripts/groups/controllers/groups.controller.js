(function () {
  'use strict';

  angular
    .module('application.groups.controllers')
    .controller('GroupsController', function (Groups, $scope) {
    var vm = this;

          Groups.all().then(function (data) {
              vm.groups = data;
          })
  })
})();