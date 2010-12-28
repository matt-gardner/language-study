$("#id_show_text").click(function () {
	$(".review_text .text").toggle(0);
	if ($("#id_show_text").val() == "Show text") {
		$("#id_show_text").val("Hide text");
	} else {
		$("#id_show_text").val("Show text");
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
$("#id_increase_text_size").click(function(){
	var currentFontSize = $('.review_text .text').css('font-size');
	var currentFontSizeNum = parseFloat(currentFontSize, 10);
	var newFontSize = currentFontSizeNum*1.2;
	$('.review_text .text').css('font-size', newFontSize);
});
$("#id_decrease_text_size").click(function(){
	var currentFontSize = $('.review_text .text').css('font-size');
	var currentFontSizeNum = parseFloat(currentFontSize, 10);
	var newFontSize = currentFontSizeNum*0.8;
	$('.review_text .text').css('font-size', newFontSize);
});
$("input[name=review_order]").click(function() {
	reorder_words($("input[name=review_order]:checked").val());
});
$("#id_add_tag_button").click(function () {
		add_tag();
});
