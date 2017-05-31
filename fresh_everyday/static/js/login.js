/**
 * Created by python on 17-5-31.
 */
$(document).ready(function () {
    var error_username=true;
    var error_passwd=true;

    $('.name_input').blur(function () {
       check_username();
    });

    $('.pass_input').blur(function () {
        check_passwd();
    });

    $('.form_input').submit(function () {
        check_username();
        if(error_username==false)
        {
            check_passwd();
        }
        if(error_username==false && error_passwd==false)
        {
            return true;
        }
        else
        {
            return false;
        }
    });

    function check_username() {
        var username=$('.name_input').val();
        $.get('/fe_user/login_checkname'+username+'/',function (reply) {
            if(reply.exist=='no')
            {
                $('.name_input').next().html('请输入正确的用户名！');
                $('.name_input').next().show();
                error_username=true;
            }
            else
            {
                $('.name_input').next().hide();
                error_username=false;
            }
        });
    };

    function check_passwd() {
        var username=$('.name_input').val();
        var passwd=$('.pass_input').val();
        $.get('/fe_user/login_checkpasswd'+username+'&'+passwd+'/',function (reply) {
            if(reply!={})
            {
                if(reply.correct=="no")
                {
                    $('.pass_input').next().html('密码错误！');
                    $('.pass_input').next().show();
                    error_passwd=true;
                }
                else
                {
                    $('.pass_input').next().hide();
                    error_passwd=false;
                }
            }
        })
    }

});
