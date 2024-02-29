$(document).ready(function () {
	$('#add_item').click(function () {
		const new_item = $('<li>').text('Item');
		$('ul.my_list').append(new_item);
	});

	$('#remove_item').click(function () {
		$('ul.my_list li:last-child').remove();
	});

	$('#clear_list').click(function () {
		$('ul.my_list').empty();
	});
});
