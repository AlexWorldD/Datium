(function () {
    'use strict';
    angular
        .module('application.profile.services')
        .factory('Profile',function ($http, $window, Auth){
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
                        url: '/api/v1/users/' + $window.localStorage.getItem('username') + "/",
                        data: data,
                        headers: {'Content-Type': 'application/json'}
                    }).then(updateSuccessFn, updateErrorFn);

                    function updateSuccessFn(data, status, headers, config) {
                    }

                    function updateErrorFn(data, status, headers, config){
                    }
                },
                remove: function () {
                    return $http({
                        method: 'DELETE',
                        url: '/api/v1/users/' + $window.localStorage.getItem('username') + "/",
                        headers: {'Content-Type': 'application/json'}
                    }).then(removeSuccess, removeError);

                    function removeSuccess(data, status, headers, config){
                        Auth.logout();
                    }

                    function removeError(data, status, headers, config){
                        alert(status);
                    }
                }
            };
        });
    })();