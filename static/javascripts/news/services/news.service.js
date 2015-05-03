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
                }
            };
        });
    })();