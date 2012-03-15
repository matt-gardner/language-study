$(document).ready(function() {

/* Vocab review scripts */
$("#id_show_definition").click(function () {
    $(".review_definition .text").toggle(0);
    var current_text = $.trim($("#id_show_definition a").text());
    if (current_text.substring(0, 4) == "Show") {
        var new_text = "Hide" + current_text.substring(4);
        $("#id_show_definition a").text(new_text);
    } else {
        var new_text = "Show" + current_text.substring(4);
        $("#id_show_definition a").text(new_text);
    }
});
$("#id_next_word").click(function () {
    next_word();
});
$("#id_prev_word").click(function () {
    prev_word();
});
$("#id_easy").click(function () {
    next_word('correct');
});
$("#id_medium").click(function () {
    next_word('neither');
});
$("#id_hard").click(function () {
    next_word('wrong');
});
$("input[name=review_order]").click(function() {
    reorder_words($("input[name=review_order]:checked").val());
});
$("#id_add_tag_button").click(function () {
    add_tag();
});
$("#id_by_definition").click(function() {
    set_by_definition();
});

/* Form drilling scripts */
$(".view_form").change(function() {
    get_new_form();
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
// I think this may be old and not used anymore
$("#id_drill_verb").click(function() {
    window.location = "/forms";
});

/* Table form view scripts */
$("#id_table_view #id_person").change(function() {
    update_table();
});
$("#id_table_view #id_number").change(function() {
    update_table();
});
$("#id_table_view #id_verb").change(function() {
    var new_id = $(this).val();
    window.location = new_id
});

/* List view scripts */
$(".message").delay(2000).fadeOut('slow');
$("#id_delete_word").click(function() {
    var answer = confirm("Delete this word?");
    if (answer) {
        window.location = "?delete"
    }
    return false;
});
$("#id_single_word_form #id_verb").click(function() {
    toggle_options($(this), 'verb');
});
$("#id_single_word_form #id_noun").click(function() {
    toggle_options($(this), 'noun');
});
$("#id_single_word_form #id_adjective").click(function() {
    toggle_options($(this), 'adjective');
});
$(".add_irregular_noun_form").live('click', function() {
    add_irregular_form($(this), "add-irregular-noun-form/");
});
$(".add_irregular_adjective_form").live('click', function() {
    add_irregular_form($(this), "add-irregular-adj-form/");
});
$(".add_irregular_verb_form").live('click', function() {
    add_irregular_form($(this), "add-irregular-verb-form/");
});
$(".add_irregular_stem").live('click', function() {
    add_irregular_form($(this), "add-irregular-stem/");
});
$(".add_irregular_augment").live('click', function() {
    add_irregular_form($(this), "add-irregular-augment/");
});
$(".add_tense_with_no_passive").live('click', function() {
    add_irregular_form($(this), "add-no-passive-tense/");
});
$(".delete_irregular_form").live('click', function() {
    delete_irregular_form($(this));
});
$(".undo_delete_irregular_form").live('click', function() {
    undo_delete_irregular_form($(this));
});
// Are these two still used?
$("#id_delete_list").click(function () {
    delete_word_list();
});
$("#id_create_list").click(function () {
    create_word_list();
});

/* JQuery UI theming scripts */
$(".ui-state-default").hover(
    function() {
        $(this).removeClass('ui-state-default').addClass('ui-state-hover');
    },
    function() {
        $(this).removeClass('ui-state-hover').addClass('ui-state-default');
    }
);
$(".ui-button").mousedown(function() {
    $(this).addClass("ui-state-active");
});
$(".ui-button").mouseup(function() {
    $(this).removeClass("ui-state-active");
});

/* Old functions (keeping around in case I decide to bring them back) */
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

});
