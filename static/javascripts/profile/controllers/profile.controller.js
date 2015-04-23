(function () {
  'use strict';

  angular
    .module('application.profile.controllers')
    .controller('ProfileController', ProfileController);

  ProfileController.$inject = ['Auth'];

  function ProfileController(Auth) {
    var vm = this;
    vm.user = Auth.currentUser;
  }
})();
