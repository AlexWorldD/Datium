(function () {
  'use strict';

  angular
    .module('application.auth.services')
    .factory('Users', Users);

  Users.$inject = ['$http'];

  function Users($http) {
    var Users = {
      all: all
    };

    return Users;

    function all() {
      return $http.get('/api/v1/users/');
    }
  }
})();
