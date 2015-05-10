(function () {
  'use strict';

  angular
    .module('application.calendar.controllers')
    .controller('CalendarController', function($scope) {

          var vm = this;
          vm.calendarOptions = {
            defaultDate: new Date(),
            minDate: new Date([1999, 12, 12]),
            maxDate: new Date([2020, 12, 31]),
            dayNamesLength: 2, // How to display weekdays (1 for "M", 2 for "Mo", 3 for "Mon"; 9 will show full day names; default is 1)
            eventClick: vm.eventClick,
            dateClick: vm.dateClick
          };
  });
})();