/* Card list functions */
function delete_card_list() {
	var list = $("#id_cardlist").val();
	var result = confirm("Are you sure you want to delete Card List "+list+"?");
	if (result == true) {
		window.location = "delete-card-list/"+list;
	}
}
function get_card_list() {
	var list = $("#id_cardlist").val();
	$.getJSON("get-card-list/"+list, {}, function(data) {
		new_word(data.card, data.card_number, data.num_cards, data.difficulty);
	});
}

/* Review option functions */
function switch_review_style() {
	window.location = $("#id_review_style").val();
}
function reorder_words(ordering) {
	$.getJSON("reorder-card-list/"+ordering, {}, function(data) {
		new_word(data.card, data.card_number, data.num_cards, data.difficulty);
	});
}

/* Get word functions */
function next_word(difficulty) {
	var link = "next-card/"
	if (difficulty) {
		link += difficulty
	}
	$.getJSON(link, {}, function(data) {
		new_word(data.card, data.card_number, data.num_cards, data.difficulty);
	});
}
function prev_word() {
	$.getJSON("prev-card/", {}, function(data) {
		new_word(data.card, data.card_number, data.num_cards, data.difficulty);
	});
}
function new_word(card, card_number, num_cards, average_difficulty) {
	if ($("#id_show_text").val() == "Hide text") {
		$("#id_show_text").val("Show text");
		$(".review_text .text").toggle(0);
	}
	switch_text(card.word, card.text);
	reset_card_number(card_number, num_cards, card.difficulty);
	reset_card_difficulty(card.difficulty);
	reset_list_difficulty(average_difficulty);
}
function switch_text(word, text) {
	$(".review_word .text").html(word);
	$(".review_text .text").html(text);
}
function reset_card_number(card_number, num_cards) {
	var html = $.fn.message_config.before_card_number;
	html += card_number;
	html += $.fn.message_config.after_card_number;
	html += num_cards;
	html += $.fn.message_config.after_num_cards;
	$(".cards").html(html);
}
function reset_card_difficulty(difficulty) {
	$(".card_difficulty").html("This card's difficulty: " +
			difficulty.toFixed(2));
}
function reset_list_difficulty(difficulty) {
	$(".cardlist_difficulty").html('Average difficulty of cards: ' +
			difficulty.toFixed(2));
}
