
$(document).ready(function(){

    $('.fa-hamburger').click(function(){
        $(this).toggleClass('fa-times');
        $('nav').toggleClass('nav-toggle');
    });

    $('nav ul li a').click(function(){
        $('.fa-hamburger').removeClass('fa-times');
        $('nav').removeClass('nav-toggle');
    });

    $('.dot1').click(function(){
        $('.vid1').css('display','block');
        $('.vid2').css('display','none');
        $('.vid3').css('display','none');
    });

    $('.dot2').click(function(){
        $('.vid2').css('display','none');
        $('.vid1').css('display','none');
        $('.vid3').css('display','block');
    });

    $('.dot3').click(function(){
        $('.vid3').css('display','none');
        $('.vid1').css('display','none');
        $('.vid2').css('display','block');
    });

    $(window).on('scroll load',function(){
        if($(window).scrollTop() > 10){
            $('#header').addClass('header-active');
        }else{
            $('#header').removeClass('header-active');
        }
    });

});




//selecting item

       $(document).ready(function () {
            
            $('.chkbx').click(function () {
            
            var text= "";
            
            $('.chkbx:checked') .each (function() {
            
            text+=$(this).val()+',';
            });
            
            text=text.substring (0,text.length-1);
            
            $('#selectedtext').val(text);
            
            var count = $("[type='checkbox']: checked").length;
            
            $('#count').val($("[type='checkbox']: checked").length);
        });
            
            
            });