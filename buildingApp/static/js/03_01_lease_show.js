function showLeaseInfo()
{
	var year = Number($('#search_year').val());
	var month = Number($('#search_month').val());
	var building_id = Number($('#search_building').val().replace('b', ''));
	var room_num = $('#search_room_num').val();
	var is_empty = $('#search_isEmpty').parent().hasClass('checked');
	var type = $('#search_type').val();
	var type_text;
	if (type == '0') type_text = 'lease';
	else if (type == '1') type_text = 'notice';
	else if (type == '2') type_text = 'payment';
	else if (type == '3') type_text = 'electricity';
	else if (type == '4') type_text = 'gas';
	else type_text = 'water';

	if (year == '' || month == '' || building_id == '') {
		alert ('비어 있는 칸이 있습니다.');
		return;
	}

	var form = document.createElement('form');
	form.setAttribute('method', 'POST');
	form.setAttribute('action', '/lease/show/'+type_text+'/');
	document.body.appendChild(form);

	var f_year = document.createElement('input');
	f_year.name = 'year';
	f_year.value = year;
	form.appendChild(f_year);

	var f_month = document.createElement('input');
	f_month.name = 'month';
	f_month.value = month;
	form.appendChild(f_month);

	var f_bid = document.createElement('input');
	f_bid.name = 'building_id';
	f_bid.value = building_id;
	form.appendChild(f_bid);
	
	var f_room = document.createElement('input');
	f_room.name = 'room_num';
	f_room.value = room_num;
	form.appendChild(f_room);

	var f_isempty = document.createElement('input');
	f_isempty.name = 'is_empty';
	f_isempty.value = is_empty;
	form.appendChild(f_isempty);

	var csrf = document.createElement('input');
	csrf.type = 'hidden';
	csrf.name = 'csrfmiddlewaretoken';
	csrf.value = $.cookie('csrftoken');
	form.appendChild(csrf);

	//postData['room_num'] = (r_num != '') ? Number(r_num) : '';
	form.submit();
}

function InitForm()
{
	$('#search_building').find('option:eq(0)').prop('selected', true);
	$('#search_year').find('option:eq(0)').prop('selected', true);
	$('#search_month').find('option:eq(0)').prop('selected', true);
	$('#search_room_num').find('option:eq(0)').prop('selected', true);
	//$('input[id=search_isEmpty]:checkbox').attr('checked', false);
	//$('#search_isEmpty').attr('checked', false);
}

function getContents(roomnum)
{
	doAjaxContents_L(roomnum);
}

var Lease;
var doAjaxContents_L = function(roomnum) {
	var postData = {};
	var csrftoken = $.cookie('csrftoken');
	postData['csrfmiddlewaretoken'] = csrftoken; 
	postData['building_id'] = Number($('#search_building').val().replace('b', ''));
	postData['year'] = $('#search_year').val().trim();
	postData['month'] = $('#search_month').val().trim();
	postData['roomnum'] = roomnum;
	postData['is_empty'] = $('#search_isEmpty').parent().hasClass('checked');

	$.ajax({
		type : 'POST',
		url : '/lease/input/getLeaseInfo/',
		data : postData,
		success : function(result) {
			Lease = result;
			var template = new EJS({url : '/static/ejs/03_01_lease_show.ejs'}).render({'data' : Lease, 'radio' : Number(0)});
			$('#contents').html(template);
			$('#contents_modal').html(template);
		},
		error : function(msg) {
			alert('데이터를 로딩하지 못했습니다...\n페이지 새로고침을 해 보시기 바랍니다.');
		},
	});
}

function showDetail(bid, rid)
{
	window.location = "/lease/show/leaseNotice/" + bid + "/" + rid + '/' + '0' + '/';
}


// 라디오 버튼 구현
// 전체(0), 선택(1), 상세전체(2), 상세선택(3)
var radioValue;
var select;
function changeRadio(val) 
{
	if (radioValue == val)
		return;

	radioValue = Number(val);

	var template;
	if (val <= 1)
		template = new EJS({url : '/static/ejs/03_01_lease_show.ejs'}).render({'data' : Lease, 'radio' : Number(val)});
	$('#contents').html(template);
	$('#contents_modal').html(template);

	if (val == 1) {
		// '선택'일 경우, 체크할 때마다 미리보기에 계속 상태를 바꿔줘야 한다.
		select = new Array();
		for (i = 0; i < Lease.length; i++)
			select.push(false);

		template = new EJS({url : '/static/ejs/03_01_lease_show.ejs'}).render({'data' : Lease, 'radio' : Number(-1), 'select' : select});
		$('#contents_modal').html(template);
		
		$('.sel').change(function() {
			idx = Number($(this).attr('id').replace('selCheck','').trim());
			select[idx] = !select[idx];
			template = new EJS({url : '/static/ejs/03_01_lease_show.ejs'}).render({'data' : Lease, 'radio' : Number(-1), 'select' : select});
			$('#contents_modal').html(template);
		});
	}
}

function pagePrint()
{
	var strFeature = "";
	strFeature += "width=" + $(document).width() * 0.8;
	strFeature += ", height=" + $(document).height() * 0.8;
	strFeature += ", left=" + $(document).width() * 0.1;
	strFeature += ", top=" + $(document).height() * 0.1;

	var objWin = window.open('', 'print', strFeature);
	objWin.document.writeln("<!DOCTYPE html>");
	objWin.document.writeln($('head').html());
	objWin.document.writeln('<body><div class="row-fluid">');
	objWin.document.writeln($('#content').html());
	objWin.document.writeln("</div></body>");
	objWin.document.close();
	
	if (radioValue == 1) {
		for (i = 0; i < Lease.length; i++) {
			if ($('input:checkbox[id="selCheck'+i+'"]').is(':checked'))
				continue;
			var useless = objWin.document.getElementById('sel'+i);
			useless.parentNode.removeChild(useless);
		}	
	}

	var useless = objWin.document.getElementById("filter-menu");
	useless.parentNode.removeChild(useless);

	objWin.print();
}

