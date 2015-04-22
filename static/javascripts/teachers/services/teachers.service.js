(function () {
  'use strict';

  angular
    .module('application.teachers.services')
    .factory('Teachers', Teachers);

  Teachers.$inject = ['$http','$q'];

  function Teachers($http) {
    var Teachers = {
        teachers : [],
        getTeachers: getTeachers
    };

    return Teachers;

    function getTeachers(){
        var def = $q.defer();
        $http.get('/api/v1/teachers/')
            .success(function(data){
                Teachers.all = data;
                def.resolve(data);
            }).error(function(){
                def.reject("Fail");
            });
        return def.promise();
    }
  }
})();
