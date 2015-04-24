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
                    delete data['avatar'];
                    console.log(data);
                    return $http({
                        method: 'PATCH',
                        url: '/api/v1/users/' + data.id + "/",
                        data: data,
                        headers: {'Content-Type': 'application/json'}
                    }).then(updateSuccessFn, updateErrorFn);

                    function updateSuccessFn(data, status, headers, config) {
                        alert("Данные изменены");
                    }

                    function updateErrorFn(data, status, headers, config){
                        alert(data.data);
                    }

                }
            };
        });
    })();