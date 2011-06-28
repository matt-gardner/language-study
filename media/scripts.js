/* Word list functions */
function delete_word_list() {
	var list = $("#id_wordlist").val();
	var result = confirm("Are you sure you want to delete Word List "+list+"?");
	if (result == true) {
		window.location = "delete-word-list/"+list;
	}
}
function toggle_verb_options($checkbox) {
	$verboptions = $checkbox.parent().parent().parent().find(".verb-option");
	if ($checkbox.is(':checked')) {
		$verboptions.parent().parent().fadeIn('fast');
		$checkbox.parent().find('.warning').remove();
	} else {
		if ($verboptions.is(":visible")) {
			$verboptions.parent().parent().fadeOut('fast');
			if ($.fn.word_vars.has_verb) {
				$checkbox.after('<span class="warning">' +
						'This will irrevocably delete all data associated ' +
						'with this verb, including irregular forms and ' +
						'drilling statistics</span>');
			}
		}
	}
}
function add_irregular_form($span, ajax_link) {
	var name = $span.parent().parent().prev().find('input').attr("name");
	if (!name) {
		var number = 0;
	} else {
		var length = name.length;
		name = name.substring(0, length-5);
		name = name.substring(name.lastIndexOf('_')+1);
		var number = parseInt(name) + 1;
	}
	var link = document.URL.split('?')[0];
	if (!link.match('/\/$/')) {
		link += '/';
	}
	link += ajax_link + '' + number
	$.get(link, {}, function(html) {
		$span.parent().parent().before(html);
	});
}
function delete_irregular_form($span) {
	var prev_val = $span.next().val();
	if (prev_val == "add") {
		$span.parent().parent().remove();
		return;
	}
	$span.parent().parent().find('input, select')
		.filter(':not(input[type="hidden"])')
		.attr('disabled', 'disabled');
	$span.next().val("delete");
	$('<span class="undo_delete_irregular_form">Undo</span>')
		.attr("prev_val", prev_val)
		.insertBefore($span.next());
	$span.next().before('<span class="warning">Will be deleted. </span>');
	$span.remove();
}
function undo_delete_irregular_form($span) {
	$span.parent().parent().find('input, select').removeAttr('disabled')
	$span.next().val($span.attr("prev_val"));
	$span.prev().remove();
	$('<span class="delete_irregular_form">X</span>')
		.insertBefore($span.next());
	$span.remove();
}

/* Form drilling functions */
function get_new_form() {
	person = $("#id_person").val();
	number = $("#id_number").val();
	tense = $("#id_tense").val();
	mood = $("#id_mood").val();
	voice = $("#id_voice").val();
	link = "/inflect-form/"+person+"/"+number+"/"+tense+"/"+mood+"/"+voice;
	$.getJSON(link, {}, function(data) {
		switch_text(data.inflected_form, "");
	});
}
function guess_form() {
	person = $("#id_person").val();
	number = $("#id_number").val();
	tense = $("#id_tense").val();
	mood = $("#id_mood").val();
	voice = $("#id_voice").val();
	link = "/guess-form/"+person+"/"+number+"/"+tense+"/"+mood+"/"+voice;
	$.getJSON(link, {}, function(data) {
		switch_text(data.result, "");
	});
}
function get_new_verb() {
	var verb = $("#id_verblist").val();
	$.getJSON("/get-new-verb/"+verb, {}, function(data) {
		switch_text(data.inflected_form, "");
	});
}
function get_new_random_form() {
	$.getJSON("/get-new-random-form/", {}, function(data) {
		switch_text(data.inflected_form, "");
	});
}

/* Review option functions */
function switch_review_style() {
	window.location = $("#id_review_style").val();
}
function reorder_words(ordering) {
	$.getJSON("reorder-word-list/"+ordering, {}, function(data) {
		new_word(data);
	});
}
function set_by_definition() {
	var link = "/set-by-definition/";
	if ($("#id_by_definition").attr("checked")) {
		link += "true";
	} else {
		link += "false";
	}
	$.getJSON(link, {}, function(data) {
		new_word(data);
	});
}

/* Get word functions */
function next_word(difficulty) {
	var link = "next-word/"
	if (difficulty) {
		link += difficulty
	}
	$.getJSON(link, {}, function(data) {
		new_word(data);
	});
}
function prev_word() {
	$.getJSON("prev-word/", {}, function(data) {
		new_word(data);
	});
}
function new_word(data) {
	var show_text = "Show ";
	if (data.by_definition) {
		show_text += "word";
	} else {
		show_text += "definition";
	}
	if ($("#id_show_definition").val().substring(0, 4) == "Hide") {
		$(".review_definition .text").toggle(0);
	}
	$("#id_show_definition").val(show_text);
	if (data.by_definition) {
		switch_text(data.word.definition, data.word.word);
	} else {
		switch_text(data.word.word, data.word.definition);
	}
	reset_drill_button(data.word);
	reset_word_number(data.word_number, data.num_words, data.word.difficulty);
	reset_word_difficulty(data.word.difficulty, data.word.review_count);
	reset_word_tags(data.word.tags);
	//reset_list_difficulty(data.average_difficulty);
}
function switch_text(word, definition) {
	$(".review_word .text").html(word);
	$(".review_definition .text").html(definition);
}
function reset_drill_button(word) {
	if (word.is_verb) {
		$("#id_drill_verb").show();
	} else {
		$("#id_drill_verb").hide();
	}
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

/* Tags */
function add_tag() {
	tag_name = $("#id_add_tag").val();
	$.getJSON("/add-tag-to-word/"+tag_name, {}, function(data) {
		$(".word_tags").html(data.tags);
	});
}
function remove_tag(tag_name) {
	$.getJSON("/remove-tag-from-word/"+tag_name, {}, function(data) {
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
function update_one_choice_filter(id)
{
	var link = "/update-one-choice-filter/" + id + "/";
	link += $("#id_one_choice_filter_"+id).val();
	$.get(link, {}, function(filter) {
		$("#id_filter_form").html(filter);
		location.reload();
	});
}
function update_value_comp_filter(id)
{
	var link = "/update-value-comp-filter/" + id + "/";
	link += $("#id_value_comp_filter_comp_"+id).val() + "/";
	link += $("#id_value_comp_filter_value_"+id).val();
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
