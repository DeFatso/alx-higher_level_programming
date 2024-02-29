$('#add_item').click(function() {
	const new_item = $('<li>').text('Item');
	$('ul.my_list').append(new_item);
});
