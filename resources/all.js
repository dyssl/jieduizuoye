 var token = "5413";
 var user_id = "5413";
 var username = "5413";
 var cards = "5413";
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
	token=localStorage.getItem("temp");
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
				alert("出牌成功");
            },
			error: function (res) {
				alert("出牌失败");
        	}
        });
}