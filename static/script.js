
let sosyalMedyaIcon = document.querySelectorAll(".sosyalMedyaIcon");
let ortakIconSosyalMedya = document.querySelectorAll(".ortakIconSosyalMedya");

sosyalMedyaIcon[0].addEventListener("mouseover",animSosyalMedya);
sosyalMedyaIcon[0].addEventListener("mouseout",animSosyalMedya);

function animSosyalMedya(){
     ortakIconSosyalMedya[0].classList.toggle("sosyalMedyaOynat");
     ortakIconSosyalMedya[0].classList.toggle("sosyalMedyaAfter");
}

document.addEventListener("keyup",butonduzenle);

function butonduzenle(){
     let inputsearchbar = document.querySelector(".inputsearchbar").value;
     let searchButton = document.querySelector(".searchButton");
     let buttonTextIns = document.querySelector(".buttonTextIns");
     if (inputsearchbar == 0){
          searchButton.style.transition=".4s";
          searchButton.style.width="15%";
          searchButton.style.backgroundColor="gray";
          searchButton.style.borderLeft="0";
          searchButton.style.color="white";
          buttonTextIns.style.transition=".5s";
          buttonTextIns.style.transform="rotate(0deg)";
     }
     else{
          searchButton.style.transition=".7s";
          searchButton.style.width="10%";
          searchButton.style.backgroundColor="transparent";
          searchButton.style.borderLeft="1px solid black";
          searchButton.style.color="black";
          buttonTextIns.style.transition=".7s";
          buttonTextIns.style.transform="rotate(25deg)";
     }
}

// KATEGORİ AÇILIR KAPANIR PENCERE

const lifeSidebar = document.querySelector('.lifeSidebar');
const solKategori = document.querySelector('.sol_kategori');

// Sayfa yüklenirken lifeSidebar'ı görünür hale getirin, sol_kategoriyi gizleyin
lifeSidebar.style.display = 'block';
solKategori.style.display = 'block';

// lifeSidebar'a tıklandığında sol_kategoriyi açıp/kapatan bir olay dinleyici ekleyin
lifeSidebar.addEventListener('click', function() {
    if (solKategori.style.display === 'none') {
        solKategori.style.display = 'block';
        lifeSidebar.style.left ="20px"

    } else {
        solKategori.style.display = 'none';
        lifeSidebar.style.left ="100px"
    }
});




