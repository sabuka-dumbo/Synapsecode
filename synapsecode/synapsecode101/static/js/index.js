const burger_menu = document.getElementById("burger-menu");
const navbar = document.getElementById("navbar");
const span1 = document.getElementById("span1");
const span2 = document.getElementById("span2");
const span3 = document.getElementById("span3");

let cooldown = false;
let open = false;

burger_menu.addEventListener("click", function () {
    if (cooldown) return;
    cooldown = true;

    if (!open) {
        navbar.style.display = "block";
        navbar.style.animation = "navbar-open ease 1s";
        span1.style.animation = "span1-open ease 1s";
        span2.style.animation = "span2-open ease 1s";
        span3.style.animation = "span3-open ease 1s";
        
        const onOpenEnd = () => {
            navbar.style.left = "0%";
            navbar.style.animation = "";

            span1.style.animation = "";
            span2.style.animation = "";
            span3.style.animation = "";

            span1.style.top = "14px";
            span2.style.opacity = "0";
            span3.style.top = "-14px";

            span1.style.rotate = "45deg";
            span3.style.rotate = "-45deg";
            open = true;
            cooldown = false;
            navbar.removeEventListener("animationend", onOpenEnd);
        };

        navbar.addEventListener("animationend", onOpenEnd);

    } else {
        navbar.style.animation = "navbar-close ease 1s";
        span1.style.animation = "span1-close ease 1s";
        span2.style.animation = "span2-close ease 1s";
        span3.style.animation = "span3-close ease 1s";

        const onCloseEnd = () => {
            navbar.style.left = "-100%";
            navbar.style.animation = "";
            navbar.style.display = "none";

            span1.style.animation = "";
            span2.style.animation = "";
            span3.style.animation = "";

            span1.style.top = "0px";
            span2.style.opacity = "1";
            span3.style.top = "0px";

            span1.style.rotate = "0deg";
            span3.style.rotate = "0deg";
            open = false;
            cooldown = false;
            navbar.removeEventListener("animationend", onCloseEnd);
        };

        navbar.addEventListener("animationend", onCloseEnd);
    }
});