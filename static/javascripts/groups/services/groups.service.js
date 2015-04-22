(function () {
  'use strict';

  angular
    .module('application.groups.services')
    .factory('Groups', Groups);

  Groups.$inject = ['$http','$q'];

  function Groups($http) {
    var Groups = {
        users : [],
        getGroups: getGroups
    };

    return Groups;

    function getGroups(){
        var def = $q.defer();
        $http.get('/api/v1/groups/')
            .success(function(data){
                Groups.all = data;
                def.resolve(data);
            }).error(function(){
                def.reject("Fail");
            });
        return def.promise();
    }
  }
})();
