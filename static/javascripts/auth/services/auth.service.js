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
      setToken: setToken,
        user : {}
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
            url: '/api/v1/auth/login/',
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
      $window.location = '/login';
    }

    function register(username, password, email, group) {
        console.log(username);
        return $http.post('/api/v1/users/', {
        username: username, password: password, email: email, group: group
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
