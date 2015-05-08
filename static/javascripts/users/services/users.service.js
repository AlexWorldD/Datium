(function () {
  'use strict';

  angular
    .module('application.users.services')
    .factory('Users', function($http, $window) {

          return {
              all: function () {
                  return $http.get("/api/v1/users/").then(function (response) {
                      return response.data;
                  });
              },
              getById: function(id){
                  return $http.get("/api/v1/users/id/" + id + "/").then(function (response) {
                      return response.data;
                  });
              },
              remove: function(id){
                  return $http({
                        method: 'DELETE',
                        url: '/api/v1/users/id/' + id + "/",
                        headers: {'Content-Type': 'application/json'}
                    }).then(removeSuccess, removeError);

                    function removeSuccess(data, status, headers, config){
                        $window.location = "/users";
                    }

                    function removeError(data, status, headers, config){
                        alert(status);
                    }
              }
          };
      });
})();
