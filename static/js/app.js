'use strict';


// Declare app level module which depends on filters, and services
// The page_editor app will allow users to add/del and arrange the
//  order of pages for this survey
// var page_editor = angular.module('page_editor', []);

// The ques_editor app will allow users to add/del/mod questions
//  for a chosen page.
var LolCompApp = angular.module('LolCompApp', ['ui.bootstrap'])

var LolCompCtrl = function ($scope, $modal) {
  // Select modals
  $scope.youtubeModal = function() {
    var modalInstance = $modal.open({
      templateUrl: 'youtubeModal.html',
      controller: StandardInstanceCtrl,
    });
  };
};


var StandardInstanceCtrl = function ($scope, $modalInstance) {
  $scope.cancel = function () {
    $modalInstance.dismiss('cancel');
  };
};