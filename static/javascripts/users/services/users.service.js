(function () {
  'use strict';

  angular
    .module('application.users.services')
    .factory('Users', function($http) {
          return {
              all: function () {
                  return $http.get("/api/v1/users/").then(function (response) {
                      return response.data;
                  });
              },
              getById: function(id){
                  return $http.get("/api/v1/users/MisterMM/").then(function (response) {
                      return response.data;
                  })
              }
          };
      });
})();
