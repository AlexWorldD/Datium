(function () {
  'use strict';



  angular
    .module('application.news.controllers')
    .controller('NewsController', function(News, Users, $window, $scope) {

          var vm = this;

          News.all().then(function (data) {

              vm.news = data;
<<<<<<< HEAD
=======
              console.log(data);
>>>>>>> dc631699d0d78df45585744ed871e301eab6a45c

          });

          vm.publish = publish;

          function publish(){
              alert("Hi");
              News.publish(vm.title, vm.text);
          }
<<<<<<< HEAD

=======
>>>>>>> dc631699d0d78df45585744ed871e301eab6a45c

  });
  angular
    .module('application.news.controllers').filter('reverse', function() {
        return function(items) {
            return items.slice().reverse();
        };
    });
})();
