window.addEventListener("scroll", () => {

    const header = document.querySelector("header");

    if(window.scrollY > 50){
        header.style.background = "#25180f";
    }else{
        header.style.background = "#3a2618";
    }

});