/* Card list functions */
function create_card_list() {
	var list = $("input[name=cardlist_name]").val();
	window.location = "/create-card-list/"+list;
}
function delete_card_list() {
	var list = $("#id_cardlist").val();
	var result = confirm("Are you sure you want to delete Card List "+list+"?");
	if (result == true) {
		window.location = "/delete-card-list/"+list;
	}
}
function get_card_list() {
	var list = $("#id_cardlist").val();
	$.getJSON("/feeds/get-card-list/"+list, {}, function(data) {
		new_word(data.card, data.card_number, data.num_cards);
	});
}

/* Review option functions */
function reset_review_style(review_style) {
	$.get("/feeds/review-style/"+review_style, {}, function(data) {});
	get_card_list()
	$(".review_style .option").attr("disabled", true);
	$(".review_style .option").removeAttr("checked");
	$("#"+review_style+" .option").removeAttr("disabled");
}
function randomize_list() {
	if ($("#id_randomize").is(":checked")) {
		$.getJSON("/feeds/randomize-card-list/", {}, function(data) {
			new_word(data.card, data.card_number, data.num_cards);
		});
	} else {
		$.getJSON("/feeds/unrandomize-card-list/", {}, function(data) {
			new_word(data.card, data.card_number, data.num_cards);
		});
	}
}

/* Get word functions */
function next_word(difficulty) {
	var link = "/feeds/next-card/"
	if (difficulty) {
		link += difficulty
	}
	$.getJSON(link, {}, function(data) {
		new_word(data.card, data.card_number, data.num_cards);
	});
}
function prev_word() {
	$.getJSON("/feeds/prev-card/", {}, function(data) {
		new_word(data.card, data.card_number, data.num_cards);
	});
}
function new_word(card, card_number, num_cards) {
	if ($("#id_show_text").val() == "Hide text") {
		$("#id_show_text").val("Show text");
		$(".review_text .text").toggle(0);
	}
	switch_text(card.word, card.text);
	reset_card_number(card_number, num_cards, card.difficulty);
}
function switch_text(word, text) {
	$(".review_word .text").html(word);
	$(".review_text .text").html(text);
}
function reset_card_number(card_number, num_cards, difficulty) {
	var html = "Reviewing card " + card_number + " out of ";
	html += num_cards;
	$(".cards").html(html);
	$(".difficulty").html('Average difficulty: ' + difficulty)
}
