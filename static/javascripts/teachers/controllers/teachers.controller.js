(function () {
  'use strict';

  angular
    .module('application.teachers.controllers')
    .controller('TeachersController', TeachersController);

  TeachersController.$inject = ['Teachers', '$http'];

  function TeachersController($scope, $http) {
      var vm = this;
      vm.teachers = [];

      $http.get("/api/v1/teachers/").success(function (data) {
          vm.teachers = data;
      })
  }
})();
