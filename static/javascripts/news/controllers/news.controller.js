(function () {
  'use strict';



  angular
    .module('application.news.controllers')
    .controller('NewsController', function(News, Users, $window, $scope) {

          var vm = this;

          News.all().then(function (data) {

              vm.news = data;
              console.log(data);

          });

          vm.publish = publish;

          function publish(){
              News.publish(vm.title, vm.text);
          }

  });
  angular
    .module('application.news.controllers').filter('reverse', function() {
        return function(items) {
            return items.slice().reverse();
        };
    });
})();
