(function () {
    'use strict';
    angular
        .module('application.comments.services')
        .factory('Comments',function ($http, $window, $route){
            return {
                all: function (table_id) {
                    return $http.get("/api/v1/commentstables/" + table_id + "/")
                        .then(function (response) {
                            return response.data.comments;
                        });
                },
                add: function(data){
                    return $http({
                        method: 'POST',
                        url: '/api/v1/comments/',
                        data: data,
                        headers: {'Content-Type': 'application/json'}
                    }).then(loginSuccessFn, loginErrorFn);

                    function loginSuccessFn(data, status, headers, config) {
                        $route.reload();
                    }

                    function loginErrorFn(data, status, headers, config) {
                        console.error(data);
                    }
                }
            };
        });
    })();