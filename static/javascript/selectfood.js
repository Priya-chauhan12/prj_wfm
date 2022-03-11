// var myN = {
//     val1: 'Blue',
//     val2: 'Orange'
// };
// var mySelect = $('#myN');
// $.each(myN, function(val, text) {
//     mySelect.append(
//         $('<option></option>').val(val).html(text)
//     );
// });

$(function() {
    var $select = $(".1-25");
    for (i = 1; i <= 25; i++) {
        $select.append($('<option></option>').val(i).html(i))
    }
});

$(function() {
    var $select = $(".1-50");
    for (i = 1; i <= 50; i++) {
        $select.append($('<option></option>').val(i).html(i))
    }
});