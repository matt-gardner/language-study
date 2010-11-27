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
	reset_card_difficulty(card.difficulty, card.review_count);
	reset_card_tags(card.tags);
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
function reset_card_difficulty(difficulty, review_count) {
	$(".card_difficulty").html("This card's difficulty: " +
			difficulty.toFixed(2) + '; Times reviewed: ' +
			review_count);
}
function reset_card_tags(tags) {
	$(".word_tags").html(tags);
}
function reset_list_difficulty(difficulty) {
	$(".cardlist_difficulty").html('Average difficulty of cards: ' +
			difficulty.toFixed(2));
}
function add_tag() {
	tag_name = $("#id_add_tag").val();
	$.getJSON("/add-tag-to-card/"+tag_name, {}, function(data) {
		$(".word_tags").html(data.tags);
	});
}

/* Filters */
function add_new_filter()
{
	var link = "/new-filter/" + $("#id_filter").val();
	$.get(link, {}, function(filter) {
		$("#id_filter_form").html(filter);
	});
}
function remove_filter(id)
{
	var link = "/remove-filter/" + id;
	$.get(link, {}, function(filter) {
		$("#id_filter_form").html(filter);
		location.reload();
	});
}
function update_tag_filter(id)
{
	var link = "/update-tag-filter/" + id + "/";
	link += $("#id_tag_filter_"+id).val();
	$.get(link, {}, function(filter) {
		$("#id_filter_form").html(filter);
		location.reload();
	});
}
function update_difficulty_filter(id)
{
	var link = "/update-difficulty-filter/" + id + "/";
	link += $("#id_difficulty_filter_comp_"+id).val() + "/";
	link += $("#id_difficulty_filter_value_"+id).val();
	$.get(link, {}, function(filter) {
		$("#id_filter_form").html(filter);
		location.reload();
	});
}
function update_string_filter(id)
{
	var link = "/update-string-filter/" + id + "/";
	link += $("#id_string_filter_"+id).val();
	$.get(link, {}, function(filter) {
		$("#id_filter_form").html(filter);
		location.reload();
	});
}
function update_date_filter(id)
{
	var link = "/update-date-filter/" + id + "/";
	link += $("#id_date_filter_"+id).val() + "/";
	link += $("#id_date_filter_"+id+"_year").val() + "/";
	link += $("#id_date_filter_"+id+"_month").val() + "/";
	link += $("#id_date_filter_"+id+"_day").val();
	$.get(link, {}, function(filter) {
		$("#id_filter_form").html(filter);
		location.reload();
	});
}
