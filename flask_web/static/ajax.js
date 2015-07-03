/**
 * Created by zhangjun on 15/6/19.
 */

function openModel(ip,status) {
$('#myModal').modal();
$('#ip').val(ip);
$('#status').val(status);
}

function delModel(ip) {
$('#delModal').modal('show');
$('#aaa').text(ip);
}

function hiModel() {
$('#delModal').modal('hide');
}

function addModel() {
$('#myModal').modal();
}

function search() {
    var content = $('#s_ip').val();
    window.location.href="/search_ip?ip=" + content;
}
