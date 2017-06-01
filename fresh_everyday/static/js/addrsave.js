/**
 * Created by python on 17-6-1.
 */
$(document).ready(function () {
    var error_postcode=true;
    var error_telephone=true;

    $('.site_con').submit(function () {
        check_postcode();
        check_telephone();
        return !(error_postcode || error_telephone);
    });

    function check_postcode()
    {
        var postCode=parseInt($('.postcode').val());
        if(postCode>=100000 && postCode<=999999)
        {
            error_postcode=false;
        }
    }

    function check_telephone()
    {
        var telephone=$('.telephone').val();
        var re=/^1[3458]\d{9}$/;
        if(re.test(telephone))
        {
            error_telephone=false;
        }
    }

});