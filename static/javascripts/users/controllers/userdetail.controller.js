(function () {
  'use strict';
    angular.
        module('application.users.controllers')
            .controller('UserDetailController', function (Users, $scope, $routeParams) {
                var vm = this;

                if ($routeParams.userId != undefined) {
                    vm.id = $routeParams.userId;
                    Users.getById(vm.id).then(function (data) {
                        vm.profile = data;
                    });
                }

                vm.init = function (id) {
                    vm.id = id;
                    Users.getById(vm.id).then(function (data) {
                        vm.profile = data;
                    });
                };


                vm.remove = function () {
                    if (!confirm("Вы действительно хотите удалить аккаунт данного пользователя?")) {
                    } else {
                        Users.remove(vm.id);
                    }
                }

    });
})();