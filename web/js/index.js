let body = document.querySelector("body"),
    bottomScroll = document.querySelector(".scroll"),
    upScroll = document.querySelector(".upscroll"),
    commentsSection = document.querySelector(".book-article");

bottomScroll.onclick = scrollBottom;
upScroll.onclick = scrollTop;

function scrollBottom(){
    window.scrollTo(0, window.pageYOffset + 10);

    if(window.pageYOffset >= commentsSection.offsetTop){
        return false;
    }else{
        setTimeout(()=>{
            scrollBottom();
        },1)
    }
}
function scrollTop(){
    window.scrollTo(0, window.pageYOffset - 10);
    console.log(window.pageYOffset);
    if(window.pageYOffset <= 0){
        return false;
    }else{
        setTimeout(()=>{
            scrollTop();
        },1)
    }
}