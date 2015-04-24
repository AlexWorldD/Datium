(function () {
    'use strict';
    angular
        .module('application.profile.services')
        .factory('Profile',function ($http, $window){
            return {
                info: function () {
                    return $http.get("/api/v1/users/" + $window.localStorage.getItem('username') + "/")
                        .then(function (response) {
                            return response.data;
                        });
                },
                update: function(data){
                    return $http.patch('/api/v1/users/' + data.id + "/", data)
                        .then(updateSuccessFn);

                    function updateSuccessFn(data, status, headers, config) {

                    }

                }
            };
        });
    })();