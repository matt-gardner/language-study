$(document).ready(function() {
$("#id_show_definition").click(function () {
	$(".review_definition .text").toggle(0);
	var current_text = $("#id_show_definition").val()
	if (current_text.substring(0, 4) == "Show") {
		var new_text = "Hide" + current_text.substring(4);
		$("#id_show_definition").val(new_text);
	} else {
		var new_text = "Show" + current_text.substring(4);
		$("#id_show_definition").val(new_text);
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
$("#id_by_definition").click(function() {
	set_by_definition();
});

/* Table form view scripts */
$("#id_table_view #id_person").change(function() {
	update_table();
});
$("#id_table_view #id_number").change(function() {
	update_table();
});
/* List view scripts */
$("#id_delete_word").click(function() {
	var answer = confirm("Delete this word?");
	if (answer) {
		window.location = "?delete"
	}
	return false;
});
$("#id_single_word_form #id_verb").click(function() {
	toggle_verb_options($(this));
});
$(".add_irregular_form").click(function() {
	add_irregular_form($(this), "add-irregular-form/");
});
$(".add_irregular_stem").click(function() {
	add_irregular_form($(this), "add-irregular-stem/");
});
$(".add_irregular_augment").click(function() {
	add_irregular_form($(this), "add-irregular-augment/");
});
$(".delete_irregular_form").live('click', function() {
	delete_irregular_form($(this));
});
$(".undo_delete_irregular_form").live('click', function() {
	undo_delete_irregular_form($(this));
});

});
