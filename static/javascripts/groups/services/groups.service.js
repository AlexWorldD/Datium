(function () {
  'use strict';

  angular
    .module('application.groups.services')
    .factory('Groups', function ($http) {
        return {
            all: function (){
                return $http.get("/api/v1/groups/").then(function(response){
                    return response.data;
                })
            }
        };
    })
})();
