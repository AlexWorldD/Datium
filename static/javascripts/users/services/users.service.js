(function () {
  'use strict';

  angular
    .module('application.users.services')
    .factory('Users', Users);

  Users.$inject = ['$http','$q'];

  function Users($http) {
    var Users = {
        users : [],
        getUsers: getUsers
    };

    return Users;

    function getUsers(){
        var def = $q.defer();
        $http.get('/api/v1/users/')
            .success(function(data){
                Users.all = data;
                def.resolve(data);
            }).error(function(){
                def.reject("Fail");
            });
        return def.promise();
    }
  }
})();
