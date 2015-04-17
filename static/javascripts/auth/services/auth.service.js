(function () {
  'use strict';

  angular
    .module('application.auth.services')
    .factory('Auth', Auth);

  Auth.$inject = ['$http', '$window'];

  function Auth($http, $window) {
    var Auth = {
      deleteToken: deleteToken,
      getToken: getToken,
      login: login,
      logout: logout,
      register: register,
      setToken: setToken
    };

    return Auth;

    function deleteToken() {
      $window.localStorage.removeItem('token');
    }

    function getToken() {
      return $window.localStorage.getItem('token');
    }

    function login(username, password) {

        $http({
            method: 'POST',
            url: '/api/v1/authentication/login/',
            data: {username: username, password: password},
            headers: {'Content-Type': 'application/json'}
        }).then(loginSuccessFn, loginErrorFn);

      function loginSuccessFn(data, status, headers, config) {
        if (data.data.token) {
          Auth.setToken(data.data.token);
        }

        $window.location = '/';
      }

      function loginErrorFn(data, status, headers, config) {
        console.error(data);
      }
    }

    function logout() {
      Auth.deleteToken();
      $window.location = '/';
    }

    function register(username, password, email) {
      return $http.post('/api/v1/authentication/', {
        username: username, password: password, email: email
      }).then(registerSuccessFn);

      function registerSuccessFn(data, status, headers, config) {
        Auth.login(username, password);
      }
    }

    function setToken(token) {
      $window.localStorage.setItem('token', token);
    }
  }
})();
