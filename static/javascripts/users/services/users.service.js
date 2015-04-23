(function () {
  'use strict';

  angular
    .module('application.users.services')
    .factory('Users', function($http) {
          return {
              all: function () {
                  return $http.get("/api/v1/users/").then(function (response) {
                      console.log(response);
                      return response.data;
                  });
              }
          };
      });
})();
