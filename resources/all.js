 var token = "5413";
 var user_id = "5413";
 var username = "5413";
 var cards = "5413";
var card2 = "5413";
var id = "5413";
var card4=new Array();
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
    if (reg_data.username == " 用户名" || reg_data.password == " 密码") {
        alert("用户名或密码不能为空");
        return;
    }
    $.ajax({
        type: "POST",
        dataType: "json",
        url: "https://api.shisanshui.rtxux.xyz/auth/register",
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
			alert(cards);
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
				alert("出牌成功");
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
	alert(id);
	console.log(card4);
	alert(card4);
	alert(card4[0]);
	alert(card4[1]);
	alert(card4[2]);
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
            alert(hisd);
            alert(timestamp);


        },
        error: function (res) {
            // $("#login_form").reset();
            console.log(token)
            console.log("https://api.shisanshui.rtxux.xyz/history/"+String(history_data.username));
            alert("查找失败");
        }
    });
}
function showhistory(){
	token=localStorage.getItem("token1");
	var history_data = ($('#history_form').serializeJson());
	$.ajax({
        url: "https://api.shisanshui.rtxux.xyz/history",
         beforeSend: function(xhr) {
                xhr.setRequestHeader("X-Auth-Token",token);
            },
        type: "GET",
        success: function (result) { //todo
			alert("查询历史成功");
            console.log(result.data);
        },
        error: function (res) {
            // $("#login_form").reset();
            console.log(token)
            alert("查找失败");
        }
    });
}
function getid(){
	user_id=localStorage.getItem("user_id1");
	return user_id;
}