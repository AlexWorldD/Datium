(function () {
  'use strict';

  angular
    .module('application.teachers.services')
    .factory('Teachers', function($http) {
          return {
              all: function () {
                  return $http.get("/api/v1/teachers/").then(function (response) {
                      console.log(response);
                      return response.data;
                  });
              }
          };
      });
})();