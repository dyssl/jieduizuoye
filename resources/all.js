 var token = "5413";
 var user_id = "5413";
 var username = "5413";
 var cards = "5413";
var card2 = "5413";
var id = "5413";
var x=0;
var detailid=0;
var card4=new Array();
var dcards=new Array();
var dids=new Array();
var dscores=new Array();
(function ($) {
    $.fn.serializeJson = function () {
        var serializeObj = {};
        var array = this.serializeArray();
        var str = this.serialize();
        $(array).each(function () {
            if (serializeObj[this.name]) {
                if ($.isArray(serializeObj[this.name]) && this.value != "") {
                    serializeObj[this.name].push(this.value);
                } else {
                    if (this.value != "") {
                        serializeObj[this.name] = [serializeObj[this.name], this.value];
                    }
                }
            } else {
                if (this.value != "") {
                    serializeObj[this.name] = this.value;
                }
            }
        });
        return serializeObj;
    };
})(jQuery);

function register() {
    var reg_data = ($('#reg_form').serializeJson());
    if (reg_data.username == " 用户名" || reg_data.password == " 密码"||reg_data.student_number == " 教务处学号"||reg_data.student_password == " 教务处密码"  ) {
        alert("必须填写完整信息");
        return;
    }
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "https://api.shisanshui.rtxux.xyz/auth/register2",
        data: JSON.stringify(reg_data), //提交的数据
        contentType: "application/json;charset-UTF-8",
        success: function (result) { //todo
            console.log(result); //打印服务端返回的数据(调试用)
            if (result.status == 0) {
                alert("注册成功");
                window.location.href = '登入.html'
            };
        },
        error: function (jqXHR, textStatus, errorThrownt) {
			
			var responseText = jQuery.parseJSON(jqXHR.responseText);
			if (responseText.status == 1001) {
                alert("用户名已被使用");
            };
			if (responseText.status == 1002) {
                alert("学号已绑定");
            };
			if (responseText.status == 1003) {
                alert("教务处认证失败");
            }
        }
    });
}
function begin() {
    var login_data = ($('#login_form').serializeJson());
    if (login_data.username == " 用户名" || login_data.password == " 密码") {
        alert("用户名或密码不能为空");
        return;
    }
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "https://api.shisanshui.rtxux.xyz/auth/login",
        data: JSON.stringify(login_data), //提交的数据
        contentType: "application/json;charset-UTF-8",
        success: function (result) { //todo
            console.log(result); //打印服务端返回的数据(调试用)
            if (result.status == 0) {
                token=result.data.token;
				user_id=result.data.user_id;
				username=login_data.username
                console.log(token);
				localStorage.setItem("token1",token);
				localStorage.setItem("user_id1",user_id);
 localStorage.setItem("username1",username);
                alert("登录成功");
                window.location.href = '已登入界面.html'
            };
        },
        error: function (res) {
            // $("#login_form").reset();
            alert("用户名或密码错误");
        }
    });
}
function logout(){
	token=localStorage.getItem("token1");
	$.ajax({
        type: "POST",
        url: "https://api.shisanshui.rtxux.xyz/auth/logout",
		beforeSend: function(xhr) {
                xhr.setRequestHeader("X-Auth-Token",token);
            },
        success: function (result) { //todo
            	console.log(result);
				console.log(token);
				alert("注销成功");
                window.location.href = '主页.html'
            },
        error: function (res) {
            alert("注销失败");
        }
    });
}
function startgame(){
	token=localStorage.getItem("token1");
	$.ajax({
            url: "https://api.shisanshui.rtxux.xyz/game/open",
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-Auth-Token",token);
            },

            type: "post",
            success: function (data) {
				
				console.log(data);
				console.log(token);
				cards=data.data.card;
				id=data.data.id;
			  localStorage.setItem("id1",id);
				play();
				//window.location.href = '开始游戏.html'
            },
			error: function (res) {
				alert("开始游戏失败");
        	}
        });
}
function play(){
			alert("你拿到的卡片是"+cards);
			console.log(cards);
			console.log(JSON.stringify({
				"card":cards
			}));
	$.ajax({
            url: "http://172.26.76.171:7777/getcards",
			data: {"card":cards},
   header:{
             "Content-Type": "application/x-www-form-urlencoded",
           },
            type: "post",
            success: function (data) {
				console.log(data);
				cardstring=data.card.toString();
				console.log(cardstring);
				cardlist=data.card;				localStorage.setItem("card1",cardstring);
				window.location.href = '开始游戏.html'
            },
			error: function (res) {
				alert("开始游戏失败");
        	}
        });
}
function submit(){
	token=localStorage.getItem("token1");
	id=localStorage.getItem("id1");
	card2=localStorage.getItem("card1");
	card3=card2.split(/[ ,]+/);
	card4[0]=card3[0]+' '+card3[1]+' '+card3[2];
	card4[1]=card3[3]+' '+card3[4]+' '+card3[5]+' '+card3[6]+' '+card3[7];
	card4[2]=card3[8]+' '+card3[9]+' '+card3[10]+' '+card3[11]+' '+card3[12];
	console.log(card4);
    id =Number(id);
	$.ajax({
            url: "https://api.shisanshui.rtxux.xyz/game/submit",
			contentType:"application/json",
		    data:JSON.stringify({
				"id":id,
				"card":card4
			}),
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-Auth-Token",token);
            },
            type: "post",
            success: function (data) {
				console.log(token);
				console.log(data);
				console.log(data.data.msg);
				alert("出牌成功");
				window.location.href = '已登入界面.html'
            },
			error: function (res) {
				alert("提交失败");
        	}
        });
}
function show(){
	card2=localStorage.getItem("card1");
	console.log(card2);
	card3=card2.split(/[ ,]+/);
}
function f(i){
	if(card3[i]=="$A"){
		return "images/开始游戏/黑桃A.png";
	}
	if(card3[i]=="$2"){
		return "images/开始游戏/黑桃2.png";
	}
	if(card3[i]=="$3"){
		return "images/开始游戏/黑桃3.png";
	}
	if(card3[i]=="$4"){
		return "images/开始游戏/黑桃4.png";
	}
	if(card3[i]=="$5"){
		return "images/开始游戏/黑桃5.png";
	}
	if(card3[i]=="$6"){
		return "images/开始游戏/黑桃6.png";
	}
	if(card3[i]=="$7"){
		return "images/开始游戏/黑桃7.png";
	}
	if(card3[i]=="$8"){
		return "images/开始游戏/黑桃8.png";
	}
	if(card3[i]=="$9"){
		return "images/开始游戏/黑桃9.png";
	}
	if(card3[i]=="$10"){
		return "images/开始游戏/黑桃10.png";
	}
	if(card3[i]=="$J"){
		return "images/开始游戏/黑桃J.png";
	}
	if(card3[i]=="$Q"){
		return "images/开始游戏/黑桃Q.png";
	}
	if(card3[i]=="$K"){
		return "images/开始游戏/黑桃K.png";
	}
	if(card3[i]=="&A"){
		return "images/开始游戏/红桃A.png";
	}
	if(card3[i]=="&2"){
		return "images/开始游戏/红桃2.png";
	}
	if(card3[i]=="&3"){
		return "images/开始游戏/红桃3.png";
	}
	if(card3[i]=="&4"){
		return "images/开始游戏/红桃4.png";
	}
	if(card3[i]=="&5"){
		return "images/开始游戏/红桃5.png";
	}
	if(card3[i]=="&6"){
		return "images/开始游戏/红桃6.png";
	}
	if(card3[i]=="&7"){
		return "images/开始游戏/红桃7.png";
	}
	if(card3[i]=="&8"){
		return "images/开始游戏/红桃8.png";
	}
	if(card3[i]=="&9"){
		return "images/开始游戏/红桃9.png";
	}
	if(card3[i]=="&10"){
		return "images/开始游戏/红桃10.png";
	}
	if(card3[i]=="&J"){
		return "images/开始游戏/红桃J.png";
	}
	if(card3[i]=="&Q"){
		return "images/开始游戏/红桃Q.png";
	}
	if(card3[i]=="&K"){
		return "images/开始游戏/红桃K.png";
	}
	if(card3[i]=="*A"){
		return "images/开始游戏/草花A.png";
	}
	if(card3[i]=="*2"){
		return "images/开始游戏/草花2.png";
	}
	if(card3[i]=="*3"){
		return "images/开始游戏/草花3.png";
	}
	if(card3[i]=="*4"){
		return "images/开始游戏/草花4.png";
	}
	if(card3[i]=="*5"){
		return "images/开始游戏/草花5.png";
	}
	if(card3[i]=="*6"){
		return "images/开始游戏/草花6.png";
	}
	if(card3[i]=="*7"){
		return "images/开始游戏/草花7.png";
	}
	if(card3[i]=="*8"){
		return "images/开始游戏/草花8.png";
	}
	if(card3[i]=="*9"){
		return "images/开始游戏/草花9.png";
	}
	if(card3[i]=="*10"){
		return "images/开始游戏/草花10.png";
	}
	if(card3[i]=="*J"){
		return "images/开始游戏/草花J.png";
	}
	if(card3[i]=="*Q"){
		return "images/开始游戏/草花Q.png";
	}
	if(card3[i]=="*K"){
		return "images/开始游戏/草花K.png";
	}
	if(card3[i]=="#A"){
		return "images/开始游戏/方片A.png";
	}
	if(card3[i]=="#2"){
		return "images/开始游戏/方片2.png";
	}
	if(card3[i]=="#3"){
		return "images/开始游戏/方片3.png";
	}
	if(card3[i]=="#4"){
		return "images/开始游戏/方片4.png";
	}
	if(card3[i]=="#5"){
		return "images/开始游戏/方片5.png";
	}
	if(card3[i]=="#6"){
		return "images/开始游戏/方片6.png";
	}
	if(card3[i]=="#7"){
		return "images/开始游戏/方片7.png";
	}
	if(card3[i]=="#8"){
		return "images/开始游戏/方片8.png";
	}
	if(card3[i]=="#9"){
		return "images/开始游戏/方片9.png";
	}
	if(card3[i]=="#10"){
		return "images/开始游戏/方片10.png";
	}
	if(card3[i]=="#J"){
		return "images/开始游戏/方片J.png";
	}
	if(card3[i]=="#Q"){
		return "images/开始游戏/方片Q.png";
	}
	if(card3[i]=="#K"){
		return "images/开始游戏/方片K.png";
	}
}
function changecard()
{
	document.getElementById("u67_img").src=f(0);
	document.getElementById("u110_img").src=f(1);
	document.getElementById("u111_img").src=f(2);
	document.getElementById("u116_img").src=f(3);
	document.getElementById("u112_img").src=f(4);
	document.getElementById("u113_img").src=f(5);
	document.getElementById("u114_img").src=f(6);
	document.getElementById("u115_img").src=f(7);
	document.getElementById("u121_img").src=f(8);
	document.getElementById("u117_img").src=f(9);
	document.getElementById("u118_img").src=f(10);
	document.getElementById("u119_img").src=f(11);
	document.getElementById("u120_img").src=f(12);
}
function lookhistory(){
    token=localStorage.getItem("token1");
    var history_data = ($('#history_form').serializeJson());
    if (history_data.username == undefined) {
        alert("战局id不能为空");
        return;
    }
    $.ajax({
        url: "https://api.shisanshui.rtxux.xyz/history/5063",
        beforeSend: function(xhr) {
            xhr.setRequestHeader("X-Auth-Token","1aace708-ccb8-41df-93fc-d9b212c9f853");
        },
        type: "GET",
        contentType: "application/json;charset-UTF-8",
        success: function (result) { //todo

            console.log(status);
            console.log(result);
            console.log(token);
            console.log(detail);
            statu=data.status;
            hisd=result.data.id;
            cards=result.data.card; timestamp=result.data.timestamp;


        },
        error: function (res) {
            // $("#login_form").reset();
            console.log(token)
            console.log("https://api.shisanshui.rtxux.xyz/history/"+String(history_data.username));
            alert("查找失败");
        }
    });
}
function lookrank() {
        var data = null;
        var obj;
        var xhr = new XMLHttpRequest();
        // xhr.withCredentials = true;
        xhr.onreadystatechange=function(){
            if(xhr.readyState==4&&xhr.status==200){
                var json=xhr.responseText;
                obj=JSON.parse(xhr.responseText);
                function getJsonLength(json){
                    var jsonLength=0;
                    for (var i in json) {
                        var j=jsonLength;
                        var s=j+1;
                        document.getElementById("demo").innerHTML+='<tr><td>'+s+'</td><td>'+obj[j].player_id+'</td><td>'+obj[j].name+'</td><td>'+obj[j].score+'</td></tr>';
                        jsonLength++;
                    }
                }
                getJsonLength(json);
            }
        }
        // xhr.addEventListener("readystatechange", function () {
        //     if (this.readyState === this.DONE) {
        //         console.log(this.responseText);
        //     }
        // });
        xhr.open("GET", "https://api.shisanshui.rtxux.xyz/rank",true);
        xhr.send(data);
    }
function getid(){
	user_id=localStorage.getItem("user_id1");
	return user_id;
}


    function add(){document.getElementById("demo").innerHTML=null;x++;my(); }
    function dec(){if(x>0){document.getElementById("demo").innerHTML=null;x--;my();} else return;}
    function my() {

        var json;
        var token = localStorage.getItem('token1');
        (function ($) {
            $.fn.serializeJson = function () {
                var serializeObj = {};
                var array = this.serializeArray();
                var str = this.serialize();
                $(array).each(function () {
                    if (serializeObj[this.name]) {
                        if ($.isArray(serializeObj[this.name]) && this.value != "") {
                            serializeObj[this.name].push(this.value);
                        } else {
                            if (this.value != "") {
                                serializeObj[this.name] = [serializeObj[this.name], this.value];
                            }
                        }
                    } else {
                        if (this.value != "") {
                            serializeObj[this.name] = this.value;
                        }
                    }
                });
                return serializeObj;
            };
        })(jQuery);
        $.ajax({
            type: "GET",
            url: "https://api.shisanshui.rtxux.xyz/history?page="+x+"&limit=20&player_id="+getid(),
            headers: {
                'x-auth-token': token
            } ,
            success: function (result) {
            console.log(result);
            console.log(token);
            json = result;
            function getJsonLength(json) {
                for (var i in json) {
                    var l = 0;
                    for (var j in json.data) {
                        document.getElementById("demo").innerHTML += '<tr><td style="width: 10%">' + json.data[l].id + '</td><td style="width: 65%;text-align: center">' + json.data[l].card + '</td><td style="width: 10%">' + json.data[l].score + '</td><td style="width: 15%">' + json.data[l].timestamp + '</td></tr>';
                        l++;
                    };
                };
            }

            getJsonLength(json);
        }
    });
    }
function gotodetail()
{
	var detail_data = ($('#detail_form').serializeJson());
    if (detail_data.detailid == " 密码" ) {
        alert("战局id不能为空");
        return;
    }
	detailid = detail_data.detailid;
	localStorage.setItem("detailid1",detailid);
	 window.location.href = '复盘.html'
}
function showdetail()
{
	detailid=localStorage.getItem("detailid1");
	console.log(detailid);
	token=localStorage.getItem("token1");
	$.ajax({
            url: "https://api.shisanshui.rtxux.xyz/history/"+detailid,
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-Auth-Token",token);
            },

            type: "GET",
            success: function (data) {				
				console.log(data);
				console.log(token);
				dcards[0]=data.data.detail[0].card;
				dids[0]=data.data.detail[0].player_id;
				dscores[0]=data.data.detail[0].score;
				var cardstring=dcards[0].toString();
				card3=cardstring.split(/[ ,]+/);
				changecard0();
document.getElementById('username0').innerHTML = dids[0];
document.getElementById('score0').innerHTML = "积分变化："+dscores[0];				
				dcards[1]=data.data.detail[1].card;
				dids[1]=data.data.detail[1].player_id;
				dscores[1]=data.data.detail[1].score;
				var cardstring=dcards[1].toString();
				card3=cardstring.split(/[ ,]+/);
				changecard1();
document.getElementById('username1').innerHTML = dids[1];
document.getElementById('score1').innerHTML = "积分变化："+dscores[1];		
				dcards[2]=data.data.detail[2].card;
				dids[2]=data.data.detail[2].player_id;
				dscores[2]=data.data.detail[2].score;
				var cardstring=dcards[2].toString();
				card3=cardstring.split(/[ ,]+/);
				changecard2();
document.getElementById('username2').innerHTML = dids[2];
document.getElementById('score2').innerHTML = "积分变化："+dscores[2];	
				dcards[3]=data.data.detail[3].card;
				dids[3]=data.data.detail[3].player_id;
				dscores[3]=data.data.detail[3].score;
				var cardstring=dcards[3].toString();
				card3=cardstring.split(/[ ,]+/);
				changecard3();
document.getElementById('username3').innerHTML = dids[3];
document.getElementById('score3').innerHTML = "积分变化："+dscores[3];	
            },
			error: function (res) {
				alert("复盘失败");
                window.location.href = '已登入界面.html'
        	}
        });
	
}
function changecard0()
{
	document.getElementById("u249_img").src=f(0);
	document.getElementById("u250_img").src=f(1);
	document.getElementById("u251_img").src=f(2);
	document.getElementById("u256_img").src=f(3);
	document.getElementById("u252_img").src=f(4);
	document.getElementById("u253_img").src=f(5);
	document.getElementById("u254_img").src=f(6);
	document.getElementById("u255_img").src=f(7);
	document.getElementById("u261_img").src=f(8);
	document.getElementById("u257_img").src=f(9);
	document.getElementById("u258_img").src=f(10);
	document.getElementById("u259_img").src=f(11);
	document.getElementById("u260_img").src=f(12);
}
function changecard1()
{
	document.getElementById("u276_img").src=f(0);
	document.getElementById("u277_img").src=f(1);
	document.getElementById("u275_img").src=f(2);
	document.getElementById("u286_img").src=f(3);
	document.getElementById("u282_img").src=f(4);
	document.getElementById("u283_img").src=f(5);
	document.getElementById("u281_img").src=f(6);
	document.getElementById("u287_img").src=f(7);
	document.getElementById("u284_img").src=f(8);
	document.getElementById("u279_img").src=f(9);
	document.getElementById("u280_img").src=f(10);
	document.getElementById("u278_img").src=f(11);
	document.getElementById("u285_img").src=f(12);
}
function changecard2()
{
	document.getElementById("u290_img").src=f(0);
	document.getElementById("u289_img").src=f(1);
	document.getElementById("u288_img").src=f(2);
	document.getElementById("u299_img").src=f(3);
	document.getElementById("u298_img").src=f(4);
	document.getElementById("u297_img").src=f(5);
	document.getElementById("u296_img").src=f(6);
	document.getElementById("u300_img").src=f(7);
	document.getElementById("u294_img").src=f(8);
	document.getElementById("u293_img").src=f(9);
	document.getElementById("u292_img").src=f(10);
	document.getElementById("u291_img").src=f(11);
	document.getElementById("u295_img").src=f(12);
}
function changecard3()
{
	document.getElementById("u262_img").src=f(0);
	document.getElementById("u264_img").src=f(1);
	document.getElementById("u263_img").src=f(2);
	document.getElementById("u272_img").src=f(3);
	document.getElementById("u265_img").src=f(4);
	document.getElementById("u267_img").src=f(5);
	document.getElementById("u266_img").src=f(6);
	document.getElementById("u271_img").src=f(7);
	document.getElementById("u274_img").src=f(8);
	document.getElementById("u268_img").src=f(9);
	document.getElementById("u270_img").src=f(10);
	document.getElementById("u269_img").src=f(11);
	document.getElementById("u273_img").src=f(12);
}getJsonLength(json){
                    var jsonLength=0;
                    for (var i in json) {
                        var j=jsonLength;
                        var s=j+1;
                        document.getElementById("demo").innerHTML+='<tr><td>'+s+'</td><td>'+obj[j].player_id+'</td><td>'+obj[j].name+'</td><td>'+obj[j].score+'</td></tr>';
                        jsonLength++;
                    }
                }
                getJsonLength(json);
            }
        }
        // xhr.addEventListener("readystatechange", function () {
        //     if (this.readyState === this.DONE) {
        //         console.log(this.responseText);
        //     }
        // });
        xhr.open("GET", "https://api.shisanshui.rtxux.xyz/rank",true);
        xhr.send(data);
    }
function getid(){
	user_id=localStorage.getItem("user_id1");
	return user_id;
}


    function add(){document.getElementById("demo").innerHTML=null;x++;my(); }
    function dec(){if(x>0){document.getElementById("demo").innerHTML=null;x--;my();} else return;}
    function my() {

        var json;
        var token = localStorage.getItem('token1');
        (function ($) {
            $.fn.serializeJson = function () {
                var serializeObj = {};
                var array = this.serializeArray();
                var str = this.serialize();
                $(array).each(function () {
                    if (serializeObj[this.name]) {
                        if ($.isArray(serializeObj[this.name]) && this.value != "") {
                            serializeObj[this.name].push(this.value);
                        } else {
                            if (this.value != "") {
                                serializeObj[this.name] = [serializeObj[this.name], this.value];
                            }
                        }
                    } else {
                        if (this.value != "") {
                            serializeObj[this.name] = this.value;
                        }
                    }
                });
                return serializeObj;
            };
        })(jQuery);
        $.ajax({
            type: "GET",
            url: "https://api.shisanshui.rtxux.xyz/history?page="+x+"&limit=20&player_id="+getid(),
            headers: {
                'x-auth-token': token
            } ,
            success: function (result) {
            console.log(result);
            console.log(token);
            json = result;
            function getJsonLength(json) {
                for (var i in json) {
                    var l = 0;
                    for (var j in json.data) {
                        document.getElementById("demo").innerHTML += '<tr><td style="width: 10%">' + json.data[l].id + '</td><td style="width: 65%;text-align: center">' + json.data[l].card + '</td><td style="width: 10%">' + json.data[l].score + '</td><td style="width: 15%">' + json.data[l].timestamp + '</td></tr>';
                        l++;
                    };
                };
            }

            getJsonLength(json);
        }
    });
    }
function gotodetail()
{
	var detail_data = ($('#detail_form').serializeJson());
    if (detail_data.detailid == " 密码" ) {
        alert("战局id不能为空");
        return;
    }
	detailid = detail_data.detailid;
	localStorage.setItem("detailid1",detailid);
	 window.location.href = '复盘.html'
}
function showdetail()
{
	detailid=localStorage.getItem("detailid1");
	console.log(detailid);
	token=localStorage.getItem("token1");
	$.ajax({
            url: "https://api.shisanshui.rtxux.xyz/history/"+detailid,
            beforeSend: function(xhr) {
                xhr.setRequestHeader("X-Auth-Token",token);
            },

            type: "GET",
            success: function (data) {				
				console.log(data);
				console.log(token);
				dcards[0]=data.data.detail[0].card;
				dids[0]=data.data.detail[0].player_id;
				dscores[0]=data.data.detail[0].score;
				var cardstring=dcards[0].toString();
				card3=cardstring.split(/[ ,]+/);
				changecard0();
document.getElementById('username0').innerHTML = dids[0];
document.getElementById('score0').innerHTML = "积分变化："+dscores[0];				
				dcards[1]=data.data.detail[1].card;
				dids[1]=data.data.detail[1].player_id;
				dscores[1]=data.data.detail[1].score;
				var cardstring=dcards[1].toString();
				card3=cardstring.split(/[ ,]+/);
				changecard1();
document.getElementById('username1').innerHTML = dids[1];
document.getElementById('score1').innerHTML = "积分变化："+dscores[1];		
				dcards[2]=data.data.detail[2].card;
				dids[2]=data.data.detail[2].player_id;
				dscores[2]=data.data.detail[2].score;
				var cardstring=dcards[2].toString();
				card3=cardstring.split(/[ ,]+/);
				changecard2();
document.getElementById('username2').innerHTML = dids[2];
document.getElementById('score2').innerHTML = "积分变化："+dscores[2];	
				dcards[3]=data.data.detail[3].card;
				dids[3]=data.data.detail[3].player_id;
				dscores[3]=data.data.detail[3].score;
				var cardstring=dcards[3].toString();
				card3=cardstring.split(/[ ,]+/);
				changecard3();
document.getElementById('username3').innerHTML = dids[3];
document.getElementById('score3').innerHTML = "积分变化："+dscores[3];	
            },
			error: function (res) {
				alert("复盘失败");
                window.location.href = '已登入界面.html'
        	}
        });
	
}
function changecard0()
{
	document.getElementById("u249_img").src=f(0);
	document.getElementById("u250_img").src=f(1);
	document.getElementById("u251_img").src=f(2);
	document.getElementById("u256_img").src=f(3);
	document.getElementById("u252_img").src=f(4);
	document.getElementById("u253_img").src=f(5);
	document.getElementById("u254_img").src=f(6);
	document.getElementById("u255_img").src=f(7);
	document.getElementById("u261_img").src=f(8);
	document.getElementById("u257_img").src=f(9);
	document.getElementById("u258_img").src=f(10);
	document.getElementById("u259_img").src=f(11);
	document.getElementById("u260_img").src=f(12);
}
function changecard1()
{
	document.getElementById("u276_img").src=f(0);
	document.getElementById("u277_img").src=f(1);
	document.getElementById("u275_img").src=f(2);
	document.getElementById("u286_img").src=f(3);
	document.getElementById("u282_img").src=f(4);
	document.getElementById("u283_img").src=f(5);
	document.getElementById("u281_img").src=f(6);
	document.getElementById("u287_img").src=f(7);
	document.getElementById("u284_img").src=f(8);
	document.getElementById("u279_img").src=f(9);
	document.getElementById("u280_img").src=f(10);
	document.getElementById("u278_img").src=f(11);
	document.getElementById("u285_img").src=f(12);
}
function changecard2()
{
	document.getElementById("u290_img").src=f(0);
	document.getElementById("u289_img").src=f(1);
	document.getElementById("u288_img").src=f(2);
	document.getElementById("u299_img").src=f(3);
	document.getElementById("u298_img").src=f(4);
	document.getElementById("u297_img").src=f(5);
	document.getElementById("u296_img").src=f(6);
	document.getElementById("u300_img").src=f(7);
	document.getElementById("u294_img").src=f(8);
	document.getElementById("u293_img").src=f(9);
	document.getElementById("u292_img").src=f(10);
	document.getElementById("u291_img").src=f(11);
	document.getElementById("u295_img").src=f(12);
}
function changecard3()
{
	document.getElementById("u262_img").src=f(0);
	document.getElementById("u264_img").src=f(1);
	document.getElementById("u263_img").src=f(2);
	document.getElementById("u272_img").src=f(3);
	document.getElementById("u265_img").src=f(4);
	document.getElementById("u267_img").src=f(5);
	document.getElementById("u266_img").src=f(6);
	document.getElementById("u271_img").src=f(7);
	document.getElementById("u274_img").src=f(8);
	document.getElementById("u268_img").src=f(9);
	document.getElementById("u270_img").src=f(10);
	document.getElementById("u269_img").src=f(11);
	document.getElementById("u273_img").src=f(12);
}
