(function () {
    'use strict';
    angular
        .module('application.news.services')
        .factory('News',function ($http, $window){
            return {
                all: function () {
                    return $http.get("/api/v1/news/")
                        .then(function (response) {
                            return response.data;
                        });
                },
                publish: function(title, text){
                    $http({
                        method: 'POST',
                        url: '/api/v1/news/',
                        data: {title: title, text: text, documents:[]},
                        headers: {'Content-Type': 'application/json'}
                    }).then(loginSuccessFn, loginErrorFn);

                    function loginSuccessFn(data, status, headers, config) {
                        console.log("Success");
                    }

                    function loginErrorFn(data, status, headers, config) {
                        console.error(data);
                    }


                }
            };
        });
    })();