(function () {
    'use strict';
    angular
        .module('application.news.services')
        .factory('News',function ($http, $route){
            return {
                all: function () {
                    return $http.get("/api/v1/news/")
                        .then(function (response) {
                            return response.data;
                        });
                },
                add: function(title, text){
                    return $http({
                        method: 'POST',
                        url: '/api/v1/news/',
                        data: {title: title, text: text, documents:[]},
                        headers: {'Content-Type': 'application/json'}
                    }).then(loginSuccessFn, loginErrorFn);

                    function loginSuccessFn(data, status, headers, config) {
                        $route.reload();
                        return data;
                    }

                    function loginErrorFn(data, status, headers, config) {
                        console.error(data);
                    }
                },
                remove: function (id) {
                  return $http({
                      method: 'DELETE',
                      url: '/api/v1/news/' + id + "/",
                      headers: {'Content-Type': 'application/json'}
                  }).then(removeSuccess, removeError);

                  function removeSuccess(data, status, headers, config){
                  }

                  function removeError(data, status, headers, config){

                  }
                }

            };
        });
    })();