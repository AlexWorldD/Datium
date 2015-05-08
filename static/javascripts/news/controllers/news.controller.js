(function () {
  'use strict';



  angular
    .module('application.news.controllers')
    .controller('NewsController', function(News, Users, $window, $scope) {

          var vm = this;

          News.all().then(function (data) {

              vm.news = data;
              data.reverse();
              console.log(data);

          });

          vm.add = add;

          function add() {
              News.add(vm.title, vm.text);
          }

          vm.remove = function (id) {
              console.log("click was");
              News.remove(id);
          }

  });
})();
