$("#id_show_definition").click(function () {
	$(".review_definition .text").toggle(0);
	if ($("#id_show_definition").val() == "Show definition") {
		$("#id_show_definition").val("Hide definition");
	} else {
		$("#id_show_definition").val("Show definition");
	}
});
$("#id_next_word").click(function () {
	next_word();
});
$("#id_prev_word").click(function () {
	prev_word();
});
$("#id_easy").click(function () {
	next_word('easy');
});
$("#id_medium").click(function () {
	next_word('medium');
});
$("#id_hard").click(function () {
	next_word('hard');
});
$("#id_delete_list").click(function () {
	delete_word_list();
});
$("#id_create_list").click(function () {
	create_word_list();
});
$("#id_increase_word_size").click(function(){
	var currentFontSize = $('.review_word .text').css('font-size');
	var currentFontSizeNum = parseFloat(currentFontSize, 10);
	var newFontSize = currentFontSizeNum*1.2;
	$('.review_word .text').css('font-size', newFontSize);
});
$("#id_decrease_word_size").click(function(){
	var currentFontSize = $('.review_word .text').css('font-size');
	var currentFontSizeNum = parseFloat(currentFontSize, 10);
	var newFontSize = currentFontSizeNum*0.8;
	$('.review_word .text').css('font-size', newFontSize);
});
$("#id_increase_definition_size").click(function(){
	var currentFontSize = $('.review_definition .text').css('font-size');
	var currentFontSizeNum = parseFloat(currentFontSize, 10);
	var newFontSize = currentFontSizeNum*1.2;
	$('.review_definition .text').css('font-size', newFontSize);
});
$("#id_decrease_definition_size").click(function(){
	var currentFontSize = $('.review_definition .text').css('font-size');
	var currentFontSizeNum = parseFloat(currentFontSize, 10);
	var newFontSize = currentFontSizeNum*0.8;
	$('.review_definition .text').css('font-size', newFontSize);
});
$("input[name=review_order]").click(function() {
	reorder_words($("input[name=review_order]:checked").val());
});
$(".view_form").change(function() {
	get_new_form();
});
$("#id_add_tag_button").click(function () {
	add_tag();
});
$("#id_verblist").click(function() {
	get_new_verb();
});
$("#id_new_form").click(function() {
	get_new_random_form();
});
$("#id_guess_form").click(function() {
	guess_form();
});
$("#id_drill_verb").click(function() {
	window.location = "/forms";
});
