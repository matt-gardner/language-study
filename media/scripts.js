/* Card list functions */
function delete_word_list() {
	var list = $("#id_wordlist").val();
	var result = confirm("Are you sure you want to delete Card List "+list+"?");
	if (result == true) {
		window.location = "delete-word-list/"+list;
	}
}
function get_word_list() {
	var list = $("#id_wordlist").val();
	$.getJSON("get-word-list/"+list, {}, function(data) {
		new_word(data.word, data.word_number, data.num_words, data.difficulty);
	});
}

/* Review option functions */
function switch_review_style() {
	window.location = $("#id_review_style").val();
}
function reorder_words(ordering) {
	$.getJSON("reorder-word-list/"+ordering, {}, function(data) {
		new_word(data.word, data.word_number, data.num_words, data.difficulty);
	});
}

/* Get word functions */
function next_word(difficulty) {
	var link = "next-word/"
	if (difficulty) {
		link += difficulty
	}
	$.getJSON(link, {}, function(data) {
		new_word(data.word, data.word_number, data.num_words, data.difficulty);
	});
}
function prev_word() {
	$.getJSON("prev-word/", {}, function(data) {
		new_word(data.word, data.word_number, data.num_words, data.difficulty);
	});
}
function new_word(word, word_number, num_words, average_difficulty) {
	if ($("#id_show_definition").val() == "Hide definition") {
		$("#id_show_definition").val("Show definition");
		$(".review_definition .definition").toggle(0);
	}
	switch_text(word.word, word.definition);
	reset_word_number(word_number, num_words, word.difficulty);
	reset_word_difficulty(word.difficulty, word.review_count);
	reset_word_tags(word.tags);
	reset_list_difficulty(average_difficulty);
}
function switch_text(word, definition) {
	$(".review_word .text").html(word);
	$(".review_definition .text").html(definition);
}
function reset_word_number(word_number, num_words) {
	var html = $.fn.message_config.before_word_number;
	html += word_number;
	html += $.fn.message_config.after_word_number;
	html += num_words;
	html += $.fn.message_config.after_num_words;
	$(".words").html(html);
}
function reset_word_difficulty(difficulty, review_count) {
	$(".word_difficulty").html("This word's difficulty: " +
			difficulty.toFixed(2) + '; Times reviewed: ' +
			review_count);
}
function reset_word_tags(tags) {
	$(".word_tags").html(tags);
}
function reset_list_difficulty(difficulty) {
	$(".wordlist_difficulty").html('Average difficulty of words: ' +
			difficulty.toFixed(2));
}
function add_tag() {
	tag_name = $("#id_add_tag").val();
	$.getJSON("/add-tag-to-word/"+tag_name, {}, function(data) {
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
