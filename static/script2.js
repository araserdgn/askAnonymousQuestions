let answerHR = document.querySelectorAll(".show-answers-hr");
let answerDiv = document.querySelectorAll(".show-the-answer-visibility-container-div");
let containerASK = document.querySelectorAll(".container-asking-question");

for(let i = 0; i < answerHR.length; i++){
     answerHR[i].addEventListener("click",()=>{
               //console.log(answerHR[i]);
               answerDiv[i].classList.toggle("getShowAnswers");
     });
}

window.addEventListener("scroll",getMenuWithScreen);
     
function getMenuWithScreen(e){
     let scrollY = window.scrollY; 
     if (scrollY > 200){

     }
}
