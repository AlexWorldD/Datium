(function () {
  'use strict';



  angular
    .module('application.news.controllers')
    .controller('NewsController', function(News, Users, $http, $scope) {

          var vm = this;

          News.all().then(function (data) {

              vm.news = data;
              data.reverse();

              for(var i in data){
                  vm.news[i].active = true;
              }
          });

          vm.add = add;

          function add() {
              News.add(vm.title, vm.text);
          }

          vm.remove = function (id) {
              for(var i in vm.news){
                  if(vm.news[i].id === id){
                      vm.news[i].active = false;
                      break;
                  }
              }
              News.remove(id);
          }

  });
})();
