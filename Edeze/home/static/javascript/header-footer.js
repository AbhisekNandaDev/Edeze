
//profile dropdown
let subMenu = document.getElementById("subMenu");
let userPic =document.getElementById("userPic")
        
userPic.addEventListener("click",function(){
    
    if (subMenu.style.display == "none") {
        subMenu.style.display = "block";
    } 
    else {
        subMenu.style.display = "none";
        }
});
        
        // profilePic.addEventListener("click", function() {
        //     subMenu.classList.toggle("open-menu");
        //     });

//Training drop down
// let trainingMenu =  document.querySelector(".training-menu");
// let trainingLink = document.querySelector("#training");
// trainingLink.addEventListener("mouseover", function() {
//     if(trainingMenu.style.display == "none"){
//         trainingMenu.style.display = "flex";
//     }
//     else{
//         trainingMenu.style.display = "none";
//     }
// });
// trainingLink.addEventListener("mouseover", function() {
//     
// });
// trainingLink.addEventListener("mouseout", function() {
//     trainingMenu.style.display = "none";
// });
