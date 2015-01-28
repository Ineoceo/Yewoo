function add() {
    var addtext = $('#addtext');
    if (addtext.val() == "")
        alert("직급 이름을 입력하세요.");
	else if ($('#addnumber').val() == '')
		alert('직급 순서를 선택해 주세요.');
	else if (Number($('#addnumber').val()) < 0)
		alert('사용중인 직급 순서입니다.');
    else {
        var csrftoken = $.cookie('csrftoken');
        var postData = {};
        postData['csrfmiddlewaretoken'] = csrftoken;
        postData['type'] = 'add';
        postData['data'] = addtext.val();
		postData['number'] = $('#addnumber').val();
        $.ajax({
            type : 'POST',
            url : '/manage/setting/position/',
            data : postData,
            success : function() {
                alert('추가되었습니다.');
                $(location).attr('href', '/manage/setting/position/');
            },
            error : function(msg) {
                alert('error : ' + msg);
            },
        });
    }
}
function del() {
    var radios = $('input[name=posselect]');
    var value = "ND";
    for (var i = 0; i < radios.length; i++) {
		if ($(radios[i]).is(':checked')) {
            value = radios[i].value;       
        }
    }
    if (value == "ND")
            alert("직급을 선택하세요.");
    else {
        var csrftoken = $.cookie('csrftoken');
        var postData = {};
        postData['csrfmiddlewaretoken'] = csrftoken;
        postData['type'] = 'del';
        postData['data'] = value;
        $.ajax({
            type : 'POST',
            url : '/manage/setting/position/',
            data : postData,
            success : function() {
                alert('삭제되었습니다.');
                $(location).attr('href', '/manage/setting/position/');
            },
            error : function(msg) {
                alert('error : ' + msg);
            },
        });
    }
}
function modify() {
    var radios = $('input[name=posselect]');
    var value = "ND";
    for (var i = 0; i < radios.length; i++) {
		if ($(radios[i]).is(':checked')) {
            value = radios[i].value;       
        }
    }
    var modtext = $('#modifytext')
    if (value == "ND")
        alert("직급을 선택하세요.");
    else if(modtext.val() == "")
        alert("직급 이름을 입력하세요.");
    else {
        var csrftoken = $.cookie('csrftoken');
        var postData = {};
        postData['csrfmiddlewaretoken'] = csrftoken;
        postData['type'] = 'mod';
        postData['data'] = value;
        postData['data2'] = modtext.val()
        $.ajax({
            type : 'POST',
            url : '/manage/setting/position/',
            data : postData,
            success : function() {
                alert('변경되었습니다.');
                $(location).attr('href', '/manage/setting/position/');
            },
            error : function(msg) {
                alert('error : ' + msg);
            },
        });
    }
}
function changeRadio(name) {
    var modtext = $('#modifytext');
	name = name.split(' ')[1].trim();
    modtext.val(name);
}
