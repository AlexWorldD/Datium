(function () {
  'use strict';

  angular
    .module('application.news.controllers')
    .controller('NewsController', function(News, Users, $window, $scope) {

          var vm = this;

          News.all().then(function (data) {

                for(var i in data){
                    Users.getById(data[i].user).then(function (user_info) {
                        console.log(user_info);
                        data[i]["user_info"] = user_info;
                    })
                }
              vm.news = data;
          });

          vm.publish = publish;

          function publish(){
              alert("Hi");
              News.publish(vm.title, vm.text);
          }


  });
})();
