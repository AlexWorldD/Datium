(function () {
  'use strict';

  angular
    .module('application.teachers.services')
    .factory('Teachers', function($http,$window) {
          return {
              all: function () {
                  return $http.get("/api/v1/teachers/").then(function (response) {
                      console.log(response);
                      return response.data;
                  });
              },
              one: function(id){
                  return $http.get("/api/v1/teachers/" + id).then(function (response) {
                      return response.data;
                  });
              },
              update: function(data){
                    console.log(data);
                    return $http({
                        method: 'PATCH',
                        url: '/api/v1/teachers/' + data.id + "/",
                        data: data,
                        headers: {'Content-Type': 'application/json'}
                    }).then(updateSuccessFn, updateErrorFn);

                    function updateSuccessFn(data, status, headers, config) {
                    }

                    function updateErrorFn(data, status, headers, config){
                    }
              },
              remove: function (id) {
                  return $http({
                      method: 'DELETE',
                      url: '/api/v1/teachers/' + id + "/",
                      headers: {'Content-Type': 'application/json'}
                  }).then(removeSuccess, removeError);

                  function removeSuccess(data, status, headers, config){
                      $window.redirectTo("/teachers");
                  }

                  function removeError(data, status, headers, config){
                      alert(status);
                  }
              },
              add: function(data){
                  $http({
                      method: 'POST',
                      url: '/api/v1/teachers/',
                      data: data,
                      headers: {'Content-Type': 'application/json'}
                  }).then(loginSuccessFn, loginErrorFn);

                  function loginSuccessFn(data, status, headers, config) {
                      console.log("New teacher was added");
                  }

                  function loginErrorFn(data, status, headers, config) {
                      console.error(data);
                  }
              }
          };
      });
})();