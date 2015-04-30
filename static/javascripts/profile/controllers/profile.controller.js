(function () {
  'use strict';

  angular
    .module('application.profile.controllers')
    .controller('ProfileController', function(Profile, $window, $scope) {

          var vm = this;
          Profile.info().then(function(data){
              vm.profile = data;
          });

          vm.update = update;
          function update(){
                Profile.update(vm.profile);
          }

          vm.remove = function () {
              if (!confirm("Вы действительно хотите удалить свой аккаунт?")) {
              } else {
                  Profile.remove();
              }
          };

  });
})();
