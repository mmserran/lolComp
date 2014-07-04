'use strict';


// Declare app level module which depends on filters, and services
// The page_editor app will allow users to add/del and arrange the
//  order of pages for this survey
// var page_editor = angular.module('page_editor', []);

// The ques_editor app will allow users to add/del/mod questions
//  for a chosen page.
var LolCompApp = angular.module('LolCompApp', ['ui.bootstrap', 'ngAnimate', 'ngSanitize', 'mgcrea.ngStrap'])
.directive('cars', function () {
  return {
    restrict: 'E',
    scope: { 'cars': '=data' },
    template: "<div ng-repeat='car in cars'>\n" +
    "  {{car.year}} {{car.make}} {{car.model}}\n" +
    "</div>"
  };
});


var LolCompCtrl = function ($scope, $modal) {

  // Select modals
  $scope.modal = {
    "title": "Title",
    "content": "Hello Modal<br />This is a multiline message!"
  };
  $scope.tooltip = {
    "title": "Hello Tooltip<br />This is a multiline message!",
    "checked": false
  };
  $scope.popover = {
    "title": "Title",
    "content": "Hello Popover<br />This is a multiline message!"
  };
  $scope.youtubeModal = function() {
    var modalInstance = $modal.open({
      templateUrl: 'youtubeModal.html',
      controller: StandardInstanceCtrl,
    });
  };
  $scope.lolcomp1Stats = [  
    { name: 'AD', value: .9, type: 'danger', win: 1 },
    { name: 'AP', value: .1, type: 'danger', win: 0 },
    { name: 'CC', value: .2, type: 'primary', win: 0 },
    { name: 'break', value: 0, type: 'none', win: 0  },
    { name: 'Sustain', value: .2, type: 'success', win: 1 },
    { name: 'Mobility', value: .2, type: 'warning', win: 0 },
    { name: 'break', value: 0, type: 'none', win: 0  },
    { name: 'Pushing', value: .4, type: 'info', win: 0 },
    { name: 'Zoning', value: 0, type: 'info', win: 0 },
    { name: 'Utility', value: .2, type: 'primary', win: 1 },
  ];
  $scope.lolcomp1Aspects = [  
    { name: 'Duel', value: .6, type: 'danger', win: 1  },
    { name: 'Skirmish', value: .8, type: 'warning', win: 0  },
    { name: 'Teamfight', value: .9, type: 'success', win: 0  },
    { name: 'break', value: 0, type: 'none', win: 0  },
    { name: 'Early', value: .6, type: 'danger', win: 1  },
    { name: 'Mid', value: .2, type: 'warning', win: 0  },
    { name: 'Late', value: .9, type: 'primary', win: 1  },
    { name: 'break', value: 0, type: 'none', win: 0  },
    { name: 'Poke', value: .1, type: 'success', win: 0  },
    { name: 'Burst', value: .8, type: 'danger', win: 0  },
  ];
};


var StandardInstanceCtrl = function ($scope, $modalInstance) {
  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
};
