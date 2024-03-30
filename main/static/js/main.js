const bottonToTop = document.querySelector('.back-to-top');

window.addEventListener('scroll', function () {
    document.getElementById('header-nav').classList.toggle('headernav-scroll', window.scrollY > 155);
});

window.addEventListener('scroll', TrackScroll);

function TrackScroll() {
    const offset = window.scrollY;
    const cords = document.documentElement.clientHeight;
    if (offset > cords) {
        bottonToTop.classList.add('back-to-top--show');
    }
    else {
        bottonToTop.classList.remove('back-to-top--show');
    }
}

bottonToTop.addEventListener('click', goTop)

function goTop(){
    if (window.scrollY > 0) {
        window.scrollBy(0, -75);
        setTimeout(goTop, 0);
    }
}

