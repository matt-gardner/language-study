$(document).ready(function() {

$('.text-body span').bind('taphold', function(e) {
  e.preventDefault();
  $.mobile.changePage($(this).data('href'), {role: 'dialog'});
});

$('.next-page').click(function() {
  var username = $(this).data('user');
  var wordlist = $(this).data('wordlist');
  var text = $('.text-body').text();
  var next_page = $(this).data('next-page');
  var book = $(this).data('book');
  var link = "/extension/read/" + username + "/" + wordlist;
  console.log('Requesting url: ' + link);
  $.get(link, {text: text});
  link = "/book/" + book + "/page/" + next_page + "/";
  $.mobile.changePage(link);
});


});
