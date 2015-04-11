(function () {
  'use strict';

  angular
    .module('application.auth.interceptors')
    .service('AuthInterceptor', AuthInterceptor);

  AuthInterceptor.$inject = ['$injector', '$location', '$q'];

  function AuthInterceptor($injector, $location, $q) {
    var AuthInterceptor = {
      request: request,
      responseError: responseError
    };

    return AuthInterceptor;

    function request(config) {
      var Auth = $injector.get('Auth');
      var token = Auth.getToken();

      if (token) {
        config.headers['Authorization'] = 'JWT ' + token;
      }

      return config;
    }

    function responseError(response) {
      if (response.status === 403) {
        if (response.data.detial === 'Signature has expired.') {
          $location.path('/login');
        }
      }

      return $q.reject(response);
    }
  }
})();
