(function () {
  'use strict';

  angular
    .module('application.comments.controllers')
    .controller('CommentsController', function(Comments, Profile, $window, $scope) {

          var vm = this;
          vm.init = function (table_id) {
            vm.table_id = table_id;
            Comments.all(vm.table_id).then(function (data) {
                vm.comments = data;
            });
              Profile.info().then(function (data) {
                vm.author = data.id;
              });
              vm.is_active = false;
          };

          vm.add = function (data) {
              data = {
                  text: vm.text,
                  author: vm.author,
                  table: vm.table_id
              };
              Comments.add(data);
          };

          vm.toggle = function () {
              vm.is_active = vm.is_active ? false : true;
          }
  });
})();
